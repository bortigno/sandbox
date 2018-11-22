import ROOT

test = 32
if(test<30):
    regressed_pt = "muons_pt_regr"
else:
    regressed_pt = "muons_corr_regr * muons.pt"

#infile = ROOT.TFile("output-with-regression-test28-attempt8.root","READ")
infile = ROOT.TFile("output-with-regression-test{0}-attempt1.root".format(test),"READ")
#infile = ROOT.TFile("/eos/cms/store/group/phys_higgs/HiggsExo/H2Mu/UF/ntuples/data_2017_and_mc_fall17/VBFHToMuMu_M125_13TeV_amcatnlo_pythia8/H2Mu_VBF/181003_121220/tuple_all.root","READ")

tree = infile.Get("tree")

#variable = "massRes"
variable = "ptRes_genPt"
output_extra_string = "_regression_test{0}".format(test)

#pt variable
variable_test_string = "({0} - muons.GEN_pt)/muons.GEN_pt:muons.GEN_pt".format(regressed_pt)
variable_ref_string = "(muons.pt - muons.GEN_pt)/muons.GEN_pt:muons.GEN_pt" 

muon_selection = "(muons.pt > 20 && abs(muons.eta)<2.4 && muons.isMediumID==1 && muons.relIso < 0.25)"
event_selection = "(muons.GEN_pt>20)" #"(muons.pt>30 && ( muons[0].isHltMatched[2]==1 || muons[0].isHltMatched[3]==1 || muons[1].isHltMatched[2]==1 || muons[1].isHltMatched[3]==1 ) )"
weightstring = "(GEN_wgt * PU_wgt)"
cut_string = "(muons.GEN_pt>20)"

c1 = ROOT.TCanvas("c1","c1",900,600)
test_th2 = ROOT.TH2F("test{0}_th2".format(variable),"test{0}_th2".format(variable),50,0,500,100,-0.2,0.2)
ref_th2 = ROOT.TH2F("ref{0}_th2".format(variable),"ref{0}_th2".format(variable),50,0,500,100,-0.2,0.2)
tree.Draw("{0}>>test{1}_th2".format(variable_test_string,variable),"{0} * ({1} && {2} && {3})".format(weightstring,event_selection,muon_selection,cut_string),"goff")
tree.Draw("{0}>>ref{1}_th2".format(variable_ref_string,variable),"{0} * ({1} && {2} && {3})".format(weightstring,event_selection,muon_selection,cut_string),"goff")
test_th2_pfx = test_th2.ProfileX("test{0}_th2_pfx".format(variable))
ref_th2_pfx = ref_th2.ProfileX("ref{0}_th2_pfx".format(variable))
test_th2_pfx.SetLineColor(ROOT.kRed)
test_th2_pfx.GetYaxis().SetRangeUser(-0.02,0.02)
test_th2_pfx.Draw()
ROOT.gPad.Update()
stat_test_th2_pfx = test_th2_pfx.FindObject("stats")
print(test_th2_pfx.GetRMS(1))
print(test_th2_pfx.GetRMS(2))
ref_th2_pfx.Draw("same")
c2 = ROOT.TCanvas("c2","c2",600,600)
ref_th2_pfx.Draw()
ROOT.gPad.Update()
#ROOT.gStyle.SetOptStat(1111)
stat_ref_th2_pfx = ROOT.TPaveText()
stat_ref_th2_pfx = ref_th2_pfx.FindObject("stats")
print(ref_th2_pfx.GetRMS(1))
print(ref_th2_pfx.GetRMS(2))
stat_ref_th2_pfx.SetY1NDC(.7)
stat_ref_th2_pfx.SetY2NDC(.9)
stat_ref_th2_pfx.SetX1NDC(.7)
stat_ref_th2_pfx.SetX2NDC(.9)
c1.cd()
ref_th2_pfx.Draw("same")
stat_test_th2_pfx.SetY1NDC(.5)
stat_test_th2_pfx.SetY2NDC(.7)
stat_test_th2_pfx.SetX1NDC(.9)
stat_test_th2_pfx.SetX2NDC(.7)
stat_ref_th2_pfx.Draw("same")

#Save plots
c1.SaveAs("h_{0}_th2_pfx{1}.pdf".format(variable,output_extra_string))


c2.cd()
th1_variable_test_string = "({0} - muons.GEN_pt)/muons.GEN_pt".format(regressed_pt) 
th1_variable_ref_string = "(muons.pt - muons.GEN_pt)/muons.GEN_pt" 
test_th1 = ROOT.TH1F("test{0}_th1".format(variable),"test{0}_th1".format(variable),100,-0.2,0.2)
test_th1.SetLineColor(ROOT.kRed)
ref_th1 = ROOT.TH1F("ref{0}_th1".format(variable),"ref{0}_th1".format(variable),100,-0.2,0.2)
tree.Draw("{0} >> test{1}_th1".format(th1_variable_test_string, variable), "{0} * ({1} && {2} && {3})".format(weightstring,event_selection,muon_selection,cut_string), "goff" )
tree.Draw("{0} >> ref{1}_th1".format(th1_variable_ref_string, variable), "{0} * ({1} && {2} && {3})".format(weightstring,event_selection,muon_selection,cut_string), "goff" )
test_th1.Draw("HIST")
ref_th1.Draw("HIST SAME")
c2.SaveAs("h_{0}_th1_{1}.pdf".format(variable,output_extra_string))


