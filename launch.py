#!/usr/bin/env python


from common import crabSubmitter

#####################
# Production config #
#####################

prod = crabSubmitter.Prod("testProd2")

##################
# Dataset config #
##################

backgroundMCPrefix = "/Phys14DR-PU20bx25_PHYS14_25_V1-v1/MINIAODSIM"
signalMCPrefix     = "/Phys14DR-PU20bx25_tsg_PHYS14_25_V1-v1/MINIAODSIM"

datasets = [
     crabSubmitter.Dataset("T2tt_425_325",   "/SMS-T2tt_2J_mStop-425_mLSP-325_Tune4C_13TeV-madgraph-tauola"+signalMCPrefix),
     crabSubmitter.Dataset("T2tt_500_325",   "/SMS-T2tt_2J_mStop-500_mLSP-325_Tune4C_13TeV-madgraph-tauola"+signalMCPrefix),
     crabSubmitter.Dataset("T2tt_650_325",   "/SMS-T2tt_2J_mStop-650_mLSP-325_Tune4C_13TeV-madgraph-tauola"+signalMCPrefix),
     crabSubmitter.Dataset("T2tt_850_100",   "/SMS-T2tt_2J_mStop-850_mLSP-100_Tune4C_13TeV-madgraph-tauola"+signalMCPrefix),

     crabSubmitter.Dataset("ttbar",          "/TTJets_MSDecaysCKM_central_Tune4C_13TeV-madgraph-tauola"    +backgroundMCPrefix),
     crabSubmitter.Dataset("Wjets",          "/WJetsToLNu_13TeV-madgraph-pythia8-tauola"                   +backgroundMCPrefix),
     crabSubmitter.Dataset("singleTop_t",    "/TBarToLeptons_t-channel_Tune4C_CSA14_13TeV-aMCatNLO-tauola" +backgroundMCPrefix),
     crabSubmitter.Dataset("singleTop_s",    "/TBarToLeptons_s-channel-CSA14_Tune4C_13TeV-aMCatNLO-tauola" +backgroundMCPrefix),
     crabSubmitter.Dataset("singleTopbar_t", "/TToLeptons_t-channel-CSA14_Tune4C_13TeV-aMCatNLO-tauola"    +backgroundMCPrefix),
     crabSubmitter.Dataset("singleTopbar_s", "/TToLeptons_s-channel-CSA14_Tune4C_13TeV-aMCatNLO-tauola"    +backgroundMCPrefix),
     crabSubmitter.Dataset("ttW",            "/TTWJets_Tune4C_13TeV-madgraph-tauola"                       +backgroundMCPrefix),
     crabSubmitter.Dataset("ttZ",            "/TTZJets_Tune4C_13TeV-madgraph-tauola"                       +backgroundMCPrefix)
]


# Launch

crabSubmitter.launchProduction(prod,datasets, checkTag=False)
