import ROOT

infile = ROOT.TFile("../GluGluHToMuMu_M125_13TeV_amcatnloFXFX_pythia8_180930_213715_tuple_all.root","READ")

tree = infile.Get("dimuons/tree")

ROOT.gROOT.LoadMacro("inlinetools_h.so")

hmass = ROOT.TH1F("hmass","hmass",50,120,130)
hmass_av = ROOT.TH1F("hmass_av","hmass_av",50,120,130)
hmass_av.SetLineColor(ROOT.kRed)
hmass_wav = ROOT.TH1F("hmass_wav","hmass_wav",50,120,130)
hmass_wav.SetLineColor(ROOT.kBlack)

weigth_string = "( PU_wgt*GEN_wgt )"
jet_string =    "( Sum$(jets.pt>30 & jets.puID> 0.)==0 )" 
muon_string =   "( muons.pt > 20 &&  muons.isMediumID==1 && muons.relIso < 0.25 ) & abs(muons.pt[0] - muons.pt[1]) < 1."
eta_string =    "( min(abs(muons.eta[0]),abs(muons.eta[1])) < 0.9 && max(abs(muons.eta[1]),abs(muons.eta[0])) > 0.9 )"
gen_string =   "muons.GEN_pt[0] > -99" #" abs(muons.GEN_pt[0] - muons.GEN_pt[1]) < 3."  #"genMuPairs.pt[0] < 5 "
extra_string = "abs(muPairs.dPhi[0]) > 3.1" 

#"GEN_wgt * PU_wgt * ( abs(muPairs.dPhi) > 3.0 & Sum$(jets.pt>30 & jets.puID> 0.)==0 & (muons.pt > 20 && abs(muons.eta)<2.4 && muons.isMediumID==1 && muons.relIso < 0.25) )"
#cut_string = "[0] * ( abs(muPairs.dPhi) > 3.0 & Sum$(jets.pt>30 & jets.puID> 0.)==0 & (muons.pt > 20 && Min$(abs(muons.eta)) < 0.9 &&  Max$(abs(muons.eta))>1.7 && muons.isMediumID==1 && muons.relIso < 0.25) ) ".format(weigth_string)
cut_string = "{0} * ( {1} & {2} & {3}  ) ".format(weigth_string, muon_string, eta_string,gen_string)
print(cut_string)

c = ROOT.TCanvas("c","c",600,600)

#mass
#tree.Draw("muPairs.mass[0]>>hmass",cut_string)
tree.Draw("inlinetools::Hmass_comb(muons.eta[0],muons.phi[0],muons.pt[0],0.105,muons.eta[1],muons.phi[1],muons.pt[1],0.105)>>hmass",cut_string, "HIST")
#average mass
tree.Draw("inlinetools::Hmass_comb(muons.eta[0],muons.phi[0],0.5*(muons.pt[0]+muons.pt[1]),0.105,muons.eta[1],muons.phi[1],0.5*(muons.pt[0]+muons.pt[1]),0.105)>>hmass_av",cut_string,"SAME HIST")
#weighted average mass
tree.Draw("inlinetools::Hmass_comb(muons.eta[0],muons.phi[0],( (muons.pt[0]/muons.ptErr[0]**2) + (muons.pt[1]/muons.ptErr[1]**2) ) / ( (1/muons.ptErr[0]**2) + (1/muons.ptErr[1]**2) ),0.105,muons.eta[1],muons.phi[1],( (muons.pt[0]/muons.ptErr[0]^2) + (muons.pt[1]/muons.ptErr[1]^2) ) / ( (1/muons.ptErr[0]^2) + (1/muons.ptErr[1]^2) ),0.105)>>hmass_wav",cut_string,"SAME HIST")

c.SaveAs("average-mass-B-nonB-deltaRecoPtless1.pdf")

print(tree.GetEntries())




