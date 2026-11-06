# Erkundung: Gravitonen am Urknall unter G2 und Δ ≲ ℓ_P. Mit Materie-Gewichten ist ΔN_eff weit zu groß

**6. November 2026. Status: Erkundung, Abschätzung, nicht blind (die N_eff-Grenze ist bekannt), ohne Kriterium.** Der Autor sagte „weiter“; es ging um den offenen Punkt aus r04.5: Wie sehen Tensormoden den Übergang, und hinterlässt das eine Spur? Code `k213_gravitonen_neff.py`, Ausgabe `k213_out.txt`.

## Vorwissen geprüft
- r04.5 (`Erkundung_Bosonen_Energie_Urknall.md`): Erzeugte Bosonen haben n₀ = 0,404 je Mode bis k_max ~ 1/Δ ≳ M_P, ρ ≈ g·0,0051·k_max⁴, keine Fermionen.
- r03.1–r03.3: Fermionen werden nicht erzeugt; Bosonen-Norm; Δ ≲ ℓ_P.
- H82/H83: Der Einstein–Cartan-Term trägt unter der zweiten Lesart Gewicht und Phase wie ein Term mit Ableitungen; die Gewichte der Gravitation sind gegen r19 offen.
- Kosmologische Eckwerte aus Vorwissen, nicht nachgeschlagen: g* = 106,75 (Standardmodell, heiß), g* = 10,75 bei der BBN, ΔN_eff ≲ 0,3, ΔN_eff = (8/7)(11/4)^{4/3}·ρ_GW/ρ_γ.

## Annahmen
1. Die Gravitonen (2 Polarisationen) tragen **Materie-Gewichte** wie die übrigen erzeugten Bosonen und bekommen dasselbe Spektrum n₀ bis k_max.
2. Die übrigen erzeugten Bosonen (g_B Freiheitsgrade) thermalisieren zusammen mit den nachgebildeten Fermionen zu einem Bad mit g* = 106,75. Die Gravitonen entkoppeln sofort und thermalisieren nicht.
3. Entropieerhaltung danach: ρ_rad·a⁴ ∝ g*^{−1/3}. Ein Gas, das nicht thermalisiert, wird dagegen nur verdünnt (ρ_GW·a⁴ fest).

## Ergebnis
| g_B (ohne Gravitonen) | Anteil der Gravitonen anfangs | ρ_GW/ρ_γ bei der BBN | ΔN_eff |
|---|---|---|---|
| 0 | 1 | ∞ | ∞ |
| 4 | 0,33 | 5,8 | 25 |
| 28 (Standardmodell-Bosonen) | 0,067 | 0,83 | **3,6** |
| 100 | 0,020 | 0,23 | 1,0 |
| 300 | 0,0066 | 0,077 | 0,34 |
| 1000 | 0,0020 | 0,023 | 0,10 |

Mit den Bosonen des Standardmodells (g_B = 28) wäre ΔN_eff ≈ 3,6. Die Grenze ≈ 0,3 verlangt g_B ≳ 300 Freiheitsgrade mit Materie-Gewichten, also weit mehr als das Standardmodell.

## Lesart
- **Gravitonen mit Materie-Gewichten sind unter G2 und Δ ≲ ℓ_P praktisch ausgeschlossen**, es sei denn, sehr viele weitere Bosonen werden erzeugt und thermalisieren. Wenn nur wenige Bosonen Materie-Gewichte tragen, wird es schlimmer, weil der Anteil der Gravitonen dann größer ist.
- Ausweg 1: **Gravitonen tragen Photon-Gewichte (a = b)**. Dann gibt es am Übergang keine Erzeugung (r85.5) und keine Gravitationswellen-Spur aus dem Urknall selbst. Das passt zu r64 („Gravitation selbst frame-unabhängig“). Es wäre eine Festlegung des Autors.
- Ausweg 2: k_max deutlich unter der Planck-Skala. Das widerspricht aber Δ ≲ ℓ_P (r03.3), weil dann die nicht unitären Moden k ~ 1/Δ im beobachtbaren Bereich lägen.
- Die Abschätzung hängt an den Annahmen 1–3. Insbesondere ist nicht gerechnet, ob Tensormoden, die nicht konform sind, am Übergang dasselbe n₀ bekommen. Am Urknall gilt a(τ) → 0, und die übliche Erzeugung durch die Expansion käme hinzu.

## Folge
Eine Entscheidung des Autors ist nötig: mit welchem Gewicht die Gravitation den Übergang sieht. Mit Photon-Gewichten ist das N_eff-Problem weg, und der Urknall erzeugt keine Gravitonen. Mit Materie-Gewichten ist das Modell an ΔN_eff gescheitert, außer mit sehr vielen zusätzlichen Bosonen.

## Nachtrag (6.11., k214)
„Mit Photon-Gewichten keine Erzeugung“ gilt nur für kΔ ≪ 1. Am glatten Übergang ist die Erzeugungsenergie auch bei a = b von gleicher Ordnung (I = 0,066 statt 0,091 Δ⁻⁴), ΔN_eff ≈ 2,6. Siehe `Erkundung_Erzeugung_Photongewichte.md`.
