import regressionTrainer as reg

reg37 = reg.RegressionTrainer()

print(reg37._RegressionTrainer__inputfiles)

reg37._RegressionTrainer__inputfiles = {"ggH125":"../../GluGluHToMuMu_M125_13TeV_amcatnloFXFX_pythia8_181126_160447_tuple_all.root"}
reg37._RegressionTrainer__title = "muonReg_test37_2000Trees_allVars"
reg37._RegressionTrainer__cut = "(( muons.pt > 20 &&  muons.isTightID==1 && muons.relIso < 0.25 & muons.GEN_pt > 0. ) & muons.GEN_idx > 0)"
reg37._RegressionTrainer__target = "(genMuons[muons.GEN_idx].pt + ((genMuons[muons.GEN_idx].FSR_pt>0) ? genMuons[muons.GEN_idx].FSR_pt>0 : 0) )/muons.pt"

reg37._RegressionTrainer__vars =  """muons.pt 
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

reg37._RegressionTrainer__spectator_vars = "muons.GEN_idx".split()

print(reg37.__dict__)
reg37.train()
