#used in pier@jarvis:~/Physics/l1trigger/L1TPaper/material/mumuplotextraction/
import sys, string,os 
import ROOT

#this is the format of the txt filed used :
#0.13910355486862436 3.5668789808920853E-4
#0.33384853168469864 5.350318471337989E-4
#0.6398763523956728 8.917197452229519E-4
#0.9180834621329215 8.917197452229519E-4
#1.1406491499227203 8.917197452229519E-4
#1.3910355486862445 8.917197452229519E-4
#1.655332302936631 8.917197452229519E-4
#1.9057187017001542 8.917197452229519E-4
#2.1561051004636784 8.917197452229519E-4
#2.4064914992272026 0.0010700636942675423
#2.656877897990727 0.0014267515923567231


def make_histo(txtfile,histo):
  ifn = os.path.expandvars(txtfile)
  infile = open (ifn, 'r')
  lines= infile.readlines()
  title = "Title" # lines[0] 
  labels = string.split("x y z") # string.split(lines[1])
  i=0
  for line in lines[2:]:
    words = string.split(line)
    row = map(float, words)
    row.insert(0,i*0.25)
#    apply( ntuple.Fill, row)
    print row
    histo.Fill(i*0.25,row[-1])
    i+=1

def main():
  outfile = ROOT.TFile("out.root","RECREATE")
  
#  ntuple = ROOT.TNtuple('ntuple', title, string.join(labels,':'))
  
  hextr = ROOT.TH1F("hextr","hextr",80,0,20) 
  hnoextr = ROOT.TH1F("hnoextr","hnoextr",80,0,20) 
  hreco = ROOT.TH1F("hreco","hreco",80,0,20) 
 
  make_histo("mumuhistopoints.txt",hextr)
  make_histo("mumuhistopointsnoextrapolation.txt",hnoextr)
  make_histo("mumuhistopointsRECO.txt",hreco)

  outfile.Write()

if __name__ == "__main__":
    main()
    sys.exit(0)


