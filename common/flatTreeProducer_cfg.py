
# Load Flat tree package
from IPHCFlatTree.FlatTreeProducer.ConfFile_MINIAOD_cfg import *

# Set max number of events to run on
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.TFileService.fileName = cms.string("FlatTree.root")

# Relval for local tests
process.source.fileNames = cms.untracked.vstring('file:./RelValTTbar_13_CMSSW_7_3_0-MCRUN2_73_V7-v1_MINIAODSIM-file1.root')


