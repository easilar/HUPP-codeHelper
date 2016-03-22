import os,sys
import ROOT
sys.path.append('../python')
from helper import DrawNicePlot, DrawAdvancedPlot
from objects import getElectron, getElectrons, getZ
from math import log,sqrt, cos, sin, atan2, sinh

file = ROOT.TFile('../rootfiles/pgs_events_Q1.root')
tree = file.Get('LHCO')

h_Zeemass = ROOT.TH1F('h_Zeemass','Z mass',2000,0,2000)
h_Zeemass.Sumw2()

fileName='eeInvMass'
path = '../plots/'
if not os.path.exists(path):
  os.makedirs(path)

n_events = tree.GetEntries()
#print n_events
for i in range(n_events):
  tree.GetEntry(i)
  eles = getElectrons(tree)
  #print eles
  Z1 = getZ(eles)
  if Z1: h_Zeemass.Fill(Z1.M())  #Z is a Lorentz vector

DrawAdvancedPlot(h_Zeemass,'ee M_{inv.}',path,fileName)

