"""k178 (Erkundung, Frame-Pruefung vor H71): die drei Involutionen auf dem Dublett-Zustand rho = 1/2(1 + b_x sx + b_z sz) (Zustandsscheibe r04/r17).
R = sigma_y (Tachyon-Abbildung z -> iz, r28), T = sigma_z (Zeitumkehr z -> zbar, Porttausch), J_B = sigma_x. Kompensator C = 1/2(1 + sigma_x),
Portgewichte = <C>, <1-C> = 1/2(1 +- b_x). Prueft fuer Zustaende auf der Kompensatorachse (b_z = 0) und abseits: Bild von b, Portgewichte."""
import numpy as np
sx=np.array([[0,1],[1,0]]);sy=np.array([[0,-1j],[1j,0]]);sz=np.diag([1.,-1]);I=np.eye(2);C=(I+sx)/2
rho=lambda b:(I+b[0]*sx+b[1]*sz)/2
bloch=lambda r:np.round([np.trace(r@sx).real,np.trace(r@sz).real],6)
ports=lambda r:np.round([np.trace(r@C).real,np.trace(r@(I-C)).real],6)
x=0.5493**2;bM=(1-x)/(1+x)
for name,b in (('M auf Achse',(bM,0.0)),('abseits',(0.4,0.3))):
    r=rho(b);print(f'{name}: b={b}, Ports={ports(r)}')
    for n,U in (('R=sy (Tachyon)',sy),('T=sz (Zeitumkehr)',sz),('J_B=sx',sx)):
        r2=U@r@U.conj().T;print(f'   {n:18s} b -> {bloch(r2)}  Ports -> {ports(r2)}')
