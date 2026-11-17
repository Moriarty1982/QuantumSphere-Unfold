"""Eine Zahl, mehrere Gestalten: gamma_L numerisch in jeder Form.  (Erkundung, Zusammenstellung, nicht blind.)"""
import numpy as np
from scipy.optimize import brentq
n = np.arange(1, 400001); j = n / 2; a = np.sqrt(j * (j + 1))
gM = brentq(lambda g: np.sum(2 * np.exp(-2 * np.pi * g * a)) - 1, 0.01, 2)
gT = np.log(2) / (np.pi * np.sqrt(3))
r = 2.0 ** (-np.sqrt(n * (n + 2) / 3))
D = brentq(lambda D: np.sum(2 * r ** D) - 1, 0.5, 5)
gL = gM / gT
beta = np.sqrt((gL - 1) / (gL + 1)); eta = np.arctanh(beta)
bM = (1 - beta ** 2) / (1 + beta ** 2)
TH = 1.0
wT = np.log(2) * TH; wM = 8 * np.pi * gM * np.sqrt(3) / 2 * TH / 4
E_boost = np.cosh(2 * eta) * wT
print(f"(1) Zaehlung      gamma_M/gamma_T            = {gL:.9f}")
print(f"(2) Moran         Hausdorff-Dimension D_M    = {D:.9f}")
print(f"(3) Frequenz      omega_M/omega_T            = {wM/wT:.9f}  (omega_T = ln2 T_H, omega_M = Quant_M T_H/4)")
print(f"(4) Lorentz       cosh 2 eta, beta = tanh eta = {np.cosh(2*eta):.9f}  (beta = {beta:.6f})")
print(f"(5) Register      1/b_M                      = {1/bM:.9f}")
print(f"(6) Boost         gamma_L * omega_T = E(T-Bit vom Gegenbeobachter) = {E_boost:.6f} T_H = omega_M {wM:.6f} T_H")
w = 2; S2 = np.sum(r ** 2)
print(f"Prinzip (Moran, nachtraeglich): groesste ganze Kopienzahl je Skala in der Ebene = floor(1/sum r^2) = floor({1/S2:.4f}) = {int(1/S2)} -> D = {D:.4f}")
