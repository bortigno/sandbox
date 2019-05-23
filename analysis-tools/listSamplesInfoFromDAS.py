#!/usr/bin/env python
"""
DBS 3 Client Example.   This script is called 

./listSampleInfoFromDAS.py 

"""

# api info https://github.com/dmwm/DBS/blob/master/Client/src/python/dbs/apis/dbsClient.py

import sys
from dbs.apis.dbsClient import DbsApi
from python.Samples import *
import gc
import re


def get_sample_list(sample_group):
  sample_list = []
  if sample_group == 'all':
    # get all objects in sample
    sample_list = [o for o in gc.get_objects() if isinstance(o, sample)]
  elif sample_group == 'background':
    # get only background
    sample_list = Background
  elif sample_group == 'signal':
    # get only the signal
    sample_list = Signal 
  else:
    print('No valid sample group')
  return sample_list

def main():
#  args=sys.argv[1:]
#  data=args[0]

  sample_group = 'signal' # signal, background, data, all
  sample_list = get_sample_list(sample_group)
  sample_list.sort()

  url="https://cmsweb.cern.ch/dbs/prod/global/DBSReader"
  api=DbsApi(url=url)

  for samp in sample_list:
    outputDataSets = ''
    #print('Checking {1}'.format(samp.DAS))
    outputDataSets = api.listDatasets(dataset=samp.DAS, detail = True, dataset_access_type='VALID')
 
    if outputDataSets:
      for ds in outputDataSets:
       #print('{0}'.format(ds['dataset']))
       #print('{0}'.format(ds['primary_ds_name']))
       #print('{0}'.format(ds['xtcrosssection']))
       nevents = api.listBlockSummaries(dataset=ds['dataset'])
       #print(nevents[0]['num_event'])    
       # this to create a table for the paper with dataset name and number of events 
       print('verb@ {0} @ & {1:.2e} & XX \\\\ '.format(ds['primary_ds_name'],nevents[0]['num_event'])) 
  sys.exit(0);

if __name__ == "__main__":
    main()
    sys.exit(0);

