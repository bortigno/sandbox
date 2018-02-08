import os
import glob


massdirlist=[]
starteosdir="/eos/cms/store/user/bortigno/mc_genproduction/darkphoton/LHE/"
massdirlist=os.listdir(starteosdir)
rootext='.*root'
print(massdirlist)
filelist={}
for root, folder, files in os.walk(starteosdir):
 if len(files) > 50 and files[0].endswith('.root') and not root.endswith('failed'):
    filename = 'mZD' + filter(str.isdigit,root[root.find('MZD'):root.find('MZD')+6])
    print(filename)
    f = open('lheInputFileList_'+filename+'_cfi.py','w')
    f.write("""
import FWCore.ParameterSet.Config as cms

# Input source
source = cms.Source("PoolSource",
         duplicateCheckMode = cms.untracked.string('checkEachFile'), #a bit safer could be checkEachFile
         fileNames = cms.untracked.vstring([
""")
    #print('root = ' + root)
    #print('folder = ') 
    #print(folder)
    #print('files = ') 
    #print(files)
    filelist[root]=files
    #print('filelist = ')
    #pr int(filelist)
    #print(filelist[root])
    for rootfile in filelist[root]:
      f.write('\''+root.replace('/eos/cms','')+'/'+rootfile+'\',\n')
    f.write(']))')


