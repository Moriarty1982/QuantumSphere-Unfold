# Ergebnis H208 (k418): sin²θ₁₂ ist nicht starr gepinnt — die Struktur handelt θ₁₂ gegen die maximale CP-Verletzung

**Datum:** 2026-11-27. **Werkzeuge:** numpy (PMNS, Richtungs-Scan über alle 8 hermiteschen Richtungen + 28 Paare, θ₁₃ an Daten gepinnt), **Wolfram Language exakt** (v₀ Eigenvektor von N̂ für symbolische b,c; TM1-Formel). Beide einig.
**Vorab:** `Vorab_H208_Theta12_TM1.md` (vor der Rechnung committet, Commit 4ee00c6). **Teilweise nicht blind** (dass K₂ sin²θ₁₂≈0,319 gibt, war aus H206 bekannt). **Nachträglich/blind:** die θ₁₂↔CP-Korrelation (nicht vorab vermutet — die Vorab-Notiz hatte eine starre Vorhersage erwartet; der Scan zeigt stattdessen einen Handel).

## Frage
Ist sin²θ₁₂ ≈ 0,318 strukturell erzwungen (TM1-Vorhersage) oder gibt es eine struktur-erhaltende Deformation, die es auf die gemessenen 0,3036 senkt, ohne θ₁₃, Massen-Erhaltung (ρ=1/Koide) und maximale CP-Verletzung (|sin δ|=1) zu brechen?

## Befund: TEILWEISE — θ₁₂ ist senkbar, aber nicht bis zum Zentralwert, und nur gegen die CP-Verletzung

**(1) Die feste Spalte v₀ ist exakt (Wolfram).** v₀ = (1,0,1)/√2 ist Eigenvektor von N̂ = [[1,b,c],[b,1,−b],[c,−b,1]] für **jedes** b,c, Eigenwert λ = 1+c (b-unabhängig). Numerisch ‖N̂v₀ − λv₀‖ ~ 1e-17 über den ganzen Versatzbereich. Aus |U_e1|² = ⅔ folgt exakt sin²θ₁₂ = (1 − 3 s₁₃)/(3(1 − s₁₃)) = 0,31800 bei s₁₃ = 0,02248 (die klassische TM1-Vorhersage).

**(2) Das Schema ist „nahe-TM1", nicht exakt-TM1.** Am physikalischen Punkt (Richtung K₂, κ* an sin²θ₁₃ gepinnt): |U_e1|² = 0,66519 (statt ⅔ = 0,66667), sin²θ₁₂ = 0,31951 (**+2,5σ**). Bei κ=0 liegt sin²θ₁₂ exakt auf der TM1-Kurve; die K₂-Korrektur addiert +1,5e-3 … +6,6e-3. Über alle Knöpfe (Neutrino-Versatz x, Stärke κ) bleibt sin²θ₁₂ im engen Band **0,313–0,326**, nie in der Nähe von 0,3036.

**(3) Rückwärtssuche.** Die Daten (sin²θ₁₂ = 0,3036) verlangen |U_e1|² = cos²θ₁₂cos²θ₁₃ = **0,6807**, also 0,014 **über** ⅔. Die feste Ein-Feld-Spalte v₀ ↔ |U_e1|² = ⅔ ist innerhalb der Ein-Feld-Form nicht verstellbar.

**(4) Voller 8-dim Störraum (290 Kandidaten, θ₁₃ immer an Daten gepinnt):**

| Zwang | min sin²θ₁₂ | z(θ₁₂) | ρ (Koide K) | \|sin δ\| | via |
|---|---|---|---|---|---|
| nur θ₁₃ (Masse+CP frei) | 0,1910 | −17,6σ | 0,944 (0,631) | 0,631 | S+c+K₁ |
| + Masse erhalten (ρ=1) | 0,2336 | −10,9σ | 1,002 (0,668) | 0,647 | S+d+K₁ |
| + Masse UND \|sin δ\|>0,99 | **0,3155** | **+1,9σ** | 1,002 (0,668) | 0,999 | S+d+K₂ |

**(5) Pareto-Front (massenerhaltend): θ₁₂ handelt gegen maximale CP-Verletzung.**

| \|sin δ\| ≥ | min sin²θ₁₂ | z(θ₁₂) | erreicht bei \|sin δ\| |
|---|---|---|---|
| ≤ 0,65 | 0,2336 | −10,9σ | 0,647 |
| ≥ 0,80 | 0,3155 | +1,9σ | 0,999 |

Der massenerhaltende θ₁₂-Boden springt von 0,234 (submaximale CP) auf 0,3155, sobald man |sin δ| ≳ 0,8 verlangt. **Die Struktur kann nicht zugleich zentrales θ₁₂ (0,3036) und maximale CP-Verletzung haben.**

**(6) JUNO.** Vorhersage 0,318 vs NuFIT 0,3036 ist heute +2,3σ; JUNO (σ ≈ 0,0005) trennt 0,318 vom NuFIT-Zentralwert mit ~29σ — die Vorhersage ist scharf falsifizierbar.

## Lesart (TEILWEISE)
- **Hergeleitet (exakt):** die feste Spalte v₀ (|U_e1|² = ⅔) ist eine echte Struktureigenschaft der Ein-Feld-Form (Wolfram, für alle b,c).
- **Vorhersage der minimalen Struktur (nur K₂):** sin²θ₁₂ = 0,3195 (+2,5σ), hohe Seite, nahe TM1.
- **Nicht starr:** ein erlaubter, aber **nicht hergeleiteter** Zusatzterm (symmetrisch A-gerade, S+d) senkt bei erhaltenen Massen und maximaler CP auf 0,3155 (+1,9σ) — besser, aber **nicht** auf den Zentralwert.
- **Der Zentralwert 0,3036 kostet die maximale CP-Verletzung** (|sin δ| fällt auf ~0,65) oder die Massen-Erhaltung. Beides sind hergeleitete Gewinne der Struktur (H206).
- **Neue, testbare Korrelation:** entweder sin²θ₁₂ ≳ 0,315 (+1,9σ) **und** maximale CP-Verletzung, **oder** zentrales sin²θ₁₂ **und** submaximale CP. JUNO (θ₁₂) + DUNE/T2K (δ_CP) prüfen diese Weggabel gemeinsam. Fällt JUNO auf 0,3036 zentral **und** δ_CP maximal, ist das Schema widerlegt.

## Bilanz der Setzungen (Strang 3, nach H205–H208 — jetzt vier Runden „trägt teilweise")
| Schritt | gesetzt | hergeleitet | offene Wahl |
|---|---|---|---|
| H173 | Ein-Feld-Form, Brannen-Spektrum | TM1-Baum (θ₂₃=45°, \|sinδ\|=1, sin²θ₁₂=⅓) | ein Winkel θ₁₃ (Stärke) |
| H205 | — | feste Spalte v₀ baumunabhängig; θ₁₃-Korrektur ⊥ v₀ | Winkel in Ebene, Stärke, Vorzeichen |
| H206 | — | Winkel = K₂ (massenerhaltend, eindeutig); θ₂₃≈45°, \|sinδ\|≈1 | Stärke; θ₁₂ ungelöst |
| H207 | — | Stärke = gemeinsamer Versatz; H168-Spannung Artefakt | Sektor-Versatz-Abstand (4,2σ); θ₁₂ |
| H208 | (S+d als Zusatz) | v₀ exakt; θ₁₂-Boden 0,3155 (+1,9σ); **θ₁₂↔CP-Korrelation** | θ₁₂ zentral ⇄ maximale CP (echte Weggabel) |

**Ziel-Prüfung (AGENTS):** Vier Runden „teilweise" am selben Strang. Die offene Wahl ist jetzt eine **physikalische Weggabel**, keine Rechenlücke: die Struktur zwingt eine Korrelation auf; welcher Ast gilt, entscheiden künftige Daten (JUNO/DUNE). Dem Autor vorgelegt.

## Ehrlichkeit
**Teilweise nicht blind:** K₂→0,319 aus H206 bekannt. **Neu/blind:** der exakte v₀-Eigenvektor-Beweis (Wolfram), der vollständige 8-dim Boden-Scan, und die **θ₁₂↔CP-Korrelation** (nachträglich, nicht in der Vorab-Notiz vermutet — dort war eine starre Vorhersage erwartet). Der Zusatzterm S+d ist erlaubt, aber nicht hergeleitet. OP4 bleibt offen.

## Dateien
- `Vorab_H208_Theta12_TM1.md` — Vorab-Notiz (vor der Rechnung).
- `k418_test_h208.py`, `k418_out.txt` — numpy-Rechnung und Ausgabe.
- `k418b_kontrolle.wl`, `k418b_out.txt` — Wolfram-Gegenkontrolle (exakt).
