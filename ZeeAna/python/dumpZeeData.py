import FWCore.ParameterSet.Config as cms

process = cms.Process("dumpZee")


process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.StandardSequences.Services_cff')
process.load('Configuration.StandardSequences.GeometryDB_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.GlobalTag.globaltag = 'FT_R_53_V18::All'

process.ZeeAna = cms.EDAnalyzer( "ZeeAna",
  PhotonCollection = cms.InputTag("NTElecTight"),
  GsfElectronCollection = cms.InputTag("PassingTightId"),
  EBSuperClusterCollection = cms.InputTag("correctedHybridSuperClusters"),
  EESuperClusterCollection = cms.InputTag("correctedMulti5x5SuperClustersWithPreshower"),
  #EBRecHitCollection = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
  #EERecHitCollection = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
  EBRecHitCollection = cms.InputTag("reducedEcalRecHitsEB"),
  EERecHitCollection = cms.InputTag("reducedEcalRecHitsEE"),
  foutName = cms.string( 'dumpZeeOutData.root' )
)


process.MessageLogger.cerr.FwkReport.reportEvery = cms.untracked.int32(100)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(10000)
)


#process.MessageLogger.cerr.FwkReport.reportEvery = cms.untracked.int32(100)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

process.options = cms.untracked.PSet(
    SkipEvent = cms.untracked.vstring('ProductNotFound')
)

process.source = cms.Source("PoolSource",
    secondaryFileNames = cms.untracked.vstring(),
    #fileNames = cms.untracked.vstring('')
    #fileNames = cms.untracked.vstring('file:///afs/cern.ch/work/h/heli/private/calib/data/RAW-RECO/02A1EC8D-8C67-E211-9729-002618943864.root')
    fileNames = cms.untracked.vstring(
  #     '/store/data/Run2012A/DoubleElectron/RAW-RECO/ZElectron-22Jan2013-v1/20000/06BA9527-AA67-E211-9372-002590593920.root'
       '/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/30000/EC8C5336-6770-E211-B31B-002618943902.root'
    )
    
#/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/30000/AC226482-6E70-E211-9E06-003048678AE2.root
#/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/30000/4A0C8B83-6470-E211-BBA0-003048679182.root
#/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20008/BEA32620-6667-E211-8B13-003048678B0C.root
)



HLTPath = "HLT_Ele*"
HLTProcessName = "HLT"
import copy 
from HLTrigger.HLTfilters.hltHighLevel_cfi import *
process.ZEEHltFilter = copy.deepcopy(hltHighLevel)
process.ZEEHltFilter.throw = cms.bool(False)
process.ZEEHltFilter.HLTPaths = [HLTPath]

#electron cuts
ELECTRON_ET_CUT_MIN = 10.0
TAG_ELECTRON_ET_CUT_MIN = 20.0
W_ELECTRON_ET_CUT_MIN = 27.0
ELECTRON_COLL = "gsfElectrons"
ELECTRON_CUTS = "(abs(superCluster.eta)<2.5) && (ecalEnergy*sin(superClusterPosition.theta)>" + str(ELECTRON_ET_CUT_MIN) + ")"

### cut on electron tag
ELECTRON_ET_CUT_MIN_TIGHT = 20.0
ELECTRON_ET_CUT_MIN_LOOSE = 10.0

#  GsfElectron ################ 
process.goodElectrons = cms.EDFilter("GsfElectronSelector",
    src = cms.InputTag( ELECTRON_COLL ),
    cut = cms.string( ELECTRON_CUTS )
)

process.PassingWP80 = process.goodElectrons.clone(
cut = cms.string(
    process.goodElectrons.cut.value() +
    " && (gsfTrack.trackerExpectedHitsInner.numberOfHits==0 && !(-0.02<convDist<0.02 && -0.02<convDcot<0.02))"
    " && (ecalEnergy*sin(superClusterPosition.theta)>" + str(ELECTRON_ET_CUT_MIN) + ")"
    " && ((isEB"
    " && ( dr03TkSumPt/p4.Pt <0.11 && dr03EcalRecHitSumEt/p4.Pt < 0.09 && dr03HcalTowerSumEt/p4.Pt  < 0.1 )"
    " && (sigmaIetaIeta<0.01)"
    " && ( -0.06<deltaPhiSuperClusterTrackAtVtx<0.06 )"
    " && ( -0.004<deltaEtaSuperClusterTrackAtVtx<0.004 )"
    " && (hadronicOverEm<0.04)"
    ")"
    " || (isEE"
    " && ( dr03TkSumPt/p4.Pt <0.05 && dr03EcalRecHitSumEt/p4.Pt < 0.06 && dr03HcalTowerSumEt/p4.Pt  < 0.03 )"
    " && (sigmaIetaIeta<0.03)"
    " && ( -0.03<deltaPhiSuperClusterTrackAtVtx<0.03 )"
    " && ( -0.007<deltaEtaSuperClusterTrackAtVtx<0.007 )"
    " && (hadronicOverEm<0.025) "
    "))"
    )
)


process.PassingVeryLooseId = process.goodElectrons.clone(
    cut = cms.string(
        process.goodElectrons.cut.value() +
        #    " && (gsfTrack.trackerExpectedHitsInner.numberOfHits<=1 && !(-0.02<convDist<0.02 && -0.02<convDcot<0.02))" #wrt std WP90 allowing 1 numberOfMissingExpectedHits
            " && (gsfTrack.trackerExpectedHitsInner.numberOfHits<=1 )" #wrt std WP90 allowing 1 numberOfMissingExpectedHits 
            " && (ecalEnergy*sin(superClusterPosition.theta)>" + str(ELECTRON_ET_CUT_MIN_LOOSE) + ")"
            " && ((isEB"
            " && ( dr03TkSumPt/p4.Pt <0.2 && dr03EcalRecHitSumEt/p4.Pt < 0.3 && dr03HcalTowerSumEt/p4.Pt  < 0.3 )"
            " && (sigmaIetaIeta<0.012)"
            " && ( -0.8<deltaPhiSuperClusterTrackAtVtx<0.8 )"
            " && ( -0.01<deltaEtaSuperClusterTrackAtVtx<0.01 )"
            " && (hadronicOverEm<0.15)"
            ")"
            " || (isEE"
            " && ( dr03TkSumPt/p4.Pt <0.2 && dr03EcalRecHitSumEt/p4.Pt < 0.3 && dr03HcalTowerSumEt/p4.Pt  < 0.3 )"
            " && (sigmaIetaIeta<0.033)"
            " && ( -0.7<deltaPhiSuperClusterTrackAtVtx<0.7 )"
            " && ( -0.01<deltaEtaSuperClusterTrackAtVtx<0.01 )"
            " && (hadronicOverEm<0.15) "
            "))"
        )
    )

process.PassingTightId = process.PassingVeryLooseId.clone(
    cut = cms.string(
        process.PassingVeryLooseId.cut.value() +
        " && (ecalEnergy*sin(superClusterPosition.theta)>" + str(ELECTRON_ET_CUT_MIN_TIGHT) + ")"
        )
    )

process.Zele_sequence = cms.Sequence(
    process.PassingVeryLooseId
    *process.PassingTightId
    )



process.output = cms.OutputModule("PoolOutputModule",
    outputCommands = cms.untracked.vstring(),
    fileName = cms.untracked.string('dumpRecoOut.root'),
)



process.NTElecTight = cms.EDFilter("PhotonSelector",
                                   src = cms.InputTag("photons"),
                                   cut = cms.string("hadronicOverEm<0.05"
                                                    " && (superCluster.rawEnergy*sin(superCluster.position.theta)>20.0)"
                                                    " && (abs(superCluster.eta)>2.5) " # && abs(superCluster.eta)<2.8
                                                    " && (sigmaIetaIeta<0.029)"
                                                    " && (ecalRecHitSumEtConeDR03/(p4.Pt) < 0.035)"
                                                    " && (hcalTowerSumEtConeDR03/(p4.Pt) < 0.11)"
                                                    " && (r9>0.89 && r9<1.02)"
                                                      )
                                   )




process.ZSkimSeq = cms.Sequence( process.ZEEHltFilter * process.Zele_sequence * process.NTElecTight )


#process.ZPath = cms.Path(process.ZSkimSeq)

process.NtuplePath = cms.Path(process.ZSkimSeq*process.ZeeAna)


#process.end = cms.EndPath(process.output)

####

process.GlobalTag = cms.ESSource("PoolDBESSource",
    DBParameters = cms.PSet(
        authenticationPath = cms.untracked.string(''),
        enableReadOnlySessionOnUpdateConnection = cms.untracked.bool(False),
        idleConnectionCleanupPeriod = cms.untracked.int32(10),
        messageLevel = cms.untracked.int32(0),
        enablePoolAutomaticCleanUp = cms.untracked.bool(False),
        enableConnectionSharing = cms.untracked.bool(True),
        connectionRetrialTimeOut = cms.untracked.int32(60),
        connectionTimeOut = cms.untracked.int32(60),
        authenticationSystem = cms.untracked.int32(0),
        connectionRetrialPeriod = cms.untracked.int32(10)
    ),
    BlobStreamerName = cms.untracked.string('TBufferBlobStreamingService'),
    toGet = cms.VPSet(),
    connect = cms.string('frontier://FrontierProd/CMS_COND_31X_GLOBALTAG'),
    globaltag = cms.string('START53_V7A::All')
)





