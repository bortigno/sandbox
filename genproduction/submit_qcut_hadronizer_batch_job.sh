#! /bin/bash
# Prepare and launch the hadronizer job in lxbatch 

mkdir hadronizer

for i in `seq 10 20` ; do sed -e s#QCUTREPLACE#$i#g PYTHIA8_Hadronizer_zd2j_mzd35_LHE-GEN-SIM_cfg.py > hadronizer/PYTHIA8_Hadronizer_zd2j_mzd35_LHE-GEN-SIM-QCUT_${i}_cfg.py ; done

for i in `seq 10 20` ; do bsub -q 1nd -J qcut${i} -o hadronizer_${4}.out -e hadronizer_{i}.err ~/bin/bjob_luncher.sh /afs/cern.ch/work/b/bortigno/sandbox/genproduction/hadronizer/PYTHIA8_Hadronizer_zd2j_mzd35_LHE-GEN-SIM-QCUT_${i}_cfg.py /afs/cern.ch/work/b/bortigno/sandbox/genproduction/CMSSW_10_0_0_pre1/src/ ; done

exit
