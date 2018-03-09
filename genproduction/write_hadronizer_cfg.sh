#! /bin/bash
# Prepare hadronizer cfg
# Use: write_config <mass> <qcut>


MASS=$1
QCUT=23
CMSSW_RELEASE=10_0_2
WORKINGDIR=/afs/cern.ch/work/b/bortigno/sandbox/genproduction/CMSSW_${CMSSW_RELEASE}/src/
STORAGEDIR=/eos/cms/store/user/bortigno/MadGraph/darkphoton/mzd${MASS}/

[ -d ${STORAGEDIR} ] || mkdir -p ${STORAGEDIR}
[ -d CMSSW_${CMSSW_RELEASE} ] || cmsrel CMSSW_${CMSSW_RELEASE}
[ -d hadronizer_${CMSSW_RELEASE} ] || mkdir hadronizer_${CMSSW_RELEASE}

sed -e s#QCUTREPLACE#${QCUT}#g PYTHIA8_Hadronizer_zd2j_LHE-GEN-SIM_cfg.py > hadronizer_${CMSSW_RELEASE}/PYTHIA8_Hadronizer_zd2j_mzd${MASS}_LHE-GEN-SIM-QCUT_${QCUT}_cfg.py
sed -i -e s#MASSREPLACE#${MASS}#g hadronizer_${CMSSW_RELEASE}/PYTHIA8_Hadronizer_zd2j_mzd${MASS}_LHE-GEN-SIM-QCUT_${QCUT}_cfg.py

exit
