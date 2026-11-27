# Ergebnis H200 / k410 — Ist die Feldgleichung holomorph (chiral) unter der Ladung?

**Datum:** 2026-11-27
**Vorab:** `Vorab_H200_chirale_Feldgleichung.md` (committet vor der Rechnung)
**Skripte:** `k410_test_h200.py` (numpy), `k410b_kontrolle.wl` (Wolfram, unabhängig)
**Ausgaben:** `k410_out.txt`, `k410b_out.txt`

## Verdikt: **teilweise**

Globale Holomorphie der Feldgleichung ist sauber **verworfen**. Die chirale Lesart erklärt das
beobachtete **Muster** (b_down ≈ 0, Up quadratisch-dominant), aber **strikte** Chiralität
(exakt D = B) ist von den Daten bei ~9σ **ausgeschlossen**; der verbleibende ~0,9-%-Rest liegt
über dem RG-Budget aus H199. Chiralität ist also **dominant, approximativ und gradselektiv**,
kein globales Prinzip.

## Was gerechnet wurde

Drei Modelle am Quarkdatensatz (6 M_Z-Yukawas, Zuordnung B, hergeleiteter Nenner (l_i+l_j)²),
alle linear und gewichtet gefittet; numpy und Wolfram stimmen exakt überein.

| Modell | Param | χ² | dof | Bemerkung |
|---|---|---|---|---|
| (1) voll holomorph (Zähler ganz ∝ P_up) | 2 (a,b; nur Up) | **44 587** | 4 | Down-Massen vorhergesagt = 0 |
| (2) gradselektiv, strikt D = B | 3 (A, C, B) | **320,7** | 3 | b_down = 0 erzwungen; p = 0 |
| (3) voll A, B, C, D (Referenz H196) | 4 | **7,91** | 2 | D/B = +1,0085 |

### (A) Operator-Kontrolle — holomorph ⇒ Down masselos (exakt)
Auf dem Farbblock (36-dim, aus H198): der chirale Projektor P_up = ½(1 + iL_U) hat auf dem
Down-Raum Norm **0,00e+00**, auf dem Up-Raum Erwartungswert **1,000000**. Ein **jeder** aus
P_up gebaute Term — linear *oder* quadratisch — gibt für Down (s = −1) null. Ein voll
holomorpher Zähler erzwingt daher a_down = 0 **und** b_down = 0, also einen verschwindenden
Down-Massenzähler. (Dieser Arm ist **nicht blind**: analytisch fixiert, als Kontrolle gerechnet.)

### (1) Voll holomorph — K1 erfüllt: verworfen
Fit des Up-Zählers (a, b) an die drei Up-Massen trifft diese (χ²_up = 4,8), die Down-Massen
sind aber als 0 vorhergesagt und liegen **77, 76 und 181 σ** daneben (χ²_down = 4,46·10⁴).
→ Eine global holomorphe Feldgleichung macht die Down-Quarks masselos und ist **ausgeschlossen**.

### (2)/(3) Gradselektive Chiralität — K3 (nicht K2): nur approximativ
Strikt D = B (Modell 2) erzwingt b_down = 0 (Down nur linear, Up linear + quadratisch) — genau
die *gradselektive* Chiralität. Das trifft die **Form** der Hierarchie, wird aber quantitativ
**verworfen**: χ² = 320,7 bei dof = 3 (p = 0), gegenüber χ² = 7,91 des freien 4-Param-Fits
(Δχ² = 312,8). Die Daten verlangen D/B = **1,0085**, also |D/B − 1| = **0,0085** (~0,9 %), über
dem RG-Budget 0,004 (0,4 %) aus H199. Die Quintik ist damit **chiral-dominant (~99 %)** mit
einem kleinen ladungsblinden Beimischungsanteil, nicht exakt chiral.

## Einordnung

- H198 gab „Down linear" einen Namen (Chiralität der Ladung, P_up). H199 schloss einen
  Laufeffekt aus. **H200** prüft, ob Chiralität ein *Strukturprinzip der Feldgleichung* sein kann:
  - **Global** (ganze Feldgleichung holomorph): nein — Down würde masselos.
  - **Gradselektiv** (nur die Quintik chiral): trifft das Muster, aber nur näherungsweise
    (~9σ von exakt D = B entfernt; ~0,9-%-Rest über dem RG-Budget).
- Die chirale/holomorphe Struktur ist also **auf den Term höchsten Grades beschränkt und
  approximativ**. Zwei neue, geschärfte offene Punkte:
  1. **Warum gerade die Quintik?** Was zeichnet den l_k²-Term (Grad-5-F4-Invariante, H197) dafür
     aus, chiral zu koppeln, während der lineare Term ladungsblind bleibt?
  2. **Woher der ~0,9-%-ladungsblinde Beimischungsanteil** (D/B − 1), der weder aus einer exakten
     Chiralität noch aus dem RG-Lauf folgt?

Damit bleibt die Quark-Massenquelle offen; der chirale Baustein ist charakterisiert (dominant,
gradselektiv, nicht exakt), aber nicht aus einem Prinzip erzwungen.

## Werkzeuge, Bereich, Grenzen

- **Werkzeuge:** numpy (Operatorbau Farbblock/L_U/P_up wie k408; drei lineare χ²-Fits) und als
  unabhängige Kontrolle Wolfram Language (gleiche drei Fits, exakt übereinstimmend). Qiskit nicht
  einschlägig (keine Schaltung/Messung).
- **Geprüfter Bereich:** die drei Modelle am festen M_Z-Datensatz mit Zuordnung B und Nenner
  (l_i+l_j)². Die Chiralität ist operatorweise exakt belegt (P_up auf Down = 0).
- **Erste/entscheidende Abweichung:** strikt D = B liegt bei Δχ² = 312,8 über dem freien Fit;
  D/B = 1,0085.
- **Grenzen / offene Voraussetzungen:** Zuordnung B gesetzt (aus H194); Nenner aus H195; die
  Funktionsform (Zähler linear + quadratisch) stammt aus H188/H196 (nachträglich gewählt). Der
  Test sagt, dass Chiralität nicht global und nicht exakt ist — er leitet nicht her, warum sie
  gerade die Quintik trifft.
- **Wolfram-Hinweis:** `N` muss vor `Sort` stehen, sonst sortiert Wolfram die symbolischen
  Vakuum-Ausdrücke kanonisch statt numerisch (ergab fälschlich χ² = 91143, D/B = 0,841). Die
  „undefined"-Warnung von LeastSquares ist kosmetisch (Scoping), kein Rechenfehler. Kein
  symbolischer Nullrest (rein numerischer Fit).

Nächste freie Nummern nach H200/k410: H201, k411 (vor Vergabe gegen `main` prüfen; der
Parallel-Thread HS(−1) vergibt ebenfalls k-Nummern).
