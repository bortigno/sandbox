import ROOT
import sys

infile_name = "/eos/cms/store/group/phys_higgs/HiggsExo/H2Mu/UF/ntuples/data_2017_and_mc_fall17/SingleMuon/SingleMu_2017B/180605_162616/0000/tuple_47.root"
print("Opening file %s" % infile_name)
infile = ROOT.TFile(infile_name,"READ")
print("%s file opened" %infile_name)
t = infile.Get("dimuons/tree")

nev ={}
print("Entries in the tree")
nev["total"] = t.GetEntries()

preselection = "( Sum$(jets.pt>20 && abs(jets.eta)<2.4 && jets.CSV>0.4941)>=0 )  && muons.pt>30 &&  muPairs.mass > 80 && muPairs.mass < 85 && ((muons[0].isHltMatched[2]==1 || muons[0].isHltMatched[3]==1) && (muons[0].isHltMatched[2]==1 || muons[0].isHltMatched[3]==1)) && eles.passConversionVeto==1"

print("Preselection string: {0}" .format(preselection))
nev[preselection] = t.GetEntries(preselection)

print("Numner of events after preselection {0}" .format(nev[preselection]))

