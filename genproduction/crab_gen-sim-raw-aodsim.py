from CRABClient.UserUtilities import config
config = config()

import datetime, time
ts = time.time()
st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d-%H-%M')

zd_mass = '120'
number_of_jets = '2'
epsilon = '2e-2'
custom_string_for_dataset = ''
step = 'GEN-SIM-RAW-AODSIM'
#total number of events is nEvents * NJOBS
nEventsPerJob = 1000
nJobs = 100
totalEvents = nEventsPerJob*nJobs


#sample dictionary
sampleDic = { 
  '55':'/ZD_UpTo2j_MZD55_Eps2e-2/bortigno-PUMoriond17-Realistic25ns13TeVEarly2017Collision-93X_mc2017_realistic_v3-LHE-6587ad5f376bd4eec46c642b5372932e/USER',
  '60':'/ZD_UpTo2j_MZD60_Eps2e-2/bortigno-PUMoriond17-Realistic25ns13TeVEarly2017Collision-93X_mc2017_realistic_v3-LHE-b87b3a6bdecc3d09b174761b6043d405/USER',
  '65':'/ZD_UpTo2j_MZD65_Eps2e-2/bortigno-PUMoriond17-Realistic25ns13TeVEarly2017Collision-93X_mc2017_realistic_v3-LHE-16cfadf8a05081630919cb2819dac26d/USER',
  '70':'/ZD_UpTo2j_MZD70_Eps2e-2/bortigno-PUMoriond17-Realistic25ns13TeVEarly2017Collision-93X_mc2017_realistic_v3-LHE-010fac160d1a5a6e9d0f08ce4945232b/USER',
  '75':'/ZD_UpTo2j_MZD75_Eps2e-2/bortigno-PUMoriond17-Realistic25ns13TeVEarly2017Collision-93X_mc2017_realistic_v3-LHE-6a44bc7642872df336658cbc6c96510f/USER',
  '80':'/ZD_UpTo2j_MZD80_Eps2e-2/bortigno-PUMoriond17-Realistic25ns13TeVEarly2017Collision-93X_mc2017_realistic_v3-LHE-295e13eef4b2aba452503ecac1bce9cf/USER',
  '85':'/ZD_UpTo2j_MZD85_Eps2e-2/bortigno-PUMoriond17-Realistic25ns13TeVEarly2017Collision-93X_mc2017_realistic_v3-LHE-b3158ddbb2e5ed7f5b79ae0c4f15f378/USER',
  '90':'/ZD_UpTo2j_MZD90_Eps2e-2/bortigno-PUMoriond17-Realistic25ns13TeVEarly2017Collision-93X_mc2017_realistic_v3-LHE-ab6210557a31b220ec271fecd91b2640/USER',
  '105':'/ZD_UpTo2j_MZD105_Eps2e-2/bortigno-PUMoriond17-Realistic25ns13TeVEarly2017Collision-93X_mc2017_realistic_v3-LHE-a32c6e0e9403f9a298f72a5ecf2bd4f3/USER',
  '110':'/ZD_UpTo2j_MZD110_Eps2e-2/bortigno-PUMoriond17-Realistic25ns13TeVEarly2017Collision-93X_mc2017_realistic_v3-LHE-8216ed3de64a1796860db48d8929256c/USER',
  '115':'/ZD_UpTo2j_MZD115_Eps2e-2/bortigno-PUMoriond17-Realistic25ns13TeVEarly2017Collision-93X_mc2017_realistic_v3-LHE-344a60491efbcbfaa6f651eec627d2c5/USER',
  '120':'/ZD_UpTo2j_MZD120_Eps2e-2/bortigno-PUMoriond17-Realistic25ns13TeVEarly2017Collision-93X_mc2017_realistic_v3-LHE-b52bb41af1dc6f373f2089eb2919cc15/USER',
  '125':'/ZD_UpTo2j_MZD125_Eps2e-2/bortigno-PUMoriond17-Realistic25ns13TeVEarly2017Collision-93X_mc2017_realistic_v3-LHE-e4a3eca9ea42f5248633ece70b42f936/USER',
  '130':'/ZD_UpTo2j_MZD130_Eps2e-2/bortigno-PUMoriond17-Realistic25ns13TeVEarly2017Collision-93X_mc2017_realistic_v3-LHE-583020e56553328011b4e47e6bbbff48/USER',
  '135':'/ZD_UpTo2j_MZD135_Eps2e-2/bortigno-PUMoriond17-Realistic25ns13TeVEarly2017Collision-93X_mc2017_realistic_v3-LHE-6aa7d50fe1c50e2896ab029c26e20c81/USER',
  '145':'/ZD_UpTo2j_MZD145_Eps2e-2/bortigno-PUMoriond17-Realistic25ns13TeVEarly2017Collision-93X_mc2017_realistic_v3-LHE-9510e1f786ebc11da0d7e57b6a3ec9d4/USER',
  '150':'/ZD_UpTo2j_MZD150_Eps2e-2/bortigno-PUMoriond17-Realistic25ns13TeVEarly2017Collision-93X_mc2017_realistic_v3-LHE-b3f93073db25b854ea1d6aa58ccb51d7/USER',
  '160':'/ZD_UpTo2j_MZD160_Eps2e-2/bortigno-PUMoriond17-Realistic25ns13TeVEarly2017Collision-93X_mc2017_realistic_v3-LHE-211264d82a0a9ea328e6dc02c71a09dc/USER',
  '165':'/ZD_UpTo2j_MZD165_Eps2e-2/bortigno-PUMoriond17-Realistic25ns13TeVEarly2017Collision-93X_mc2017_realistic_v3-LHE-5fa4ca8ec92e02a6fd5a6e113e761952/USER',
  '170':'/ZD_UpTo2j_MZD170_Eps2e-2/bortigno-PUMoriond17-Realistic25ns13TeVEarly2017Collision-93X_mc2017_realistic_v3-LHE-b727ed07d651499b7f04671c8f667872/USER',
  '175':'/ZD_UpTo2j_MZD175_Eps2e-2/bortigno-PUMoriond17-Realistic25ns13TeVEarly2017Collision-93X_mc2017_realistic_v3-LHE-28de74d02c43eaf2efe8d8e741f68501/USER',
  '180':'/ZD_UpTo2j_MZD180_Eps2e-2/bortigno-PUMoriond17-Realistic25ns13TeVEarly2017Collision-93X_mc2017_realistic_v3-LHE-4ad9aab91e6c4e01cc4e92508ddc7eb1/USER',
  '185':'/ZD_UpTo2j_MZD185_Eps2e-2/bortigno-PUMoriond17-Realistic25ns13TeVEarly2017Collision-93X_mc2017_realistic_v3-LHE-ee6482f2ad1e1fe907f9d9a84bc94965/USER',
  '190':'/ZD_UpTo2j_MZD190_Eps2e-2/bortigno-PUMoriond17-Realistic25ns13TeVEarly2017Collision-93X_mc2017_realistic_v3-LHE-88064c4e450ab1a3a883b45822eace5b/USER',
  '180':'/ZD_UpTo2j_MZD195_Eps2e-2/bortigno-PUMoriond17-Realistic25ns13TeVEarly2017Collision-93X_mc2017_realistic_v3-LHE-2f5bc6d99ba19290d14779f9558e2d3c/USER',
  '200':'/ZD_UpTo2j_MZD200_Eps2e-2/bortigno-PUMoriond17-Realistic25ns13TeVEarly2017Collision-93X_mc2017_realistic_v3-LHE-db11759337d3e5d00c9d00458d0a5729/USER'
  }

job_label = 'ZD_UpTo'+number_of_jets+'j_MZD'+zd_mass+'_Eps'+epsilon
config.General.requestName = st+'mc_genproduction_'+step+'_'+job_label+custom_string_for_dataset
config.General.transferOutputs = True
config.General.transferLogs = False

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'darkphoton_RunIIFall17DRPremix_AODSIM_step3_cfg.py' #dummy cfg with the right output file name
config.JobType.numCores = 8
config.JobType.scriptExe = 'gen-sim-raw_aodsim_steps.sh'
config.JobType.scriptArgs = ['zd_mass='+zd_mass]
config.JobType.inputFiles = ['darkphoton_RunIIFall17DRPremix_AODSIM_step3_cfg.py','Hadronizer_TuneCP5_13TeV_MLM_5f_max2j_LHE_pythia8_cff.py','customiseGenSimRawAodsim.py']
config.JobType.maxMemoryMB = 6000
config.JobType.outputFiles = ['darkphoton_step3.root']

#config.Data.inputDataset = '/ZD_UpTo2j_MZD125_Eps2e-2/bortigno-PUMoriond17-Realistic25ns13TeVEarly2017Collision-93X_mc2017_realistic_v3-LHE-e4a3eca9ea42f5248633ece70b42f936/USER' 
config.Data.inputDataset = sampleDic[zd_mass]
config.Data.inputDBS = 'phys03'
#config.Data.outputPrimaryDataset = job_label
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1 # the number of events here must match the number of events in the externalLHEProducer
#config.Data.totalUnits = 
config.Data.outLFNDirBase = '/store/user/bortigno/mc_genproduction/darkphoton/'+step+'/'+job_label
config.Data.outputDatasetTag = 'PUMoriond17-Realistic25ns13TeVEarly2017Collision-93X_mc2017_realistic_v3-'+step
config.Data.publication = True
config.Data.publishDBS = 'https://cmsweb.cern.ch/dbs/prod/phys03/DBSWriter/'

config.Site.whitelist = ['T2_CH_CERN']
config.Site.blacklist = ['T2_PK_NCP','T2_KR_KNU']
config.Site.storageSite = 'T2_CH_CERN'
