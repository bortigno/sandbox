import ROOT
from plotMass import file_names, get_tree 

#infile = ROOT.TFile("GluGlu_HToMuMu_M125_GEN_test.root","READ")
#infile = ROOT.TFile("/eos/cms/store/group/phys_higgs/HiggsExo/H2Mu/UF/ntuples/data_2017_and_mc_fall17/VBFHToMuMu_M125_13TeV_amcatnlo_pythia8/H2Mu_VBF/181003_121220/tuple_all.root","READ")
#tree = infile.Get("dimuons/tree")

samp = "ggh18bsr_hadded" 
file_name = file_names[samp] 
tree = get_tree(file_name)

variable = "massRes"
#variable = "ptRes"

#positive muons

#mass viariables
#variable_kinfit_string = "(muPairs.mass_kinfit - 125.):muons.d0_PV"
variable_kinfit_string = "(muPairs.mass_bs - 125.):muons.d0_PV"
variable_pf_string = "(muPairs.mass - 125.):muons.d0_PV"

#pt variable
#variable_kinfit_string = "(muons.pt_kinfit - muons.GEN_pt):muons.d0_PV" 
#variable_kinfit_string = "(muons.pt_bs - muons.GEN_pt):muons.d0_PV" 
#variable_pf_string = "(muons.pt - muons.GEN_pt):muons.d0_PV" 

muon_selection = "(muons.pt > 20 & abs(muons.eta)<2.4 & muons.isMediumID==1 & muons.relIso < 0.25)"
event_selection = "muons.pt>20" # dummy
#event_selection = "(muons.pt>30 && ( muons[0].isHltMatched[2]==1 || muons[0].isHltMatched[3]==1 || muons[1].isHltMatched[2]==1 || muons[1].isHltMatched[3]==1 ) )"
weightstring = "(GEN_wgt * PU_wgt)"

#cut_string = "muons.charge>0 & abs(muons.pt_kinfit - muons.GEN_pt)<20"
cut_string = "muons.charge>0 & abs(muons.pt_bs - muons.GEN_pt)<20"

c1 = ROOT.TCanvas("c1","c1",900,600)
kfgend0pos = ROOT.TH2F("kf{0}gend0pos".format(variable),"kf{0}gend0pos".format(variable),20,-0.005,0.005,20,-5,5)
pfgend0pos = ROOT.TH2F("pf{0}gend0pos".format(variable),"pf{0}gend0pos".format(variable),20,-0.005,0.005,20,-5,5)

tree.Draw("{0}>>kf{1}gend0pos".format(variable_kinfit_string,variable),"{0} * ({1} & {2} & {3})".format(weightstring,event_selection,muon_selection,cut_string),"goff")
tree.Draw("{0}>>pf{1}gend0pos".format(variable_pf_string,variable),"{0} * ({1} & {2} & {3})".format(weightstring,event_selection,muon_selection,cut_string),"goff")

kfgend0pos_pfx = kfgend0pos.ProfileX("kf{0}gend0pos_pfx".format(variable))
pfgend0pos_pfx = pfgend0pos.ProfileX("pf{0}gend0pos_pfx".format(variable))
kfgend0pos_pfx.SetLineColor(ROOT.kRed)
kfgend0pos_pfx.Draw()
ROOT.gPad.Update()
stat_kfgend0pos_pfx = kfgend0pos_pfx.FindObject("stats")
print(kfgend0pos_pfx.GetRMS(1))
print(kfgend0pos_pfx.GetRMS(2))
pfgend0pos_pfx.Draw("same")
c2 = ROOT.TCanvas("c2","c2",600,600)
pfgend0pos_pfx.Draw()
ROOT.gPad.Update()
#ROOT.gStyle.SetOptStat(1111)
stat_pfgend0pos_pfx = ROOT.TPaveText()
stat_pfgend0pos_pfx = pfgend0pos_pfx.FindObject("stats")
print(pfgend0pos_pfx.GetRMS(1))
print(pfgend0pos_pfx.GetRMS(2))
stat_pfgend0pos_pfx.SetY1NDC(.7)
stat_pfgend0pos_pfx.SetY2NDC(.9)
stat_pfgend0pos_pfx.SetX1NDC(.7)
stat_pfgend0pos_pfx.SetX2NDC(.9)
c1.cd()
pfgend0pos_pfx.Draw("same")
stat_kfgend0pos_pfx.SetY1NDC(.5)
stat_kfgend0pos_pfx.SetY2NDC(.7)
stat_kfgend0pos_pfx.SetX1NDC(.9)
stat_kfgend0pos_pfx.SetX2NDC(.7)
stat_pfgend0pos_pfx.Draw("same")

#negative muons
cut_string = "muons.charge<0 & abs(muons.pt_kinfit - muons.GEN_pt)<20"


c3 = ROOT.TCanvas("c3","c3",900,600)
kfgend0neg = ROOT.TH2F("kf{0}gend0neg".format(variable),"kf{0}gend0neg".format(variable),20,-0.005,0.005,20,-5,5)
pfgend0neg = ROOT.TH2F("pf{0}gend0neg".format(variable),"pf{0}gend0neg".format(variable),20,-0.005,0.005,20,-5,5)
tree.Draw("{0}>>kf{1}gend0neg".format(variable_kinfit_string,variable),"{0} * ({1} && {2} && {3})".format(weightstring,event_selection,muon_selection,cut_string),"goff")
tree.Draw("{0}>>pf{1}gend0neg".format(variable_pf_string,variable),"{0} * ({1} && {2} && {3})".format(weightstring,event_selection,muon_selection,cut_string),"goff")
kfgend0neg_pfx = kfgend0neg.ProfileX("kf{0}gend0neg_pfx".format(variable))
pfgend0neg_pfx = pfgend0neg.ProfileX("pf{0}gend0neg_pfx".format(variable))
kfgend0neg_pfx.SetLineColor(ROOT.kRed)
kfgend0neg_pfx.Draw()
ROOT.gPad.Update()
stat_kfgend0neg_pfx = kfgend0neg_pfx.FindObject("stats")
print(kfgend0neg_pfx.GetRMS(1))
print(kfgend0neg_pfx.GetRMS(2))
pfgend0neg_pfx.Draw("same")
#pfmassgend0neg = ROOT.TH2F("pfmassgend0neg","pfmassgend0neg",20,-0.005,0.005,20,-5,5)
#kfmassgend0neg = ROOT.TH2F("kfmassgend0neg","kfmassgend0neg",20,-0.005,0.005,20,-5,5)
#tree.Draw("{0}>>kfmassgend0neg".format(variable_kinfit_string),"{0} * ({1} && {2} && {3})".format(weightstring,event_selection,muon_selection,cut_string),"goff")
#tree.Draw("{0}>>pfmassgend0neg".format(variable_pf_string),"{0} * ({1} && {2} && {3})".format(weightstring,event_selection,muon_selection,cut_string),"goff")
#kfmassgend0neg_pfx = kfmassgend0neg.ProfileX("kfmassgend0neg_pfx")
#pfmassgend0neg_pfx = pfmassgend0neg.ProfileX("pfmassgend0neg_pfx")
#kfmassgend0neg_pfx.SetLineColor(ROOT.kRed)
#kfmassgend0neg_pfx.Draw()
#ROOT.gPad.Update()
#stat_kfmassgend0neg_pfx = kfmassgend0neg_pfx.FindObject("stats")
#pfmassgend0neg_pfx.Draw("same")
c4 = ROOT.TCanvas("c4","c4",600,600)
pfgend0neg_pfx.Draw()
ROOT.gPad.Update()
#ROOT.gStyle.SetOptStat(1111)
stat_pfgend0neg_pfx = ROOT.TPaveText()
stat_pfgend0neg_pfx = pfgend0neg_pfx.FindObject("stats")
stat_pfgend0neg_pfx.SetY1NDC(.7)
stat_pfgend0neg_pfx.SetY2NDC(.9)
stat_pfgend0neg_pfx.SetX1NDC(.7)
stat_pfgend0neg_pfx.SetX2NDC(.9)
c3.cd()
pfgend0neg_pfx.Draw("same")
stat_kfgend0neg_pfx.SetY1NDC(.5)
stat_kfgend0neg_pfx.SetY2NDC(.7)
stat_kfgend0neg_pfx.SetX1NDC(.9)
stat_kfgend0neg_pfx.SetX2NDC(.7)
stat_pfgend0neg_pfx.Draw("same")

#pfmassgend0neg_pfx.Draw()
#ROOT.gPad.Update()
##ROOT.gStyle.SetOptStat(1111)
#stat_pfmassgend0neg_pfx = ROOT.TPaveText()
#stat_pfmassgend0neg_pfx = pfmassgend0neg_pfx.FindObject("stats")
#stat_pfmassgend0neg_pfx.SetY1NDC(.7)
#stat_pfmassgend0neg_pfx.SetY2NDC(.9)
#stat_pfmassgend0neg_pfx.SetX1NDC(.7)
#stat_pfmassgend0neg_pfx.SetX2NDC(.9)
#c3.cd()
#pfmassgend0neg_pfx.Draw("same")
#stat_kfmassgend0neg_pfx.SetY1NDC(.5)
#stat_kfmassgend0neg_pfx.SetY2NDC(.7)
#stat_kfmassgend0neg_pfx.SetX1NDC(.9)
#stat_kfmassgend0neg_pfx.SetX2NDC(.7)
#stat_pfmassgend0neg_pfx.Draw("same")



#mass plots
#c1.SaveAs("hmassgend0pos_pfx.pdf")
#c3.SaveAs("hmassgend0neg_pfx.pdf")

#Save plots
c1.SaveAs("h_{0}gend0pos_pfx.pdf".format(variable))
c3.SaveAs("h_{0}gend0neg_pfx.pdf".format(variable))






