# Ergebnis H27: Ein Kompensator der Form ½(id + J) ergänzt die Dubletts zum vollen linkshändigen Inhalt einer Generation

Vorab-Notiz: `Vorab_Notiz_H27_MM_Kompensator_Chiralitaet.md`, Commit 614ac3e (2026-10-23 20:12 MESZ), vor der Rechnung. Das Ladungsmuster
war dort **vorab analytisch offengelegt**; die Rechnung prüft es an den Matrizen, sie sagt es nicht vorher. Skript `k83_test_h27.py`,
Ausgabe `k83_out.txt`.

**Erstlauf und Korrektur (offen gelegt).** Der erste Lauf (`k83_out_erstlauf.txt`) meldete H27b als widerlegt, weil alle Farb-Tripletts
fehlten. Ursache war ein Fehler im Skript, nicht in der Mathematik: Die Kandidatenwerte von Y/2 wurden auf 9 Stellen gerundet, der
Nullraum-Test verlangte 10⁻¹⁰. Damit gingen alle nicht-dyadischen Werte (±1/6, −2/3, 1/3) verloren, die dyadischen (0, 1, −1/2) nicht. Die
Korrektur ersetzt nur diese Rundung durch exakte Bruchwerte. Das Kriterium blieb unverändert.

## Konstruktion

Aufteilung D aus r41 auf ℂ⊗ℍ⊗𝕆 ≅ ℂ³². Kompensator C_ch = ½(1 + J), J = i·L_{e₇} (äußere mal innere Einheit, J² = 1).
Schwache SU(2)′: T_a′ = C_ch T_a. Hyperladung Y/2 = Q − ½ + (1 − C_ch)T₃. Q_em = T₃ + Q − ½.

## Ergebnisse

| Hypothese | Ergebnis | Befund |
|---|---|---|
| H27a Kompensator | **bestätigt** | C_ch hermitesch, idempotent, J² = 1; vertauscht mit Farbe, Lorentz, R_q, Q; Bild = Q-Sektoren 0 und 2/3, Rang 16 von 32 |
| H27b Quantenzahlen | **bestätigt** (nach Korrektur) | siehe Tabelle; Y/2 vertauscht mit SU(2)′, Farbe, Lorentz; Q_em = T₃′ + Y/2 |
| H27c Anomalien | **bestätigt** | Tr Y, Tr Y³, SU(2)²Y, SU(3)²Y verschwinden |
| H27d Chiralität, Frame | **bestätigt** | SU(2)′ lebt nur auf dem Bild von C_ch; T C_ch T⁻¹ = 1 − C_ch |
| H27e MM-Lesart | **bestätigt** (Kontrolle) | 𝓜 = λ₀C_ch + λ₁(1 − C_ch) hat C_ch als Spektralprojektor |

| (Farbe, SU(2), Y/2) | Q_em | Zustand | komplexe Dimension |
|---|---|---|---|
| (3, 2, 1/6) | 2/3, −1/3 | Quark-Dublett (u, d)_L | 12 |
| (1, 2, −1/2) | 0, −1 | Lepton-Dublett (ν, e)_L | 4 |
| (3̄, 1, −2/3) | −2/3 | u^c | 6 |
| (3̄, 1, 1/3) | 1/3 | d^c | 6 |
| (1, 1, 1) | 1 | e^c | 2 |
| (1, 1, 0) | 0 | ν^c | 2 |

Zusammen 16 Weyl-Zustände × 2 Lorentz-Komponenten = 32: genau eine Generation des Standardmodells mit rechtshändigem Neutrino, in der
üblichen linkshändigen Schreibweise.

## Einordnung

1. **Die fehlende Hälfte kommt aus einem Kompensator, wie vom Autor vermutet.**
   - C_ch hat die Companion-Form ½(id + J). Das J ist das Produkt aus äußerer und innerer Einheit, also genau die beiden Einheiten aus r35.
   - Die schwache SU(2) wirkt nur auf dem Bild des Kompensators. Das ist im Modell die **Chiralität**: Sie wirkt auf die linkshändigen
     Dubletts, nicht auf die konjugierten Singuletts.
   - Ein Kompensator der MM-Matrix trennt damit die Chiralitäten (Lesart von `thm:hc-spectral-projector`).
2. **Der Frame-Wechsel T vertauscht Bild und Kern des Kompensators.** Im T-Frame wirkt die schwache SU(2) auf der anderen Hälfte. Mit r41
   (T = Ladungskonjugation) heißt das: Materie- und Tachyon-Frame sind im Modell Teilchen und Antiteilchen mit gespiegelter Chiralität,
   also ein CP-Spiegelbild. Das ist eine Lesart.
3. **Die Zahl 16:** Die Millennium-Matrix ist im Text 16 × 16. Der Inhalt einer Generation mit ν_R hat 16 Weyl-Zustände. Das wird
   festgehalten, nicht gedeutet; ob 𝓜₁₆ so gemeint war, kann nur der Autor sagen.
4. **Grenzen, deutlich:**
   - Das ist eine **Konstruktion unter Wahlen**, keine Herleitung. J = i·L_{e₇} und die Formel für Y/2 sind so gewählt, dass das bekannte
     Ergebnis herauskommt, und das Muster war vorab gesehen.
   - Gezeigt ist, dass die Bausteine des Companion dafür ausreichen: Kompensator, zwei Einheiten, zwei Seiten, Triality.
   - Die Anomaliefreiheit folgt aus dem Inhalt; sie ist keine unabhängige Bestätigung.
   - Ähnliche Konstruktionen gibt es in der Literatur zu ℂ⊗ℍ⊗𝕆 (Dixon, Furey, Gresnigt u. a.).
   - Nicht berührt: warum gerade diese Wahl, die Symmetriebrechung, Massen und Mischungen. Massen und Mischungswinkel bleiben widerlegt bzw.
     offen.
