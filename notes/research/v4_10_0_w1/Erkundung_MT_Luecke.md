# Erkundung: Die M–T-Lücke der komplexen Lesart (k174)

**5. November 2026. Status: Erkundung ohne Kriterium.** Ausgangspunkt (k170, k172): Mit unabhängiger Verbindung erzwingt die komplexe Lesart K bei nicht symmetrisierter Kinetik j^a = 0. In einem Frame folgt daraus Ψ = 0, weil j⁰ = |ψ|² ≥ 0. Der Autor will prüfen, ob Anteile im Tachyon-Frame das umgehen.

## Tachyon-Frame nach Konvention F
T ist die Fortsetzung der Rapidität η → η + iπ/2 entlang einer Achse n (r20, r22). Daraus folgt γ = cosh 2η → −γ, und eine Größe vom Gewicht k in γ bekommt die Phase (−1)^k (F3).
- **Vektorebene:** Λ(iπ) = diag(−1, 1, 1, −1) für n = z, also die Spiegelung der (t, n)-Ebene.
- **Spinorebene:** exp(−(iπ/2)σ_n) = −iσ_n ist unitär. Damit gilt j(ψ_T) = R_n(π) j_M, und die Dichte bleibt positiv.
- **Beides passt zusammen:** Λ(iπ) = −R_n(π) (k174, exakt). Der Strom eines T-Anteils ist mit dem Vorzeichen aus F3 also j_T = −j(ψ_T) = Λ(iπ) j_M. Er trägt negative Dichte gegenüber M.

## Befund
1. **Summe:** j_M + j_T = 2 j_⊥, der Anteil quer zur M–T-Achse (k174, exakt).
2. **K-Bedingung im System M + T:** j_gesamt = 0 genau dann, wenn der Gesamtstrom von M in der (t, n)-Ebene liegt, also Materie nur entlang der M–T-Achse strömt. Geprüft mit 16 Zuständen, Spin entlang n: J_M + J_T = 0 exakt. Für allgemeine Zustände gilt |J_M + J_T| = 2|J_⊥|.
3. **Die übrigen Gleichungen aus Im S:**
   - Die Variation nach dem Koframe ist ∝ j_gesamt und verschwindet damit.
   - Die Variation nach Ψ enthält nur die Spur der Torsion. Die reelle Wirkung liefert aber nur total antisymmetrische Torsion (k173), deren Spur null ist.
   - Die K-Lesart ist also mit der reellen Wirkung verträglich.
4. **Folge:** Mit j_gesamt = 0 verschwindet auch die Vier-Fermionen-Kopplung −(3/16)κ j², und damit die Torsion ganz.

## Lesart und Preis
- Die Lücke existiert. In einem System aus Materie- und Tachyon-Anteilen nach Konvention F tilgt die komplexe Lesart die Spinoren nicht. Sie verlangt stattdessen eine **exakte Strombilanz zwischen M und T**: Materie- und Tachyonstrom heben sich auf, quer zur Achse fließt nichts, und die Torsion verschwindet. Das erinnert an die Paarerzeugung aus dem Vakuum R (r29), ist aber nur eine Lesart.
- **Preis 1:** Der T-Anteil hat gegenüber M eine Kinetik mit umgekehrtem Vorzeichen (Gewicht 1, Phase −1). In der Buchführung von M ist er ein Feld negativer Norm. Ob das physikalisch zulässig ist (Energievorzeichen, Stabilität), ist offen.
- **Preis 2:** Die Achse n ist ausgezeichnet, die Isotropie also gebrochen. Die Wahl der Achse ist eine Eingabe.
- **Beobachtung ohne Schluss:** Im Vergleichsmodell (k168) strömten die drei Blöcke entlang einer Achse (x), mit Gegenströmung. Das ist ein anderes Modell; der Anklang wird nur festgehalten.
- **Konvention F:** Beide Frames sind ausdrücklich getrennt geführt (ψ_M, ψ_T, Abbildung über Λ(iπ)). Verglichen wird erst nach der erklärten Abbildung.

## Nächste Fragen
- Ist der T-Anteil ein eigenes Feld (16 weitere Zustände) oder dasselbe Feld in zweiter Lesart?
- Was sagt die reelle Wirkung zum T-Anteil mit umgekehrtem Kinetikvorzeichen (Energie, Hamilton-Funktion)?
- Liefert die Bedingung „kein Querstrom“ eine Vorhersage, oder ist sie nur eine Einschränkung?

## Nachtrag (5.11., Autorfrage „wer sagt, dass Frames im Normalzustand synchron sind?“)
Lesart: Der T-Anteil ist dasselbe Feld, mit Versatz δ gelesen, ψ_T(x) = −iσ_n ψ_M(x + δ). Eine reine Phase fällt aus allen Strömen heraus; es zählt nur ein Raum- bzw. Zeitversatz. Die K-Bedingung wird zu j_M(x) + Λ(iπ) j_M(x + δ) = 0:
- t- und n-Komponente: j(x) = j(x + δ), also periodisch mit Periode δ;
- Querkomponente: j_⊥(x) = −j_⊥(x + δ), also antiperiodisch, eine Schwingung mit Periode 2δ (ω = π/δ).

Synchrone Frames (δ = 0) verbieten jeden Querstrom. Versetzte Frames erlauben ihn als Schwingung mit einer durch δ festgelegten Frequenz; gemittelt verschwindet er. „Eigenes Feld“ und „dieselbe Generation“ sind damit Grenzfälle einer Familie (δ = 0 starre Spiegelung, freies δ fast unabhängig). Mögliche Verwandte im Companion, nur als Lesart: β_sym als „Frame-Versatz“, Kick = Schwebung/6 (r13). Analytisch hergeleitet, noch nicht mit der Weyl-Gleichung zusammen gelöst.

Nächste Frage: Erlaubt die Weyl-Gleichung (mit A, ohne Torsion wegen j_gesamt = 0) Lösungen, deren Querstrom antiperiodisch mit Periode δ ist, und was legt δ fest?

## Nachtrag 2 (5.11., Autor: „Der Versatz könnte durch eine kosmische Expansionsvariable festgelegt werden; deswegen wurde OP5 eröffnet.“)
- Fundstelle: `thm:expansion` (Monolith ~Z. 6925): a(t) ∼ τ_n = √(t_n² − β_sym²), β_sym als Frame-Versatz des Beobachters. Expansion und Frame-Versatz sind dort verknüpft. Grenze: Die Herleitung über Riemann-Nullstellen ist seit v4.8.0-r04 zurückgezogen (T4); der Zusammenhang ist neu zu begründen.
- Plan für H69 (Vorab-Notiz vor jeder Rechnung): (a) Kopplung δ = δ(a) bzw. δ ∝ 1/H vorab festlegen; (b) prüfen, ob die Weyl-Gleichung Lösungen mit antiperiodischem Querstrom (Periode 2δ) zulässt; (c) OP5-Frage: Erzeugt die versetzte M–T-Paarung (T-Anteil mit umgekehrtem Kinetikvorzeichen) einen effektiven Vakuumterm, den W1 allein nicht hat? Kandidaten für δ(a) nur aus vorab genannten Formen, nicht nachträglich anpassen.

## Nachtrag 3 (5.11., Autorfrage „gilt das für alle Frames, oder wirkt die Idee erst bei einer anderen Mischung?“; k177, Erkundung)
H69/H70 nutzten gleiche Gewichte für M und T. Mit den Frame-Gewichten von Konvention F (p₊ für M, p₋ für T) und Δω·δ = π:
| Gewichte | p₊ − p₋ | max|j_gesamt| | Energierest / |T^M| | Mittel des Rests | Spur |
|---|---|---|---|---|---|
| P (½, ½) | 0 | 6e-15 | 3e-16 | 0 | 0 |
| M (1/(1+x), x/(1+x)), x = β_sym² | +0,5364 | 4,7 | 0,536 | T_tt = T_zz = +7,9, sonst 0 | 0 |
| T (vertauscht) | −0,5364 | 4,7 | 0,536 | T_tt = T_zz = −7,9 | 0 |

- Die bisher gerechnete Paarung mit gleichen Gewichten ist genau die **Photon-Frame-Mischung P**. Dort ist alles neutral, verträglich mit der Lesart „Λ = 0 im Photon-Frame“ (T9).
- Mit den Gewichten des Materie-Frames verletzt das Paar die K-Bedingung (j ≠ 0). Es bleibt ein homogener Rest proportional zu p₊ − p₋ = |b| = 1/γ = 0,536, und zwar exakt (k177). Der Rest ist strahlungsartig entlang der Achse (T_tt = T_zz) und **spurfrei**, also nicht Λ-artig. Im T-Frame hat er das umgekehrte Vorzeichen.
- **Strukturgrund:** Masselose Weyl-Felder haben einen spurfreien Energie-Impuls-Tensor. Ein Λ-artiger Term T_μν = −ρ_Λ g_μν hat die Spur −4ρ_Λ ≠ 0. Mit masselosen Feldern gibt keine Mischung von M, T und P einen Vakuumterm.
- **Wo die Idee greifen könnte:** Spur braucht Masse. Nach r44 sind die Massenterme der Ablage antilinear, sie enthalten T und koppeln damit die Frames. Ein massives M–T-Paar mit den Gewichten des Materie-Frames, gekoppelt über den Massenterm, ist die nächste Stelle, an der ein Rest mit Spur, also ein Vakuumbeitrag, entstehen kann. Das wäre H71 mit eigener Vorab-Notiz.

## Nachtrag 4 (5.11.): Die Prämisse für H71 hält nicht ohne Frame-Prüfung
- r44 liest die antilinearen Massenterme als „Kopplung zwischen Materie- und Tachyon-Frame“, weil sie T enthalten. In r41–r49 ist T aber die komplexe Konjugation, also die **Zeitumkehr** (z ↦ z̄, σ_z, Porttausch), nicht die Tachyon-Abbildung (z ↦ iz, σ_y). Das hat r51.1, Lesart 3, festgestellt: Korrektur der Frame-Zeilen von r41, r43, r47, r48, r49. **r44 fehlt in dieser Liste**, obwohl seine Lesart 1 („mass is a coupling between matter frame and tachyon frame“) dieselbe Verwechslung enthält. Kandidat für eine Korrektur in der nächsten Runde.
- Damit ist „Masse koppelt M und T“ nicht belegt. Belegt ist: Massenterme sind antilinear und enthalten die Zeitumkehr.
- In Nachtrag 3 und im Vorschlag für H71 wurde die r44-Lesart übernommen. Vor H71 ist deshalb eine kleine Frame-Prüfung nötig, auf dem Dublett von r17 mit den drei Involutionen R = σ_y (Tachyon-Abbildung), T = σ_z (Zeitumkehr, Porttausch) und J_B = σ_x. Zu klären ist, welche von ihnen (a) γ → −γ macht (das in H69 benutzte Vorzeichen), (b) die Gewichte p₊ ↔ p₋ tauscht (Materie- gegen Tachyon-Gewichte, r22) und (c) die Massen-Konnektoren enthält.

## Nachtrag 5 (5.11., Frame-Prüfung k178; präzisiert Nachtrag 4)
Auf dem Dublett ρ = ½(1 + b_xσ_x + b_zσ_z) mit Kompensator C = ½(1 + σ_x), Portgewichte ½(1 ± b_x):
| Involution | Zustand auf der Kompensatorachse (M, b_z = 0) | Zustand abseits (b_z ≠ 0) |
|---|---|---|
| R = σ_y (Tachyon-Abbildung) | b → −b, Gewichte getauscht (0,768 ↔ 0,232) | b → −b, Gewichte getauscht |
| T = σ_z (Zeitumkehr) | **dasselbe Bild wie R** | b_x → −b_x, b_z bleibt; Gewichte getauscht |
| J_B = σ_x | nichts ändert sich | nur b_z → −b_z |

- **Auf der Kompensatorachse sind Tachyon-Abbildung und Zeitumkehr ununterscheidbar.** Beide tauschen die Gewichte von M gegen die von T. Der Materie-Frame von Konvention F liegt genau dort. Deshalb ist die Verwechslung in r41–r49 und r44 so leicht passiert.
- Sie unterscheiden sich (i) abseits der Achse, in b_z (der Kohärenz), und (ii) in der Dixon-Ablage: R lässt alle Ladungssektoren fest, T vertauscht sie und konjugiert die Ladung (r51.1(a)).
- **Präzisierung von Nachtrag 4:** Die r44-Lesart ist halb richtig. Massenterme (antilinear, mit T) koppeln einen Zustand an einen Partner mit den **Gewichten des Tachyon-Frames**, aber dieser Partner ist zusätzlich ladungskonjugiert. Es ist nicht das Bild unter der Tachyon-Abbildung R. Für r81 ist das als Präzisierung zu r44 und r51 vorzumerken.
- **Offen vor H71:**
  1. Ist der Massenpartner das R-Bild, das T-Bild oder beides (auf der Achse gleich)?
  2. Trägt das T-Bild das Vorzeichen aus F3 (γ → −γ), das in H69 dem R-Bild gegeben wurde? Auf der Scheibe ist γ = 1/|b| bei beiden gleich, das Vorzeichen ist dort unsichtbar.
