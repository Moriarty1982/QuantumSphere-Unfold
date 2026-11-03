# Vorab-Notiz H64: Ist die Konstruktion R kovariant?

**Geschrieben und committet am 4. November 2026 vor der Rechnung. Status: vorregistriert.**

## Vorwissen geprüft (Suche nach „kovarian / covarian / boost / Lorentz“ in `analysis/OP5_*`, r6x–r7x, predictions)
- `OP5_Boost_Tangent_Result.md` und `OP5_Boosted_Triad_And_Coframe_Feedback.md` (27.10.) prüfen geboostete Feldfamilien als Lösungskandidaten. Den Kovarianztest der Konstruktion auf Symbolebene machen sie nicht.
- `OP5_Covariant_Readout_Completion.md` betrifft den Readout und nicht R.
- H62 und H63 prüfen Invarianz bei festem Hintergrund; deren Scheitern ist nach dem Nachtrag zu H62 strukturell erwartet.
- Ein Test der Äquivarianz von R liegt nicht vor.

## Aufbau
R(ψ, ∂ψ; A, ∂A, h, ∂h) wie in k127:
- Koframe E_a^m = Re ψ†Q_a D_mψ, V = E⁻¹;
- F = i V^m_a K_a D_mψ − hYψ;
- G und dg wie in k127.

Die Hintergrundfelder werden als Eingaben behandelt: der Farbzusammenhang A_m (3 × 3 ⊗ 1₄) mit ∂A sowie h mit ∂h. Am Keim (k127, Abgleich mit dem gespeicherten J auf 4e-9) werden drei Transformationen angewandt:
- (a) eine lineare Koordinatenänderung x' = Mx mit M ∈ GL(4) zufällig; ∂ψ, A, ∂A und ∂h transformieren tensoriell, ψ bleibt;
- (b) eine innere Lorentz-Transformation ψ' = (1₃ ⊗ S)ψ mit S ∈ Spin(1,3) zufällig (Drehung und Boost); die Koordinaten bleiben;
- (c) beides zusammen.

J' = ∂R'/∂j' wird neu aufgebaut, mit L als realifizierter Jet-Transformation (j' = L j). Gemessen wird das relative Residuum

res = min_C ‖J'L − CJ‖ / ‖J'L‖,

blockweise für F, G und dg. C ist frei, die Zeilen dürfen also beliebig gemischt werden.

## Kontrollen
- Positiv: M = 1 und S = 1 ergeben res ≤ 1e-9.
- Negativ: In (a) wird der Hintergrund nicht mittransformiert (A, ∂A, ∂h bleiben). Das muss res ≥ 1e-3 ergeben, sonst trennt der Test nicht.

## Hypothese H64
In (a), (b) und (c) gilt res ≤ 1e-7 für F, für G und für dg. R ist dann koordinatenkovariant und intern lorentzkovariant, sobald der Hintergrund mittransformiert wird. Das Scheitern von H62 und H63 käme dann ganz vom Hintergrund (Ψ am Keim, A, h).

## Entscheidung
| Ergebnis | Bedingung |
|---|---|
| bestätigt | alle res ≤ 1e-7 |
| widerlegt | ein res ≥ 1e-4; benannt wird der brechende Block und die brechende Transformation |
| ungültig | eine Kontrolle verfehlt, oder ein res liegt zwischen 1e-7 und 1e-4 |

Finite Differenzen mit Schritt 1e-5 erlauben etwa 1e-10.

## Nachtrag vom 4. November 2026, nach Lauf 1 und vor Lauf 2
**Lauf 1 ist ungültig.** Die positive Kontrolle ergab res = 2.1e-7 und verfehlte damit die Schranke 1e-9.

Werte von Lauf 1:
| Fall | res |
|---|---|
| Kontrolle negativ | F 0.26, G 0.26, dg 2e-7 |
| (a) | ≤ 2.1e-7 |
| (b) | ≤ 2.1e-7 |
| (c) | ≤ 2.1e-7 |

Ursache: J₀ hat Rang 31 mit einem Singulärwert von 1.3e-11 relativ. Die Pseudoinverse ohne Abschneiden verstärkt das Rauschen der finiten Differenzen.

Lauf 2 nutzt die Pseudoinverse mit rcond = 1e-6; alle Kriterien bleiben unverändert. **Lauf 2 ist nicht blind**, weil die Werte von Lauf 1 bekannt sind.

Zur negativen Kontrolle: Der dg-Block hängt im Symbol nur von h ab, nicht von ∂h, A oder ∂A. Er kann die Kontrolle deshalb nicht verfehlen. Für F und G gilt die Kontrolle (≥ 1e-3).
