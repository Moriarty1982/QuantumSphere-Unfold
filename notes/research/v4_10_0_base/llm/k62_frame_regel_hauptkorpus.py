"""k62: Konvention F (v4.9.0-r22) auf den Hauptkorpus (Zeilen 1-52111) angewandt.

Erfasst werden alle theorem/proposition/corollary/lemma/conjecture/definition-Umgebungen, die \\bsym, \\gL, \\zminus,
\\gBI, \\gstring oder die Woerter photon frame / matter frame / tachyon enthalten.
Kategorien:
  F  frame-frei (Materie = Tachyon nach F; haengt nur von |b|, |gamma|, k = 0 oder reiner Arithmetik ab)
  M  nur Materie-Frame (haengt vom vorzeichen- oder portempfindlichen beta ab; im Tachyon-Frame x -> 1/x anders)
  C  Umrechnung mit Gewicht k: Materie-Wert; Tachyon Betrag nach Klasse (r19), Phase (-1)^k (F3)
  S  Aussage am Photon-Frame des Hauptkorpus (beta = 0, sigma = 0); unter F ist das der reine Zustand |b| = 1, nicht P
  P  Grenzwert beta -> 1; unter F der Photon-Fixpunkt b = 0, entartet (F2)
  D  definiert Sektoren oder Frames selbst
  N  traegt "photon-frame" nur als Namen, ohne Frame-Groesse; formal frame-frei
Mit dem Hauptkorpus-eigenen Tachyon (beta -> -beta, thm:symmetric-frame) waeren gerade Funktionen von beta frame-frei;
die Spalte "alt" vermerkt das.
"""
import io
import re
import collections

B = chr(92)
SRC = "Quantum_Sphaera_Companion_v4_8_0_source.tex"

# Etikett -> (Kategorie, alt-T frame-frei?, Notiz)
CLS = {
    "thm:unity": ("D", "", "collapse state z_- = 0"),
    "thm:origin": ("F", "", "|z_-|_min = l_P, Betrag"),
    "prop:compensator": ("D", "", "Kompensator zwischen den Sektoren"),
    "prop:shared-vacuum-planck": ("F", "", "beiden Sektoren gemeinsam"),
    "thm:wick": ("D", "", "Wick-Rotation = Tachyonsektor"),
    "thm:triolic-gBI": ("F", "", "k = 0"),
    "thm:frame-offset": ("C", "", "gamma_obs = gamma_0 gamma; gamma_L strukturell"),
    "thm:symmetric-frame": ("D", "", "setzt Tachyon bei -beta (alte Lesart), F bei 1/beta"),
    "prop:horizon-cascade-singularity": ("P", "", "beta -> 1 = Photon-Fixpunkt unter F"),
    "thm:hawking-triolic": ("M", "ja", "Paar bei +-beta (alte Lesart)"),
    "prop:hawking-gBI-tachyon": ("C", "", "k(T_H) = -1: Tachyon-Phase -1"),
    "thm:dual-origin": ("M", "", "gamma_L ~ 1/beta; im Tachyon 1/beta_T = beta"),
    "thm:core": ("D", "", "Kern z_- -> unendlich"),
    "thm:artqft": ("M", "ja", "g_tt = -beta^2"),
    "thm:bsym-hopf": ("M", "", "beta = sin(theta_H/2); 1/beta > 1 undefiniert"),
    "thm:koide-triolic": ("M", "", "arcsin(beta)"),
    "thm:expansion": ("M", "ja", "tau^2 = t^2 - beta^2"),
    "thm:dark-offset": ("M", "ja", "Lambda_eff ~ beta^2"),
    "thm:spring": ("M", "ja", "Kraefte +-k beta symmetrisch nur bei -beta"),
    "thm:light-equil": ("M", "ja", "beta^2-Term"),
    "thm:dark-energy": ("M", "ja", "Omega_M = beta^2"),
    "cor:gue-frame": ("C", "", "k = 1; (i) Abstandsverhaeltnis frame-frei"),
    "thm:toe": ("D", "", "Axiom"),
    "def:lagrangian": ("M", "ja", "L_frame = beta^2 <f,f>"),
    "prop:lambda-from-frame": ("S", "ja", "Lambda = 0 bei beta = 0; unter F bei P Rahmenterm 1"),
    "thm:gue-selfdet": ("F", "", "gamma_L als Betrag"),
    "cor:odlyzko": ("C", "", "k = 1; durch r08 nicht bestaetigt"),
    "thm:k-values": ("F", "", "die k selbst"),
    "thm:planck-photon": ("C", "", "k = 3/2: Phase -+i, Quadrat -1 (r82)"),
    "thm:dirac-probe": ("M", "", "Phase e^{i pi beta}"),
    "prop:three-compatible-readings": ("M", "", "ueber thm:dirac-probe"),
    "cor:SM-spectral-realization": ("D", "", "Spektralzerlegung"),
    "thm:hc-readout-geometry": ("D", "", "allgemeines beta"),
    "prop:z3z-orbits": ("M", "", "Hopf-Winkel"),
    "prop:cl-shift": ("M", "", "beta = beta_Hopf delta_CL"),
    "def:dirac-op-Hplusminus": ("M", "", "(T4) mit beta"),
    "prop:op2-targets": ("M", "", "OP2 mit beta"),
    "thm:op2-T4-equals-op1": ("M", "", "beta als Spektralverhaeltnis"),
    "thm:tribonacci": ("F", "", "Fixpunkt in |gamma|"),
    "cor:tribonacci-cosmo": ("M", "", "Omega_M = 1/T^2"),
    "thm:self-consistent-gL": ("M", "", "SC2 beta = sqrt((mu-1)/(mu+1))"),
    "cor:op1-resolved": ("M", "", "beta-Ausgabe"),
    "prop:exponent-5": ("M", "", "beta im Exponenten"),
    "thm:hc-quasiconformal": ("M", "ja", "mu = beta^2; Tachyon |mu| > 1, K = -gamma: orientierungsumkehrend"),
    "thm:tribonacci-beltrami": ("M", "ja", "mu = beta^2 = 1/K"),
    "prop:inflow-cascade": ("M", "ja", "Anteil beta^2"),
    "prop:k-neutrino": ("C", "", "k = 4: Phase +1"),
    "prop:H0-tension": ("M", "", "beta(t)"),
    "prop:muon-g2": ("C", "", "k = -1, -2"),
    "prop:saturation": ("P", "", "beta -> 1 = Photon-Fixpunkt unter F"),
    "thm:op1op4-unified": ("M", "", "delta_CL, beta"),
    "prop:uv-photon": ("C", "", "k = 5 (r03): Phase -1"),
    "cor:matter-error": ("C", "", "k = 5"),
    "prop:bare-lambda": ("C", "", "k = -2"),
    "thm:lambda-zero": ("S", "ja", "Lambda = 0 bei beta = 0"),
    "def:tr-balance": ("S", "ja", "rechte Seite beta^2 l_P^2"),
    "prop:open-steps": ("S", "", "Photon-Frame-Schritte"),
    "thm:partial-cancel": ("F", "", "Guinand-Weil, reine Arithmetik"),
    "cor:falsifiable": ("M", "", "gemischt: P1, P6 C; P2-P4 M; P5 F"),
    "prop:theta-remainder-trivial": ("S", "", "Schritt A im Photon-Frame"),
    "prop:theta-required-B": ("S", "ja", "beta^2-Term"),
    "def:theta-sum-B": ("S", "", "gamma_n/gamma_L"),
    "conj:theta-sum-B": ("S", "ja", "durch r05 widerlegt"),
    "def:delta-theta-r-residual": ("S", "ja", "beta^2-Term"),
    "def:working-op1-rounded-gap": ("N", "", ""),
    "cor:working-op1-narrowed-live-burden": ("N", "", ""),
    "thm:working-op1-admissible-readout-uniqueness": ("N", "", ""),
    "cor:toe_triolic_realization": ("D", "", ""),
    "thm:master-structural": ("D", "", ""),
    "thm:three-readout-principle": ("D", "", ""),
    "def:psi-cl": ("N", "", ""),
    "cor:op1-r03-target": ("N", "", ""),
    "def:routed-balance-witness-live-op5b-kernel": ("N", "", ""),
    "prop:live-op5b-kernel-carrier-upgraded-witness-problem": ("N", "", ""),
}
# unbeschriftete Eintraege nach Zeile
BYLINE = {6101: ("D", "", "Sektoren nach Re(z_-); Materie beta < 0, gegen thm:symmetric-frame (+beta)"),
          6485: ("P", "", "Horizont bei beta -> 1"),
          7673: ("C", "", "Definition von k"),
          7742: ("M", "ja", "Lambda_obs ~ beta^2, Vakuum gamma^6"),
          7760: ("C", "", "alpha-Drift, k = 1: Phase -1"),
          18244: ("D", "", "Tachyon-Zweig"),
          26200: ("N", "", "")}

def scan():
    t = io.open(SRC, encoding="utf-8").read().split("\n")[:52111]
    txt = "\n".join(t)
    pat = re.compile(B + B + r"begin\{(theorem|proposition|corollary|lemma|conjecture|definition)\}(\[[^\]]*\])?(.*?)"
                     + B + B + r"end\{\1\}", re.S)
    mac = [B + "bsym", B + "gL", B + "zminus", B + "gBI", B + "gstring"]
    W = re.compile(r"photon[- ]frame|matter[- ]frame|tachyon[- ]frame|\btachyon", re.I)
    out = []
    for m in pat.finditer(txt):
        body = m.group(3)
        if not (any(x in body for x in mac) or W.search(body)):
            continue
        lab = re.search(B + B + r"label\{([^}]*)\}", body)
        out.append((txt.count("\n", 0, m.start()) + 1, lab.group(1) if lab else None, (m.group(2) or "").strip("[]")))
    return out

items = scan()
rows, missing = [], []
for line, lab, title in items:
    if lab and lab in CLS:
        c = CLS[lab]
    elif line in BYLINE:
        c = BYLINE[line]
    elif lab is None and 43381 <= line <= 46716:
        c = ("N", "", "OP5-HC-Grammatik")
    else:
        missing.append((line, lab, title)); continue
    rows.append((line, lab, title, *c))
print("erfasst %d, klassifiziert %d, offen %d" % (len(items), len(rows), len(missing)))
for m in missing:
    print("   OFFEN", m)
cnt = collections.Counter(r[3] for r in rows)
print("Kategorien:", dict(sorted(cnt.items())))
alt = [r for r in rows if r[4] == "ja"]
print("unter dem alten Tachyon (-beta) frame-frei, unter F nicht: %d" % len(alt))
for cat in "FMCSPDN":
    labs = [r[1] for r in rows if r[3] == cat and r[1]]
    print("%s (%d): %s" % (cat, sum(1 for r in rows if r[3] == cat), ", ".join(labs)))
    for r in rows:
        if r[3] == cat and r[5]:
            print("      %-44s %s" % (r[1] or "Zeile %d" % r[0], r[5]))
