import os,random

def randomSeed(process):
  random.seed = os.urandom(10) #~10^14
  process.RandomNumberGeneratorService.externalLHEProducer.initialSeed = random.randint(0,999999)
  process.RandomNumberGeneratorService.generator.initialSeed = random.randint(0,999999)
  return process

#this will probably not fly
def movingFirstLumi(process):
  from FWCore.ParameterSet.VarParsing import VarParsing
  options = VarParsing ('analysis')
  options.register('jobNum', 0, VarParsing.multiplicity.singleton,VarParsing.varType.int,"jobNum")
  options.parseArguments()  
  firstLumi=10*options.jobNum+1 ## eventsPerJob/eventsPerLumi*jobNum +1
  process.source.firstLuminosityBlock  = cms.untracked.uint32(firstLumi)
  process.source.numberEventsInLuminosityBlock = cms.untracked.uint32(100)
  return process
