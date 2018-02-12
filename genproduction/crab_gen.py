from CRABClient.UserUtilities import config
config = config()

import datetime, time
ts = time.time()
st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d-%H-%M')

zd_mass = '125'
number_of_jets = '2'
epsilon = '2e-2'
custom_string_for_dataset = ''
step = 'LHE-GEN-SIM'

job_label = 'ZD_UpTo'+number_of_jets+'j_MZD'+zd_mass+'_Eps'+epsilon+'_QCUT23_'+step
config.General.requestName = st+'mc_genproduction_'+step+'_'+job_label+custom_string_for_dataset
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
#config.JobType.generator='lhe'
config.JobType.psetName = 'hadronizer/PYTHIA8_Hadronizer_zd2j_mzd'+zd_mass+'_LHE-GEN-SIM-QCUT_23_cfg.py'
#config.JobType.inputFiles = ['hadronizer/PYTHIA8_Hadronizer_zd2j_mzd'+zd_mass+'_LHE-GEN-SIM-QCUT_23_cfg.py','lheInputFileList_mZD'+zd_mass+'_cfi.py']
config.JobType.numCores = 8

config.Data.inputDataset = '/ZD_UpTo2j_MZD125_Eps2e-2/bortigno-PUMoriond17-Realistic25ns13TeVEarly2017Collision-93X_mc2017_realistic_v3-LHE-e4a3eca9ea42f5248633ece70b42f936/USER'
config.Data.inputDBS='phys03'
#config.Data.outputPrimaryDataset = job_label
config.Data.splitting = 'Automatic'
#config.Data.unitsPerJob = 1000 # the number of events here must match the number of events in the externalLHEProducer
#NJOBS = 100
#config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.outLFNDirBase = '/store/user/bortigno/mc_genproduction/darkphoton/'+step+'/'+job_label
config.Data.outputDatasetTag = 'PUMoriond17-Realistic25ns13TeVEarly2017Collision-93X_mc2017_realistic_v3-'+step
config.Data.publication = True
config.Data.publishDBS = 'https://cmsweb.cern.ch/dbs/prod/phys03/DBSWriter/'

#config.Site.whitelist = ['T2_CH_CERN']
#config.Site.blacklist = ['T2_PK_NCP','T2_KR_KNU']
config.Site.storageSite = 'T2_CH_CERN'
