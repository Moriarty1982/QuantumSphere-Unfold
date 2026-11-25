# Ergebnis H142: Mit einer vierten Kopie (HS(5)) kann der Rest eine vollständige, ladungsstabile Generation sein, Leptonen eingeschlossen; eine gemeinsame Ladung entsteht nicht

**25.11.2026. Vorab-Notiz `Vorab_Notiz_H142_Vier_Kopien_HS5.md` (Commit 1bc8fb4, Nachtrag zur Orientierung f578bff nach einem Vorlauf; teilweise
nicht blind). Skripte `k325_vier_kopien.py` (`k325_out.txt`, Vorlauf `k325_vorlauf_out.txt`), `k325b_gegenprobe.wl` (`k325b_out.txt`, Wolfram
exakt), `k325c_lepton_auswahl.py` (`k325c_out.txt`) und k325d (`k325d_out.txt`, beide nachträglich). Status: H142a bestätigt, **H142b widerlegt**,
H142c bestätigt, H142d bestätigt.**

Anlass: Autor: „ok, versuche noch eine Generation mehr.“ In 𝕊 gibt es keine vierte Kopie (H138), deshalb HS(5) mit seinen 9 oktonionischen
Kopien v = a ⊗ b. Werkzeuge: Python (numpy, scipy) für alle 126 Viererauswahlen; Wolfram Language exakt für zwei Auswahlen. Qiskit nicht eingesetzt.

## Vorlauf offengelegt
Der erste Lauf verfehlte die Kontrolle (H141 nicht reproduziert), weil die Richtungen aus Wolfram willkürliche Vorzeichen hatten und die
Ladungsrichtung u = e₇ ⊗ v vom Vorzeichen abhängt. Nach dem Nachtrag wird die Orientierung durch die Automorphismen transportiert
(v = a ⊗ b, a, b ∈ {f₀, f₁₂₀, f₂₄₀}); damit ist die Kontrolle exakt erfüllt. Bei freien Vorzeichen (nicht gewertet) schließen sich die Leptonen in
27 von 1008 Auswahl-Orientierungs-Paaren, bei drei Kopien in keinem (0 von 336).

## Ergebnis
| Teil | Messwert | Kriterium | Entscheidung |
|---|---|---|---|
| H142a | su(3) für alle 9 Kopien gleich (cos 1,000000000000); jede Kopie: Leck ≤ 5·10⁻¹⁷, Generationsspektrum | vorab | **bestätigt** |
| Kontrolle | drei Sedenion-Kopien in A₅: Kern 9, Spektrum ⅓³, ½³, ⅔³ (wie H141) | vorab | erfüllt |
| H142b | in **9 von 126** Viererauswahlen enthält der Kern 0 und 1 (Spektrum 0, ⅓³, ½², ⅔³, 1; Wolfram exakt) | keine | **widerlegt** |
| H142c | min Leck² der gemeinsamen Ladung 3,5 / 4,18 / 5,0 je Klasse | > 10⁻³ | **bestätigt** (keine gemeinsame Ladung) |
| H142d | Rang 4 (81 Auswahlen): Kern = 3 Singuletts (½); Rang 3 (45): Kern 10 = 4 Singuletts ⊕ 3 ⊕ 3̄ | vorab | **bestätigt** |

**Die 9 Lepton-Auswahlen (k325c, k325d, nachträglich):**
- Ihr Kern enthält einen Teil mit dem Spektrum (0, ⅓³, ⅔³, 1), der unter der Ladung **exakt stabil** ist (Leck ≤ 4·10⁻¹⁵) und unter su(3) als
  1 ⊕ 1 ⊕ 3 ⊕ 3̄ zerfällt: eine **vollständige Generation** mit Neutrino (0), d-artigen (⅓), u-artigen (⅔) Zuständen und Elektron-Ladung (1).
  Dazu kommen zwei Singuletts mit ½, die weiter lecken.
- Kennzeichen: Die vier Richtungen erfüllen eine Relation v₁ − v₂ + v₃ − v₄ = 0 (alle Koeffizienten vom Betrag 1, Summe 0). In den anderen 36
  Rang-3-Auswahlen steckt dagegen ein Sedenion-artiges Tripel (Relation mit Koeffizienten 0, 1, 1, 1, Summe 3), und der Kern hat nur den
  Quark-Satz wie in H141 (Spektrum mit ¼ und ¾ statt 0 und 1, Wolfram exakt).
- Keine der 9 Auswahlen enthält alle drei Sedenion-Kopien; „drei Sedenion-Kopien plus eine“ gibt die Leptonen nicht.

## Warum es so ist (Lesart der Rechnung)
Ein Kernzustand muss sich in A₅ aufheben, also müssen sich auch die reellen Anteile (die Eins jeder Kopie) aufheben. Das gelingt nur, wenn die
Relation der Richtungen die Summe 0 hat. Bei drei Kopien (f₀ + f₁₂₀ + f₂₄₀ = 0, Summe 3) ist das unmöglich, deshalb hat der Rest in H141 nur
die Farbanteile, die Quarks. Bei vier Kopien mit der Wechselrelation v₁ − v₂ + v₃ − v₄ = 0 heben sich auch die reellen Anteile auf, und die
farblosen Zustände der Generation (Ladung 0 und 1) kommen dazu.

## Lesart
- **Antwort:** Mit einer Generation mehr wird der Rest in bestimmten Anordnungen zu einer vollständigen, ladungsstabilen Generation, Leptonen
  eingeschlossen. Die Bedingung ist eine Wechselrelation zwischen vier Kopien, die es erst ab HS(5) gibt.
- **Was nicht entsteht:** eine gemeinsame erhaltene Ladung für alle Kopien (H142c), und auch hier lecken zwei Singuletts mit ½.
- **Gesetzt bzw. offen:** die Orientierung der Kopien (Transport durch die Automorphismen; bei freien Vorzeichen ändern sich die Fälle, das
  Vorzeichen bleibt offen bis zur Feldgleichung), die Wahl der vier Kopien (9 gleichwertige Auswahlen), die k85-Ladung. Ob die Rest-Generation
  ein physikalischer Zustand ist (sie lebt im Kern, hebt sich in A₅ also auf), ist nicht gezeigt.
- Massen, Mischung nicht berührt. OP3, OP4 offen; kein Guard berührt.
- **Mögliche nächste Frage (nur mit neuer Vorab-Notiz):** Bilden die 9 Lepton-Auswahlen unter S₃ × S₃ eine Bahn, und zählt die Bahn wieder drei?
