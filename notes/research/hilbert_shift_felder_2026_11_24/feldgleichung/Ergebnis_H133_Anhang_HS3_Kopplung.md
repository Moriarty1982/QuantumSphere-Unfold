# Ergebnis H133: Der Turm legt die Form der Kopplung des HS(3)-Anhangs fest, den Wert nicht

**Stand:** 2026-11-25. Test nach Vorab-Notiz `notes/research/predictions/Vorab_Notiz_H133_Anhang_HS3_Kopplung.md` (Commit b7b0597, vor dem ersten Lauf).
**Teilweise nicht blind:** K-a stand nach einer Überlegung von Hand vorab fest, K-b bis auf Regel R3, K-c war offen.
Skripte: `k302_test_h133.py` (Python: numpy für Lie-Algebren und Invarianten, sympy für den Fluss, scipy für die Integration), Ausgabe `k302_out.txt`;
Gegenprobe `k302b_gegenprobe.wl` (Wolfram Language, unabhängig aufgebaut), Ausgabe `k302b_out.txt`. Qiskit nicht eingesetzt (keine Schaltung).
Kein Guard berührt. OP1 bis OP5 bleiben offen.

## Gesamturteil
**H133 nicht bestätigt. Die Form ist festgelegt, der Wert ist frei.**

| Kriterium | Vorhersage | Ergebnis |
|---|---|---|
| K-a (Form) | bestätigt | **bestätigt** (nicht blind) |
| K-b (Wert) | widerlegt | **widerlegt** |
| K-c (Tragfähigkeit) | trägt teilweise | **trägt teilweise**, knapp: Pol bei 1,4·10⁴ GeV im günstigsten Fall, sonst unter 3 TeV |

## 1. Form (K-a)
ψ = a + b·ℓ mit a, b ∈ ℍ, A = N(a), C = N(b). Setzt man die Eichwirkung aus k299 (Linksmultiplikation mit i, j, k und Rechtsmultiplikation mit i) auf 𝕆 fort,
gilt p(a + bℓ) = pa + (bp)ℓ und (a + bℓ)q = aq + (b·q̄)ℓ (geprüft). Daraus folgt:
- Die Linksmultiplikationen bilden auf 𝕆 keine SU(2) mehr: [L_i, L_j] = 2L_k gilt auf a, auf b gilt −2L_k. Ihr Abschluss hat Dimension 6.
- L_j und R_i vertauschen auf a, auf b nicht.
- Die erzeugte Lie-Algebra hat **Dimension 7**: su(2) ⊕ u(1) auf a (Rang 4) und eine eigene su(2), die nur auf b wirkt (Dimension 3).
- Invarianten: Grad 2 genau A und C, Grad 4 genau A², AC, C². **Es gibt einen einzigen gemischten Term κ·A·C.**
- Der Block b ist irreduzibel (quaternionischer Typ, Kommutant 4). Die vier neuen Felder haben deshalb **dieselbe Masse**, m² = 2κv².

Das passt zu dem Fall „vier Felder bei einer Masse“ aus k300. Zwei weitere Terme, die in einem gewöhnlichen Modell mit zwei Dubletts die Massen
aufspalten würden, sind hier verboten. Ursache ist die Nicht-Assoziativität von 𝕆.

**Andere Lesarten der Symmetrie** (zum Vergleich, Vorab-Notiz „Aufbau“):

| Lesart | Algebra | neue Felder | Kommutant | nötige Masse | nötiges κ |
|---|---|---|---|---|---|
| S-a: fortgesetzte Eichwirkung | su(2) ⊕ u(1) ⊕ su(2), 7 | 4 entartet | 4 | 382,1 GeV | 1,204 |
| S-c: su(3), Stabilisator von u = i | 8 | 6 entartet (ein farbiges Triplett) | 2 | 345,2 GeV | 0,983 |
| S-b: g₂ | 14 | 7 entartet | 1 | 332,2 GeV | 0,910 |

Fehlende Summe wie in k300: 8,522·10¹⁰ GeV⁴. In S-c gehören j und k zum Triplett, A·C ist dort nicht invariant, und x₀²·T ist in S-a nicht invariant:
Die Lesarten vertragen sich nicht.

**Nachträglich gefunden (nicht in der Vorab-Notiz):** S-a und S-c zusammen erzeugen so(8) (Dimension 28). Dann bleibt als einzige Invariante vom Grad 4 die
volle Norm N(ψ)². Verlangt man vom Potential also beides, die fortgesetzte schwache Wirkung und die Farbe, dann ist die Kopplung festgelegt, aber auf den
Wert, bei dem die neuen Felder masselos sind (Regel R1).

## 2. Wert (K-b)
- **R1 (volle Norm):** κ = 2λ_A, die neuen Felder sind Goldstone-Richtungen. Summe null. Außerhalb.
- **R2 (HC-Strafe η(C − μ²A)²):** κ = −2ημ² = −0,182·η. Negativ, und η bleibt frei. Legt nicht fest.
- **R3 (Fluss mit einer Schleife, nur Skalare):** für (4, 4): 16π²·dλ_A/dt = 8(κ² + 12λ_A²), 16π²·dκ/dt = 16κ(κ + 3λ_A + 3λ_C), 16π²·dλ_C/dt = 8(κ² + 12λ_C²).
  Feste Strahlen: κ = 0 (entkoppelt) und (κ, λ_C) = (2λ_A, λ_A), das ist wieder die volle Norm. Für (2, 6) und (1, 7) gibt es je einen weiteren
  Strahl (κ/λ_A = 0,155 bzw. 0,362). Im skalenfreien Fall ist λ_A an der Skala null, ein festes Verhältnis κ/λ_A legt dort keinen Wert fest.

Keine Regel liefert κ ≈ 1,2. Damit ist K-b widerlegt, wie vorhergesagt. Offen war nur R3, und R3 führt auf dieselben zwei Punkte wie in H129.

## 3. Tragfähigkeit (K-c)
Start bei μ = v mit λ_A = 0 und dem nötigen κ; der Pol ist der Ort, an dem eine Kopplung 4π überschreitet.

| Lesart | λ_C(v) = 0 | λ_C(v) = 0,5 | λ_C(v) = 1 |
|---|---|---|---|
| S-a (4, 4), κ = 1,204 | 1,43·10⁴ GeV | 2,86·10³ GeV | 1,01·10³ GeV |
| S-c (2, 6), κ = 0,983 | 4,53·10⁴ GeV | 2,91·10³ GeV | 8,8·10² GeV |
| S-b (1, 7), κ = 0,910 | 8,04·10⁴ GeV | 2,79·10³ GeV | 8,2·10² GeV |

Mit halbem κ läge der Pol bei 1,1·10⁶ GeV, mit doppeltem bei 1,6·10³ GeV. Nach dem Kriterium (10 TeV bis 10¹⁶ GeV) ist das „trägt teilweise“, aber nur für
λ_C(v) = 0 und nur knapp. Meine Schätzung vorab (10⁵ bis 10⁷ GeV) war zu hoch. Die Kopplung, die 125 GeV verlangen würde, ist stark: Das Bild gilt
höchstens bis etwa 14 TeV und braucht darüber etwas Neues.

## Was daraus folgt
1. Der Turm sagt etwas Prüfbares über die Form: genau ein gemischter Term, vier neue Felder mit gleicher Masse, keine Aufspaltung.
2. Den Wert der Kopplung legt keine der bisherigen Regeln fest. Wo eine Regel ihn festlegt (volle Norm, auch aus S-a und S-c zusammen), sind die neuen
   Felder masselos, und die Schleifen-Skala bleibt bei 9,8 GeV bzw. wird mit Top negativ.
3. Der Weg „skalenfrei plus Anhang von HS(3)“ erklärt die 125 GeV damit nicht. Er ist nicht ausgeschlossen, aber er bräuchte eine eingesetzte Zahl κ ≈ 1,2
   und wäre nur bis etwa 14 TeV gültig.

## Grenzen
Eine Schleife; im Fluss nur Skalare, ohne Eichfelder und Top (Top würde λ_A bremsen, die Größenordnung des Pols ändert das voraussichtlich nicht; ungeprüft).
Start bei μ = v ist eine Vereinfachung. Massen und v aus dem Gedächtnis wie in k300. Die Cayley–Dickson-Konvention steht im Skript; die Aussagen über
Dimension und Invarianten hängen nicht an ihr, das ist aber nur für diese eine Konvention gerechnet. Schranken aus Beschleuniger-Suchen sind nicht geprüft;
ein farbiges Triplett bei 345 GeV (S-c) dürfte dort Schwierigkeiten haben (aus dem Gedächtnis, nicht belegt). Welche Lesart der Turm meint, ist offen.

## Nächster möglicher Schritt
Die Rückwärtsfrage stellen: Welche Regel müsste gelten, damit κ ≈ 1,2 herauskommt, und gibt es sie im Turm? Oder die skalenfreie Annahme fallen lassen
und die Skala als Setzung führen (k295: μ² ist die einzige Skala, Vorzeichen frei).
