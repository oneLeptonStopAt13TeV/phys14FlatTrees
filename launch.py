#!/usr/bin/env python

from common import crabSubmitter
# Aliases
Prod = crabSubmitter.Prod
Dataset = crabSubmitter.Dataset

#####################
# Production config #
#####################

prod = Prod("v20150314-WildBeast")

##################
# Dataset config #
##################

Phys14AODSIM    = "/Phys14DR-PU20bx25_PHYS14_25_V1-v1/MINIAODSIM"
Phys14tsgAODSIM = "/Phys14DR-PU20bx25_tsg_PHYS14_25_V1-v1/MINIAODSIM"

datasets = [

     # Signals
     Dataset("T2tt_425_325",   "/SMS-T2tt_2J_mStop-425_mLSP-325_Tune4C_13TeV-madgraph-tauola"+Phys14tsgAODSIM),
     Dataset("T2tt_500_325",   "/SMS-T2tt_2J_mStop-500_mLSP-325_Tune4C_13TeV-madgraph-tauola"+Phys14tsgAODSIM),
     Dataset("T2tt_650_325",   "/SMS-T2tt_2J_mStop-650_mLSP-325_Tune4C_13TeV-madgraph-tauola"+Phys14tsgAODSIM),
     Dataset("T2tt_850_100",   "/SMS-T2tt_2J_mStop-850_mLSP-100_Tune4C_13TeV-madgraph-tauola"+Phys14tsgAODSIM),

     Dataset("ttH",            "/TTbarH_M-125_13TeV_amcatnlo-pythia8-tauola/Phys14DR-PU20bx25_tsg_PHYS14_25_V1-v2/MINIAODSIM"),

     # ttbar and related
     Dataset("ttbar-madgraph", "/TTJets_MSDecaysCKM_central_Tune4C_13TeV-madgraph-tauola"    +Phys14AODSIM),
     Dataset("ttbar-pythia8",  "/TT_Tune4C_13TeV-pythia8-tauola"                             +Phys14tsgAODSIM),
     Dataset("ttW",            "/TTWJets_Tune4C_13TeV-madgraph-tauola"                       +Phys14AODSIM),
     Dataset("ttZ",            "/TTZJets_Tune4C_13TeV-madgraph-tauola"                       +Phys14AODSIM),

     # Wjets
     Dataset("Wjets",          "/WJetsToLNu_13TeV-madgraph-pythia8-tauola"                   +Phys14AODSIM),

     # Singletop
     Dataset("singleTop_t",    "/TBarToLeptons_t-channel_Tune4C_CSA14_13TeV-aMCatNLO-tauola" +Phys14AODSIM),
     Dataset("singleTop_s",    "/TBarToLeptons_s-channel-CSA14_Tune4C_13TeV-aMCatNLO-tauola" +Phys14AODSIM),
     Dataset("singleTopbar_t", "/TToLeptons_t-channel-CSA14_Tune4C_13TeV-aMCatNLO-tauola"    +Phys14AODSIM),
     Dataset("singleTopbar_s", "/TToLeptons_s-channel-CSA14_Tune4C_13TeV-aMCatNLO-tauola"    +Phys14AODSIM),

     # Rare / bosons
     Dataset("DY",             "/DYJetsToLL_M-50_13TeV-madgraph-pythia8"                     +Phys14AODSIM),
     Dataset("ZZ",             "/ZZTo4L_Tune4C_13TeV-powheg-pythia8"                         +Phys14AODSIM),
     Dataset("WZ",             "/WZJetsTo3LNu_Tune4C_13TeV-madgraph-tauola"                  +Phys14AODSIM)
]


# Launch

crabSubmitter.launchProduction(prod,datasets)
