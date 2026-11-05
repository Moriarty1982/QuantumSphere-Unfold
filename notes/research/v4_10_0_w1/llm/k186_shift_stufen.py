"""k186 (Erkundung, I1 / QAM-Shift): Ergeben Sigma-Verkettungen (Impulssumme) der Konnektoren aus k185 eine vierte, gleichabstaendige
String-Stufe q^2 = +4 m^2 sinh 2eta fuer jedes eta? Zusaetzlich: Konnektoren unter wiederholter Frame-Fortsetzung eta -> eta + i pi/2."""
import numpy as np, itertools
def vecs(eta):
    c,s=np.cosh(eta),np.sinh(eta);pM=np.array([c,s]);pTp=np.array([s,c]);pTm=np.array([s,-c])
    return {'c0 Uebergang gegen':pM-pTm,'c1a mit (Summe)':pM+pTp,'c1b mit (Differenz)':pM-pTp,'c2 Paar gegen':pM+pTm}
q2=lambda q:q[0]**2-q[1]**2
etas=[0.1,0.3,np.arctanh(0.5493),1.0,1.5]
names=list(vecs(0.3).keys());res={}
for a,b in itertools.combinations_with_replacement(names,2):
    vals=[q2(vecs(e)[a]+vecs(e)[b])/(np.sinh(2*e)) for e in etas];res[(a,b)]=vals
print('q^2 / (m^2 sinh 2eta) der Sigma-Verkettungen (Ziel fuer Stufe 4: +4 bei jedem eta):')
for (a,b),v in res.items(): print(f'  {a:22s} + {b:22s}: {np.round(v,4)}')
print('q^2 / m^2 (absolut) fuer c0+c2 und c1a+c1b:',[round(q2(vecs(e)['c0 Uebergang gegen']+vecs(e)['c2 Paar gegen']),10) for e in etas],[round(q2(vecs(e)['c1a mit (Summe)']+vecs(e)['c1b mit (Differenz)']),10) for e in etas])
# Frame-Fortsetzung: Bilder von p_M unter eta -> eta + k i pi/2
e=0.6;c,s=np.cosh(e),np.sinh(e);imgs={'p_M':np.array([c,s]),'p_T':np.array([s,c]),'-p_M':-np.array([c,s]),'-p_T':-np.array([s,c])}
print('Fortsetzung zyklisch der Ordnung 4: p(eta + 2 i pi) = p(eta). Konnektor-Massen p_M +- Bild (/m^2):',{k:(round(q2(imgs['p_M']+v),4),round(q2(imgs['p_M']-v),4)) for k,v in imgs.items()},' sinh 2eta =',round(np.sinh(2*e),4))
