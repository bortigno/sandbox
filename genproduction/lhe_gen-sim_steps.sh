# This script is copied from one of the McM wmLHE campaign and adapted to dark photon production
#!/bin/bash
source /cvmfs/cms.cern.ch/cmsset_default.sh
export SCRAM_ARCH=slc6_amd64_gcc630
if [ -r CMSSW_10_0_0_pre1/src ] ; then 
 echo release CMS_10_0_0_pre1 already exists
else
scram p CMSSW CMSSW_10_0_0_pre1
fi
cd CMSSW_10_0_0_pre1/src
eval `scram runtime -sh`

JOB_LABEL=zd2j_m35
INPUT_FRAGMENT=externalLHEProducer_and_PYTHIA8_Hadronizer_cff.py
GRIDPACK_LOCATION=/afs/cern.ch/work/b/bortigno/darkphotons/genproductions/bin/MadGraph5_aMCatNLO/
GRIDPACK_NAME=darkphoton_slc6_amd64_gcc481_CMSSW_7_1_30_tarball.tar.xz.v9.good.upto2j.MZd35.eps2e-2.auto-width.tar.xz
OUTPUT_FRAGMENT=${INPUT_FRAGMENT}_${JOB_LABEL}

sed -e s#GRIDPACKNAME#${GRIDPACK_NAME}/g  ${INPUT_FRAGMENT} > ${OUTPUT_FRAGMENT}

#[ -s ${GRIDPACK_LOCATION}${GRIDPACK_NAME} ] || cp ${GRIDPACK_LOCATION}${GRIDPACK_NAME} . # not needed as the gridpack can be sent to the sandbox directly from the crab_cfg

[ -d Configuration/GenProduction/python/ThirteenTeV/Hadronizer ] || mkdir -p Configuration/GenProduction/python/ThirteenTeV/Hadronizer
cp ${OUTPUT_FRAGMENT} Configuration/GenProduction/python/ThirteenTeV/Hadronizer/${OUTPUT_FRAGMENT}_cff.py
[ -s Configuration/GenProduction/python/ThirteenTeV/Hadronizer/${OUTPUT_FRAGMENT}_cff.py ] || exit $?;

scram b
cd ../../
cmsDriver.py Configuration/GenProduction/python/ThirteenTeV/Hadronizer/${OUTPUT_FRAGMENT} --fileout file:${JOB_LABEL}_GEN-SIM-LHE.root --mc --eventcontent RAWSIM,LHE --datatier GEN-SIM,LHE --conditions 93X_mc2017_realistic_v3 --beamspot Realistic25ns13TeVEarly2017Collision --step LHE,GEN,SIM --nThreads 8 --geometry DB:Extended --era Run2_2017 --python_filename ${JOB_LABEL}_GEN-SIM-LHEcfg.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n 4941 || exit $? ; 

