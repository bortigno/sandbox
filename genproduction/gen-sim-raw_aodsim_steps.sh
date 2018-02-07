#!/bin/bash
source /cvmfs/cms.cern.ch/cmsset_default.sh
export SCRAM_ARCH=slc6_amd64_gcc630
if [ -r CMSSW_10_0_o_pre1/src ] ; then 
 echo release CMSSW_10_0_0_pre1 already exists
else
scram p CMSSW CMSSW_10_0_0_pre1
fi
cd CMSSW_10_0_0_pre1/src
eval `scram runtime -sh`


scram b
cd ../../
cmsDriver.py step1 --filein "dbs:/ZD_UpTo2j_MZD125_Eps2e-2/bortigno-PUMoriond17-Realistic25ns13TeVEarly2017Collision-93X_mc2017_realistic_v3-LHE-e4a3eca9ea42f5248633ece70b42f936/USER instance=prod/phys03" --fileout file:DP_MZd125Epsilon2e-2_fall17_GEN-SIM-RAW_step2.root  --pileup_input "dbs:/Neutrino_E-10_gun/RunIISummer17PrePremix-MC_v2_94X_mc2017_realistic_v9-v1/GEN-SIM-DIGI-RAW" --mc --eventcontent PREMIXRAW --datatier GEN-SIM-RAW --conditions 94X_mc2017_realistic_v10 --step DIGIPREMIX_S2,DATAMIX,L1,DIGI2RAW,HLT:2e34v40 --nThreads 8 --datamix PreMix --era Run2_2017 --python_filename DP_MZd125Epsilon2e-2_RunIIFall17DRPremix_GEN-SIM-RAW_step2_cfg.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n 1751 || exit $? ; 
#file:/afs/cern.ch/user/b/bortigno/workspace/darkphotons/dp_mc_genproduction_fall17/DP_MZd35Epsilon2e-2_fall17.root"

cmsDriver.py step2 --filein file:DP_MZd125Epsilon2e-2_fall17_GEN-SIM-RAW_step2.root --fileout file:DP_MZd125Epsilon2e-2_fall17_AODSIM_step3.root --mc --eventcontent AODSIM runUnscheduled --datatier AODSIM --conditions 94X_mc2017_realistic_v10 --step RAW2DIGI,RECO,RECOSIM,EI --nThreads 8 --era Run2_2017 --python_filename DP_MZd125Epsilon2e-2_RunIIFall17DRPremix_AODSIM_step3_cfg.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n 1751 || exit $? ; 

