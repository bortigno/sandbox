#!/bin/bash
source /cvmfs/cms.cern.ch/cmsset_default.sh

ConfigRelease=CMSSW_9_4_6
RunningRelease=${ConfigRelease}

echo "================= PB: Starting cmssw environment prepration ====================" | tee -a job.log

export SCRAM_ARCH=slc6_amd64_gcc630
if [ -r ${ConfigRelease}/src ] ; then 
 echo release ${ConfigRelease} already exists
else
scram p CMSSW ${ConfigRelease}
fi
cd ${ConfigRelease}/src
eval `scram runtime -sh`

INPUT_FRAGMENT=externalLHEProducer_cff.py

#Print out the list of arguments passed to the script. The first argument is always the job number. Then begin the custom arguments.
echo $@
echo "param 1 = Zdmass = ${2}"
echo "param 2 = nEvents = ${3}"
ZDMASS="${2#*=}"
NOFJET=2
ESPILON=2e-2
GLOBALTAG=93X_mc2017_realistic_v3
NEVENTS="${3#*=}"
samplename="darkphoton"

#for crab GRIDPACK_LOCATION should be PWD - and the gridpack should be copied in the sandbox.tar.gz using the crab config...
GRIDPACK_LOCATION=$PWD
# for local testing the full path should be given
#GRIDPACK_LOCATION=/afs/cern.ch/user/b/bortigno/workspace/sandbox/genproduction/

echo "================= PB: Input Paramateres ========================================"  | tee -a job.log
echo $ZDMASS
echo $NOFJET
echo $ESPILON
echo $GLOBALTAG
echo $NEVENTS
echo $samplename

GRIDPACK_NAME=darkphoton_slc6_amd64_gcc481_CMSSW_7_1_30_tarball.tar.xz.ZD_UpTo2j_MZD${ZDMASS}_Eps${ESPILON}.tar.xz

echo "================= PB: Gridpack name ========================================"  | tee -a job.log
echo $GRIDPACK_NAME

echo "================= PB: Preparing the configs from gragments ====================" | tee -a job.log

JOB_LABEL=zd${NOFJET}j_mzd${ZDMASS}
OUTPUT_FRAGMENT=${INPUT_FRAGMENT/_cff.py/}_${JOB_LABEL}_cff.py
OUTPUT_FRAGMENT_STEP2=darkphoton_step2_cfg.py
OUTPUT_FRAGMENT_STEP3=darkphoton_step3_cfg.py


cd ../../
sed -e s#GRIDPACKNAME#${GRIDPACK_NAME}#g  ${INPUT_FRAGMENT} > ${ConfigRelease}/src/${OUTPUT_FRAGMENT}
sed -i s#THISDIR#${GRIDPACK_LOCATION}#g ${ConfigRelease}/src/${OUTPUT_FRAGMENT}
cd -

#This is for step1
[ -d Configuration/GenProduction/python/ThirteenTeV/LHE ] || mkdir -p Configuration/GenProduction/python/ThirteenTeV/LHE
cp -v ${OUTPUT_FRAGMENT} Configuration/GenProduction/python/ThirteenTeV/LHE/${OUTPUT_FRAGMENT}
[ -s Configuration/GenProduction/python/ThirteenTeV/LHE/${OUTPUT_FRAGMENT} ] || exit $?;

# This is for step2
[ -d Configuration/GenProduction/python/ ] || mkdir -p Configuration/GenProduction/python/
cp -v ../../Hadronizer_TuneCP5_13TeV_MLM_5f_max2j_LHE_pythia8_cff.py Configuration/GenProduction/python/

# This is for the customisation for all steps
cp -v ../../customiseGenSimRawAodsim.py Configuration/GenProduction/python/


echo "================= PB: Compiling fragments from release ====================" | tee -a job.log

scram b
cd ../../
CONFIG_TO_RUN=${OUTPUT_FRAGMENT/_cff/_LHE_cfg}

echo "================= PB: Running cmsDriver ====================" | tee -a job.log
# Preparing the configuration for running LHE aka step1
echo cmsDriver.py Configuration/GenProduction/python/ThirteenTeV/LHE/${OUTPUT_FRAGMENT} --fileout file:${samplename}_lhe.root --mc --eventcontent LHE --datatier LHE --conditions ${GLOBALTAG}  --beamspot Realistic25ns13TeVEarly2017Collision --step LHE --nThreads 8 --geometry DB:Extended --era Run2_2017 --python_filename ${CONFIG_TO_RUN} --no_exec  -n ${NEVENTS} || exit $? ; 
cmsDriver.py Configuration/GenProduction/python/ThirteenTeV/LHE/${OUTPUT_FRAGMENT} --fileout file:${samplename}_lhe.root --mc --eventcontent LHE --datatier LHE --conditions ${GLOBALTAG}  --beamspot Realistic25ns13TeVEarly2017Collision --step LHE --nThreads 8 --geometry DB:Extended --era Run2_2017 --python_filename ${CONFIG_TO_RUN} --no_exec -n ${NEVENTS} || exit $? ; 

echo "================= PB: Dumping step1 config file ====================" | tee -a job.log
cat ${CONFIG_TO_RUN}


echo "================ PB: cmsDriver preparing step2 =====================" | tee -a job.log
# Preparing the configuration for running GEN-SIM-RAW aka step2
cmsDriver.py Configuration/GenProduction/python/Hadronizer_TuneCP5_13TeV_MLM_5f_max2j_LHE_pythia8_cff.py --filein "file:${samplename}_lhe.root" --fileout file:${samplename}_gen-sim-raw.root  --pileup_input "das:/Neutrino_E-10_gun/RunIISummer17PrePremix-MC_v2_94X_mc2017_realistic_v9-v1/GEN-SIM-DIGI-RAW site=T2_CH_CERN" --mc --eventcontent PREMIXRAW --datatier GEN-SIM-RAW --conditions 94X_mc2017_realistic_v10 --step GEN,SIM,DIGIPREMIX_S2,DATAMIX,L1,DIGI2RAW,HLT:2e34v40 --nThreads 8 --datamix PreMix --era Run2_2017 --no_exec  --customise=Configuration/GenProduction/customiseGenSimRawAodsim.noLumiCheck --customise=Configuration/DataProcessing/Utils.addMonitoring --customise=Configuration/GenProduction/customiseGenSimRawAodsim.randomSeed --python_filename=${OUTPUT_FRAGMENT_STEP2}  -n -1 || exit $? ; 


echo "================= PB: cmsDriver preparing step 3 ====================" | tee -a job.log
# Preparing configuration for running RAW-RECO-AODSIM aka step3
cmsDriver.py step3 --filein file:${samplename}_gen-sim-raw.root --fileout file:${samplename}_aodsim.root --mc --eventcontent AODSIM runUnscheduled --datatier AODSIM --conditions 94X_mc2017_realistic_v10 --step RAW2DIGI,RECO,RECOSIM,EI --nThreads 8 --era Run2_2017 --no_exec --customise=Configuration/GenProduction/customiseGenSimRawAodsim.noLumiCheck --customise=Configuration/DataProcessing/Utils.addMonitoring --python_filename=${OUTPUT_FRAGMENT_STEP3} -n -1 || exit $? ; 


# ========= Now run the LHE =============
echo "================= PB: Now start the setup for running the LHE ====================" | tee -a job.log


echo "================= PB: CMSRUN starting jobNum=$1 ====================" | tee -a job.log
echo "================= PB: CMSRUN setting up " ${RunningRelease} " ===================="| tee -a job.log
if [ -r ${RunningRelease}/src ] ; then 
     echo release ${RunningRelease} already exists
 else
     scram p CMSSW ${RunningRelease}
 fi

cd ${RunningRelease}/src
eval `scram runtime -sh`

scram b
cd ../../

echo "================= PB: CMSRUN starting Step 1 ====================" | tee -a job.log
echo cmsRun -e -j ${samplename}_step1.log -p $CONFIG_TO_RUN jobNum=$1
cmsRun -e -j ${samplename}_step1.log -p $CONFIG_TO_RUN 
# jobNum=$1

echo "================= PB: checking outputfile ====================" | tee -a job.log
[ -s ${samplename}_lhe.root ] || echo "==================== ERROR: LHE output file not present ======================" 
[ -s ${samplename}_lhe.root ] || exit $?

echo "================= PB: CMSRUN starting Step 2 ====================" | tee -a job.log
echo cmsRun -e -j ${samplename}_step2.log ${OUTPUT_FRAGMENT_STEP2}
cmsRun -e -j ${samplename}_step2.log ${OUTPUT_FRAGMENT_STEP2}

#cleaning
rm -rfv ${samplename}_lhe.root

echo "================= PB: checking outputfile ====================" | tee -a job.log
[ -s ${samplename}_gen-sim-raw.root ] || echo "================= ERROR: GEN--SIM-RAW output file not present =====================" 
[ -s ${samplename}_gen-sim-raw.root ] || exit $?


echo "================= PB: CMSRUN starting step 3 ====================" | tee -a job.log
echo cmsRun -e -j FrameworkJobReport.xml ${OUTPUT_FRAGMENT_STEP3}
cmsRun -e -j FrameworkJobReport.xml ${OUTPUT_FRAGMENT_STEP3}

echo "================= Cleaning up step 2 output ====================" | tee -a job.log
# cleaning
rm -rfv ${samplename}_gen-sim-raw.root


