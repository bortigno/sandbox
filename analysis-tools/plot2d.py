import ROOT

from plotMass import file_names, get_tree 


ROOT.gROOT.LoadMacro("GeoFitCorr_C.so")


samp = "ggh18bsr_hadded" 
file_name = file_names[samp] 
tree = get_tree(file_name)


var_name = "corr-geofit-bs" #"ptcorr-geofit-bs"
var_dic = {"corr-geofit-bs":"(muons[0].pt_bs/muons[0].pt):(GeoFit::PtCorrGeoFit(muons[0].d0_BS*muons[0].charge, muons[0].pt_Roch, muons[0].eta, 2018)/muons[0].pt)",
           "ptcorr-geofit-pf":"muons[0].pt:GeoFit::PtCorrGeoFit(muons[0].d0_BS*muons[0].charge, muons[0].pt_Roch, muons[0].eta, 2018)" ,
           "ptcorr-geofit-bs":"muons[0].pt_bs:GeoFit::PtCorrGeoFit(muons[0].d0_BS*muons[0].charge, muons[0].pt_Roch, muons[0].eta, 2018)"}

muon_selection = "(muons.pt > 20 & abs(muons.eta)<2.4 & muons.isMediumID==1 & muons.relIso < 0.25)"
event_selection = "muons.pt>20" # dummy
#event_selection = "(muons.pt>30 && ( muons[0].isHltMatched[2]==1 || muons[0].isHltMatched[3]==1 || muons[1].isHltMatched[2]==1 || muons[1].isHltMatched[3]==1 ) )"
weightstring = "(GEN_wgt * PU_wgt)"

cut_string = "muons.pt>20" # dummy

variable = var_dic[var_name]

c1 = ROOT.TCanvas("c1","c1",600,600)
histo_name = "h2_{0}".format(var_name)
histo_title = "GeoFit - BS correction correlation"
th2 = ROOT.TH2F(histo_name,histo_title,100,0.98,1.02,100,0.98,1.02)
th2.GetXaxis().SetTitle("p_{T} (BS)/ p_{T} (PF)")
th2.GetYaxis().SetTitle("p_{T} (GeoFit)/ p_{T} (PF)")
th2.GetYaxis().SetTitleOffset(1.2)

tree.Draw("{0}>>{1}".format(variable,histo_name),"{0} * ({1} & {2} & {3})".format(weightstring,event_selection,muon_selection,cut_string),"COLZ")

#th2.SetLineColor(ROOT.kRed)
th2.Draw("COLZ")
ROOT.gPad.Update()
stat_th2 = th2.FindObject("stats")
print(th2.GetRMS(1))
print(th2.GetRMS(2))
ROOT.gPad.Update()
#ROOT.gStyle.SetOptStat(1111)
stat_th2.SetY1NDC(.3)
stat_th2.SetY2NDC(.5)
stat_th2.SetX1NDC(.9)
stat_th2.SetX2NDC(.7)
stat_th2.Draw("same")

c1.SaveAs("{0}.pdf".format(histo_name))


