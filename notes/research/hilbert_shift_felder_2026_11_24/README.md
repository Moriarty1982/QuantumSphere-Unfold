# Eine Erzeugungsregel für den Hilbert-Shift-Turm (Erkundung k253, nicht blind, 24.11.2026)

**Ergebnis in einem Satz:** Eine einzige Regel erzeugt HS(0) bis HS(3) als Feldkonfigurationen: Der Feldwert ψ lebt in der
Cayley–Dickson-Algebra A_n (Dimension 2ⁿ = Trägergröße C_n des Atlas), und jeder Shift fügt eine neue imaginäre Einheit hinzu, um die das
Feld kreisen kann (ψ̇ = u·ω·ψ). Die Stufen liefern der Reihe nach: Linie ohne Fläche (HS(0)), Ellipse mit Fläche und Drehsinn (HS(1), U(1)),
erste Holonomie auf der Hopf-Sphäre (HS(2), SU(2)), Farbgruppe SU(3) als Stabilisator (HS(3)). Ab HS(4) bringt die Verdopplung **keine neue
Symmetrie** mehr (Der bleibt 14-dimensional) und die Kreisbahn schließt sich nicht mehr; der Turm muss dort auf Produkte der drei
Divisionsstufen umschalten, und HS(6) = C⊗H⊗O = 2^(1+2+3) ist genau das Produkt von HS(1), HS(2), HS(3). Das stützt die Vermutung des
Autors, dass spätere Shifts einfacher werden und in bekannte Physik münden, allerdings im algebraischen Sinn (Hurwitz), nicht dynamisch.

Auftrag des Autors (24.11.2026): eine Feldkonfiguration (oder Familie) für den ersten Hilbert-Shift, dann eine für den zweiten und alle
folgenden; Vermutung: die späteren werden einfacher, weil sie in bekannte Physik konvergieren. Ergänzung: HS(0) als Grundlage mitbestimmen.
**Erkundung, nicht blind:** Die Algebra-Fakten (Hurwitz, Der(O) = g₂, Stabilisator su(3), Berry-Phase −Ω/2) sind Standard; neu ist nur die
Zuordnung zum Turm. Keine H-Nummer, keine Runde. Vergeben: Skripte **k253** (k253, k253b, k253c).

Werkzeuge: Python (numpy) für die Strukturrechnung bis Dimension 32 (k253, k253c); Wolfram Language exakt für HS(0)–HS(2) und als
unabhängige Kontrolle von dim Der bis n = 4 (k253b). Qiskit nicht eingesetzt: Es gibt keine Schaltung und keinen Messablauf; die
Bargmann-Kontrolle liegt aus H123/k244 vor. Kein HDL/MMA-Vergleich (kein RUN_TAPE, kein endlicher Auswahlablauf).

## Vorwissen geprüft
- Atlas `v470/32_atlas_and_op_promotion.tex` Z. 2386–2430 (Zwei-Uhren-Grammatik C_n = 2ⁿ, Lesarten HS(0)–HS(6)); QAM
  `v470/07_qam_infrastructure.tex` Z. 975–1050 (first boundary shift 0 → 1, ass:v3360-r16-hc-activation-first-boundary: HC als Normalisierer, gesetzt).
- `licht_vermittler_zeit_2026_11_24/` (Gedankenexperiment, Kirchhoff-Ellipse, Julia-3-Zyklus k249, Gegenwirbel nach Kelvin), k246
  (Holonomie braucht ≥ 3 Dimensionen), k245 (Hopf-Lücke), k250 (a − b wählt den Drehsinn nicht).
- H8 (Cayley–Dickson-Involution als CP, in Spannung), `op3_dixon_times_sedenions_2026_11_16/` (S bricht Alternativität und
  Normmultiplikativität, Nullteiler; C⊗H⊗O⊗S ist HS(10)), r13 (C⊗S, S₃ ist dort Phase, kein Generationsschritt), r27.2 (Leckregister statt freier Sedenionen).
- Neu gegenüber dem Bestand: die einheitliche Regel ψ̇ = uωψ über alle Stufen, die Rechnung dim Der / Stabilisator / L_u² = −1 je Stufe
  und die Lesart HS(6) = HS(1)⊗HS(2)⊗HS(3).

## Die Regel
Feldwert ψ(t) ∈ A_n, Verdopplung A_{n+1} = A_n ⊕ A_n·ℓ mit neuer Einheit ℓ² = −1. Bewegung ψ̈ = −ω²ψ, Grundbahn ψ(t) = exp(uωt)·ψ₀ mit u einer
Einheits-Imaginären. Je Stufe wählt das Feld ein u; was u festhält, ist die verbleibende Symmetrie (Stabilisator).

| Stufe | Algebra | Bahn / Konfiguration | Wahl von u | Symmetrie (Der, Stabilisator) | Atlas-Lesart |
|---|---|---|---|---|---|
| HS(0) | R | Hin und her auf einer Linie, ψ = 2a cos ωt, Fläche 0 | keine (nur ±, S⁰ der Werte) | 0 | radialer Kern, Kollaps-Auslese |
| HS(1) | C | Ellipse ψ = a e^{iωt} + b e^{−iωt}, Fläche π(a² − b²) | u = ±i (S⁰ = Drehsinn) | U(1); Der 0 | HC-Kragen, Periapsis-Aufspaltung |
| HS(2) | H = C² | Hopf-Kreise auf S³, Zustand auf S² | u ∈ S² (Achse und Sinn = Helizität) | Der su(2) (3), Stab u(1) | stabilisierter Orbit |
| HS(3) | O | Kreise auf S⁷ | u ∈ S⁶ = G₂/SU(3) | Der g₂ (14), Stab su(3) (8) | Fano/Oktonion-Faser |
| HS(4) | S | Bahn schließt nicht mehr (L_u² ≠ −1) | nicht mehr gleichwertig | Der g₂ (14), Stab su(3) (8): nichts Neues | Meta-Septum-Lecktest |

## Ergebnisse
1. **HS(0) (Grundlage).** Ein reelles Feld schwingt auf einer Linie. Eingebettet in HS(1) ist es genau der Fall a = b: zwei gleich starke,
   entgegengesetzte Kreisanteile (der Kelvin-Gegenwirbel ±Γ), Bahn {2a cos ωt, 0}, Fläche 0 (k253b). Die Zeitumkehr vertauscht a und b (k253b),
   also ist HS(0) **genau die zeitumkehrinvariante Teilfamilie**. „Keine Zeit“ ist hier wörtlich: Es gibt keine Größe, die eine Zeitrichtung
   auszeichnet. Stabil, weil die Bahn beschränkt ist.
2. **HS(1) (erster Shift), Familie.** Alle Ellipsen mit a ≠ b. Fläche A = π(a² − b²) und Ladung L = ω(a² − b²) (k253b) sind dieselbe Größe:
   die U(1)-Ladung. Die Aufspaltung in die zwei Kreisanteile (positive und negative Frequenz) ist die sym/antisym-Trennung des HC; die
   Halbachsen a + b und a − b sind Periapsis und Apoapsis. Ein ungerader (tangentialer) Stoß verschiebt a gegen b und erzeugt HS(1); ein
   radialer (gerader) Stoß lässt a = b. Das bestätigt die Lesart vom 24.11. (Abschnitt 1.4). **Der Drehsinn bleibt gesetzt:** u = +i und u = −i
   sind beide Lösungen, die Wahl ist der zweielementige Raum S⁰ (wie k246, k250).
3. **HS(2) (zweiter Shift).** Zwei komplexe Kanäle (H = C²); Zustände bis auf Phase liegen auf der Hopf-Sphäre S². Ein geschlossener Weg auf S²
   gibt die Berry-Phase γ = −Ω/2 (exakt, k253b): die **erste Holonomie**, also die erste bleibende Restdrehung. HS(1) hat keine (Zustandsraum
   CP⁰ = Punkt). Das passt zu „Urknall bei HS(2)“ und zu k246 (≥ 3 Dimensionen: die Stokes-Richtungen S₁, S₂, S₃). Bekannte Physik: Spin ½,
   SU(2), Pancharatnam-Phase der Lichtpolarisation, Dirac-Monopol der Ladung ½. Lineare Polarisationen (HS(0)) liegen am Äquator, die
   reinen Kreisanteile (HS(1)) an den Polen. Links- und Rechtsmultiplikation sind zwei verschiedene SU(2): Chiralität tritt hier zuerst auf.
4. **HS(3).** Der(O) = g₂ (14 Dimensionen), Stabilisator einer Einheit su(3) (8), Lie-Algebra der Linksmultiplikationen so(8) (28, Trialität)
   (k253). Die Wahl u ∈ S⁶ bricht G₂ auf SU(3): Farbe.
5. **Ab HS(4) keine neue Symmetrie (Konvergenz).** dim Der(A_n) = 0, 0, 3, 14, 14, 14 für n = 0 … 5, Stabilisator 0, 1, 8, 8, 8 (Python bis
   n = 5, Wolfram bis n = 4 unabhängig gleich). Die Regel ψ̇ = uωψ gibt nur bis O für jedes u eine geschlossene Kreisbahn: max|L_u² + 1| ≈ 10⁻¹⁶
   für n ≤ 3, aber 0,85 (n = 4) und 0,74 (n = 5) (k253c); dazu Nullteiler (e₁ + e₁₀)(e₄ − e₁₅) = 0 und |xy| ≠ |x||y| (k253). Das ist der
   Lecktest des Atlas als Rechnung: Die reine Verdopplung erschöpft sich bei O (Hurwitz).
6. **Fortsetzung durch Produkte.** Danach baut der Turm aus den drei Divisionsstufen: 2⁴ = C⊗O (Furey: eine Generation), 2⁵ = H⊗O
   (= zwei Kopien von C⊗O, die Vorder/Rück-Verdopplung des Atlas), **2⁶ = C⊗H⊗O = HS(1)⊗HS(2)⊗HS(3)** (Dixon). Die Faktoren der
   Standardmodell-Eichgruppe entstehen je einmal auf einer Divisionsstufe: U(1) bei HS(1), SU(2) bei HS(2), SU(3) bei HS(3).

## Grenzen
- Nicht blind: Die Algebra ist Standard (Hurwitz, Günaydin–Gürsey, Dixon, Furey). Neu ist nur die Zuordnung zum Turm, und die ist eine Lesart.
- **Gesetzt bleiben** der Drehsinn (u = ±i), die Achse bei HS(2), die Richtung bei HS(3) und die Zuordnung „Kanal = reelle Trägerdimension“.
  Die Regel sagt, *welche* Wahl je Stufe ansteht, nicht *wie* sie fällt.
- Die Eichgruppen erscheinen als Symmetrien des Feldwerts, nicht als Eichfelder; Hyperladung, Ladungszuordnung und Kopplungen sind nicht
  hergeleitet. Die Produktstufen 2⁴, 2⁵ sind nicht eindeutig (2⁴ = C⊗O oder H⊗H); die Wahl C⊗O folgt der Dixon-Kette, nicht einer Rechnung.
- „Einfacher“ heißt hier: keine neue Symmetrie und keine neue Wahl ab HS(4). Ob die Dynamik späterer Stufen einfacher wird, ist nicht gezeigt.
- Kirchhoff-Ellipse: Die HS(1)-Familie hat dieselbe Gestalt (starr rotierende Ellipse, zwei Brennpunkte), ist aber ein Oszillator, kein
  Wirbelfleck. Der Wirbelbezug ist Bild, nicht Rechnung. Die frühere Lesart „Rankine-Kreis ≈ HS(0)“ passt hier nicht: HS(0) ist die flache
  Ellipse (a = b), der Kreis ist der reine Grenzfall b = 0 von HS(1).
- OP1, OP3, OP5, Q1a offen; kein Guard berührt.

## Mögliche nächste Schritte
- **Blinder Test (H-Nummer nötig):** Sagt die Regel eine Zahl voraus, die nicht schon in der Algebra steht? Kandidat: die Pancharatnam-Phase
  eines bestimmten HS(2)-Zyklus gegen die Bargmann-Invariante des Oktant-Tripels (1/4 + i/4, H123).
- Den Übergang HS(0) → HS(1) dynamisch machen: Schwelle des ungeraden Stoßes am Drei-Mulden-Modell (k248) mit a − b als Ordnungsparameter.
- Atlas-Lesarten HS(4)/HS(5) gegen C⊗O und H⊗O prüfen (Meta-Septum-Projektor P̂_{C₇} ⊂ M₁₆).

## Dateien
`k253_cayley_dickson_turm.py` (`k253_out.txt`), `k253b_hs0_hs1_hs2.wl` (`k253b_out.txt`), `k253c_linksdrehung.py` (`k253c_out.txt`). Aufruf aus diesem Ordner (k253c liest k253 relativ ein).
