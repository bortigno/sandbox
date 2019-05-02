# Collection of commands to get histograms from TCanvas.
# These tools will be useful to edit histograms saves in .root - which usually save only the TCanvas

import ROOT

infile = ROOT.TFile("plot.root")

infile.ls()

c1= ROOT.TCanvas() 
c1 = infile.Get("c1")

# this is giving the list of the objects
c1.GetListOfPrimitives().Print()

# ROOT equivalent:
# c1->GetListOfPrimitives()->Print()

#Here an example of output:
#Collection name='TList', class='TList', size=10
# TFrame  X1=0.000000 Y1=0.000000 X2=3.000000 Y2=0.153941 FillStyle=1001
# TH1.Print Name  = hEt_Data_barrel, Entries= 690523, Total sum= 1
# TH1.Print Name  = hEt_Data_endcap, Entries= 222584, Total sum= 1
# Function based on a list of points from a compiled based function: CBFuncAsymm.  Ndim = 1, Npar = 7, Npx = 103
#Contained histogram
#TH1.Print Name  = Func, Entries= 3000, Total sum= 16.5079
# Function based on a list of points from a compiled based function: CBFuncAsymm.  Ndim = 1, Npar = 7, Npx = 103
#Contained histogram
#TH1.Print Name  = Func, Entries= 3000, Total sum= 16.573
# TLegend  X1=1.831169 Y1=0.103960 X2=2.610390 Y2=0.133949 FillStyle=1001
# Collection name='TList', class='TList', size=2
#  TLegendEntry: Object hEt_Data_barrel Label Barrel Option lp
#  TLegendEntry: Object hEt_Data_endcap Label Endcaps Option lp
# Text  X=0.660000 Y=0.910000 Text=40.9 fb^{-1} (13 TeV) Font=62 Size=0.035000 Align=11
# Text  X=0.110000 Y=0.910000 Text=#scale[1.5]{CMS} Font=62 Size=0.030000 Align=11
# Text  X=0.550000 Y=0.500000 Text=#splitline{|#eta|_{Barrel} < 1.305}{1.479 < |#eta|_{Endcap} < 2.1} Font=62 Size=0.035000 Align=11
# Text  X=0.550000 Y=0.350000 Text=p_{T}^{#tau, offline} > 30 GeV Font=62 Size=0.035000 Align=11


# Here you can see that there is a histogram called hEt_Data_barrel 
# A way to test this is ROOT is:
# hEt_Data_barrel_1->ClassName()
# (const char *) "TH1F"

hEt_Data_barrel_obj = c1.GetPrimitive("hEt_Data_barrel")
# ROOT equivalent:
# TObject * hEt_Data_barrel_obj = c1->GetPrimitive("hEt_Data_barrel")

h1 = ROOT.TH1F()
h1 = hEt_Data_barrel_obj
# ROOT equivalent:
# TH1F * h1 = new TH1F()
# h1=(TH1F*)hEt_Data_barrel_obj
# (TH1F *) 0x7feb172a4b30

c2 = ROOT.TCanvas("c2","c2",600,600)
h1.Draw()
c2.Print("test_c2.pdf")


