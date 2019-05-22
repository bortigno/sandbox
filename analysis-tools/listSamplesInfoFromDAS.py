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
    outputDataSets = api.listDatasets(dataset=samp.DAS, detail = True, dataset_access_type='VALID')
 
    if outputDataSets:
      for ds in outputDataSets:
       print('{0}'.format(ds['dataset']))
       print('{0}'.format(ds['primary_ds_name']))
       print('{0}'.format(ds['xtcrosssection']))
       nevents = api.listBlockSummaries(dataset=ds['dataset'])
       print(nevents[0]['num_event'])    
       # this to create a table for the paper with dataset name and number of events 
       print('verb@ {0} & {1}'.format(ds['primary_ds_name'],nevents[0]['num_event'])) 
  sys.exit(0);

if __name__ == "__main__":
    main()
    sys.exit(0);

