
//
// Package:    ZeeAna
// Class:      ZeeAna
// 
/**\class ZeeAna ZeeAna.cc HengneTools/ZeeAna/src/ZeeAna.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Hengne Li @ UVa
//         Created:  Mon May 27 22:34:13 CEST 2013
// $Id$
//
//


// system include files

// user include files
#include "DataFormats/Common/interface/View.h"
#include "DataFormats/Candidate/interface/Candidate.h"

#include "DataFormats/PatCandidates/interface/Electron.h"
#include "DataFormats/PatCandidates/interface/Photon.h"
#include "DataFormats/EgammaCandidates/interface/GsfElectronFwd.h"
#include "DataFormats/CaloRecHit/interface/CaloClusterFwd.h"
#include "DataFormats/EgammaReco/interface/SuperClusterFwd.h"
#include "DataFormats/EcalRecHit/interface/EcalRecHitCollections.h"
#include "DataFormats/EgammaReco/interface/SuperCluster.h"
#include "DataFormats/EcalDetId/interface/EBDetId.h"
#include "DataFormats/EcalDetId/interface/EEDetId.h"
#include "DataFormats/EcalDetId/interface/ESDetId.h"
#include "DataFormats/EgammaReco/interface/BasicCluster.h"
#include "Geometry/CaloGeometry/interface/CaloSubdetectorGeometry.h"
#include "Geometry/CaloGeometry/interface/CaloGeometry.h"
#include "Geometry/CaloGeometry/interface/CaloCellGeometry.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"
#include "FWCore/Framework/interface/ESHandle.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Utilities/interface/InputTag.h"


#include "SimGeneral/HepPDTRecord/interface/ParticleDataTable.h"

#include "TFile.h"
#include "TTree.h"
#include "TMath.h"
#include "TList.h"
#include "TLorentzVector.h"
#include "TVector3.h"
#include "TH1D.h"


//
// class declaration
//

class ZeeAna : public edm::EDAnalyzer {
public:
  ZeeAna(const edm::ParameterSet&);
  ~ZeeAna();

  static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

private:

  std::string foutName_;
  edm::Timestamp runTime_;
  edm::ESHandle<ParticleDataTable> pdt_;

  edm::Handle<reco::PhotonCollection> PhotonsHandle;
  edm::Handle<reco::GsfElectronCollection> GsfElectronsHandle;
  edm::Handle<std::vector<reco::SuperCluster>> EBSuperClustersHandle;
  edm::Handle<std::vector<reco::SuperCluster>> EESuperClustersHandle;
  edm::Handle<EBRecHitCollection> barrelRecHitsHandle;
  edm::Handle<EERecHitCollection> endcapRecHitsHandle;
 
  edm::InputTag PhotonsTAG;
  edm::InputTag GsfElectronsTAG;
  edm::InputTag EBSuperClustersTAG;
  edm::InputTag EESuperClustersTAG;
  edm::InputTag EBRecHitsTAG;
  edm::InputTag EERecHitsTAG;

  TFile* fout_;
  TTree* tree_;

  // tree variables
  Int_t         _runNum;
  Long64_t      _evtNum;
  Int_t         _lumBlk;
  UInt_t        _runTime;
  Int_t         _nVtx;

  Int_t _tnPar;

  Int_t _rStat[100]; // 0: not found, 1: GsfElectron, 2: Photon, 3: SuperCluster 
  Double_t _rR9[100];
  Double_t _rPx[100];
  Double_t _rPy[100];
  Double_t _rPz[100];
  Double_t _rPt[100];
  Double_t _rE[100];
  Double_t _rEta[100];
  Double_t _rPhi[100];
  Double_t _rVtx[100];
  Double_t _rVty[100];
  Double_t _rVtz[100];

  Double_t _rERaw[100];
  Int_t    _rNBCl[100];
  Double_t _rEtaWidth[100];
  Double_t _rPhiWidth[100];

  Float_t _rCaloE[100];
  Float_t _rEcalE[100];
  Float_t _rPresE[100];

  Int_t _rEB[100];
   
  Float_t _rSeedE[100];
  Int_t _rSeedIX[100];
  Int_t _rSeedIY[100];
  Int_t _rSeedIZ[100];

  Int_t _rNHits[100];
  Float_t _rHitE[100][200];
  Int_t _rHitIX[100][200];
  Int_t _rHitIY[100][200];
  Int_t _rHitIZ[100][200];
    

  Int_t _rZStat; //0 : less than 2 electrons, 1: Two GsfElectrons, 2: One GsfElectron one Photon, 3: Two Photons

  virtual void beginJob() ;
  virtual void analyze(const edm::Event&, const edm::EventSetup&);
  virtual void endJob() ;

  virtual void beginRun(edm::Run const&, edm::EventSetup const&);
  virtual void endRun(edm::Run const&, edm::EventSetup const&);
  virtual void beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&);
  virtual void endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&);

  void ResetTreeVars();
  void InitTree(void);
  void SetTreeEventSummaryVars(const edm::Event&);
  int SetTreeElectronVars(int, reco::GsfElectronCollection::const_iterator);
  int SetTreePhotonVars(int, reco::PhotonCollection::const_iterator);

  void SetTreeZVarsElecElec(reco::GsfElectronCollection::const_iterator, reco::GsfElectronCollection::const_iterator);
  void SetTreeZVarsElecPhot(reco::GsfElectronCollection::const_iterator, reco::PhotonCollection::const_iterator);

  // histograms
  TList _Hist1D;  
 
  // ----------member data ---------------------------
};

using namespace std;
using namespace edm;
using namespace reco;


ZeeAna::ZeeAna(const edm::ParameterSet& iConfig) {

  foutName_ = iConfig.getParameter<string>( "foutName" );
  PhotonsTAG = iConfig.getParameter<InputTag>("PhotonCollection");
  GsfElectronsTAG = iConfig.getParameter<InputTag>("GsfElectronCollection");
  EBSuperClustersTAG = iConfig.getParameter<InputTag>("EBSuperClusterCollection");
  EESuperClustersTAG = iConfig.getParameter<InputTag>("EESuperClusterCollection");
  EBRecHitsTAG = iConfig.getParameter<InputTag>("EBRecHitCollection");
  EERecHitsTAG = iConfig.getParameter<InputTag>("EERecHitCollection");

}


ZeeAna::~ZeeAna() { }

//
// member functions
//

// ------------ method called for each event  ------------
void ZeeAna::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup) {
       
  iSetup.getData( pdt_ );
     
  iEvent.getByLabel(PhotonsTAG, PhotonsHandle);
  iEvent.getByLabel(GsfElectronsTAG, GsfElectronsHandle);
  iEvent.getByLabel(EBSuperClustersTAG, EBSuperClustersHandle);
  iEvent.getByLabel(EESuperClustersTAG, EESuperClustersHandle);
  iEvent.getByLabel(EBRecHitsTAG,barrelRecHitsHandle);
  iEvent.getByLabel(EERecHitsTAG,endcapRecHitsHandle);

  //
  ResetTreeVars();
  //    
  SetTreeEventSummaryVars(iEvent);


  // at least one GsfElectron
  if (GsfElectronsHandle->size()<1) return;

  // at least two EM particles
  if ((GsfElectronsHandle->size()+PhotonsHandle->size())<2) return;

  // let's always only take 2
  _tnPar = 2;

  // ZStat at least be 1
  _rZStat = 1; 

  // number of electrons and photons
  int NGsfEles = GsfElectronsHandle->size();
  int NPhotons = PhotonsHandle->size();

  // iterators storing GsfElectons and Photons 
  GsfElectronCollection::const_iterator GsfEle1(NULL);
  GsfElectronCollection::const_iterator GsfEle2(NULL);   
  PhotonCollection::const_iterator Photon1(NULL);   
  PhotonCollection::const_iterator Photon2(NULL);   

  // look for 2 leading pT gsf electrons
  // leading
  double maxpT(-10000.0);
  for( GsfElectronCollection::const_iterator eleIter1 = GsfElectronsHandle->begin();
       eleIter1 != GsfElectronsHandle->end();
       eleIter1++){
    if (eleIter1->pt() > maxpT) {
      maxpT = eleIter1->pt();
      GsfEle1 = eleIter1;
    } 
  }

  // next leading
  if (NGsfEles>1) {
    maxpT = -100000.0;
    for( GsfElectronCollection::const_iterator eleIter1 = GsfElectronsHandle->begin();
         eleIter1 != GsfElectronsHandle->end();
         eleIter1++){
      if (eleIter1 == GsfEle1) continue;
      if (eleIter1->pt() > maxpT) {
        maxpT = eleIter1->pt();
        GsfEle2 = eleIter1;
      }
    }
  }
  
  // look for 2 leading pT photons
  // leading
  if (NPhotons>0) {
    maxpT = -10000.0;
    for( PhotonCollection::const_iterator eleIter1 = PhotonsHandle->begin();
         eleIter1 != PhotonsHandle->end();
         eleIter1++){
      if (eleIter1->pt() > maxpT) {
        maxpT = eleIter1->pt();
        Photon1 = eleIter1;
      }
    }
  }

  // next to leading
  if (NPhotons>1) {
    maxpT = -10000.0;
    for( PhotonCollection::const_iterator eleIter1 = PhotonsHandle->begin();
         eleIter1 != PhotonsHandle->end();
         eleIter1++){
      if (eleIter1 == Photon1) continue;
      if (eleIter1->pt() > maxpT) {
        maxpT = eleIter1->pt();
        Photon2 = eleIter1;
      }
    }
  }

  // always require at least one GsfElectron
  if (NGsfEles>=1) {
    SetTreeElectronVars(0, GsfEle1);
  } 

  // if has another GsfElectron, take it
  if (NGsfEles>=2) {
    SetTreeElectronVars(1, GsfEle2);
    _rZStat = 1;
  }

  // if only 1 GsfElectron, the 2nd one take the leading Photon
  if (NGsfEles==1&&NPhotons>=1) {
    SetTreePhotonVars(1, Photon1);
    // ZStat be 2 if second elec is a photon 
    _rZStat = 2;
  }

  if (_rZStat>0) tree_->Fill();

  return;
}

void ZeeAna::InitTree(){

  if(tree_==NULL) return;

  tree_->Branch("runNum", &_runNum, "runNum/I");
  tree_->Branch("evtNum", &_evtNum, "evtNum/l");
  tree_->Branch("lumBlk", &_lumBlk, "lumBlk/I");
  tree_->Branch("runTime", &_runTime, "runTime/i");
  tree_->Branch("nVtx", &_nVtx, "nVtx/I");
  

  // reco
  tree_->Branch("tnPar", &_tnPar, "tnPar/I");
  tree_->Branch("rStat", _rStat, "rStat[tnPar]/I"); //  0: not found, 1: GsfElectron, 2: Photon, 3: SuperCluster  
  tree_->Branch("rR9", _rR9, "rR9[tnPar]/D");
  tree_->Branch("rPx", _rPx, "rPx[tnPar]/D");
  tree_->Branch("rPy", _rPy, "rPy[tnPar]/D");
  tree_->Branch("rPz", _rPz, "rPz[tnPar]/D");
  tree_->Branch("rPt", _rPt, "rPt[tnPar]/D");
  tree_->Branch("rE", _rE, "rE[tnPar]/D");
  tree_->Branch("rEta", _rEta, "rEta[tnPar]/D");
  tree_->Branch("rPhi", _rPhi, "rPhi[tnPar]/D");
  tree_->Branch("rVtx", _rVtx, "rVtx[tnPar]/D");
  tree_->Branch("rVty", _rVty, "rVty[tnPar]/D");
  tree_->Branch("rVtz", _rVtz, "rVtz[tnPar]/D");

  tree_->Branch("rERaw", _rERaw, "rERaw[tnPar]/D");
  tree_->Branch("rNBCl", _rNBCl, "rNBCl[tnPar]/D");
  tree_->Branch("rEtaWidth", _rEtaWidth, "rEtaWidth[tnPar]/D");
  tree_->Branch("rPhiWidth", _rPhiWidth, "rPhiWidth[tnPar]/D");

  tree_->Branch("rCaloE", _rCaloE, "rCaloE[tnPar]/F");
  tree_->Branch("rEcalE", _rEcalE, "rEcalE[tnPar]/F");
  tree_->Branch("rPresE", _rPresE, "rPresE[tnPar]/F");
  tree_->Branch("rEB", _rEB, "rEB[tnPar]/I");
  tree_->Branch("rSeedE", _rSeedE, "rSeedE[tnPar]/F");
  tree_->Branch("rSeedIX", _rSeedIX, "rSeedIX[tnPar]/I");
  tree_->Branch("rSeedIY", _rSeedIY, "rSeedIY[tnPar]/I");
  tree_->Branch("rSeedIZ", _rSeedIZ, "rSeedIZ[tnPar]/I");
  tree_->Branch("rNHits", _rNHits, "rNHits[tnPar]/I");
  tree_->Branch("rHitE", _rHitE, "rHitE[tnPar][200]/F");
  tree_->Branch("rHitIX", _rHitIX, "rHitIX[tnPar][200]/I");
  tree_->Branch("rHitIY", _rHitIY, "rHitIY[tnPar][200]/I");
  tree_->Branch("rHitIZ", _rHitIZ, "rHitIZ[tnPar][200]/I");

  tree_->Branch("rZStat", &_rZStat, "rZStat/I"); // 0: not found, 1: patElec, 2: EB SuperCluster, 3: EE SuperCluster 

}


void ZeeAna::SetTreeEventSummaryVars(const edm::Event& iEvent){
  runTime_   = iEvent.eventAuxiliary().time();
  _runTime = runTime_.unixTime();
  _runNum = iEvent.id().run();
  _evtNum = iEvent.id().event();
  if( iEvent.isRealData() ) {
    _lumBlk = iEvent.luminosityBlock();
  } else {
    _lumBlk = -1;
  }
  return;
}


// ------------ method called once each job just before starting event loop  ------------
void ZeeAna::beginJob() {

  fout_ = new TFile(foutName_.c_str(), "recreate");
  if(fout_->IsZombie()){
    throw cms::Exception("OutputError") <<  "Output tree not created (Zombie): " << foutName_;
    return;
  }
  fout_->cd();

  tree_ = new TTree("tree", "tree");

  tree_->SetDirectory(fout_);

  InitTree(); 

}

void ZeeAna::ResetTreeVars() {
  // reco Z
  _rZStat = 0;
  _tnPar = 0;

  for (int i=0; i<2; i++) {
    _rStat[i]=0; //   0: not found, 1: GsfElectron, 2: Photon, 3: SuperCluster 
    _rR9[i]=-100000;
    _rPx[i]=-100000;
    _rPy[i]=-100000;
    _rPz[i]=-100000;
    _rPt[i]=-100000;
    _rE[i]=-100000;
    _rEta[i]=-100000;
    _rPhi[i]=-100000;
    _rVtx[i]=-100000;
    _rVty[i]=-100000;
    _rVtz[i]=-100000;
    _rERaw[i]=-100000;
    _rNBCl[i]=-100000;
    _rEtaWidth[i]=-100000;
    _rPhiWidth[i]=-100000;
    _rCaloE[i]=-100000;
    _rEcalE[i]=-100000;
    _rPresE[i]=-100000;
    _rEB[i]=-100000;
    _rSeedE[i]=-100000;
    _rSeedIX[i]=-100000;
    _rSeedIY[i]=-100000;
    _rSeedIZ[i]=-100000;
    _rNHits[i]=-100000;
    for (int j=0; j<200; j++){
      _rHitE[i][j]=-100000;
      _rHitIX[i][j]=-100000;
      _rHitIY[i][j]=-100000;
      _rHitIZ[i][j]=-100000;
    }
  }


}

int ZeeAna::SetTreeElectronVars(int i, GsfElectronCollection::const_iterator eleIter1) {

  _rStat[i] = 1; 
  _rR9[i] = double(eleIter1->r9());
  _rPx[i] = eleIter1->px();
  _rPy[i] = eleIter1->py();
  _rPz[i] = eleIter1->pz();
  _rPt[i] = eleIter1->pt();
  _rE[i] = eleIter1->energy();
  _rEta[i] = eleIter1->eta();
  _rPhi[i] = TVector2::Phi_0_2pi(eleIter1->phi());
  _rVtx[i] = eleIter1->vx();
  _rVty[i] = eleIter1->vy();
  _rVtz[i] = eleIter1->vz();
  _rERaw[i] = eleIter1->superCluster()->rawEnergy();
  _rNBCl[i] = int(eleIter1->superCluster()->clustersSize());
  _rEtaWidth[i] = eleIter1->superCluster()->etaWidth();
  _rPhiWidth[i] = eleIter1->superCluster()->phiWidth();

  _rCaloE[i] = eleIter1->caloEnergy();
  _rEcalE[i] = eleIter1->ecalEnergy();
  _rPresE[i] = eleIter1->superCluster()->preshowerEnergy();

  // EB or EE
  _rEB[i] = (eleIter1->isEB() ? 1 : 0 );

  // get SuperCluster and Calo Hit
  const reco::SuperCluster& sc = *(eleIter1->superCluster());
  const std::vector< std::pair<DetId, float> > & scHits = sc.hitsAndFractions();
 
  DetId seed = (sc.seed()->seed()); 
  if (seed.subdetId()==EcalBarrel) {
    // Seed in EB
    const EcalRecHit seedHit = *(barrelRecHitsHandle->find(seed));
    _rSeedE[i] = seedHit.energy();
    _rSeedIX[i] = EBDetId(seed).ieta();
    _rSeedIY[i] = EBDetId(seed).iphi();
    _rSeedIZ[i] = 0; // 0 for EB
  }
  else if (seed.subdetId()==EcalEndcap) {
    // seed in EE
    const EcalRecHit seedHit = *(endcapRecHitsHandle->find(seed));
    _rSeedE[i] = seedHit.energy();
    _rSeedIX[i] = EEDetId(seed).ix();
    _rSeedIY[i] = EEDetId(seed).iy();
    _rSeedIZ[i] = EEDetId(seed).zside(); // +1 for EE+; -1 for EE-
  }
  else {
    // seed neither EB nor EE, seed position -1000, -1000.
    _rSeedIX[i] = -1000;
    _rSeedIY[i] = -1000;
    _rSeedIZ[i] = -1000;
  }

  // loop over Hits
  int iHit = 0; 
  for(std::vector< std::pair<DetId, float> >::const_iterator scHit_itr = scHits.begin();
        scHit_itr != scHits.end(); scHit_itr++){
    // get hit position, etc..
    if ((*scHit_itr).first.subdetId()==EcalBarrel) {
      // EB
      const EcalRecHit ecalRecHit = *(barrelRecHitsHandle->find( (*scHit_itr).first ));
      EBDetId ecalrechit((*scHit_itr).first );
      // get hit energy, position, etc..
      _rHitE[i][iHit] = ecalRecHit.energy();
      _rHitIX[i][iHit] = ecalrechit.ieta();
      _rHitIY[i][iHit] = ecalrechit.iphi();
      _rHitIZ[i][iHit] = 0; // 0 for EB
    }
    else if ((*scHit_itr).first.subdetId()==EcalEndcap) {
      // EE
      const EcalRecHit ecalRecHit = *(endcapRecHitsHandle->find( (*scHit_itr).first ));
      EEDetId ecalrechit((*scHit_itr).first );
      // get hit energy, position, etc..
      _rHitE[i][iHit] = ecalRecHit.energy();
      _rHitIX[i][iHit] = ecalrechit.ix();
      _rHitIY[i][iHit] = ecalrechit.iy();
      _rHitIZ[i][iHit] = ecalrechit.zside(); //  +1 for EE+; -1 for EE-  
    }
    else {
      // neither EB nor EE, continue
      continue;
    }
    iHit++;
  }
  //
  _rNHits[i] = iHit;


/*
  // EB
  if (eleIter1->isEB()) {
    // find the seed 
    EBDetId seed=(sc.seed()->seed());
    const EcalRecHit seedHit = *(barrelRecHitsHandle->find(seed));
    
    _rSeedE[i] = seedHit.energy();
    _rSeedIX[i] = seed.ieta();
    _rSeedIY[i] = seed.iphi();
    _rSeedIZ[i] = 0; // 0 for EB

    // loop over Hits
    int iHit = 0; 
    for(std::vector< std::pair<DetId, float> >::const_iterator scHit_itr = scHits.begin();
          scHit_itr != scHits.end(); scHit_itr++){
      const EcalRecHit ecalRecHit = *(barrelRecHitsHandle->find( (*scHit_itr).first ));
      EBDetId ecalrechit((*scHit_itr).first );
      // get hit energy, position, etc..
      _rHitE[i][iHit] = ecalRecHit.energy();
      _rHitIX[i][iHit] = ecalrechit.ieta();
      _rHitIY[i][iHit] = ecalrechit.iphi();
      _rHitIZ[i][iHit] = 0; // 0 for EB
      iHit++;
    }
    //
    _rNHits[i] = iHit;
  }
  // EE 
  else {
    // find the seed 
    EEDetId seed=(sc.seed()->seed());
    const EcalRecHit seedHit = *(endcapRecHitsHandle->find(seed));
    _rSeedE[i] = seedHit.energy();
    _rSeedIX[i] = seed.ix();
    _rSeedIY[i] = seed.iy();
    _rSeedIZ[i] = seed.zside(); // +1 for EE+; -1 for EE-
    // loop over Hits
    int iHit = 0;
    for(std::vector< std::pair<DetId, float> >::const_iterator scHit_itr = scHits.begin();
          scHit_itr != scHits.end(); scHit_itr++){
      const EcalRecHit ecalRecHit = *(endcapRecHitsHandle->find( (*scHit_itr).first ));
      EEDetId ecalrechit((*scHit_itr).first );
      // get hit energy, position, etc..
      _rHitE[i][iHit] = ecalRecHit.energy();
      _rHitIX[i][iHit] = ecalrechit.ix();
      _rHitIY[i][iHit] = ecalrechit.iy();
      _rHitIZ[i][iHit] = ecalrechit.zside(); //  +1 for EE+; -1 for EE-
      iHit++;
    }
    //
    _rNHits[i] = iHit;
  }
*/    
  // return 0 if all success
  return 0;
}

int ZeeAna::SetTreePhotonVars(int i, PhotonCollection::const_iterator eleIter1) {

  _rStat[i] = 2;
  _rR9[i] = double(eleIter1->r9());
  _rPx[i] = eleIter1->px();
  _rPy[i] = eleIter1->py();
  _rPz[i] = eleIter1->pz();
  _rPt[i] = eleIter1->pt();
  _rE[i] = eleIter1->energy();
  _rEta[i] = eleIter1->eta();
  _rPhi[i] = TVector2::Phi_0_2pi(eleIter1->phi());
  _rVtx[i] = eleIter1->vx();
  _rVty[i] = eleIter1->vy();
  _rVtz[i] = eleIter1->vz();
  _rERaw[i] = eleIter1->superCluster()->rawEnergy();
  _rNBCl[i] = int(eleIter1->superCluster()->clustersSize());
  _rEtaWidth[i] = eleIter1->superCluster()->etaWidth();
  _rPhiWidth[i] = eleIter1->superCluster()->phiWidth();

  //_rCaloE[i] = eleIter1->caloEnergy();
  //_rEcalE[i] = eleIter1->ecalEnergy();
  _rPresE[i] = eleIter1->superCluster()->preshowerEnergy(); 
  // EB or EE
  _rEB[i] = (eleIter1->isEB() ? 1 : 0);
  
  // get SuperCluster and Calo Hit
  const reco::SuperCluster& sc = *(eleIter1->superCluster());
  const std::vector< std::pair<DetId, float> > & scHits = sc.hitsAndFractions();

  DetId seed = (sc.seed()->seed());
  const EcalRecHit seedHit = *(barrelRecHitsHandle->find(seed));
  _rSeedE[i] = seedHit.energy();
  if (seed.subdetId()==EcalBarrel) {
    // Seed in EB
    _rSeedIX[i] = EBDetId(seed).ieta();
    _rSeedIY[i] = EBDetId(seed).iphi();
    _rSeedIZ[i] = 0; // 0 for EB
  }
  else if (seed.subdetId()==EcalEndcap) {
    // seed in EE
    _rSeedIX[i] = EEDetId(seed).ix();
    _rSeedIY[i] = EEDetId(seed).iy();
    _rSeedIZ[i] = EEDetId(seed).zside(); // +1 for EE+; -1 for EE-
  }
  else {
    // seed neither EB nor EE, seed position -1000, -1000.
    _rSeedIX[i] = -1000;
    _rSeedIY[i] = -1000;
    _rSeedIZ[i] = -1000;
  }

  // loop over Hits
  int iHit = 0;
  for(std::vector< std::pair<DetId, float> >::const_iterator scHit_itr = scHits.begin();
        scHit_itr != scHits.end(); scHit_itr++){
    const EcalRecHit ecalRecHit = *(barrelRecHitsHandle->find( (*scHit_itr).first ));
    // get hit energy, position, etc..
    _rHitE[i][iHit] = ecalRecHit.energy();
    // get hit position, etc..
    if ((*scHit_itr).first.subdetId()==EcalBarrel) {
      // EB
      EBDetId ecalrechit((*scHit_itr).first );
      _rHitIX[i][iHit] = ecalrechit.ieta();
      _rHitIY[i][iHit] = ecalrechit.iphi();
      _rHitIZ[i][iHit] = 0; // 0 for EB
    }
    else if ((*scHit_itr).first.subdetId()==EcalEndcap) {
      // EE
      EEDetId ecalrechit((*scHit_itr).first );
      _rHitIX[i][iHit] = ecalrechit.ix();
      _rHitIY[i][iHit] = ecalrechit.iy();
      _rHitIZ[i][iHit] = ecalrechit.zside(); //  +1 for EE+; -1 for EE-  
    }
    else {
      // neither EB nor EE, continue
      continue;
    }
    iHit++;
  }
  //
  _rNHits[i] = iHit;
 
/* 
  // EB
  if (eleIter1->isEB()) {
    // find the seed 
    EBDetId seed=(sc.seed()->seed());
    const EcalRecHit seedHit = *(barrelRecHitsHandle->find(seed));
    
    _rSeedE[i] = seedHit.energy();
    _rSeedIX[i] = seed.ieta();
    _rSeedIY[i] = seed.iphi();
    _rSeedIZ[i] = 0; // 0 for EB
    

    // loop over Hits
    int iHit = 0; 
    for(std::vector< std::pair<DetId, float> >::const_iterator scHit_itr = scHits.begin();
          scHit_itr != scHits.end(); scHit_itr++){
      const EcalRecHit ecalRecHit = *(barrelRecHitsHandle->find( (*scHit_itr).first ));
      EBDetId ecalrechit((*scHit_itr).first );
      // get hit energy, position, etc..
      _rHitE[i][iHit] = ecalRecHit.energy();
      _rHitIX[i][iHit] = ecalrechit.ieta();
      _rHitIY[i][iHit] = ecalrechit.iphi();
      _rHitIZ[i][iHit] = 0; // 0 for EB
      iHit++;
    }
    //
    _rNHits[i] = iHit;
  }
  // EE 
  else {
    // find the seed 
    EEDetId seed=(sc.seed()->seed());
    const EcalRecHit seedHit = *(endcapRecHitsHandle->find(seed));
    _rSeedE[i] = seedHit.energy();
    _rSeedIX[i] = seed.ix();
    _rSeedIY[i] = seed.iy();
    _rSeedIZ[i] = seed.zside(); // +1 for EE+; -1 for EE-
    // loop over Hits
    int iHit = 0;
    for(std::vector< std::pair<DetId, float> >::const_iterator scHit_itr = scHits.begin();
          scHit_itr != scHits.end(); scHit_itr++){
      const EcalRecHit ecalRecHit = *(endcapRecHitsHandle->find( (*scHit_itr).first ));
      EEDetId ecalrechit((*scHit_itr).first );
      // get hit energy, position, etc..
      _rHitE[i][iHit] = ecalRecHit.energy();
      _rHitIX[i][iHit] = ecalrechit.ix();
      _rHitIY[i][iHit] = ecalrechit.iy();
      _rHitIZ[i][iHit] = ecalrechit.zside(); //  +1 for EE+; -1 for EE-
      iHit++;
    }
    //
    _rNHits[i] = iHit;
  }
*/
  // return 0 if all success
  return 0;
}

// ------------ method called once each job just after ending the event loop  ------------
void ZeeAna::endJob() {
  if (tree_->GetEntries()>0){
    tree_->BuildIndex("runNum","evtNum");
  }
  fout_->cd();
  tree_->Write();
 
  // write hists
  TIter next(&_Hist1D);
  while (TObject *obj = next()) {
   obj->Write();
  }
  
  fout_->Close();
}

// ------------ method called when starting to processes a run  ------------
void ZeeAna::beginRun(edm::Run const&, edm::EventSetup const&){}

// ------------ method called when ending the processing of a run  ------------
void ZeeAna::endRun(edm::Run const&, edm::EventSetup const&){}

// ------------ method called when starting to processes a luminosity block  ------------
void ZeeAna::beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&){}

// ------------ method called when ending the processing of a luminosity block  ------------
void ZeeAna::endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&){}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void ZeeAna::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(ZeeAna);
