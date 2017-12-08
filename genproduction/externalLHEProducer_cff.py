import FWCore.ParameterSet.Config as cms
import os 

from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.MCTunes2017.PythiaCP5Settings_cfi import *

# Avoid to have multiple lumi in the same job and therefore auto-cleaning
# This means that it need an argument to be run
# from FWCore.ParameterSet.VarParsing import VarParsing
# options = VarParsing ('analysis')
# options.register('jobNum', 0, VarParsing.multiplicity.singleton,VarParsing.varType.int,"jobNum")
# options.parseArguments ()
# firstLumi=10*options.jobNum+1 ## eventsPerJob/eventsPerLumi*jobNum +1
# source = cms.Source("EmptySource",
#         firstLuminosityBlock  = cms.untracked.uint32(firstLumi),
#         numberEventsInLuminosityBlock = cms.untracked.uint32(100)
#         )


# External lHE producer configuration
externalLHEProducer = cms.EDProducer("ExternalLHEProducer",
    args = cms.vstring( 'THISDIR' + '/GRIDPACKNAME'),
    nEvents = cms.untracked.uint32(5000),
    numberOfParameters = cms.uint32(1),
    outputFile = cms.string('cmsgrid_final.lhe'),
    scriptName = cms.FileInPath('GeneratorInterface/LHEInterface/data/run_generic_tarball_cvmfs.sh')
)


