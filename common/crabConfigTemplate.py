
# ============================================

#datasetName = "RelValTTbar"
#datasetPath = "/RelValTTbar_13/CMSSW_7_3_0-MCRUN2_73_V7-v1/MINIAODSIM"
#prodTag     = "crabTest"

import os
userName=os.getlogin()
outputPath="/store/user/"+userName+"/FlatTrees/"+prodTag+"/"

# ============================================

from WMCore.Configuration import Configuration as crabTemplate

config = crabTemplate()

config.section_('General')
# =====================

config.General.transferOutputs = True
config.General.workArea        = prodTag
config.General.requestName     = datasetName

config.section_('JobType')
# =====================

config.JobType.psetName     = './common/flatTreeProducer_cfg.py'
config.JobType.pluginName   = 'Analysis'
config.JobType.inputFiles   = ['./common/conf.xml']
config.JobType.outputFiles  = ['FlatTree.root']
#config.JobType.pyCfgParams  = ['isData=0']

config.section_('Data')
# =====================

config.Data.totalUnits      = 10000
config.Data.unitsPerJob     = 2
config.Data.splitting       = 'FileBased'

config.Data.inputDataset    = datasetPath
config.Data.outLFNDirBase   = outputPath

config.Data.publication     = False
config.Data.publishDataName = ''
config.Data.publishDBS      = 'https://cmsweb.cern.ch/dbs/prod/phys03/DBSWriter'

config.section_('User')
# =====================

config.section_('Site')
# =====================

config.Site.storageSite = 'T2_FR_IPHC'
