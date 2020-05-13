import ROOT

from plotMass import file_names, get_tree 


ROOT.gROOT.LoadMacro("GeoFitCorr_C.so")


samp = "ggh18bsr_hadded" 
file_name = file_names[samp] 
tree = get_tree(file_name)


var_name = "ptreldiff-geofit-pf" #"ptcorr-geofit-bs"
var_dic = {"ptreldiff-geofit-pf":"(muons[0].pt-GeoFit::PtCorrGeoFit(muons[0].d0_BS*muons[0].charge, muons[0].pt_Roch, muons[0].eta, 2018))/muons[0].pt" ,
           "ptreldiff-geofit-bs":"(muons[0].pt_bs-GeoFit::PtCorrGeoFit(muons[0].d0_BS*muons[0].charge, muons[0].pt_Roch, muons[0].eta, 2018))/muons[0].pt_bs",
           "ptdiff-geofit-pf":"muons[0].pt-GeoFit::PtCorrGeoFit(muons[0].d0_BS*muons[0].charge, muons[0].pt_Roch, muons[0].eta, 2018)" ,
           "ptdiff-geofit-bs":"muons[1].pt_bs-GeoFit::PtCorrGeoFit(muons[0].d0_BS*muons[0].charge, muons[0].pt_Roch, muons[0].eta, 2018)" }

muon_selection = "(muons.pt > 20 & abs(muons.eta)<2.4 & muons.isMediumID==1 & muons.relIso < 0.25)"
event_selection = "muons.pt>20" # dummy
#event_selection = "(muons.pt>30 && ( muons[0].isHltMatched[2]==1 || muons[0].isHltMatched[3]==1 || muons[1].isHltMatched[2]==1 || muons[1].isHltMatched[3]==1 ) )"
weightstring = "(GEN_wgt * PU_wgt)"

cut_string = "muons.pt>20" # dummy

variable = var_dic[var_name]

c1 = ROOT.TCanvas("c1","c1",600,600)
histo_name = "h1_{0}".format(var_name)
histo_title = "GeoFit - PF refit pt correlation"
th1 = ROOT.TH1F(histo_name,histo_title,100,-0.02,0.02)
th1.GetXaxis().SetTitle("#Delta p_{T}/p_{T}(PF - GeoFit)")

tree.Draw("{0}>>{1}".format(variable,histo_name),"{0} * ({1} & {2} & {3})".format(weightstring,event_selection,muon_selection,cut_string),"H")

c1.SaveAs("{0}.pdf".format(histo_name))


