import ROOT

#get one electron from an event
def getElectron(tree,j):
  pt = tree.GetLeaf('Electron.PT').GetValue(j)
  eta = tree.GetLeaf('Electron.Eta').GetValue(j)
  phi= tree.GetLeaf('Electron.Phi').GetValue(j)
  charge = tree.GetLeaf('Electron.Charge').GetValue(j)
  Ntrk = tree.GetLeaf('Electron.Ntrk').GetValue(j)
  hadOverE = tree.GetLeaf('Electron.EhadOverEem').GetValue(j)
  cand={'pt':pt, 'eta':eta, 'phi':phi,'charge':charge,'Ntrk':Ntrk,'hadOverE':hadOverE}
  if pt > 15 and eta<2.5 and hadOverE < 0.2:
    return cand

#get all electrons insede an event
def getElectrons(tree):
  nelectrons = tree.GetLeaf('Electron_size').GetValue()
  electrons=[]
  for e in range(int(nelectrons)):
    electron = getElectron(tree,e)
    if electron:
      electrons.append(electron)
  return electrons

#get 2 electron lorentz vector 
def getZ(eles):
  e1 = ROOT.TLorentzVector()
  e2 = ROOT.TLorentzVector()
  Z = ROOT.TLorentzVector()
  if len(eles)==2:
    for perm in [eles, reversed(eles)]:
      elep,elen = perm
      if elep['charge'] == -elen['charge'] and elep['charge'] >0:
        e1.SetPtEtaPhiM(elen['pt'],elen['eta'],elen['phi'],0)
        e2.SetPtEtaPhiM(elep['pt'],elep['eta'],elep['phi'],0)
        Z = e1+e2
    return Z

