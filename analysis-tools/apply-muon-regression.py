import ROOT
from array import array

infile = ROOT.TFile("../../GluGluHToMuMu_M125_13TeV_amcatnloFXFX_pythia8_181126_160447_tuple_all.root","READ")
tree = infile.Get("dimuons/tree")

outfile = ROOT.TFile("output-with-regression-test37-attempt1.root","RECREATE")
newtree = tree.CloneTree(0)

# booking the regressed variable.
pt_regr = []
kMaxMuons = 10
pt_regr.append(array('f',[0]*kMaxMuons))
newtree.Branch("muons_corr_regr",pt_regr[0],"muons_corr_regr[nMuons]/F")


#bdtmethod = "BDT_REG_muonReg_test28_2000Trees_allVars_30Oct"
bdtmethod = "BDT_REG_muonReg_test37_2000Trees_allVars"
#bdtmethod = "ciccio"
weightfile = "./regressionDataLoader/weights/TMVARegression_BDT_REG_muonReg_test37_2000Trees_allVars.weights.xml"

reader = ROOT.TMVA.Reader("!Color:!Silent")
input_variables = """muons.pt 
                   muons.charge 
                   abs(muons.eta) 
                   muons.ptErr/muons.pt 
                   muons.pt_trk 
                   muons.ptErr_trk/muons.pt_trk 
                   muons.d0_PV*muons.charge 
                   muons.dz_PV 
                   muons.hcalIso 
                   muons.ecalIso 
                   muons.sumPhotonEtR03 
                   muons.sumPhotonEtR04 
                   muons.sumPUPtR04 
                   muons.sumPUPtR03 
                   muons.sumChargedHadronPtR03 
                   muons.sumChargedHadronPtR04 
                   muons.sumChargedParticlePtR03 
                   muons.sumChargedParticlePtR04 
                   muons.sumNeutralHadronEtR03 
                   muons.relIso 
                   muons.trackIsoSumPt 
                   muons.trackIsoSumPtCorr 
                   muons.pt_kinfit
                   nVertices 
                   nJets 
                   nEles 
                   nPU 
                   vertices.rho""" .split()


spectator_variables = "muons.GEN_idx".split()

## for training 32
#"muons.pt muons.charge abs(muons.eta) muons.ptErr/muons.pt muons.pt_trk muons.ptErr_trk/muons.pt_trk muons.d0_PV*muons.charge muons.dz_PV muons.hcalIso muons.ecalIso muons.sumPhotonEtR04 muons.sumPUPtR04 muons.sumPUPtR03 muons.sumPhotonEtR03 muons.sumChargedHadronPtR03 muons.sumChargedParticlePtR03 muons.sumNeutralHadronEtR03 muons.sumChargedHadronPtR04 muons.sumChargedParticlePtR04 muons.relIso muons.trackIsoSumPt muons.trackIsoSumPtCorr muons.isTightID".split()
 
## For trasining <  test31
#input_variables = "muons.pt muons.charge abs(muons.eta) muons.ptErr muons.pt_trk muons.ptErr_trk muons.d0_PV muons.dz_PV muons.hcalIso muons.ecalIso muons.sumPhotonEtR04 muons.sumPUPtR04 muons.sumPUPtR03 muons.sumPhotonEtR03 muons.sumChargedHadronPtR03 muons.sumChargedParticlePtR03 muons.sumNeutralHadronEtR03 muons.sumChargedHadronPtR04 muons.sumChargedParticlePtR04 muons.relIso muons.trackIsoSumPt muons.trackIsoSumPtCorr muons.isStandAlone muons.isGlobal muons.isTightID".split()


input_vars_buffer = []
input_vars_formulas = []
#print(input_vars_formulas)

#if I use only the branches for regression application the other are not saved in the new tree
#tree.SetBranchStatus("*",0)
#tree.SetBranchStatus("nMuons",1)

# Looping over the training variables and an associated numerical index i
for i,var in zip( range(0,len(input_variables)) ,input_variables):
  # initiate only branches that are needed
#  if(var == "abs(muons.eta)"):
#    tree.SetBranchStatus("muons.eta",1)
#  else:
#    tree.SetBranchStatus(var,1)
  # instantiating the arrays that will be filled with the correct value in the event loop
  input_vars_buffer.append(array('f',[0]))
  # adding variables to the reader - for the moment are empty arrays
  reader.AddVariable(var,input_vars_buffer[i])
  # creating the formula to associated the values to the arrays
  input_vars_formulas.append(ROOT.TTreeFormula("mva_formula_{0}".format(var),"{0}".format(var),tree))

# spectator variables
spectator_vars_buffer = []
spectator_vars_formulas = []

for i,spec_var in zip( range(0, len(spectator_variables)), spectator_variables):
    spectator_vars_buffer.append(array('f',[0]))
    reader.AddSpectator(spec_var,spectator_vars_buffer[i])
    spectator_vars_formulas.append((ROOT.TTreeFormula("mva_formula_{0}".format(spec_var),"{0}".format(spec_var),tree)))

# booking the MVA reader
reader.BookMVA(bdtmethod,weightfile)

for entry in range(0,tree.GetEntries()):
    if(entry % 10000 == 0): print(entry) # print update every 100k events processed
    for i in range(0,len(pt_regr[0])): pt_regr[0][i] = 0. # init the array
    tree.GetEntry(entry)
    for muon_idx in range(0,tree.nMuons): 
      for s_var_i in range(0,len(spectator_variables)):
        spectator_vars_formulas[s_var_i].GetNdata()
        spectator_vars_buffer[s_var_i][0] = spectator_vars_formulas[s_var_i].EvalInstance(muon_idx) 
      for var_i in range(0,len(input_variables)):
        input_vars_formulas[var_i].GetNdata()
        input_vars_buffer[var_i][0] = input_vars_formulas[var_i].EvalInstance(muon_idx)
      pt_regr[0][muon_idx] = reader.EvaluateRegression(bdtmethod)[0]
    newtree.Fill()

newtree.AutoSave()
outfile.Close()


