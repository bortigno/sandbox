from CRABClient.UserUtilities import config
config = config()

import datetime, time
ts = time.time()
st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d-%H-%M')

zd_mass = '35'
number_of_jets = '2'
epsilon = '2e-2'
custom_string_for_dataset = ''
step = 'LHE-GEN-SIM'

job_label = 'ZD_UpTo'+number_of_jets+'j_MZD'+zd_mass+'_Eps'+epsilon
config.General.requestName = st+'mc_genproduction_'+step+'_'+job_label+custom_string_for_dataset
config.General.transferOutputs = True
config.General.transferLogs = False

config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = 'externalLHEProducer_and_PYTHIA8_Hadronizer_zd'+number_of_jets+'j_mzd'+zd_mass+'_'+step+'_cfg.py'
config.JobType.inputFiles = ['externalLHEProducer_and_PYTHIA8_Hadronizer_cff.py','/afs/cern.ch/work/b/bortigno/darkphotons/genproductions/bin/MadGraph5_aMCatNLO/darkphoton_slc6_amd64_gcc481_CMSSW_7_1_30_tarball.tar.xz.'+job_label+'.tar.xz']
config.JobType.numCores = 8
config.JobType.scriptExe = 'lhe_gen-sim_steps.sh'
#config.JobType.outputFiles = ['cmsgrid_final.lhe']

config.Data.outputPrimaryDataset = job_label
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 1000 # the number of events here must match the number of events in the exeternalLHEProducer
NJOBS = 10
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.outLFNDirBase = '/store/user/bortigno/mc_genproduction/darkphoton/'+step+'/'+job_label
config.Data.outputDatasetTag = 'PUMoriond17-Realistic25ns13TeVEarly2017Collision-93X_mc2017_realistic_v3-'+step
config.Data.publication = True
config.Data.publishDBS = 'https://cmsweb.cern.ch/dbs/prod/phys03/DBSWriter/'

#config.Site.whitelist = ['T2_CH_CERN']
config.Site.blacklist = ['T2_PK_NCP','T2_KR_KNU']
config.Site.storageSite = 'T2_CH_CERN'
