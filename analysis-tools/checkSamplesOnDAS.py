#!/usr/bin/env python
"""
DBS 3 Client Example.   This script is called 

./checkSampleOnDAS.py 

"""


import sys
from dbs.apis.dbsClient import DbsApi
from python.Samples import *
import gc
import re

def main():
#  args=sys.argv[1:]
#  data=args[0]
  sample_list = []
  sample_list = [o for o in gc.get_objects() if isinstance(o, sample)]

  url="https://cmsweb.cern.ch/dbs/prod/global/DBSReader"
  api=DbsApi(url=url)

  for samp in sample_list:
    outputDataSets = ''
    #print('Checking {1}'.format(samp.DAS))
    outputDataSets = api.listDatasets(dataset=samp.DAS, dataset_access_type='VALID')
    if not outputDataSets :
      print('{0} does not correspond to any VALID DAS sample.'.format(samp.DAS))
      prodOutputDataset = api.listDatasets(dataset=samp.DAS, dataset_access_type='PRODUCTION')
      if (prodOutputDataset):
        print('Dataset {0} is in PRODUCTION state.'.format(prodOutputDataset))
        continue
      print('Possible alternatives: ')
      altsampDAS = samp.DAS
      altsampDAS = re.sub(r'v[0-9]*','v*', samp.DAS)
      altsampDAS = re.sub(r'13TeV[a-zA-Z0-9_-]*/','*/', altsampDAS)
      altsampDAS = re.sub(r'4F_TuneCP5_','*',altsampDAS)
      altsampDAS = re.sub(r'_PSweights_','*',altsampDAS)
      print(altsampDAS)
      matchedAltSamples = api.listDatasets(dataset=altsampDAS, dataset_access_type='*')
      print(matchedAltSamples)
#    for dataset in outputDataSets:
#        inp=dataset['dataset']
#        print inp
#        reply= api.listBlockSummaries(dataset=inp)  
#        print reply[0]['num_event']
  sys.exit(0);

if __name__ == "__main__":
    main()
    sys.exit(0);

