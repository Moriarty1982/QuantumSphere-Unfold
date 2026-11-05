"""k174 (Erkundung, M-T-Luecke von k170): Tachyon-Frame nach Konvention F als Fortsetzung der Rapiditaet eta -> eta + i pi/2 entlang
einer Achse n (hier z). Vektorebene: Lambda(i pi) = diag(-1, 1, 1, -1) (Phase (-1)^k, F3, fuer Gewicht 1 in gamma).
Spinorebene: exp(-(i pi/2) sigma_z) = -i sigma_z, unitaer; j(psi_T) = R_z(pi) j_M. Prueft
 (1) Lambda(i pi) = -R_z(pi) auf Vektoren, also j_T := -j(psi_T) (F3-Vorzeichen) = Lambda(i pi) j_M;
 (2) j_M + j_T = 2 j_perp (Anteil quer zur Achse);
 (3) fuer 16 Zustaende: K-Bedingung j_gesamt = 0 <=> Gesamtstrom von M liegt in der (t, n)-Ebene; dann ist auch die Torsion -3/16 kappa j^2 = 0."""
import numpy as np
rng=np.random.default_rng(5);I=np.eye(2);sx=np.array([[0,1],[1,0]]);sy=np.array([[0,-1j],[1j,0]]);sz=np.diag([1.,-1]);sb=[I,-sx,-sy,-sz]
cur=lambda p:np.array([(p.conj()@m@p).real for m in sb])
Lam=np.diag([-1.,1,1,-1]);Rz=np.diag([1.,-1,-1,1])
print('(1) Lambda(i pi) = -R_z(pi):',np.allclose(Lam,-Rz))
p=rng.normal(size=2)+1j*rng.normal(size=2);pT=-1j*sz@p
print('    j(psi_T) = R_z(pi) j_M:',np.allclose(cur(pT),Rz@cur(p)))
jM=cur(p);jT=-cur(pT);print('(2) j_M + j_T = 2 j_perp:',np.allclose(jM+jT,2*np.array([0,jM[1],jM[2],0])))
# (3) 16 Zustaende mit Strom in der (t,z)-Ebene: Zustaende als Eigenvektoren von sigma_z (Spin entlang z) mit beliebigen Betraegen
ps=[(a*np.array([1,0])+0j) if k%2 else (a*np.array([0,1])+0j) for k,a in enumerate(rng.uniform(0.3,1.5,16))]
J=sum(cur(q) for q in ps);JT=sum(-cur(-1j*sz@q) for q in ps)
print('(3) 16 Zustaende, Spin entlang z: J_M =',np.round(J,3),' J_M + J_T =',np.round(J+JT,12),' j^2 gesamt =',round(float((J+JT)@np.diag([1,-1,-1,-1])@(J+JT)),12))
ps2=[rng.normal(size=2)+1j*rng.normal(size=2) for _ in range(16)];J2=sum(cur(q) for q in ps2);JT2=sum(-cur(-1j*sz@q) for q in ps2)
print('    allgemein: |J_M + J_T| =',round(float(np.linalg.norm(J2+JT2)),4),' = 2|J_perp| =',round(float(2*np.linalg.norm(J2[1:3])),4))
