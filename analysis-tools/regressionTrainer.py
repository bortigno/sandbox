import sys,re,ROOT
ROOT.gROOT.SetBatch(True)

''' Code used to train a regression for muons pT using as input X2MuMu ntuples '''

def get_tree(input_file,tree_full_name,cutstring):
 infile = ROOT.TFile(input_file,"READ")
 tree = infile.Get(tree_full_name)
 print(tree.GetEntries())
 ROOT.gDirectory.ls()
 ROOT.gROOT.cd()
 if (tree.GetEntries(cutstring)/tree.GetEntries() > 0.7): # if the cutsting has an efficiency larger than 30% then spend the time to copy, otherwise don't bother and use the cutstring directly in the training
   out_tree = tree.CopyTree(cutstring)
 else:
   print("cutsting has an efficiency lower than 30%. Tree won't be copied. Use cutstring directly in the training.")
   out_tree = tree.CopyTree("")
 # from https://root.cern.ch/input-and-output
 # You can change the directory of a histogram with the SetDirectory(newDir) method.
 out_tree.SetDirectory(0) # If the parameter is 0, the histogram is no longer associated with a directory.
 # Once a histogram is removed from the directory, it will no longer be deleted when the directory is closed. 
 # It is now your responsibility to delete this histogram object once you are finished with it.
 ROOT.gDirectory.ls()
 infile.Close()
 del infile
 del tree
 return out_tree


class RegressionTrainer():
    def __init__(self):
        ROOT.gSystem.Load("inlinetools_h.so")
        self.__weight = "(PU_wgt*GEN_wgt)"
        self.__vars = "muons.pt muons.charge abs(muons.eta) muons.ptErr/muons.pt muons.pt_trk muons.ptErr_trk/muons.pt_trk muons.d0_PV*muons.charge muons.dz_PV muons.hcalIso muons.ecalIso muons.sumPhotonEtR04 muons.sumPUPtR04 muons.sumPUPtR03 muons.sumPhotonEtR03 muons.sumChargedHadronPtR03 muons.sumChargedParticlePtR03 muons.sumNeutralHadronEtR03 muons.sumChargedHadronPtR04 muons.sumChargedParticlePtR04 muons.relIso muons.trackIsoSumPt muons.trackIsoSumPtCorr muons.pt_kinfit met.pt nVertices nJets nEles nPU vertices.rho met.sumEt".split()
        self.__target = "muons.GEN_pt/muons.pt"
        self.__cut = "( muons.pt > 20 &&  muons.isTightID==1 && muons.relIso < 0.25 & muons.GEN_pt > 0. )"
        self.__title = "muonReg_test32_2000Trees_allVars_12Nov"
        self.__samples = ["ggH125"]
        self.__inputfiles = {"ggH125":"../GluGluHToMuMu_M125_13TeV_amcatnloFXFX_pythia8_180930_213715_tuple_all.root"}
        self.__regOptions = "!H:!V:NTrees=10::BoostType=Grad:SeparationType=RegressionVariance:Shrinkage=0.3:nCuts=200:MaxDepth=5:NegWeightTreatment=IgnoreNegWeightsInTraining"
        self.__trainCut = "event.event%2==0"
        self.__testCut = "event.event%2!=0"
        
 

    def train(self):
        signals = []
        signalsTest = []
        for job in self.__samples:
            print '\tREADING IN %s AS SIG' %job
            tree_full_name = "dimuons/tree"
            input_file = self.__inputfiles[job]
            tree_cut_string = self.__cut 
            tree = get_tree(input_file,tree_full_name,tree_cut_string)
            print(tree)
            print(tree.GetEntries())
            train_full_cut = "{0} & {1}" .format(self.__cut,self.__trainCut)
            print(train_full_cut)
            test_full_cut = "{0} & {1}" .format(self.__cut,self.__testCut)
            signals.append(tree)
            signalsTest.append(tree)
            print(signals)       
        sWeight = 1.0
        fnameOutput='training_Reg_%s.root' %(self.__title)
        output = ROOT.TFile.Open(fnameOutput, "RECREATE")
 
        factory = ROOT.TMVA.Factory('TMVARegression', output, '!V:!Silent:!Color:!DrawProgressBar:Transformations=I:AnalysisType=Regression')
        print(factory)
        print("Signals : ")
        print(signals)
        loader = ROOT.TMVA.DataLoader("regressionDataLoader")
        loader.SetWeightExpression( self.__weight, "Regression" )
        #set input trees
        for i, signal in enumerate(signals):
            print("In the loop to add regression tree. Signal:")
            print(signal)
            print("i : ")
            print(i)
            loader.AddRegressionTree(signal, sWeight)
            print(self.__cut)
            mycut = ROOT.TCut(self.__cut)
            print(signal.GetEntries())
            print(signal.GetEntries(self.__cut))
        self.__apply = []
        p = re.compile(r'muons.pt\w+')
        for var in self.__vars:
            loader.AddVariable(var,'D') # add the variables
            self.__apply.append(p.sub(r'\g<0>[0]', var))
            print (self.__apply)

        for spectator_var in self.__spectator_vars:
            loader.AddSpectator(spectator_var,'D') # add the spectator variables
            self.__apply.append(p.sub(r'\g<0>[0]', spectator_var))
            print (self.__apply)


        loader.AddTarget( self.__target )
        mycut = ROOT.TCut( self.__cut )
        factory.BookMethod(loader,ROOT.TMVA.Types.kBDT,'BDT_REG_%s'%(self.__title),self.__regOptions) # book an MVA method
        factory.TrainAllMethods()
        factory.TestAllMethods()
        factory.EvaluateAllMethods()
        output.Write()
        regDict = dict(zip(self.__vars, self.__apply)) 


# NOTE: This part is a draft in case I want to write a ini file related to the application of the regression
#        self.__config.set('Regression', 'regWeight', '../data/MVA_BDT_REG_%s.weights.xml' %self.__title)
#        self.__config.set('Regression', 'regDict', '%s' %regDict)
#        self.__config.set('Regression', 'regVars', '%s' %self.__vars)
#        for section in self.__config.sections():
#            if not section == 'Regression':
#                self.__config.remove_section(section)
#        with open('8TeVconfig/appReg', 'w') as configfile:
#            self.__config.write(configfile)
#        with open('8TeVconfig/appReg', 'r') as configfile:
#            for line in configfile:
#                print line.strip()

# NOTE: Uncomment this if you want to run this script
#regTrainer = RegressionTrainer()
#regTrainer.train()
