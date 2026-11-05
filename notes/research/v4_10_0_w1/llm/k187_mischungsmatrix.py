"""k187 (Erkundung, Autor: 'alles durchspielen und die Mischungen in einer Matrix festhalten'): Alle Sigma-Mischungen (Teilmengen, jede einmal)
der vier Konnektoren aus k185 (c0 Uebergang gegen, c1a mit/Summe, c1b mit/Differenz, c2 Paar gegen). Klassifikation von q^2/m^2 ueber eta:
konstant, proportional zu sinh 2eta, oder keines. Dazu die Maskennummer unter allen Bit-Zuordnungen (Permutationen der Bits 0..3)."""
import numpy as np, itertools, json
def vecs(eta):
    c,s=np.cosh(eta),np.sinh(eta);pM=np.array([c,s]);pTp=np.array([s,c]);pTm=np.array([s,-c])
    return [pM-pTm,pM+pTp,pM-pTp,pM+pTm]
names=['c0','c1a','c1b','c2'];etas=np.array([0.1,0.3,np.arctanh(0.5493),1.0,1.5,2.0])
q2=lambda q:q[0]**2-q[1]**2;rows=[]
for r in range(1,5):
    for S in itertools.combinations(range(4),r):
        v=np.array([q2(sum(vecs(e)[i] for i in S)) for e in etas]);sh=np.sinh(2*etas)
        if np.ptp(v)<1e-9: cls=f'konstant {v[0]:+.4f} m^2'
        elif np.ptp(v/sh)<1e-9: cls=f'{(v/sh)[0]:+.4f} m^2 sinh 2eta'
        else: cls='eta-abhaengig ('+', '.join(f'{x:+.2f}' for x in v[[0,2,5]])+' bei eta=0.1, eta_sym, 2)'
        rows.append(dict(teilmenge='+'.join(names[i] for i in S),klasse=cls,S=S))
perms=list(itertools.permutations(range(4)))
def maske(S,p): return sum(2**p[i] for i in S)
print(f"{'Mischung':18s} {'Klasse':55s} Maskennummern unter den 24 Bit-Zuordnungen")
for r in rows:
    ms=sorted(set(maske(r['S'],p) for p in perms));print(f"{r['teilmenge']:18s} {r['klasse']:55s} {ms}")
nat=(0,1,1,2)  # nicht benutzt
json.dump([{k:v for k,v in r.items() if k!='S'} for r in rows],open('k187_out.json','w'),indent=1)
print('\nZuordnung nach Masse (c0=Bit0, c1a=Bit1, c1b=Bit2, c2=Bit3):')
p=(0,1,2,3)
for r in rows: print(f"  Maske {maske(r['S'],p):2d} = {r['teilmenge']:18s} {r['klasse']}")
