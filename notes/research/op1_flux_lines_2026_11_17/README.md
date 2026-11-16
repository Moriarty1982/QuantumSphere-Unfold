# OP1, (S1′): Querungen oder Flusslinien? (Erkundung, nicht blind)

17. November 2026. Auftrag des Autors: „weiter“ nach dem Release v5.2.0; nächster Schritt laut Übergabe: prüfen, ob die Punktierungs-Stränge masselos
sind und normal queren (S1′). Zuerst die offene Literaturfrage aus `../op1_s1_check_2026_11_16/` (Nachtrag, Punkt 4), dann eine kurze Rechnung am
Bestand. Skript `flux_lines.py`, Ausgabe `run/flux_lines_stdout.txt`. Nicht blind: Alles Gerechnete folgt analytisch aus der Definition von χ.
Keine H-Nummer.

## Vorwissen geprüft
- `../op1_s1_check_2026_11_16/`: (S1′) gibt U1 und U2 zusammen (DL-Zählung), lässt aber (A) fallen; Spannung 4: masselose Stränge sind Nullfelder
  (Sektor P), M ist ein nicht-null Dublett. Literatur: ABK (Achse = Normale), Mitra (U2 aus U1), Ghosh–Noui–Perez (Statistik offen).
- `../op1_u1_check_2026_11_16/`: Dualität dreht χ um die Helizitätsachse um −2a; Pole = Ports.
- `../op1_entropy_count_2026_11_17/`: P (maximal gemischt) zählt 2j + 1, die Regel von M = reine Stränge mit unbekanntem Port.
- Bestand: r16.3(a)–(c) (χ = (√s₊, √s₋), Nullfelder ohne Punkt, für reelle Felder √s₋ = conj √s₊), r16.8 (zeitharmonische Felder, s(t)).
- Übergabe 16.11.: „Verbleibender Ausweg: verschiedene Objekte (Flusslinien gegen Querungen)“.

## Literatur
Gelesen: Eder–Sahlmann, „Quantum theory of charged isolated horizons“, [arXiv:1801.00747](https://arxiv.org/abs/1801.00747) (Abschnitte II.B,
III.A, III.C, IV.B–D); Vaid, „Quantum Hall Effect and Black Hole Entropy in Loop Quantum Gravity“, [arXiv:1208.3335](https://arxiv.org/abs/1208.3335).

1. **Am isolierten Horizont quert keine Strahlung.** Die Randbedingung T(l, l) = 0 entlang der Nullnormalen gibt φ₀ = o^A o^B φ_AB = 0 (Eder–Sahlmann,
   Gl. II.19–II.20). Übrig bleiben φ₁ und φ₂; auf dem Horizontschnitt sind E_n = −2 Re φ₁ und B_n = −2 Im φ₁ die einzigen Normalkomponenten.
2. **Maxwell-Punktierungen sind Flusslinien.** Quantisiert bilden Eichfelder dieselben eindimensionalen Anregungen wie die Gravitation; sie
   durchstoßen den Horizont und tragen ganzzahlige elektrische (und, für U(1), magnetische) Ladung je Punktierung. Bei Kugelsymmetrie ist die
   Ladung je Punktierung direkt an die Fläche gekoppelt, Q(p) ∝ √(j(j+1)), und die Vorzeichen aller Punktierungen stimmen mit Q_H überein.
3. **Keine Helizitätslesart.** Weder hier noch bei Vaid (U(1)-Chern–Simons als Quanten-Hall-Flüssigkeit der Punktierungen, Flussanheftung) wird die
   U(1)-Zählung als Zählung masseloser Helizitäten gelesen. Die Suche (alphaXiv, Web) fand auch sonst keine solche Lesart; ein Fehlen ist damit nicht
   bewiesen.

## Rechnung am Bestand

| Prüfung | Ergebnis |
|---|---|
| (1) reelle Felder, darunter statische Flusslinien (E_n, B_n beliebig) | Breite χ_z = 0 (Abweichung 4·10⁻¹⁷): **Lage von P**, nie an einem Port-Pol |
| (2) Dualität E + iB ↦ e^{ia}(E + iB) an einer Flusslinie | Azimut von χ dreht um −2a, Breite bleibt 0; der Azimut ist der Ladungswinkel elektrisch/magnetisch |
| (3) Breite von M (b = 0,5363) | nur von komplexen, zeitharmonischen Feldern erreichbar (Beispiel gerechnet), nie von reellen |
| (4) Normalfluss S·n | Flusslinie 0 (keine Querung), normal laufende Welle 1 |

(1) folgt direkt aus r16.3(c): Für reelle Felder ist s₋ = conj s₊, also |s₊| = |s₋| und das Helizitätsvorzeichen 0.

## Einordnung
1. **(S1′) in der Form „masselose Querung“ widerspricht dem isolierten Horizont.** Eine normal querende Welle trägt Normalfluss, T(l, l) > 0; ABK und
   DL zählen aber gerade am isolierten Horizont, wo φ₀ = 0. Die Stränge eines isolierten Horizonts sind Flusslinien, keine Querungen. Das bestätigt
   den in der Übergabe notierten Ausweg „verschiedene Objekte“ von der Literaturseite.
2. **Flusslinien liegen auf der χ-Kugel bei P.** Eine statische Flusslinie ist ein reelles Feld; sie hat Helizität 0 und liegt auf dem Äquator. Die
   Dualität dreht dort nur den Ladungswinkel. Die Ports (Pole), über die U1 und der Frame M erklärt sind, erreicht eine Flusslinie nicht.
3. **Lesart (nicht hergeleitet):** Ein Horizont im Gleichgewicht trüge dann Punktierungen in der Lage von P. Nach `../op1_entropy_count_2026_11_17/`
   zählt P alle 2j + 1 Zustände (γ = 0,274067); das ist der Wert, den die SU(2)-Behandlung des isolierten Horizonts (ENP, Ghosh–Mitra) liefert.
   Die Gewicht-2-Zählung von M (DL, γ = 0,237533) bräuchte Helizität, also einen zeitharmonischen, strahlenden Anteil, den der isolierte Horizont
   gerade ausschließt. Wenn M überhaupt an einem Horizont zählt, dann eher an einem nicht isolierten (dynamischen), oder M liest dort etwas anderes
   als die Punktierungsfelder.
4. **Folge für H102 (Warnung, kein Befund):** H102 steht auf γ_M. Liest man den isolierten Horizont als P, spricht das eher für 0,274 und damit gegen
   H102 (m_τ ≈ 1868 MeV). Das ist eine Lesart; H102 bleibt bis zur nächsten PDG-Ausgabe offen und unverändert.

## Grenzen
- Die LQG-Stränge sind gravitative Flusslinien (Fläche = elektrischer Fluss des Ashtekar–Barbero-Feldes), nicht Maxwell-Linien. Eine Lage auf der
  χ-Kugel ist im Bestand nur für das elektromagnetische Feld erklärt; die Übertragung auf gravitative Stränge ist eine Analogie.
- (1)–(4) sind analytisch und nicht blind. Die Lesart 3 ist nicht gegen Daten geprüft.
- OP1 offen; (S1) und (S1′) unverändert offen; H102 unverändert.

## Ergebnis in einem Satz
Am isolierten Horizont quert keine Strahlung (φ₀ = 0); seine Punktierungen sind Flusslinien, und Flusslinien liegen auf der χ-Kugel bei P, nicht an
den Ports. (S1′) als masselose Querung passt deshalb nicht zum isolierten Horizont, und die Gewicht-2-Zählung von M bleibt unbegründet. OP1 offen.
