import ROOT

#ROOT.gROOT.SetBatch(True)


def create_th1(name,title,nbins,minbin,maxbin,linecolor,xaxistitle="",yaxistitle="Entries"):
  h = ROOT.TH1F(name,title,nbins, minbin, maxbin)
  h.SetLineColor(linecolor)
  h.GetXaxis().SetTitle(xaxistitle)
  h.GetYaxis().SetTitle(yaxistitle)
  return h


def find_fwhm(f):
  epsilon = 0.01
  f_max = f.GetMaximum(); #print(f_max);
  f_mode = f.GetMaximumX(); #print(f_mode);
  f_left = f.GetX(f_max/2.,120.,f_mode - epsilon); #print(f_left);
  f_right = f.GetX(f_max/2.,f_mode+epsilon, 130);# print(f_right);
  return (f_right - f_left)



infile = ROOT.TFile("../GluGluHToMuMu_M125_13TeV_amcatnloFXFX_pythia8_180930_213715_tuple_all.root","READ")
#infile = ROOT.TFile("/eos/cms/store/group/phys_higgs/HiggsExo/H2Mu/UF/ntuples/data_2017_and_mc_fall17/GluGluHToMuMu_M125_13TeV_amcatnloFXFX_pythia8/H2Mu_gg/180930_213715/tuple_all.root","READ")
#infile = ROOT.TFile("/eos/cms/store/group/phys_higgs/HiggsExo/H2Mu/UF/ntuples/data_2017_and_mc_fall17/VBFHToMuMu_M125_13TeV_amcatnlo_pythia8/H2Mu_VBF/181003_121220/tuple_all.root","READ")

tree = infile.Get("dimuons/tree")

canvas = ROOT.TCanvas("c","cmass",600,600)
resolution_canvas = ROOT.TCanvas("res_c","res_c",600,600)

#hmass_pf = ROOT.TH1F("hmass_pf","MuPair mass",15, 120, 130)
#hmass_pf.SetLineColor(ROOT.kBlue)
hmass_pf = create_th1("hmass_pf","MuPair mass",50, 120, 130,ROOT.kBlue,"m(#mu,#mu)")
#hmass_kinfit = ROOT.TH1F("hmass_kinfit","MuPair mass",15, 120, 130)
#hmass_kinfit.SetLineColor(ROOT.kRed)
hmass_kinfit = create_th1("hmass_kinfit","MuPair mass",50, 120, 130,ROOT.kRed,"m(#mu,#mu)")

#hres_pf = ROOT.TH1F("hres_pf","Muon resolution", 100,-0.2,0.2)
hres_pf = create_th1("hres_pf","Muon resolution", 100,-0.2,0.2,ROOT.kBlue,"#Delta(p_{T},p_{T}^{GEN})/p_{T}^{GEN}")
#hres_pf.SetLineColor(ROOT.kBlue)
hres_kinfit = create_th1("hres_kinfit","Muon resolution", 100,-0.2,0.2,ROOT.kRed,"#Delta(p_{T},p_{T}^{GEN})/p_{T}^{GEN}")
#hres_kinfit = ROOT.TH1F("hres_kinfit","Muon resolution", 100,-0.2,0.2)
#hres_kinfit.SetLineColor(ROOT.kRed)

jet_selection = "( Sum$(jets.pt>20 && abs(jets.eta)<2.4 && jets.CSV>0.4941)>=0 ) "
muon_selection = "(muons.pt > 20 && abs(muons.eta)<2.4 && muons.isMediumID==1 && muons.relIso < 0.25)"
event_selection = "(muons.pt>30 && ( muons[0].isHltMatched[2]==1 || muons[0].isHltMatched[3]==1 || muons[1].isHltMatched[2]==1 || muons[1].isHltMatched[3]==1 ) )"
weightstring = "(GEN_wgt * PU_wgt)"
#cutstring = "(abs(muons[muPairs.iMu1].eta) < 0.9 & abs(muons[muPairs.iMu2].eta) < 0.9)"
#cutstring = "(abs(muons[muPairs.iMu1].eta) < 2.5 & abs(muons[muPairs.iMu2].eta) < 2.5)"
#cutstring = "(abs(muons[muPairs.iMu1].eta) > 1.7 & abs(muons[muPairs.iMu2].eta) > 1.7)"
#cutstring = "(abs(muons[muPairs.iMu1].eta) > 1.2 | abs(muons[muPairs.iMu2].eta) > 1.2)"
#cutstring = "abs(muons[muPairs.iMu1].d0_PV) > 0.002 & abs(muons[muPairs.iMu2].d0_PV) > 0.002"
cutstring = "abs(muons[muPairs.iMu1].d0_PV) > 0.002 | abs(muons[muPairs.iMu2].d0_PV) > 0.002"
#cutstring = "abs(muons[muPairs.iMu1].d0_PV) < 0.002 & abs(muons[muPairs.iMu2].d0_PV) < 0.002"
#cutstring = "( Sum$(jets.pt>40 && abs(jets.eta)<2.4) > 0 )"

#post string for output file name
#post_string="EE_1p7_15bins"
#post_string="XE"
#post_string="BB"
#post_string="inclusive"
#post_string="absd0bothmin0p002"
post_string="absd0min0p002"
#post_string="absd0max0p002"
#post_string="_atLeastOneCentralJetAt40GeV."


resolution_canvas.cd()
tree.Draw("(muons.pt_kinfit-muons.GEN_pt)/muons.GEN_pt>>hres_kinfit","{0} * ({1} && {2} && {3})".format(weightstring,event_selection,muon_selection, cutstring) )
tree.Draw("(muons.pt-muons.GEN_pt)/muons.GEN_pt>>hres_pf","{0} * ({1} && {2} && {3})".format(weightstring,event_selection,muon_selection, cutstring) )

hres_pf.Draw("HIST")
ROOT.gStyle.SetOptStat(1)
stat_res_pf = ROOT.TPaveText()
stat_res_pf = hres_pf.FindObject("stats")
stat_res_pf.SetY1NDC(.7)
stat_res_pf.SetY2NDC(.9)
stat_res_pf.SetX1NDC(.7)
stat_res_pf.SetX2NDC(.9)

hres_kinfit.Draw("HIST")
ROOT.gStyle.SetOptStat(1)
stat_res_kinfit = ROOT.TPaveText()
stat_res_kinfit = hres_kinfit.FindObject("stats")
stat_res_kinfit.SetY1NDC(.5)
stat_res_kinfit.SetY2NDC(.7)
stat_res_kinfit.SetX1NDC(.9)
stat_res_kinfit.SetX2NDC(.7)

hres_kinfit.Draw("HIST")
hres_pf.Draw("HIST same")
stat_res_pf.Draw("same")
stat_res_kinfit.Draw("same")

canvas.cd()
tree.Draw("muPairs.mass>>hmass_pf","{0} * ({1} && {2} && {3})".format(weightstring,event_selection,muon_selection, cutstring) )
tree.Draw("muPairs.mass_kinfit>>hmass_kinfit","{0} * ({1} && {2} && {3})".format(weightstring,event_selection,muon_selection, cutstring) )

fit_pf = ROOT.TF1("doublegaus_pf","gaus(0)+gaus(3)",120,130)
fit_kinfit =  ROOT.TF1("doublegaus_kinfit","gaus(0)+gaus(3)",120,130)

fit_pf.SetParameter(1,125.)
fit_pf.SetParameter(2,1.2)
fit_pf.SetParameter(4,124.)
fit_pf.SetParameter(5,2.5)

fit_kinfit.SetParameter(1,125.)
fit_kinfit.SetParameter(2,1.5)
fit_kinfit.SetParameter(4,124.)
fit_kinfit.SetParameter(5,2.5)

hmass_pf.Fit("doublegaus_pf")
hmass_kinfit.Fit("doublegaus_kinfit")

hmass_pf.Draw()
ROOT.gStyle.SetOptStat(1)
ROOT.gStyle.SetOptFit(1112)
stat_pf = ROOT.TPaveText()
stat_pf = hmass_pf.FindObject("stats")
stat_pf.SetOptStat(1)
stat_pf.SetOptFit(1112)
stat_pf.SetY1NDC(.7)
stat_pf.SetY2NDC(.9)
stat_pf.SetX1NDC(.7)
stat_pf.SetX2NDC(.9)

hmass_kinfit.GetYaxis().SetRangeUser(0,hmass_kinfit.GetMaximum()*1.2) #170 for inclusive. 70 for BB
hmass_kinfit.Draw("HIST")
ROOT.gStyle.SetOptStat(1)
ROOT.gStyle.SetOptFit(1112)

stat_kinfit = ROOT.TPaveText()
stat_kinfit = hmass_kinfit.FindObject("stats")
stat_kinfit.SetOptStat(1)
stat_kinfit.SetOptFit(1112)
stat_kinfit.SetY1NDC(.5)
stat_kinfit.SetY2NDC(.7)
stat_kinfit.SetX1NDC(.9)
stat_kinfit.SetX2NDC(.7)
stat_kinfit.Draw("same")

hmass_pf.Draw("HIST same")
stat_pf.Draw("same")


fwhm_pf = find_fwhm(fit_pf)
fwhm_kinfit = find_fwhm(fit_kinfit)

print(fwhm_pf)
print(fwhm_kinfit)
print("FWMH ratio = {0}".format(fwhm_kinfit/fwhm_pf))
print("FWHM/Mean PF = {0}".format(fwhm_pf/fit_pf.GetMaximumX()))
print("FWHM/Mean Regr = {0}".format(fwhm_kinfit/fit_kinfit.GetMaximumX()))

textpad = ROOT.TPaveText(.15,.75,.4,.88,"NDC ARC")
textpad.AddText("FWMH KinFit/PF ratio = {:.3f}".format(fwhm_kinfit/fwhm_pf))
textpad.AddText("FWHM/Mean PF = {:.4f}".format(fwhm_pf/fit_pf.GetMaximumX()))
textpad.AddText("FWHM/Mean KinFit = {:.4f}".format(fwhm_kinfit/fit_kinfit.GetMaximumX()))
textpad.Draw("same")


fit_pf.SetLineColor(ROOT.kBlue)
fit_pf.Draw("same")

fit_kinfit.SetLineColor(ROOT.kRed)
fit_kinfit.Draw("same")

#ROOT.gPad.BuildLegend()


canvas.Print("hmass_ggH_{0}.pdf".format(post_string))
resolution_canvas.Print("hres_ggH_{0}.pdf".format(post_string))


print(tree.GetEntries())



