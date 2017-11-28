#!/bin/bash
source /cvmfs/cms.cern.ch/cmsset_default.sh

ConfigRelease=CMSSW_10_0_0_pre1

export SCRAM_ARCH=slc6_amd64_gcc630
if [ -r ${ConfigRelease}/src ] ; then 
 echo release ${ConfigRelease} already exists
else
scram p CMSSW ${ConfigRelease}
fi
cd ${ConfigRelease}/src
eval `scram runtime -sh`

INPUT_FRAGMENT=externalLHEProducer_and_PYTHIA8_Hadronizer_cff.py
#GRIDPACK_LOCATION=/afs/cern.ch/work/b/bortigno/darkphotons/genproductions/bin/MadGraph5_aMCatNLO/

ZDMASS=35
NOFJET=2
ESPILON=2e-2

#GRIDPACK_NAME=darkphoton_slc6_amd64_gcc481_CMSSW_7_1_30_tarball.tar.xz.v9.good.upto2j.MZd35.eps2e-2.auto-width.tar.xz
GRIDPACK_NAME=darkphoton_slc6_amd64_gcc481_CMSSW_7_1_30_tarball.tar.xz.ZD_UpTo2j_MZD${ZDMASS}_Eps${ESPILON}.tar.xz
echo $GRIDPACK_NAME

JOB_LABEL=zd${NOFJET}j_mzd${ZDMASS}
OUTPUT_FRAGMENT=${INPUT_FRAGMENT/_cff.py/}_${JOB_LABEL}_cff.py

GLOBALTAG=93X_mc2017_realistic_v3
NEVENTS=999

cd ../../
sed -e s#GRIDPACKNAME#${GRIDPACK_NAME}#g  ${INPUT_FRAGMENT} > ${ConfigRelease}/src/${OUTPUT_FRAGMENT}
sed -i s#THISDIR#${PWD}#g ${ConfigRelease}/src/${OUTPUT_FRAGMENT}
cd -

#[ -s ${GRIDPACK_LOCATION}${GRIDPACK_NAME} ] || cp ${GRIDPACK_LOCATION}${GRIDPACK_NAME} . # not needed as the gridpack can be sent to the sandbox directly from the crab_cfg

[ -d Configuration/GenProduction/python/ThirteenTeV/Hadronizer ] || mkdir -p Configuration/GenProduction/python/ThirteenTeV/Hadronizer
cp ${OUTPUT_FRAGMENT} Configuration/GenProduction/python/ThirteenTeV/Hadronizer/${OUTPUT_FRAGMENT}
[ -s Configuration/GenProduction/python/ThirteenTeV/Hadronizer/${OUTPUT_FRAGMENT} ] || exit $?;

scram b
cd ../../
CONFIG_TO_RUN=${OUTPUT_FRAGMENT/_cff/_LHE-GEN-SIM_cfg}
echo cmsDriver.py Configuration/GenProduction/python/ThirteenTeV/Hadronizer/${OUTPUT_FRAGMENT} --fileout file:${JOB_LABEL}_LHE-GEN-SIM.root --mc --eventcontent RAWSIM,LHE --datatier GEN-SIM,LHE --conditions ${GLOBALTAG}  --beamspot Realistic25ns13TeVEarly2017Collision --step LHE,GEN,SIM --nThreads 8 --geometry DB:Extended --era Run2_2017 --python_filename ${CONFIG_TO_RUN} --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n ${NEVENTS} || exit $? ; 
cmsDriver.py Configuration/GenProduction/python/ThirteenTeV/Hadronizer/${OUTPUT_FRAGMENT} --fileout file:${JOB_LABEL}_LHE-GEN-SIM.root --mc --eventcontent RAWSIM,LHE --datatier GEN-SIM,LHE --conditions ${GLOBALTAG}  --beamspot Realistic25ns13TeVEarly2017Collision --step LHE,GEN,SIM --nThreads 8 --geometry DB:Extended --era Run2_2017 --python_filename ${CONFIG_TO_RUN} --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n ${NEVENTS} || exit $? ; 


# ========= Now run the LHE =============


CMSSW_release_LHE=CMSSW_9_3_1

echo "================= CMSRUN starting jobNum=$1 ====================" | tee -a job.log
source /cvmfs/cms.cern.ch/cmsset_default.sh
export SCRAM_ARCH=slc6_amd64_gcc481
echo "================= CMSRUN setting up " ${CMSSW_release_LHE} " ===================="| tee -a job.log
if [ -r ${CMSSW_release_LHE}/src ] ; then 
     echo release ${CMSSW_release_LHE} already exists
 else
     scram p CMSSW ${CMSSW_release_LHE}
 fi

BASE=$PWD
NUM=500

cd ${CMSSW_release_LHE}/src
eval `scram runtime -sh`

scram b
cd ../../

echo "================= CMSRUN starting Step 1 ====================" | tee -a job.log
cmsRun -j lhe_step1.log $CONFIG_TO_RUN jobNum=$1

#echo "-> cleaning"
#xrdcp cmsgrid_final.lhe '/store/user/bortigno/mc_genproduction/darkphoton/'+'lhe_files/'+$JOB_LABEL+'cmsgridfinal'+$jobNum+'.lhe'
#rm -v *.root  


