import ROOT


def find_fwhm(f):
  epsilon = 0.01
  f_max = f.GetMaximum(); #print(f_max);
  f_mode = f.GetMaximumX(); #print(f_mode);
  f_left = f.GetX(f_max/2.,120.,f_mode - epsilon); #print(f_left);
  f_right = f.GetX(f_max/2.,f_mode+epsilon, 130);# print(f_right);
  return (f_right - f_left)

ROOT.gSystem.Load("inlinetools_h.so")

input_id = "test37"
infile = ROOT.TFile("output-with-regression-{0}-attempt1.root".format(input_id),"READ")

tree = infile.Get("tree")

nBins_mass = 100
minB_mass = 120
maxB_mass = 130

collection = "pf"
h_mass_pf = ROOT.TH1F("h_mass_{0}".format(collection),"h_mass_{0}".format(collection),nBins_mass, minB_mass, maxB_mass)
h_mass_pf.Sumw2()
h_mass_pf.SetLineColor(ROOT.kBlue)

collection = "regr"
h_mass_regr = ROOT.TH1F("h_mass_{0}".format(collection),"h_mass_{0}".format(collection),nBins_mass, minB_mass, maxB_mass)
h_mass_regr.Sumw2()
h_mass_regr.SetLineColor(ROOT.kRed)

## Fit functions
fit_pf = ROOT.TF1("gaus_pf","gaus(0)+gaus(3)",120,130)
fit_regr =  ROOT.TF1("gaus_regr","gaus(0)+gaus(3)",120,130)
fit_pf.SetParameter(1,125.)
fit_pf.SetParameter(2,1.3)
fit_pf.SetParameter(4,124.)
fit_pf.SetParameter(5,2.5)

#fit_regr.SetParameter(1,125.)
#fit_regr.SetParameter(2,1.3)
#fit_regr.SetParameter(4,124.)
#fit_regr.SetParameter(5,2.5)

fit_regr.SetParameter(1,126.)
fit_regr.SetParameter(2,1.3)
fit_regr.SetParameter(4,125.)
fit_regr.SetParameter(5,2.5)




weight_string = "(PU_wgt*GEN_wgt)"
test_event_string = "(event.event%1==0)" #"(event.event%2==0)"
phase_space_string = "muons.GEN_idx[0] > 0 & muons.GEN_idx[1] > 0 & genMuons[muons.GEN_idx[0]].FSR_pt == 0 & genMuons[muons.GEN_idx[1]].FSR_pt == 0"
#phase_space_string = "(max(abs(muons.eta[0]),abs(muons.eta[1])) > 1.7)"
#phase_space_string = "(min(abs(muons.eta[0]),abs(muons.eta[1])) < 0.9)"

full_cut_string_and_label = ["{0}*({1}&{2})".format(weight_string,test_event_string,phase_space_string), "events_without_FSR"]

tree.Draw("inlinetools::Hmass_comb(muons.eta[0],muons.phi[0],muons_corr_regr[0]*muons.pt[0],0.105,muons.eta[1],muons.phi[1],muons_corr_regr[1]*muons.pt[1],0.105)>>h_mass_regr",full_cut_string_and_label[0],"goff")

tree.Draw("inlinetools::Hmass_comb(muons.eta[0],muons.phi[0],muons.pt[0],0.105,muons.eta[1],muons.phi[1],muons.pt[1],0.105)>>h_mass_pf",full_cut_string_and_label[0],"goff")

h_mass_pf.Fit("gaus_pf")
h_mass_regr.Fit("gaus_regr")


# Graphics
c_mass = ROOT.TCanvas("c_mass","c_mass",600,600)

h_mass_regr.Draw("HIST")
ROOT.gStyle.SetOptStat(1)
ROOT.gStyle.SetOptFit(1112)
stat_regr = ROOT.TPaveText()
stat_regr = h_mass_regr.FindObject("stats")
stat_regr.SetOptStat(1)
stat_regr.SetOptFit(1112)
stat_regr.SetY1NDC(.5)
stat_regr.SetY2NDC(.7)
stat_regr.SetX1NDC(.9)
stat_regr.SetX2NDC(.7)


h_mass_pf.Draw("HIST")
ROOT.gStyle.SetOptStat(1)
ROOT.gStyle.SetOptFit(1112)
stat_pf = ROOT.TPaveText()
stat_pf = h_mass_pf.FindObject("stats")
stat_pf.SetOptStat(1)
stat_pf.SetOptFit(1112)
stat_pf.SetY1NDC(.7)
stat_pf.SetY2NDC(.9)
stat_pf.SetX1NDC(.7)
stat_pf.SetX2NDC(.9)
stat_pf.Draw("same")

#h_mass_pf.Draw("HIST") 
h_mass_regr.Draw("HIST SAME")
#stat_pf.Draw("same")
stat_regr.Draw("same")

fwhm_pf = find_fwhm(fit_pf)
fwhm_regr = find_fwhm(fit_regr)

print(fwhm_pf)
print(fwhm_regr)
print("FWMH ratio = {0}".format(fwhm_regr/fwhm_pf))
print("FWHM/Mean PF = {0}".format(fwhm_pf/fit_pf.GetMaximumX()))
print("FWHM/Mean Regr = {0}".format(fwhm_regr/fit_regr.GetMaximumX()))

textpad = ROOT.TPaveText(.15,.75,.4,.88,"NDC ARC")
textpad.AddText("FWMH Regr/PF ratio = {:.3f}".format(fwhm_regr/fwhm_pf))
textpad.AddText("FWHM/Mean PF = {:.4f}".format(fwhm_pf/fit_pf.GetMaximumX()))
textpad.AddText("FWHM/Mean Regr = {:.4f}".format(fwhm_regr/fit_regr.GetMaximumX()))
textpad.Draw("same")

fit_pf.SetLineColor(ROOT.kBlue)
fit_pf.Draw("same")

fit_regr.SetLineColor(ROOT.kRed)
fit_regr.Draw("same")


c_mass.SaveAs("{0}_{1}_mass.pdf".format(input_id,full_cut_string_and_label[1]))


######### RESOLUTION #############

## Leading muon ## 

# what variable to compare the muon pt with. Could be muons.GEN_pt for postFSR or (genMuons[muons.GEN_idx].pt + ((genMuons[muons.GEN_idx].FSR_pt>0) ? genMuons[muons.GEN_idx].FSR_pt>0 : 0) ) for preFSR 
target_string = "(genMuons[muons.GEN_idx[0]].pt + ((genMuons[muons.GEN_idx[0]].FSR_pt>0) ? genMuons[muons.GEN_idx[0]].FSR_pt>0 : 0) )"

c_res = ROOT.TCanvas("c_res","c_resolution",600,600)

h_res_pf = ROOT.TH1F("h_res_pf","PF Resolution",100,-0.2,0.2)
h_res_pf.SetLineColor(ROOT.kBlue)

h_res_regr = ROOT.TH1F("h_res_regr","Regr Resolution",100,-0.2,0.2)
h_res_regr.SetLineColor(ROOT.kRed)
h_res_regr.GetXaxis().SetTitle("#Delta(p_{T}^{RECO},p_{T}^{GEN})/p_{T}^{GEN}")
ROOT.gStyle.SetOptStat(0)

tree.Draw("(muons.pt[0]- {0})/({0}) >>h_res_pf".format(target_string),full_cut_string_and_label[0])
tree.Draw("(muons_corr_regr[0]*muons.pt[0] - {0})/({0})>>h_res_regr".format(target_string),full_cut_string_and_label[0])

h_res_regr.Draw("HIST")
h_res_pf.Draw("HIST same")

textpadres = ROOT.TPaveText(.15,.75,.4,.88,"NDC ARC")
textpadres.AddText("RMS Regr/PF ratio = {:.3f}".format(h_res_regr.GetRMS()/h_res_pf.GetRMS()))
textpadres.Draw("same")

c_res.SaveAs("{0}_{1}_leadingMuon_res.pdf".format(input_id,full_cut_string_and_label[1]))

## Subleading muon ## 

# what variable to compare the muon pt with. Could be muons.GEN_pt for postFSR or (genMuons[muons.GEN_idx].pt + ((genMuons[muons.GEN_idx].FSR_pt>0) ? genMuons[muons.GEN_idx].FSR_pt>0 : 0) ) for preFSR 
target_string = "(genMuons[muons.GEN_idx[1]].pt + ((genMuons[muons.GEN_idx[1]].FSR_pt>0) ? genMuons[muons.GEN_idx[1]].FSR_pt>0 : 0) )"

c_res_subleading = ROOT.TCanvas("c_res_subleading","c_resolution_subleading",600,600)

h_res_pf_subleading = ROOT.TH1F("h_res_pf_subleading","PF Resolution",100,-0.2,0.2)
h_res_pf_subleading.SetLineColor(ROOT.kBlue)

h_res_regr_subleading = ROOT.TH1F("h_res_regr_subleading","Regr Resolution",100,-0.2,0.2)
h_res_regr_subleading.SetLineColor(ROOT.kRed)
h_res_regr_subleading.GetXaxis().SetTitle("#Delta(p_{T}^{RECO},p_{T}^{GEN})/p_{T}^{GEN}")
ROOT.gStyle.SetOptStat(0)

tree.Draw("(muons.pt[1]- {0})/({0}) >>h_res_pf_subleading".format(target_string),full_cut_string_and_label[0])
tree.Draw("(muons_corr_regr[1]*muons.pt[1] - {0})/({0})>>h_res_regr_subleading".format(target_string),full_cut_string_and_label[0])

h_res_regr_subleading.Draw("HIST")
h_res_pf_subleading.Draw("HIST same")

textpadres_subleading = ROOT.TPaveText(.15,.75,.4,.88,"NDC ARC")
textpadres_subleading.AddText("RMS Regr/PF ratio = {:.3f}".format(h_res_regr.GetRMS()/h_res_pf.GetRMS()))
textpadres_subleading.Draw("same")

c_res_subleading.SaveAs("{0}_{1}_subleadingMuon_res.pdf".format(input_id,full_cut_string_and_label[1]))



######### CORRECTION FACTORS #############


c_cor = ROOT.TCanvas("c_cor","c_corrections",600,600)

h_cor_pf = ROOT.TH1F("h_cor_pf","PF Corrections",100,0.8,1.2)
h_cor_pf.SetLineColor(ROOT.kBlue)

h_cor_regr = ROOT.TH1F("h_cor_regr","Regr Corrections",100,0.8,1.2)
h_cor_regr.SetLineColor(ROOT.kRed)
h_cor_regr.GetXaxis().SetTitle("p_{T}^{RECO}/p_{T}^{GEN}")
ROOT.gStyle.SetOptStat(0)

tree.Draw("muons.pt/muons.GEN_pt>>h_cor_pf",full_cut_string_and_label[0])
tree.Draw("(muons_corr_regr*muons.pt)/muons.GEN_pt>>h_cor_regr",full_cut_string_and_label[0])

h_cor_regr.Draw("HIST")
h_cor_pf.Draw("HIST same")

textpadcor = ROOT.TPaveText(.15,.75,.4,.88,"NDC ARC")
textpadcor.AddText("RMS Regr/PF ratio = {:.3f}".format(h_cor_regr.GetRMS()/h_cor_pf.GetRMS()))
textpadcor.Draw("same")

c_cor.SaveAs("{0}_{1}_cor.pdf".format(input_id,full_cut_string_and_label[1]))


print(tree.GetEntries())
