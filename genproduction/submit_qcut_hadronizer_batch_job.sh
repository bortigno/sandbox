#! /bin/bash
# Prepare and launch the hadronizer job in lxbatch 


MASS=70
WORKINGDIR=/afs/cern.ch/work/b/bortigno/sandbox/genproduction/CMSSW_10_0_0_pre1/src/
STORAGEDIR=/eos/cms/store/user/bortigno/MadGraph/darkphoton/mzd${MASS}/

[ -d ${STORAGEDIR} ] || mkdir -p ${STORAGEDIR}
[ -d hadronizer ] || mkdir hadronizer

for i in `seq 10 20` ; do sed -e s#QCUTREPLACE#$i#g PYTHIA8_Hadronizer_zd2j_mzd${MASS}_LHE-GEN-SIM_cfg.py > hadronizer/PYTHIA8_Hadronizer_zd2j_mzd${MASS}_LHE-GEN-SIM-QCUT_${i}_cfg.py ; done

for i in `seq 10 20` ; do bsub -q 1nd -J qcut${i} -o hadronizer_${i}.out -e hadronizer_${i}.err ~/bin/bjob_luncher.sh /afs/cern.ch/work/b/bortigno/sandbox/genproduction/hadronizer/PYTHIA8_Hadronizer_zd2j_mzd${MASS}_LHE-GEN-SIM-QCUT_${i}_cfg.py ${WORKINGDIR} ${STORAGEDIR} ; done

exit
