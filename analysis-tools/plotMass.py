import ROOT, sys, os
#ROOT.gROOT.SetBatch(True)

# from https://stackoverflow.com/questions/15753701/argparse-option-for-passing-a-list-as-option
import argparse # for options parsing
parser = argparse.ArgumentParser(description="Pass arguments")
parser.add_argument("-s", "--samples", nargs='*', dest="samps", default  = [],
                 help = "List of samples")
parser.add_argument("-c","--cut-list",nargs='*',dest="cuts", default = [],
                 help = "List of cuts strings to process")
parser.add_argument("-v","--variable-selection",nargs='*',dest="variables_selection", default = [],
                 help = "List of variables to process")
args = parser.parse_args()


########################
## example of running ##
########################


####################
## some functions ##
####################


def get_tree(file_name, data_path="/Users/pier/Physics/data/", path_to_tree="dimuons/tree"):
  if ( os.path.isfile('{0}/{1}.root'.format(data_path,file_name) ) ):
    infile = ROOT.TFile("{0}/{1}.root".format(data_path,file_name))
    tree = infile.Get("dimuons/tree")
  else : 
    entries = os.listdir('{0}/{1}'.format(data_path,file_name))
    for entry in entries:
        print('Adding {0} file to chain.'.format(entry))
        tree = ROOT.TChain(path_to_tree)
        tree.Add('{0}/{1}/{2}'.format(data_path,file_name,entry))
  print(tree.GetEntries())
  return tree



def create_th1(name,title,nbins,minbin,maxbin,linecolor,xaxistitle="",yaxistitle="Entries"):
  h = ROOT.TH1F(name,title,nbins, minbin, maxbin)
  h.SetLineColor(linecolor)
  h.GetXaxis().SetTitle(xaxistitle)
  h.GetYaxis().SetTitle(yaxistitle)
  h.GetYaxis().SetTitleOffset(1.5)
  return h


def find_fwhm(f):
  epsilon = 0.01
  f_max = f.GetMaximum(); #print(f_max);
  f_mode = f.GetMaximumX(); #print(f_mode);
  f_left = f.GetX(f_max/2.,120.,f_mode - epsilon); #print(f_left);
  f_right = f.GetX(f_max/2.,f_mode+epsilon, 130);# print(f_right);
  return (f_right - f_left)

#######################
## some dictionaries ##
#######################

file_names = {
        #2016
        "ggh16":"h2mu_ggH_125_prod-v16.0.7_hadded",
        "vbf16":"h2mu_vbf_125_prod-v16.0.7_hadded",
        "whp16":"h2mu_WplusH_125_prod-v16.0.7_hadded",
        "whm16":"h2mu_WminusH_125_prod-v16.0.7_hadded",
        "tth16":"h2mu_ttH_125_prod-v16.0.7_hadded",
        #2017
        "ggh17":"h2mu_ggh_125_prod-v17.3.0_hadded",
        #2018
        "ggh18":"h2mu_ggh_125_prod-v18.1.2_hadded",
        "vbf18":"h2mu_vbf_125_prod-v18.1.2_hadded",
        "whp18":"h2mu_WplusH_125_prod-v18.1.2_hadded",
        "whm18":"h2mu_WminusH_125_prod-v18.1.2_hadded",
        "tth18":"h2mu_tth_125_prod-v18.1.2_hadded",
        #2018 w beamspot refitting covariance
        "ggh18bs":"tuple_with_beamspot_covariance3d_GluGluHToMuMu_M125_TuneCP5_PSweights_13TeV_amcatnloFXFX_pythia8",
         #2018 w beamspot refitting rotated covariance
        "ggh18bsr":"tuple_2_with_beamspot_rotatedcovariance3d_GluGluHToMuMu_M125_TuneCP5_PSweights_13TeV_amcatnloFXFX_pythia8",
        #2018 w beamspot refitting rotated covariance
        "ggh18bsr_all":"tuple_with_beamspot_rotatedcovariance3d_GluGluHToMuMu_M125_TuneCP5_PSweights_13TeV_amcatnloFXFX_pythia8",
        #2018 w beamspot refitting rotated covariance
        "ggh18bsr_hadded":"tuple_with_beamspot_rotatedcovariance3d_GluGluHToMuMu_M125_TuneCP5_PSweights_13TeV_amcatnloFXFX_pythia8/hadded"
        }

cutstrings = {
  "inclusive_d0cat_PF":"(abs(muons[muPairs.iMu1].eta) < 2.5 & abs(muons[muPairs.iMu2].eta) < 2.5)",
  "inclusive_d0cat_PF_Roch":"(abs(muons[muPairs.iMu1].eta) < 2.5 & abs(muons[muPairs.iMu2].eta) < 2.5)",
  "inclusive_d0cat_kinfit":"(abs(muons[muPairs.iMu1].eta) < 2.5 & abs(muons[muPairs.iMu2].eta) < 2.5)",
  "inclusive_d0cat_kinfit_Roch":"(abs(muons[muPairs.iMu1].eta) < 2.5 & abs(muons[muPairs.iMu2].eta) < 2.5)",
  "inclusive_d0cat_Kalman":"(abs(muons[muPairs.iMu1].eta) < 2.5 & abs(muons[muPairs.iMu2].eta) < 2.5)",
  "XE":"(abs(muons[muPairs.iMu1].eta) > 1.2 | abs(muons[muPairs.iMu2].eta) > 1.2)",
  "BB":"(abs(muons[muPairs.iMu1].eta) < 0.9 & abs(muons[muPairs.iMu2].eta) < 0.9)",
  "inclusive":"(abs(muons[muPairs.iMu1].eta) < 2.5 & abs(muons[muPairs.iMu2].eta) < 2.5)",
  "absd0bothmin0p002":"abs(muons[muPairs.iMu1].d0_PV) > 0.002 & abs(muons[muPairs.iMu2].d0_PV) > 0.002",
  "absd0min0p002":"abs(muons[muPairs.iMu1].d0_PV) > 0.002 | abs(muons[muPairs.iMu2].d0_PV) > 0.002",
  "absd0max0p002":"abs(muons[muPairs.iMu1].d0_PV) < 0.002 & abs(muons[muPairs.iMu2].d0_PV) < 0.002",
  "atLeastOneCentralJetAt40GeV":"( Sum$(jets.pt>40 && abs(jets.eta)<2.4) > 0 )"
        }

variables_dictionary = {
  "hmass_PF":["muPairs.mass","m(#mu#mu) PF"],
  "hmass_PF_Roch":["muPairs.mass_Roch","m(#mu#mu) Roch"],
  "hmass_kinfit":["(muPairs.mass_kinfit>0?muPairs.mass_kinfit:muPairs.mass)","m(#mu#mu) kinfit"],
  "hmass_kinfit_Roch":["(muPairs.mass_kinfit>0?(muPairs.mass_kinfit*muPairs.mass_Roch/muPairs.mass):muPairs.mass_Roch)","m(#mu#mu) kinfit + Roch"],
  "hmass_kalman":["muPairs.mass_KaMu","m(#mu#mu) kalman"],
  "hmass_bs":["(muPairs.mass_bs>0?muPairs.mass_bs:muPairs.mass)","m(#mu#mu) bs refit"],
  "hmass_geofit":["GeoFit::mass(muons[0].eta, muons[0].phi,GeoFit::PtCorrGeoFit(muons[0].d0_BS*muons[0].charge, muons[0].pt_Roch, muons[0].eta, 2018),muons[1].eta, muons[1].phi,GeoFit::PtCorrGeoFit(muons[1].d0_BS*muons[1].charge, muons[1].pt_Roch, muons[1].eta, 2018) )","m(#mu#mu) geoFit"]
  }


#class variable:
#    def __init__(self,name,bin,min,max,title,cut,color):
#      name: "",
#      title: "",
#      cut: "",
#      color: 
#      "mass_kinfit":"muPairs.mass_kinfit",
#        "pt_res": ... 
#

##########
## main ##
##########

def main(sample,variables_selection,cut):

  '''
  Functions taking sample and cut and producing dimuon mass and muon resolution 
  comparison between kinfit and pf muons, including triple gaussian fit.
  
  Example of running :
  python % -s ggh16 whp16 whm16 tth16 vbf16 -c inclusive BB XE absd0min0p002

  All possibilities are in the dictionaries file_names and cutstrings

  '''

  ROOT.gROOT.LoadMacro("GeoFitCorr_C.so")

  tree = get_tree(file_name)
  sample_type = sample

  ROOT.gStyle.SetFillStyle(4000) # transparent pads
  canvas = ROOT.TCanvas("c","cmass",600,600)
  resolution_canvas = ROOT.TCanvas("res_c","res_c",600,600)
  
#  hmass_pf = create_th1("hmass_pf","MuPair mass", 100, 120, 130,ROOT.kBlue,"m(#mu,#mu)")
#  hmass_kinfit = create_th1("hmass_kinfit","MuPair mass",50, 120, 130,ROOT.kRed,"m(#mu,#mu)")
 
  hmass_pf = create_th1("hmass_blue","MuPair mass", 50, 120, 130,ROOT.kBlue,variables_dictionary[variables_selection][1])
  hmass_kinfit = create_th1("hmass_red","MuPair mass",50, 120, 130,ROOT.kRed,variables_dictionary[variables_selection][1])
  
  hres_pf = create_th1("hres_pf","Muon resolution", 100,-0.2,0.2,ROOT.kBlue,"#Delta(p_{T},p_{T}^{GEN})/p_{T}^{GEN}")
  hres_red = create_th1("hres_red","Muon resolution", 100,-0.2,0.2,ROOT.kRed,"#Delta(p_{T},p_{T}^{GEN})/p_{T}^{GEN}")
  
  jet_selection = "( Sum$(jets.pt>20 && abs(jets.eta)<2.4 && jets.CSV>0.4941)>=0 ) "
  muon_selection = "(muons.pt > 20 && abs(muons.eta)<2.4 && muons.isMediumID==1 && muons.relIso < 0.25)"
  event_selection = "(muons.pt>30)"
  #event_selection = "(muons.pt>30 && ( muons[0].isHltMatched[2]==1 || muons[0].isHltMatched[3]==1 || muons[1].isHltMatched[2]==1 || muons[1].isHltMatched[3]==1 ) )"
  weightstring = "(GEN_wgt)" # * PU_wgt)"
  
  post_string = cut
  # cut string matching the post string
  cutstring=cutstrings[post_string]
  
  resolution_canvas.cd()
  reference_var = "(muons.pt-muons.GEN_pt)/muons.GEN_pt"
  #reference_var = "( GeoFit::PtCorrGeoFit(muons.d0_BS*muons.charge, muons.pt_Roch, muons.eta, 2018)-muons.GEN_pt)/muons.GEN_pt"
  #var="( (muons.pt_kinfit>0?muons.pt_kinfit:muons.pt) -muons.GEN_pt)/muons.GEN_pt>>hres_red"
  var="( (muons.pt_bs>0?muons.pt_bs:muons.pt) -muons.GEN_pt)/muons.GEN_pt>>hres_red"
  tree.Draw(var,"{0} * ({1} && {2} && {3})".format(weightstring,event_selection,muon_selection, cutstring) )
  tree.Draw("{0}>>hres_pf".format(reference_var),"{0} * ({1} && {2} && {3})".format(weightstring,event_selection,muon_selection, cutstring) )
  
  hres_pf.Draw("HIST")
  ROOT.gStyle.SetOptStat(1)
  stat_res_pf = ROOT.TPaveText()
  stat_res_pf = hres_pf.FindObject("stats")
  stat_res_pf.SetY1NDC(.7)
  stat_res_pf.SetY2NDC(.9)
  stat_res_pf.SetX1NDC(.7)
  stat_res_pf.SetX2NDC(.9)
  
  hres_red.Draw("HIST")
  ROOT.gStyle.SetOptStat(1)
  ROOT.gStyle.SetOptTitle(0)
  stat_res_kinfit = ROOT.TPaveText()
  stat_res_kinfit = hres_red.FindObject("stats")
  stat_res_kinfit.SetY1NDC(.5)
  stat_res_kinfit.SetY2NDC(.7)
  stat_res_kinfit.SetX1NDC(.9)
  stat_res_kinfit.SetX2NDC(.7)
  
  hres_red.Draw("HIST")
  hres_pf.Draw("HIST same")
  stat_res_pf.Draw("same")
  stat_res_kinfit.Draw("same")
  
  canvas.cd()
  var=variables_dictionary['hmass_PF'][0]#"muPairs.mass"
  #var=variables_dictionary['hmass_geofit'][0]
  var_histo="hmass_blue"
  #cutstring="(muons[1].d0_PV < 0 & muons[1].charge > 0 & muons[0].d0_PV > 0 & muons[0].charge < 0) || (muons[0].d0_PV < 0 & muons[0].charge > 0 & muons[1].d0_PV > 0 & muons[1].charge < 0)"
  tree.Draw("{0}>>{1}".format(var,var_histo),"{0} * ({1} && {2} && {3})".format(weightstring,event_selection,muon_selection, cutstring) )
#  var="(muPairs.mass_kinfit>0?muPairs.mass_kinfit:muPairs.mass)>>hmass_kinfit"
  #cutstring="(muons[1].d0_PV > 0 & muons[1].charge > 0 & muons[0].d0_PV < 0 & muons[0].charge < 0) || (muons[0].d0_PV > 0 & muons[0].charge > 0 & muons[1].d0_PV < 0 & muons[1].charge < 0)"
  var=variables_dictionary[variables_selection][0]#"muPairs.mass"
  var_histo="hmass_red"
  tree.Draw("{0}>>{1}".format(var,var_histo),"{0} * ({1} && {2} && {3})".format(weightstring,event_selection,muon_selection, cutstring) )
  
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
  ROOT.gStyle.SetOptTitle(0)
  ROOT.gStyle.SetOptFit(1112)
  stat_pf = ROOT.TPaveText()
  stat_pf = hmass_pf.FindObject("stats")
  #stat_pf.SetLabel("Bleu")
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
  #stat_kinfit.SetLabel("Red")
  #stat_kinfit.SetTextSize(0.05)
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
  
#  textpad = ROOT.TPaveText(.13,.85,.5,.90,"NDC ARC")
#  textpad.AddText("Fit mean difference : {:.3f} GeV".format(abs(fit_pf.GetMaximumX() - fit_kinfit.GetMaximumX())))
  textpad = ROOT.TPaveText(.15,.75,.4,.88,"NDC ARC") 
  textpad.AddText("FWMH BS/PF ratio = {:.3f}".format(fwhm_kinfit/fwhm_pf))
  textpad.AddText("FWHM/Mean PF = {:.4f}".format(fwhm_pf/fit_pf.GetMaximumX()))
  textpad.AddText("FWHM/Mean BS = {:.4f}".format(fwhm_kinfit/fit_kinfit.GetMaximumX()))
  textpad.SetFillColor(4000)
  textpad.Draw("same")


  cmstex = ROOT.TLatex();
  cmstex.SetTextSize(0.03);
##  cmstex.DrawLatexNDC(0.11,0.91,"#scale[1.5]{CMS} Private");
  cmstex.DrawLatexNDC(0.11,0.91,"#font[42]{#bf{CMS} #scale[0.8]{#it{Internal}}}");
  cmstex.Draw("same");
  
  fit_pf.SetLineColor(ROOT.kBlue)
  fit_pf.Draw("same")
  
  fit_kinfit.SetLineColor(ROOT.kRed)
  fit_kinfit.Draw("same")
  
  #ROOT.gPad.BuildLegend() 
  legend = ROOT.TLegend(.13,.63,.45,.70) # (.13,.78,.45,.85)
  legend.SetLineColor(0)
  legend.AddEntry("hmass_red","BS refit")
  legend.AddEntry("hmass_blue","PF")
  #legend.AddEntry("hmass_blue","GeoFit")
  #legend.AddEntry("hmass_red","d0(#mu^{+}) > 0, d0(#mu^{-}) < 0")
  #legend.AddEntry("hmass_blue","d0(#mu^{+}) < 0, d0(#mu^{-}) > 0")
  legend.Draw("same")

  canvas.Print("{0}_{1}_{2}.pdf".format(variables_selection,sample_type,post_string))
  resolution_canvas.Print("hres_{0}_{1}.pdf".format(sample_type,post_string))
  canvas.Print("{0}_{1}_{2}.png".format(variables_selection,sample_type,post_string))
  resolution_canvas.Print("hres_{0}_{1}.png".format(sample_type,post_string))
  canvas.Print("{0}_{1}_{2}.root".format(variables_selection,sample_type,post_string))
  resolution_canvas.Print("hres_{0}_{1}.root".format(sample_type,post_string))
   
  print(tree.GetEntries())
  


#########################
## execution bahavious ##
#########################

if __name__ == "__main__":

  for samp in args.samps:
    file_name = file_names[samp]
    for var in args.variables_selection:
      for cut in args.cuts:
        main(samp,var,cut)
  sys.exit(0);


