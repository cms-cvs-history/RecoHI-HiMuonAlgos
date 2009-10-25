import FWCore.ParameterSet.Config as cms

from RecoMuon.Configuration.RecoMuon_cff import *

hiTracks = 'hiGlobalPrimTracks' #heavy ion track label

# replace with heavy ion track label
muons.inputCollectionLabels = [hiTracks, 'globalMuons', 'standAloneMuons:UpdatedAtVtx']

calomuons.inputTracks = hiTracks

globalMuons.TrackerCollectionLabel = hiTracks

# replace with heavy ion jet label
muons.JetExtractorPSet.JetCollectionLabel = cms.InputTag("iterativeConePu5CaloJets")

# HI muon sequence (passed to RecoHI.Configuration.Reconstruction_HI_cff)
muonRecoPbPb = cms.Sequence(muonreco_plus_isolation)

