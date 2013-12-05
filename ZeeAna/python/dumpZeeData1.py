import FWCore.ParameterSet.Config as cms

process = cms.Process("dumpZee")

process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.StandardSequences.Services_cff')
process.load('Configuration.StandardSequences.GeometryDB_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.ZeeAna = cms.EDAnalyzer( "ZeeAna",
  PhotonCollection = cms.InputTag("NTElecTight"),
  GsfElectronCollection = cms.InputTag("PassingTightId"),
  EBSuperClusterCollection = cms.InputTag("correctedHybridSuperClusters"),
  EESuperClusterCollection = cms.InputTag("correctedMulti5x5SuperClustersWithPreshower"),
  foutName = cms.string( 'dumpZeeOutData_1.root' )
)



process.MessageLogger.cerr.FwkReport.reportEvery = cms.untracked.int32(1000)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

process.options = cms.untracked.PSet(
    SkipEvent = cms.untracked.vstring('ProductNotFound')
)



process.source = cms.Source("PoolSource",
    secondaryFileNames = cms.untracked.vstring(),
    #fileNames = cms.untracked.vstring('file:///afs/cern.ch/work/h/heli/private/calib/data/RAW-RECO/02A1EC8D-8C67-E211-9729-002618943864.root')
    fileNames = cms.untracked.vstring(
'/store/data/Run2012A/DoubleElectron/RAW-RECO/ZElectron-22Jan2013-v1/20000/70617445-9C67-E211-A592-003048678B08.root',
'/store/data/Run2012A/DoubleElectron/RAW-RECO/ZElectron-22Jan2013-v1/20000/7420C376-7267-E211-99C2-00261894394F.root',
'/store/data/Run2012A/DoubleElectron/RAW-RECO/ZElectron-22Jan2013-v1/20000/7425FAD1-8A67-E211-8042-002618943856.root',
'/store/data/Run2012A/DoubleElectron/RAW-RECO/ZElectron-22Jan2013-v1/20000/78D53F9B-B367-E211-9937-003048FFD744.root',
'/store/data/Run2012A/DoubleElectron/RAW-RECO/ZElectron-22Jan2013-v1/20000/7A0B772A-A667-E211-B3FC-002618943908.root',
'/store/data/Run2012A/DoubleElectron/RAW-RECO/ZElectron-22Jan2013-v1/20000/7A2F2F20-8467-E211-9440-003048FFD732.root',
'/store/data/Run2012A/DoubleElectron/RAW-RECO/ZElectron-22Jan2013-v1/20000/7A6CE74F-3069-E211-AF4D-002618943962.root',
'/store/data/Run2012A/DoubleElectron/RAW-RECO/ZElectron-22Jan2013-v1/20000/7A9B4A72-B967-E211-819C-002618943963.root',
'/store/data/Run2012A/DoubleElectron/RAW-RECO/ZElectron-22Jan2013-v1/20000/7CCD9971-7367-E211-B628-003048FFD75C.root',
'/store/data/Run2012A/DoubleElectron/RAW-RECO/ZElectron-22Jan2013-v1/20000/7E13C623-AC67-E211-BBDC-002618943821.root',
'/store/data/Run2012A/DoubleElectron/RAW-RECO/ZElectron-22Jan2013-v1/20000/7E238282-A467-E211-A1B2-00261894387A.root',
'/store/data/Run2012A/DoubleElectron/RAW-RECO/ZElectron-22Jan2013-v1/20000/7E267B90-B367-E211-9598-003048679294.root',
'/store/data/Run2012A/DoubleElectron/RAW-RECO/ZElectron-22Jan2013-v1/20000/7E8879F3-A967-E211-91E0-002618FDA28E.root',
'/store/data/Run2012A/DoubleElectron/RAW-RECO/ZElectron-22Jan2013-v1/20000/8255CD8E-A867-E211-8DBA-003048678AC0.root',
'/store/data/Run2012A/DoubleElectron/RAW-RECO/ZElectron-22Jan2013-v1/20000/82882342-9967-E211-968E-0026189438AC.root',
'/store/data/Run2012A/DoubleElectron/RAW-RECO/ZElectron-22Jan2013-v1/20000/866C662D-A667-E211-AB86-002618943950.root',
'/store/data/Run2012A/DoubleElectron/RAW-RECO/ZElectron-22Jan2013-v1/20000/86E6F6B9-E167-E211-A48C-0025905964A2.root',
'/store/data/Run2012A/DoubleElectron/RAW-RECO/ZElectron-22Jan2013-v1/20000/884AEC44-9C67-E211-9CAB-00261894394B.root',
'/store/data/Run2012A/DoubleElectron/RAW-RECO/ZElectron-22Jan2013-v1/20000/886C734A-A767-E211-9392-002618943877.root',
'/store/data/Run2012A/DoubleElectron/RAW-RECO/ZElectron-22Jan2013-v1/20000/8890F1C8-9F67-E211-A0E7-002618943856.root',
'/store/data/Run2012A/DoubleElectron/RAW-RECO/ZElectron-22Jan2013-v1/20000/88D6ADF3-A967-E211-8BAC-00304867BFB2.root',
'/store/data/Run2012A/DoubleElectron/RAW-RECO/ZElectron-22Jan2013-v1/20000/8A2BE74D-9767-E211-A5C1-003048678E52.root',
'/store/data/Run2012A/DoubleElectron/RAW-RECO/ZElectron-22Jan2013-v1/20000/8A92B99D-9067-E211-A5C1-003048FF9AA6.root',
'/store/data/Run2012A/DoubleElectron/RAW-RECO/ZElectron-22Jan2013-v1/20000/8C219E4A-A067-E211-AF85-002590596468.root',
'/store/data/Run2012A/DoubleElectron/RAW-RECO/ZElectron-22Jan2013-v1/20000/8E575836-C767-E211-A8C0-003048678A6C.root',
'/store/data/Run2012A/DoubleElectron/RAW-RECO/ZElectron-22Jan2013-v1/20000/8E6E0520-D367-E211-819F-003048678BB2.root',
'/store/data/Run2012A/DoubleElectron/RAW-RECO/ZElectron-22Jan2013-v1/20000/8E900B4C-8E67-E211-AAC2-003048679228.root',
'/store/data/Run2012A/DoubleElectron/RAW-RECO/ZElectron-22Jan2013-v1/20000/909B7BEF-A967-E211-B794-003048FF86CA.root',
'/store/data/Run2012A/DoubleElectron/RAW-RECO/ZElectron-22Jan2013-v1/20000/92D15870-AF67-E211-B9CE-0026189438A2.root',
'/store/data/Run2012A/DoubleElectron/RAW-RECO/ZElectron-22Jan2013-v1/20000/944469D8-AD67-E211-A865-002618943921.root',
'/store/data/Run2012A/DoubleElectron/RAW-RECO/ZElectron-22Jan2013-v1/20000/9479AC91-A467-E211-8E74-003048678A80.root',
'/store/data/Run2012A/DoubleElectron/RAW-RECO/ZElectron-22Jan2013-v1/20000/948C8072-AF67-E211-9C13-0026189438D9.root',
'/store/data/Run2012A/DoubleElectron/RAW-RECO/ZElectron-22Jan2013-v1/20000/949A7E05-1A68-E211-B6C5-002618FDA26D.root',
'/store/data/Run2012A/DoubleElectron/RAW-RECO/ZElectron-22Jan2013-v1/20000/9656DCC3-C267-E211-B3D4-002618943882.root',
'/store/data/Run2012A/DoubleElectron/RAW-RECO/ZElectron-22Jan2013-v1/20000/968452E8-B367-E211-8F88-0025905964C4.root',
'/store/data/Run2012A/DoubleElectron/RAW-RECO/ZElectron-22Jan2013-v1/20000/96B6AB1E-9867-E211-9290-003048678F8E.root',
'/store/data/Run2012A/DoubleElectron/RAW-RECO/ZElectron-22Jan2013-v1/20000/9AC4BF5F-AE67-E211-9BBC-0026189437FA.root',
'/store/data/Run2012A/DoubleElectron/RAW-RECO/ZElectron-22Jan2013-v1/20000/9AD15A97-A167-E211-8886-002590596498.root',
'/store/data/Run2012A/DoubleElectron/RAW-RECO/ZElectron-22Jan2013-v1/20000/9ADC90C4-6067-E211-BDD5-002618943934.root',
'/store/data/Run2012A/DoubleElectron/RAW-RECO/ZElectron-22Jan2013-v1/20000/9E559F62-AF67-E211-A2CC-003048FFD75C.root',
'/store/data/Run2012A/DoubleElectron/RAW-RECO/ZElectron-22Jan2013-v1/20000/A2A64736-A767-E211-8308-0026189437F5.root',
'/store/data/Run2012A/DoubleElectron/RAW-RECO/ZElectron-22Jan2013-v1/20000/A61A623C-7D67-E211-A39F-0025905938A4.root',
'/store/data/Run2012A/DoubleElectron/RAW-RECO/ZElectron-22Jan2013-v1/20000/A8D40E41-9C67-E211-81B7-00261894391B.root',
'/store/data/Run2012A/DoubleElectron/RAW-RECO/ZElectron-22Jan2013-v1/20000/B058A593-A467-E211-AFEE-0026189438E4.root',
'/store/data/Run2012A/DoubleElectron/RAW-RECO/ZElectron-22Jan2013-v1/20000/B4420B33-0168-E211-8229-002618943918.root',
'/store/data/Run2012A/DoubleElectron/RAW-RECO/ZElectron-22Jan2013-v1/20000/B67E975B-8767-E211-B074-003048678A7E.root',
'/store/data/Run2012A/DoubleElectron/RAW-RECO/ZElectron-22Jan2013-v1/20000/B6859838-A767-E211-B1D5-0026189438F2.root',
'/store/data/Run2012A/DoubleElectron/RAW-RECO/ZElectron-22Jan2013-v1/20000/B6C7D973-7F67-E211-B820-003048679168.root',
'/store/data/Run2012A/DoubleElectron/RAW-RECO/ZElectron-22Jan2013-v1/20000/BA0A989A-9E67-E211-92D4-003048678B0A.root',
'/store/data/Run2012A/DoubleElectron/RAW-RECO/ZElectron-22Jan2013-v1/20000/BCC12C9E-C067-E211-9AEE-003048678AE4.root',
'/store/data/Run2012A/DoubleElectron/RAW-RECO/ZElectron-22Jan2013-v1/20000/BE9CF974-886A-E211-957E-0025905964CC.root',
'/store/data/Run2012A/DoubleElectron/RAW-RECO/ZElectron-22Jan2013-v1/20000/BEA00DAE-6767-E211-99A5-0026189438B1.root',
'/store/data/Run2012A/DoubleElectron/RAW-RECO/ZElectron-22Jan2013-v1/20000/C03776EB-AA67-E211-9702-002618943986.root',
'/store/data/Run2012A/DoubleElectron/RAW-RECO/ZElectron-22Jan2013-v1/20000/C0413699-BA67-E211-835F-002618FDA216.root',
'/store/data/Run2012A/DoubleElectron/RAW-RECO/ZElectron-22Jan2013-v1/20000/C09BCFDF-CB67-E211-86A8-00304867908C.root',
'/store/data/Run2012A/DoubleElectron/RAW-RECO/ZElectron-22Jan2013-v1/20000/C0EADC52-A767-E211-993D-003048FFCB96.root',
'/store/data/Run2012A/DoubleElectron/RAW-RECO/ZElectron-22Jan2013-v1/20000/C0ED970A-6467-E211-B66C-003048679228.root',
'/store/data/Run2012A/DoubleElectron/RAW-RECO/ZElectron-22Jan2013-v1/20000/C0F2C63E-A667-E211-A23D-002618943964.root',
'/store/data/Run2012A/DoubleElectron/RAW-RECO/ZElectron-22Jan2013-v1/20000/C2797617-A467-E211-B157-003048678B0A.root',
'/store/data/Run2012A/DoubleElectron/RAW-RECO/ZElectron-22Jan2013-v1/20000/C2C26413-5D67-E211-9A79-003048679150.root',
'/store/data/Run2012A/DoubleElectron/RAW-RECO/ZElectron-22Jan2013-v1/20000/C2D4A590-5F67-E211-A8C1-0026189437F5.root',
'/store/data/Run2012A/DoubleElectron/RAW-RECO/ZElectron-22Jan2013-v1/20000/C455C00E-BC67-E211-89D9-003048FFCC18.root',
'/store/data/Run2012A/DoubleElectron/RAW-RECO/ZElectron-22Jan2013-v1/20000/C63675A9-BB67-E211-A7AE-00261894397B.root',
'/store/data/Run2012A/DoubleElectron/RAW-RECO/ZElectron-22Jan2013-v1/20000/C87BA980-B967-E211-9054-0026189438F8.root',
'/store/data/Run2012A/DoubleElectron/RAW-RECO/ZElectron-22Jan2013-v1/20000/C8ABA273-AC67-E211-A290-00304867D836.root',
'/store/data/Run2012A/DoubleElectron/RAW-RECO/ZElectron-22Jan2013-v1/20000/C8B31691-B367-E211-9E41-00261894380D.root',
'/store/data/Run2012A/DoubleElectron/RAW-RECO/ZElectron-22Jan2013-v1/20000/CA5B3377-B167-E211-B2FE-002618943910.root',
'/store/data/Run2012A/DoubleElectron/RAW-RECO/ZElectron-22Jan2013-v1/20000/CAB18055-BC67-E211-A7D5-003048678F9C.root',
'/store/data/Run2012A/DoubleElectron/RAW-RECO/ZElectron-22Jan2013-v1/20000/CC31E0FD-A067-E211-88D1-0030486792B6.root',
'/store/data/Run2012A/DoubleElectron/RAW-RECO/ZElectron-22Jan2013-v1/20000/CC335AE6-9667-E211-B643-0026189438B4.root',
'/store/data/Run2012A/DoubleElectron/RAW-RECO/ZElectron-22Jan2013-v1/20000/CCEBA523-A667-E211-9916-0026189438DE.root',
'/store/data/Run2012A/DoubleElectron/RAW-RECO/ZElectron-22Jan2013-v1/20000/CE447D60-6967-E211-974A-003048678B38.root',
'/store/data/Run2012A/DoubleElectron/RAW-RECO/ZElectron-22Jan2013-v1/20000/CEE3258E-B267-E211-9C84-003048678B36.root',
'/store/data/Run2012A/DoubleElectron/RAW-RECO/ZElectron-22Jan2013-v1/20000/D08A2363-A067-E211-847A-002618943934.root',
'/store/data/Run2012A/DoubleElectron/RAW-RECO/ZElectron-22Jan2013-v1/20000/D0C2E606-B667-E211-953A-00261894388D.root',
'/store/data/Run2012A/DoubleElectron/RAW-RECO/ZElectron-22Jan2013-v1/20000/D21C88F1-BE67-E211-801A-003048FFD7C2.root',
'/store/data/Run2012A/DoubleElectron/RAW-RECO/ZElectron-22Jan2013-v1/20000/D287818C-7E67-E211-B95B-00261894398A.root',
'/store/data/Run2012A/DoubleElectron/RAW-RECO/ZElectron-22Jan2013-v1/20000/D2A1CF6C-AE67-E211-B11E-002590593872.root',
'/store/data/Run2012A/DoubleElectron/RAW-RECO/ZElectron-22Jan2013-v1/20000/D2C7EEF9-A967-E211-9DF6-003048FFD760.root',
'/store/data/Run2012A/DoubleElectron/RAW-RECO/ZElectron-22Jan2013-v1/20000/D4FD63C3-6567-E211-BFEB-00259059391E.root',
'/store/data/Run2012A/DoubleElectron/RAW-RECO/ZElectron-22Jan2013-v1/20000/D60ECC9E-9B67-E211-9050-00304867924E.root',
'/store/data/Run2012A/DoubleElectron/RAW-RECO/ZElectron-22Jan2013-v1/20000/D67D0407-AA67-E211-B991-002590593902.root',
'/store/data/Run2012A/DoubleElectron/RAW-RECO/ZElectron-22Jan2013-v1/20000/D67EE061-B867-E211-B7A6-0026189438DB.root',
'/store/data/Run2012A/DoubleElectron/RAW-RECO/ZElectron-22Jan2013-v1/20000/DA8A1025-A667-E211-B0E2-00261894391C.root',
'/store/data/Run2012A/DoubleElectron/RAW-RECO/ZElectron-22Jan2013-v1/20000/DC9BB842-BE67-E211-B562-002354EF3BE3.root',
'/store/data/Run2012A/DoubleElectron/RAW-RECO/ZElectron-22Jan2013-v1/20000/DCAAA4FC-A967-E211-A229-003048678F92.root',
'/store/data/Run2012A/DoubleElectron/RAW-RECO/ZElectron-22Jan2013-v1/20000/DCC66F09-B667-E211-9777-00261894380B.root',
'/store/data/Run2012A/DoubleElectron/RAW-RECO/ZElectron-22Jan2013-v1/20000/DCDB1400-6567-E211-A505-003048679012.root',
'/store/data/Run2012A/DoubleElectron/RAW-RECO/ZElectron-22Jan2013-v1/20000/DE1C76FF-B667-E211-8E9E-00304867C034.root',
'/store/data/Run2012A/DoubleElectron/RAW-RECO/ZElectron-22Jan2013-v1/20000/DEC6CB11-9B67-E211-8ECE-003048FFD752.root',
'/store/data/Run2012A/DoubleElectron/RAW-RECO/ZElectron-22Jan2013-v1/20000/DEF5DD9D-5F67-E211-9C47-003048679070.root',
'/store/data/Run2012A/DoubleElectron/RAW-RECO/ZElectron-22Jan2013-v1/20000/E03D1C29-8867-E211-8ABF-0030486792A8.root',
'/store/data/Run2012A/DoubleElectron/RAW-RECO/ZElectron-22Jan2013-v1/20000/E086F08D-BA67-E211-84C5-002618943981.root',
'/store/data/Run2012A/DoubleElectron/RAW-RECO/ZElectron-22Jan2013-v1/20000/E0F3F335-9367-E211-BE9B-00261894397F.root',
'/store/data/Run2012A/DoubleElectron/RAW-RECO/ZElectron-22Jan2013-v1/20000/E20DBB2F-C567-E211-84D7-00259059642A.root',
'/store/data/Run2012A/DoubleElectron/RAW-RECO/ZElectron-22Jan2013-v1/20000/E44ED9D7-7567-E211-B043-00304867924A.root',
'/store/data/Run2012A/DoubleElectron/RAW-RECO/ZElectron-22Jan2013-v1/20000/E4869F18-A067-E211-9785-003048678FFA.root',
'/store/data/Run2012A/DoubleElectron/RAW-RECO/ZElectron-22Jan2013-v1/20000/E4D6398C-9767-E211-8CB3-00261894383E.root',
'/store/data/Run2012A/DoubleElectron/RAW-RECO/ZElectron-22Jan2013-v1/20000/E4FAA653-BC67-E211-9D48-003048FFCC18.root',
'/store/data/Run2012A/DoubleElectron/RAW-RECO/ZElectron-22Jan2013-v1/20000/E87B3F98-AF67-E211-8DB1-003048678B84.root',
'/store/data/Run2012A/DoubleElectron/RAW-RECO/ZElectron-22Jan2013-v1/20000/E8E12631-A667-E211-9DE4-002618943969.root',
'/store/data/Run2012A/DoubleElectron/RAW-RECO/ZElectron-22Jan2013-v1/20000/EC1C4470-CE67-E211-8450-002618943885.root',
'/store/data/Run2012A/DoubleElectron/RAW-RECO/ZElectron-22Jan2013-v1/20000/ECDADF74-6667-E211-84C0-0025905964BE.root',
'/store/data/Run2012A/DoubleElectron/RAW-RECO/ZElectron-22Jan2013-v1/20000/EE455869-9667-E211-BA05-003048678DA2.root',
'/store/data/Run2012A/DoubleElectron/RAW-RECO/ZElectron-22Jan2013-v1/20000/EEB433D0-BC67-E211-9962-002354EF3BDA.root',
'/store/data/Run2012A/DoubleElectron/RAW-RECO/ZElectron-22Jan2013-v1/20000/EEDE93EA-A967-E211-933A-003048678E52.root',
'/store/data/Run2012A/DoubleElectron/RAW-RECO/ZElectron-22Jan2013-v1/20000/F01F8D21-9667-E211-BC7C-00261894385A.root',
'/store/data/Run2012A/DoubleElectron/RAW-RECO/ZElectron-22Jan2013-v1/20000/F05E3C89-A467-E211-B6B8-002618943948.root',
'/store/data/Run2012A/DoubleElectron/RAW-RECO/ZElectron-22Jan2013-v1/20000/F06DB36C-AE67-E211-AC03-002590593872.root',
'/store/data/Run2012A/DoubleElectron/RAW-RECO/ZElectron-22Jan2013-v1/20000/F27542F4-BA67-E211-B695-003048FFD7D4.root',
'/store/data/Run2012A/DoubleElectron/RAW-RECO/ZElectron-22Jan2013-v1/20000/F44B569E-A767-E211-8D84-00259059391E.root',
'/store/data/Run2012A/DoubleElectron/RAW-RECO/ZElectron-22Jan2013-v1/20000/F46022CF-8B67-E211-BBAD-002590596490.root',
'/store/data/Run2012A/DoubleElectron/RAW-RECO/ZElectron-22Jan2013-v1/20000/F634F471-B967-E211-B98D-002618943807.root',
'/store/data/Run2012A/DoubleElectron/RAW-RECO/ZElectron-22Jan2013-v1/20000/F80C3D64-B867-E211-96C3-00304867920C.root',
'/store/data/Run2012A/DoubleElectron/RAW-RECO/ZElectron-22Jan2013-v1/20000/F8102E5F-6E67-E211-AAC6-002590593876.root',
'/store/data/Run2012A/DoubleElectron/RAW-RECO/ZElectron-22Jan2013-v1/20000/F8B43C67-9567-E211-94F8-00261894383E.root',
'/store/data/Run2012A/DoubleElectron/RAW-RECO/ZElectron-22Jan2013-v1/20000/F8D995F4-5B68-E211-9C28-0026189438CB.root',
'/store/data/Run2012A/DoubleElectron/RAW-RECO/ZElectron-22Jan2013-v1/20000/F8E0E07A-AC67-E211-B4B0-002618943957.root',
'/store/data/Run2012A/DoubleElectron/RAW-RECO/ZElectron-22Jan2013-v1/20000/FA6EFA7F-A367-E211-AB4E-003048678B94.root',
'/store/data/Run2012A/DoubleElectron/RAW-RECO/ZElectron-22Jan2013-v1/20000/FACAD462-A367-E211-B831-00261894383C.root',
'/store/data/Run2012A/DoubleElectron/RAW-RECO/ZElectron-22Jan2013-v1/20000/FAEE677C-A067-E211-B7B6-002618FDA208.root',
'/store/data/Run2012A/DoubleElectron/RAW-RECO/ZElectron-22Jan2013-v1/30000/B06652D0-7170-E211-9BD0-00304867BFBC.root'
        )
      
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





