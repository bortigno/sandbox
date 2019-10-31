import ROOT 

#barrel
#name = "2d_best_probe_absEtaMin0_absEtaMax0p83_ptmin10_deta0p15_matched_l1_muon_qualMin8_ptmin7_dinvrecopt"
#overlap
#name = "2d_best_probe_absEtaMin0p83_absEtaMax1p24_ptmin10_deta0p15_matched_l1_muon_qualMin8_ptmin7_dinvrecopt"
#endcap
name = "2d_best_probe_absEtaMin1p24_absEtaMax2p4_ptmin10_deta0p15_matched_l1_muon_qualMin8_ptmin7_dinvrecopt"

infile = ROOT.TFile( "{0}.root".format(name) )

infile.ls()

c1 = ROOT.TCanvas()
c1 = infile.Get("c_{0}".format(name))

c1.GetListOfPrimitives().Print()

h2 = c1.GetPrimitive("{0}".format(name))

h2new = h2
c2 = ROOT.TCanvas("c2","c2",600,600)
#h2.Draw()

#for b in range(0,h2.GetXaxis().GetMaximum()*h2.GetYaxis().GetMaximum()):
#  h2.UpdateBinContent(b,h2.GetBinContent(b)*h2.Get)

weight = [1] * h2.GetNbinsX()

for ix in range(0,h2.GetNbinsX()):
  sum_ = 0.
  for iy in range(0,h2.GetNbinsY()):
    sum_ += h2.GetBinContent(ix,iy)
  weight[ix] = 1/sum_ if sum_ > 0 else 1

print(weight)

for ix in range(0,h2.GetNbinsX()):
  for iy in range(0,h2.GetNbinsY()):
    bxy = h2.GetBinContent(ix,iy)
#    weight = (h2.GetXaxis().GetBinCenter(ix)) if ix > 0 else 1
#    if iy > 0. : print ("ix_value = {0}, weight = {1}".format(h2.GetXaxis().GetBinCenter(ix),weight))
    h2new.SetBinContent(ix,iy,bxy*weight[ix])

h2new.GetXaxis().SetRangeUser(0,0.1)
h2new.GetYaxis().SetRangeUser(0,0.1)

h2new.Draw("COLZ")
c2.Print("test_{0}.pdf".format(name))




