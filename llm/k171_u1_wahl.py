"""k171 (Erkundung, Wirkung W1): Welches U(1) ist auf dem Bild von C_ch = 1/2(1 + i L_e7) nichttrivial und anomaliefrei?
Raum C x H x O = C^32 (H: Lorentz links (Weyl-Index), schwach rechts). Prueft: i L_e7 auf Bild C_ch konstant;
Eigenwerte von i R_e7 und von Q, B-L dort; Anomaliesummen Tr q, Tr q^3 ueber das Bild (16 linkshaendige Weyl-Felder
= Bild / Weyl-Index 2)."""
import numpy as np, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from k69_test_h17 import omul
E=np.eye(8);L8=[np.array([omul(E[a],E[j]) for j in range(8)]).T for a in range(8)];R8=[np.array([omul(E[j],E[a]) for j in range(8)]).T for a in range(8)]
iL=1j*L8[7];iR=1j*R8[7]
print('(iL)^2=1:',np.allclose(iL@iL,np.eye(8)),' [iL,iR]=0:',np.allclose(iL@iR,iR@iL))
C=0.5*(np.eye(8)+iL)
w,V=np.linalg.eigh(C);B=V[:,w>0.5]                     # Bild von C_ch auf O_C, Dimension 4
print('dim Bild C_ch auf O:',B.shape[1])
ev=lambda M:np.round(np.linalg.eigvalsh(B.conj().T@M@B),10)
print('i L_e7 auf Bild:',ev(iL));print('i R_e7 auf Bild:',ev(iR))
Q=0.5*np.eye(8)-(1/6)*iL-(1/3)*iR;BL=2*(Q-0.5*np.eye(8))
print('Q auf Bild:',ev(Q),' B-L auf Bild:',ev(BL))
# Weyl-Felder: Bild auf O (4) x schwach (2) x Farbe steckt in O; Weyl-Index nicht gezaehlt -> 8 Felder je ... :
# Auf C x H x O: H = Weyl(2) x schwach(2). Felder = Bild(4 auf O, komplex) x schwach 2 = 8 komplexe 2-Spinoren.
for name,M in (('iL_e7',iL),('iR_e7',iR),('B-L',BL)):
    q=ev(M);tr1=2*q.sum();tr3=2*(q**3).sum()     # Faktor 2: schwaches Dublett
    print(f'{name}: Tr q = {tr1:+.4f}, Tr q^3 = {tr3:+.4f}')
# --- richtig nach r42: ganzer Raum C x H x O (32 = 16 Weyl-Zustaende x 2 Lorentz-Komponenten); C_ch trennt Dubletts (Bild) von Singuletts (Kern)
print('--- ganzer Raum (r42): Felder = O_C (8) x schwach-Index (2) = 16 Weyl-Zustaende')
evf=lambda M:np.round(np.linalg.eigvalsh(M),10)
for name,M in (('J=iL_e7',iL),('iR_e7',iR),('B-L',BL)):
    q=evf(M);print(f'{name}: Ladungen {sorted(set(q))}, Tr q = {2*q.sum():+.4f}, Tr q^3 = {2*(q**3).sum():+.4f}')
