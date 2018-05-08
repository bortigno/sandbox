#!/bin/bash
source /cvmfs/cms.cern.ch/cmsset_default.sh
export SCRAM_ARCH=slc6_amd64_gcc630
CMSSW_release=CMSSW_9_4_6

if [ -r ${CMSSW_release}/src ] ; then 
 echo release ${CMSSW_release} already exists
else
scram p CMSSW ${CMSSW_release}
fi
cd ${CMSSW_release}/src
eval `scram runtime -sh`

#make voms-proxy-init -voms cms available in the CERN batch https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookXrootdService
#export X509_USER_PROXY=//afs/cern.ch/user/b/bortigno/workspace/sandbox/genproduction/x509up_u52020

samplename="darkphoton"
nEvents=-1

[ -d Configuration/GenProduction/python/ ] || mkdir -p Configuration/GenProduction/python/
cp -v ../../Hadronizer_TuneCP5_13TeV_MLM_5f_max2j_LHE_pythia8_cff.py Configuration/GenProduction/python/
cp -v ../../customiseGenSimRawAodsim.py Configuration/GenProduction/python/

scram b
cd ../../


echo "================= cmsDriver preparing Step 2 ====================" | tee -a job.log
# Preparing the configuration for running GEN-SIM-RAW aka step2
#cmsDriver.py Configuration/GenProduction/python/Hadronizer_TuneCP5_13TeV_MLM_5f_max2j_LHE_pythia8_cff.py --filein "dbs:/ZD_UpTo2j_MZD125_Eps2e-2/bortigno-PUMoriond17-Realistic25ns13TeVEarly2017Collision-93X_mc2017_realistic_v3-LHE-e4a3eca9ea42f5248633ece70b42f936/USER instance=prod/phys03" --fileout file:${samplename}_fall17_GEN-SIM-RAW_step2.root --mc --eventcontent PREMIXRAW --datatier GEN-SIM-RAW --conditions 94X_mc2017_realistic_v10 --step GEN,SIM,DIGIPREMIX_S2,DATAMIX,L1,DIGI2RAW,HLT:2e34v40 --nThreads 8 --datamix PreMix --era Run2_2017 --python_filename ${samplename}_RunIIFall17DRPremix_GEN-SIM-RAW_step2_cfg.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n ${nEvents} || exit $? ;
cmsDriver.py Configuration/GenProduction/python/Hadronizer_TuneCP5_13TeV_MLM_5f_max2j_LHE_pythia8_cff.py --filein "das:/ZD_UpTo2j_MZD125_Eps2e-2/bortigno-PUMoriond17-Realistic25ns13TeVEarly2017Collision-93X_mc2017_realistic_v3-LHE-e4a3eca9ea42f5248633ece70b42f936/USER instance=prod/phys03" --fileout file:${samplename}_fall17_GEN-SIM-RAW_step2.root  --pileup_input "das:/Neutrino_E-10_gun/RunIISummer17PrePremix-MC_v2_94X_mc2017_realistic_v9-v1/GEN-SIM-DIGI-RAW site=T2_CH_CERN" --mc --eventcontent PREMIXRAW --datatier GEN-SIM-RAW --conditions 94X_mc2017_realistic_v10 --step GEN,SIM,DIGIPREMIX_S2,DATAMIX,L1,DIGI2RAW,HLT:2e34v40 --nThreads 8 --datamix PreMix --era Run2_2017 --python_filename ${samplename}_RunIIFall17DRPremix_GEN-SIM-RAW_step2_cfg.py --no_exec  --customise=Configuration/GenProduction/customiseGenSimRawAodsim.noLumiCheck --customise=Configuration/DataProcessing/Utils.addMonitoring --customise=Configuration/GenProduction/customiseGenSimRawAodsim.randomSeed  -n ${nEvents} || exit $? ; 
#file:/afs/cern.ch/user/b/bortigno/workspace/darkphotons/dp_mc_genproduction_fall17/DP_MZd35Epsilon2e-2_fall17.root"
echo "================= CMSRUN starting step 2 ====================" | tee -a job.log
# and now running GEM-SIM-RAW
cmsRun -e -j ${samplename}_step2.log ${samplename}_RunIIFall17DRPremix_GEN-SIM-RAW_step2_cfg.py


echo "================= cmsDriver preparing step 3 ====================" | tee -a job.log
# Preparing configuration for running RAW-RECO-AODSIM aka step3
cmsDriver.py step3 --filein file:${samplename}_fall17_GEN-SIM-RAW_step2.root --fileout file:${samplename}_fall17_AODSIM_step3.root --mc --eventcontent AODSIM runUnscheduled --datatier AODSIM --conditions 94X_mc2017_realistic_v10 --step RAW2DIGI,RECO,RECOSIM,EI --nThreads 8 --era Run2_2017 --python_filename ${samplename}_RunIIFall17DRPremix_AODSIM_step3_cfg.py --no_exec --customise=Configuration/GenProduction/customiseGenSimRawAodsim.noLumiCheck --customise=Configuration/DataProcessing/Utils.addMonitoring -n ${nEvents} || exit $? ; 


echo "================= CMSRUN starting step 3 ====================" | tee -a job.log
# and now running it
cmsRun -e -j FrameworkJobReport.xml ${samplename}_RunIIFall17DRPremix_AODSIM_step3_cfg.py

echo "================= Cleaning up step 2 output ====================" | tee -a job.log
# cleaning
rm -rv ${samplename}_fall17_GEN-SIM-RAW_step2.root

# this is only for batch jobs
#mv -v ${samplename}_fall17_AODSIM_step3.root /eos/cms/store/user/bortigno/mc_genproduction/darkphoton/

