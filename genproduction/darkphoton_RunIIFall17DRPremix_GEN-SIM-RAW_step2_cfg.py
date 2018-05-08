# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: Configuration/GenProduction/python/Hadronizer_TuneCP5_13TeV_MLM_5f_max2j_LHE_pythia8_cff.py --filein das:/ZD_UpTo2j_MZD125_Eps2e-2/bortigno-PUMoriond17-Realistic25ns13TeVEarly2017Collision-93X_mc2017_realistic_v3-LHE-e4a3eca9ea42f5248633ece70b42f936/USER instance=prod/phys03 --fileout file:darkphoton_fall17_GEN-SIM-RAW_step2.root --pileup_input das:/Neutrino_E-10_gun/RunIISummer17PrePremix-MC_v2_94X_mc2017_realistic_v9-v1/GEN-SIM-DIGI-RAW site=T2_CH_CERN --mc --eventcontent PREMIXRAW --datatier GEN-SIM-RAW --conditions 94X_mc2017_realistic_v10 --step GEN,SIM,DIGIPREMIX_S2,DATAMIX,L1,DIGI2RAW,HLT:2e34v40 --nThreads 8 --datamix PreMix --era Run2_2017 --python_filename darkphoton_RunIIFall17DRPremix_GEN-SIM-RAW_step2_cfg.py --no_exec --customise=Configuration/GenProduction/customiseGenSimRawAodsim.noLumiCheck --customise=Configuration/DataProcessing/Utils.addMonitoring --customise=Configuration/GenProduction/customiseGenSimRawAodsim.randomSeed -n -1
import FWCore.ParameterSet.Config as cms

from Configuration.StandardSequences.Eras import eras

process = cms.Process('HLT',eras.Run2_2017)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.Geometry.GeometrySimDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.Generator_cff')
process.load('IOMC.EventVertexGenerators.VtxSmearedRealistic50ns13TeVCollision_cfi')
process.load('GeneratorInterface.Core.genFilterSummary_cff')
process.load('Configuration.StandardSequences.SimIdeal_cff')
process.load('Configuration.StandardSequences.DigiDMPreMix_cff')
process.load('SimGeneral.MixingModule.digi_MixPreMix_cfi')
process.load('Configuration.StandardSequences.DataMixerPreMix_cff')
process.load('Configuration.StandardSequences.SimL1EmulatorDM_cff')
process.load('Configuration.StandardSequences.DigiToRawDM_cff')
process.load('HLTrigger.Configuration.HLT_2e34v40_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

# Input source
process.source = cms.Source("PoolSource",
    dropDescendantsOfDroppedBranches = cms.untracked.bool(False),
    fileNames = cms.untracked.vstring('/store/user/bortigno/mc_genproduction/darkphoton/LHE/ZD_UpTo2j_MZD125_Eps2e-2/ZD_UpTo2j_MZD125_Eps2e-2/PUMoriond17-Realistic25ns13TeVEarly2017Collision-93X_mc2017_realistic_v3-LHE/171214_103244/0000/zd2j_LHE_57.root', 
        '/store/user/bortigno/mc_genproduction/darkphoton/LHE/ZD_UpTo2j_MZD125_Eps2e-2/ZD_UpTo2j_MZD125_Eps2e-2/PUMoriond17-Realistic25ns13TeVEarly2017Collision-93X_mc2017_realistic_v3-LHE/171214_103244/0000/zd2j_LHE_86.root', 
        '/store/user/bortigno/mc_genproduction/darkphoton/LHE/ZD_UpTo2j_MZD125_Eps2e-2/ZD_UpTo2j_MZD125_Eps2e-2/PUMoriond17-Realistic25ns13TeVEarly2017Collision-93X_mc2017_realistic_v3-LHE/171214_103244/0000/zd2j_LHE_82.root', 
        '/store/user/bortigno/mc_genproduction/darkphoton/LHE/ZD_UpTo2j_MZD125_Eps2e-2/ZD_UpTo2j_MZD125_Eps2e-2/PUMoriond17-Realistic25ns13TeVEarly2017Collision-93X_mc2017_realistic_v3-LHE/171214_103244/0000/zd2j_LHE_81.root', 
        '/store/user/bortigno/mc_genproduction/darkphoton/LHE/ZD_UpTo2j_MZD125_Eps2e-2/ZD_UpTo2j_MZD125_Eps2e-2/PUMoriond17-Realistic25ns13TeVEarly2017Collision-93X_mc2017_realistic_v3-LHE/171214_103244/0000/zd2j_LHE_79.root', 
        '/store/user/bortigno/mc_genproduction/darkphoton/LHE/ZD_UpTo2j_MZD125_Eps2e-2/ZD_UpTo2j_MZD125_Eps2e-2/PUMoriond17-Realistic25ns13TeVEarly2017Collision-93X_mc2017_realistic_v3-LHE/171214_103244/0000/zd2j_LHE_76.root', 
        '/store/user/bortigno/mc_genproduction/darkphoton/LHE/ZD_UpTo2j_MZD125_Eps2e-2/ZD_UpTo2j_MZD125_Eps2e-2/PUMoriond17-Realistic25ns13TeVEarly2017Collision-93X_mc2017_realistic_v3-LHE/171214_103244/0000/zd2j_LHE_93.root', 
        '/store/user/bortigno/mc_genproduction/darkphoton/LHE/ZD_UpTo2j_MZD125_Eps2e-2/ZD_UpTo2j_MZD125_Eps2e-2/PUMoriond17-Realistic25ns13TeVEarly2017Collision-93X_mc2017_realistic_v3-LHE/171214_103244/0000/zd2j_LHE_44.root', 
        '/store/user/bortigno/mc_genproduction/darkphoton/LHE/ZD_UpTo2j_MZD125_Eps2e-2/ZD_UpTo2j_MZD125_Eps2e-2/PUMoriond17-Realistic25ns13TeVEarly2017Collision-93X_mc2017_realistic_v3-LHE/171214_103244/0000/zd2j_LHE_95.root', 
        '/store/user/bortigno/mc_genproduction/darkphoton/LHE/ZD_UpTo2j_MZD125_Eps2e-2/ZD_UpTo2j_MZD125_Eps2e-2/PUMoriond17-Realistic25ns13TeVEarly2017Collision-93X_mc2017_realistic_v3-LHE/171214_103244/0000/zd2j_LHE_31.root', 
        '/store/user/bortigno/mc_genproduction/darkphoton/LHE/ZD_UpTo2j_MZD125_Eps2e-2/ZD_UpTo2j_MZD125_Eps2e-2/PUMoriond17-Realistic25ns13TeVEarly2017Collision-93X_mc2017_realistic_v3-LHE/171214_103244/0000/zd2j_LHE_58.root', 
        '/store/user/bortigno/mc_genproduction/darkphoton/LHE/ZD_UpTo2j_MZD125_Eps2e-2/ZD_UpTo2j_MZD125_Eps2e-2/PUMoriond17-Realistic25ns13TeVEarly2017Collision-93X_mc2017_realistic_v3-LHE/171214_103244/0000/zd2j_LHE_55.root', 
        '/store/user/bortigno/mc_genproduction/darkphoton/LHE/ZD_UpTo2j_MZD125_Eps2e-2/ZD_UpTo2j_MZD125_Eps2e-2/PUMoriond17-Realistic25ns13TeVEarly2017Collision-93X_mc2017_realistic_v3-LHE/171214_103244/0000/zd2j_LHE_32.root', 
        '/store/user/bortigno/mc_genproduction/darkphoton/LHE/ZD_UpTo2j_MZD125_Eps2e-2/ZD_UpTo2j_MZD125_Eps2e-2/PUMoriond17-Realistic25ns13TeVEarly2017Collision-93X_mc2017_realistic_v3-LHE/171214_103244/0000/zd2j_LHE_45.root', 
        '/store/user/bortigno/mc_genproduction/darkphoton/LHE/ZD_UpTo2j_MZD125_Eps2e-2/ZD_UpTo2j_MZD125_Eps2e-2/PUMoriond17-Realistic25ns13TeVEarly2017Collision-93X_mc2017_realistic_v3-LHE/171214_103244/0000/zd2j_LHE_46.root', 
        '/store/user/bortigno/mc_genproduction/darkphoton/LHE/ZD_UpTo2j_MZD125_Eps2e-2/ZD_UpTo2j_MZD125_Eps2e-2/PUMoriond17-Realistic25ns13TeVEarly2017Collision-93X_mc2017_realistic_v3-LHE/171214_103244/0000/zd2j_LHE_43.root', 
        '/store/user/bortigno/mc_genproduction/darkphoton/LHE/ZD_UpTo2j_MZD125_Eps2e-2/ZD_UpTo2j_MZD125_Eps2e-2/PUMoriond17-Realistic25ns13TeVEarly2017Collision-93X_mc2017_realistic_v3-LHE/171214_103244/0000/zd2j_LHE_27.root', 
        '/store/user/bortigno/mc_genproduction/darkphoton/LHE/ZD_UpTo2j_MZD125_Eps2e-2/ZD_UpTo2j_MZD125_Eps2e-2/PUMoriond17-Realistic25ns13TeVEarly2017Collision-93X_mc2017_realistic_v3-LHE/171214_103244/0000/zd2j_LHE_29.root', 
        '/store/user/bortigno/mc_genproduction/darkphoton/LHE/ZD_UpTo2j_MZD125_Eps2e-2/ZD_UpTo2j_MZD125_Eps2e-2/PUMoriond17-Realistic25ns13TeVEarly2017Collision-93X_mc2017_realistic_v3-LHE/171214_103244/0000/zd2j_LHE_14.root', 
        '/store/user/bortigno/mc_genproduction/darkphoton/LHE/ZD_UpTo2j_MZD125_Eps2e-2/ZD_UpTo2j_MZD125_Eps2e-2/PUMoriond17-Realistic25ns13TeVEarly2017Collision-93X_mc2017_realistic_v3-LHE/171214_103244/0000/zd2j_LHE_39.root', 
        '/store/user/bortigno/mc_genproduction/darkphoton/LHE/ZD_UpTo2j_MZD125_Eps2e-2/ZD_UpTo2j_MZD125_Eps2e-2/PUMoriond17-Realistic25ns13TeVEarly2017Collision-93X_mc2017_realistic_v3-LHE/171214_103244/0000/zd2j_LHE_96.root', 
        '/store/user/bortigno/mc_genproduction/darkphoton/LHE/ZD_UpTo2j_MZD125_Eps2e-2/ZD_UpTo2j_MZD125_Eps2e-2/PUMoriond17-Realistic25ns13TeVEarly2017Collision-93X_mc2017_realistic_v3-LHE/171214_103244/0000/zd2j_LHE_9.root', 
        '/store/user/bortigno/mc_genproduction/darkphoton/LHE/ZD_UpTo2j_MZD125_Eps2e-2/ZD_UpTo2j_MZD125_Eps2e-2/PUMoriond17-Realistic25ns13TeVEarly2017Collision-93X_mc2017_realistic_v3-LHE/171214_103244/0000/zd2j_LHE_8.root', 
        '/store/user/bortigno/mc_genproduction/darkphoton/LHE/ZD_UpTo2j_MZD125_Eps2e-2/ZD_UpTo2j_MZD125_Eps2e-2/PUMoriond17-Realistic25ns13TeVEarly2017Collision-93X_mc2017_realistic_v3-LHE/171214_103244/0000/zd2j_LHE_7.root', 
        '/store/user/bortigno/mc_genproduction/darkphoton/LHE/ZD_UpTo2j_MZD125_Eps2e-2/ZD_UpTo2j_MZD125_Eps2e-2/PUMoriond17-Realistic25ns13TeVEarly2017Collision-93X_mc2017_realistic_v3-LHE/171214_103244/0000/zd2j_LHE_17.root', 
        '/store/user/bortigno/mc_genproduction/darkphoton/LHE/ZD_UpTo2j_MZD125_Eps2e-2/ZD_UpTo2j_MZD125_Eps2e-2/PUMoriond17-Realistic25ns13TeVEarly2017Collision-93X_mc2017_realistic_v3-LHE/171214_103244/0000/zd2j_LHE_19.root', 
        '/store/user/bortigno/mc_genproduction/darkphoton/LHE/ZD_UpTo2j_MZD125_Eps2e-2/ZD_UpTo2j_MZD125_Eps2e-2/PUMoriond17-Realistic25ns13TeVEarly2017Collision-93X_mc2017_realistic_v3-LHE/171214_103244/0000/zd2j_LHE_83.root', 
        '/store/user/bortigno/mc_genproduction/darkphoton/LHE/ZD_UpTo2j_MZD125_Eps2e-2/ZD_UpTo2j_MZD125_Eps2e-2/PUMoriond17-Realistic25ns13TeVEarly2017Collision-93X_mc2017_realistic_v3-LHE/171214_103244/0000/zd2j_LHE_61.root', 
        '/store/user/bortigno/mc_genproduction/darkphoton/LHE/ZD_UpTo2j_MZD125_Eps2e-2/ZD_UpTo2j_MZD125_Eps2e-2/PUMoriond17-Realistic25ns13TeVEarly2017Collision-93X_mc2017_realistic_v3-LHE/171214_103244/0000/zd2j_LHE_56.root', 
        '/store/user/bortigno/mc_genproduction/darkphoton/LHE/ZD_UpTo2j_MZD125_Eps2e-2/ZD_UpTo2j_MZD125_Eps2e-2/PUMoriond17-Realistic25ns13TeVEarly2017Collision-93X_mc2017_realistic_v3-LHE/171214_103244/0000/zd2j_LHE_99.root', 
        '/store/user/bortigno/mc_genproduction/darkphoton/LHE/ZD_UpTo2j_MZD125_Eps2e-2/ZD_UpTo2j_MZD125_Eps2e-2/PUMoriond17-Realistic25ns13TeVEarly2017Collision-93X_mc2017_realistic_v3-LHE/171214_103244/0000/zd2j_LHE_51.root', 
        '/store/user/bortigno/mc_genproduction/darkphoton/LHE/ZD_UpTo2j_MZD125_Eps2e-2/ZD_UpTo2j_MZD125_Eps2e-2/PUMoriond17-Realistic25ns13TeVEarly2017Collision-93X_mc2017_realistic_v3-LHE/171214_103244/0000/zd2j_LHE_37.root', 
        '/store/user/bortigno/mc_genproduction/darkphoton/LHE/ZD_UpTo2j_MZD125_Eps2e-2/ZD_UpTo2j_MZD125_Eps2e-2/PUMoriond17-Realistic25ns13TeVEarly2017Collision-93X_mc2017_realistic_v3-LHE/171214_103244/0000/zd2j_LHE_84.root', 
        '/store/user/bortigno/mc_genproduction/darkphoton/LHE/ZD_UpTo2j_MZD125_Eps2e-2/ZD_UpTo2j_MZD125_Eps2e-2/PUMoriond17-Realistic25ns13TeVEarly2017Collision-93X_mc2017_realistic_v3-LHE/171214_103244/0000/zd2j_LHE_53.root', 
        '/store/user/bortigno/mc_genproduction/darkphoton/LHE/ZD_UpTo2j_MZD125_Eps2e-2/ZD_UpTo2j_MZD125_Eps2e-2/PUMoriond17-Realistic25ns13TeVEarly2017Collision-93X_mc2017_realistic_v3-LHE/171214_103244/0000/zd2j_LHE_89.root', 
        '/store/user/bortigno/mc_genproduction/darkphoton/LHE/ZD_UpTo2j_MZD125_Eps2e-2/ZD_UpTo2j_MZD125_Eps2e-2/PUMoriond17-Realistic25ns13TeVEarly2017Collision-93X_mc2017_realistic_v3-LHE/171214_103244/0000/zd2j_LHE_85.root', 
        '/store/user/bortigno/mc_genproduction/darkphoton/LHE/ZD_UpTo2j_MZD125_Eps2e-2/ZD_UpTo2j_MZD125_Eps2e-2/PUMoriond17-Realistic25ns13TeVEarly2017Collision-93X_mc2017_realistic_v3-LHE/171214_103244/0000/zd2j_LHE_10.root', 
        '/store/user/bortigno/mc_genproduction/darkphoton/LHE/ZD_UpTo2j_MZD125_Eps2e-2/ZD_UpTo2j_MZD125_Eps2e-2/PUMoriond17-Realistic25ns13TeVEarly2017Collision-93X_mc2017_realistic_v3-LHE/171214_103244/0000/zd2j_LHE_3.root'),
    inputCommands = cms.untracked.vstring('keep *', 
        'drop LHEXMLStringProduct_*_*_*'),
    secondaryFileNames = cms.untracked.vstring()
)

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('Configuration/GenProduction/python/Hadronizer_TuneCP5_13TeV_MLM_5f_max2j_LHE_pythia8_cff.py nevts:-1'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.PREMIXRAWoutput = cms.OutputModule("PoolOutputModule",
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('generation_step')
    ),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('GEN-SIM-RAW'),
        filterName = cms.untracked.string('')
    ),
    fileName = cms.untracked.string('file:darkphoton_fall17_GEN-SIM-RAW_step2.root'),
    outputCommands = process.PREMIXRAWEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

# Additional output definition

# Other statements
process.genstepfilter.triggerConditions=cms.vstring("generation_step")
process.mix.digitizers = cms.PSet(process.theDigitizersMixPreMix)
process.mixData.input.fileNames = cms.untracked.vstring(['/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MC_v2_94X_mc2017_realistic_v9-v1/30042/64252196-EDD3-E711-BEB5-002590A88800.root', '/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MC_v2_94X_mc2017_realistic_v9-v1/30042/BC1EFA79-EED3-E711-8893-A4BF011253C0.root', '/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MC_v2_94X_mc2017_realistic_v9-v1/30000/BC2F3F07-ACD3-E711-BCC2-001E67792872.root', '/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MC_v2_94X_mc2017_realistic_v9-v1/30040/1E4A0C8E-EFD3-E711-AFBB-001E6739811A.root', '/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MC_v2_94X_mc2017_realistic_v9-v1/30042/782DFE65-EDD3-E711-AC1B-001E673969FF.root', '/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MC_v2_94X_mc2017_realistic_v9-v1/30041/D6FA398B-EDD3-E711-BD9D-001E67E71BC8.root', '/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MC_v2_94X_mc2017_realistic_v9-v1/30041/96C95837-EED3-E711-B4DB-001E67E6F5EE.root', '/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MC_v2_94X_mc2017_realistic_v9-v1/30043/8A81A5FD-EDD3-E711-BA88-001E6779264E.root', '/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MC_v2_94X_mc2017_realistic_v9-v1/30040/04E48CDA-EDD3-E711-BDA8-A4BF0112BC6A.root', '/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MC_v2_94X_mc2017_realistic_v9-v1/30042/8EC6E218-EDD3-E711-BEC5-A4BF01125620.root', '/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MC_v2_94X_mc2017_realistic_v9-v1/30039/F6DC9E06-EDD3-E711-AED7-001E6779254E.root', '/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MC_v2_94X_mc2017_realistic_v9-v1/30042/C849424C-EDD3-E711-A63D-001E67E6F922.root', '/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MC_v2_94X_mc2017_realistic_v9-v1/30000/0012E563-A6D3-E711-B543-001E67E6F8CD.root', '/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MC_v2_94X_mc2017_realistic_v9-v1/30040/00B98BDC-EED3-E711-94EB-A4BF0112BE12.root', '/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MC_v2_94X_mc2017_realistic_v9-v1/30041/5441B054-EED3-E711-A430-002590A88806.root', '/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MC_v2_94X_mc2017_realistic_v9-v1/30000/B83EBC4D-A6D3-E711-A424-001E67E6F4A9.root', '/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MC_v2_94X_mc2017_realistic_v9-v1/30042/E2693628-EDD3-E711-93DF-A4BF0112BDEA.root', '/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MC_v2_94X_mc2017_realistic_v9-v1/30000/EED74ED4-9AD3-E711-9CB0-001E67E71E20.root', '/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MC_v2_94X_mc2017_realistic_v9-v1/40018/3A5BAB8A-28CD-E711-B709-0CC47AA53D6A.root', '/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MC_v2_94X_mc2017_realistic_v9-v1/40022/409D469E-7CCD-E711-BE3B-00259048A860.root', '/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MC_v2_94X_mc2017_realistic_v9-v1/40021/0072356A-4BCD-E711-B649-0025907859C4.root', '/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MC_v2_94X_mc2017_realistic_v9-v1/40021/8C8AF9C9-4BCD-E711-9510-0CC47A57D164.root', '/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MC_v2_94X_mc2017_realistic_v9-v1/40035/9AA1E755-CFCD-E711-9814-002590FD5A52.root', '/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MC_v2_94X_mc2017_realistic_v9-v1/40018/BADB67D0-2ACD-E711-8E95-0025907859B4.root', '/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MC_v2_94X_mc2017_realistic_v9-v1/40018/267642CC-2ACD-E711-AE27-0CC47A57D164.root', '/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MC_v2_94X_mc2017_realistic_v9-v1/40032/04230B18-C7CD-E711-BA52-0025902BD8CE.root', '/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MC_v2_94X_mc2017_realistic_v9-v1/40020/D64581FF-65CD-E711-9D8F-0CC47A0AD3BC.root', '/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MC_v2_94X_mc2017_realistic_v9-v1/40019/00DBFECA-08CD-E711-86E7-00259019A43E.root', '/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MC_v2_94X_mc2017_realistic_v9-v1/40016/DE94AD8B-CFCC-E711-B419-002590D9D8AA.root', '/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MC_v2_94X_mc2017_realistic_v9-v1/40018/72BFE07B-29CD-E711-B33E-0025907E343C.root', '/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MC_v2_94X_mc2017_realistic_v9-v1/30000/8CFFD53A-DFCC-E711-AD17-0CC47A7AB7A0.root', '/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MC_v2_94X_mc2017_realistic_v9-v1/30034/188F079A-8CCD-E711-8C5E-0025905A609E.root', '/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MC_v2_94X_mc2017_realistic_v9-v1/30036/8A257186-8DCD-E711-B2AF-0025905B858E.root'])
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '94X_mc2017_realistic_v10', '')

process.generator = cms.EDFilter("Pythia8HadronizerFilter",
    PythiaParameters = cms.PSet(
        parameterSets = cms.vstring('pythia8CommonSettings', 
            'pythia8CP5Settings', 
            'processParameters'),
        processParameters = cms.vstring('JetMatching:setMad = off', 
            'JetMatching:scheme = 1', 
            'JetMatching:merge = on', 
            'JetMatching:jetAlgorithm = 2', 
            'JetMatching:etaJetMax = 5.', 
            'JetMatching:coneRadius = 1.', 
            'JetMatching:slowJetPower = 1', 
            'JetMatching:qCut = 23.', 
            'JetMatching:nQmatch = 5', 
            'JetMatching:nJetMax = 2', 
            'JetMatching:doShowerKt = off'),
        pythia8CP5Settings = cms.vstring('Tune:pp 14', 
            'Tune:ee 7', 
            'MultipartonInteractions:ecmPow=0.03344', 
            'PDF:pSet=20', 
            'MultipartonInteractions:bProfile=2', 
            'MultipartonInteractions:pT0Ref=1.41', 
            'MultipartonInteractions:coreRadius=0.7634', 
            'MultipartonInteractions:coreFraction=0.63', 
            'ColourReconnection:range=5.176', 
            'SigmaTotal:zeroAXB=off', 
            'SpaceShower:alphaSorder=2', 
            'SpaceShower:alphaSvalue=0.118', 
            'SigmaProcess:alphaSvalue=0.118', 
            'SigmaProcess:alphaSorder=2', 
            'MultipartonInteractions:alphaSvalue=0.118', 
            'MultipartonInteractions:alphaSorder=2', 
            'TimeShower:alphaSorder=2', 
            'TimeShower:alphaSvalue=0.118'),
        pythia8CommonSettings = cms.vstring('Tune:preferLHAPDF = 2', 
            'Main:timesAllowErrors = 10000', 
            'Check:epTolErr = 0.01', 
            'Beams:setProductionScalesFromLHEF = off', 
            'SLHA:keepSM = on', 
            'SLHA:minMassSM = 1000.', 
            'ParticleDecays:limitTau0 = on', 
            'ParticleDecays:tau0Max = 10', 
            'ParticleDecays:allowPhotonRadiation = on')
    ),
    comEnergy = cms.double(13000.0),
    filterEfficiency = cms.untracked.double(1.0),
    maxEventsToPrint = cms.untracked.int32(1),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    pythiaPylistVerbosity = cms.untracked.int32(1)
)


# Path and EndPath definitions
process.generation_step = cms.Path(process.pgen)
process.simulation_step = cms.Path(process.psim)
process.digitisation_step = cms.Path(process.pdigi)
process.datamixing_step = cms.Path(process.pdatamix)
process.L1simulation_step = cms.Path(process.SimL1Emulator)
process.digi2raw_step = cms.Path(process.DigiToRaw)
process.genfiltersummary_step = cms.EndPath(process.genFilterSummary)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.PREMIXRAWoutput_step = cms.EndPath(process.PREMIXRAWoutput)

# Schedule definition
process.schedule = cms.Schedule(process.generation_step,process.genfiltersummary_step,process.simulation_step,process.digitisation_step,process.datamixing_step,process.L1simulation_step,process.digi2raw_step)
process.schedule.extend(process.HLTSchedule)
process.schedule.extend([process.endjob_step,process.PREMIXRAWoutput_step])
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)

#Setup FWK for multithreaded
process.options.numberOfThreads=cms.untracked.uint32(8)
process.options.numberOfStreams=cms.untracked.uint32(0)
# filter all path with the production filter sequence
for path in process.paths:
	getattr(process,path)._seq = process.generator * getattr(process,path)._seq 

# customisation of the process.

# Automatic addition of the customisation function from Configuration.GenProduction.customiseGenSimRawAodsim
from Configuration.GenProduction.customiseGenSimRawAodsim import noLumiCheck,randomSeed 

#call to customisation function noLumiCheck imported from Configuration.GenProduction.customiseGenSimRawAodsim
process = noLumiCheck(process)

#call to customisation function randomSeed imported from Configuration.GenProduction.customiseGenSimRawAodsim
process = randomSeed(process)

# Automatic addition of the customisation function from Configuration.DataProcessing.Utils
from Configuration.DataProcessing.Utils import addMonitoring 

#call to customisation function addMonitoring imported from Configuration.DataProcessing.Utils
process = addMonitoring(process)

# Automatic addition of the customisation function from HLTrigger.Configuration.customizeHLTforMC
from HLTrigger.Configuration.customizeHLTforMC import customizeHLTforMC 

#call to customisation function customizeHLTforMC imported from HLTrigger.Configuration.customizeHLTforMC
process = customizeHLTforMC(process)

# End of customisation functions

# Customisation from command line

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
