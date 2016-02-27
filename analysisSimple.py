import ROOT
from makeNicePlot import DrawNicePlot
import os,sys

file = ROOT.TFile('HPQ.root')
tree = file.Get('LHCO')

ptCut = 15
etaCut = 2.1
nPhotonsCut = 2
selection = 'abs(Photon.Eta)<'+str(etaCut)+'&&Photon.PT>'+str(ptCut)+'&&Photon_size=='+str(nPhotonsCut)
fileName='PhotonPt_For_selection_'+selection+'_.png'
path = 'plots/'
if not os.path.exists(path):
  os.makedirs(path)

histo = ROOT.TH1F('histo','Pt',100,0,500)
tree.Draw('Photon.PT>>histo',selection)
DrawNicePlot(histo,'Photon Pt',path,fileName)

