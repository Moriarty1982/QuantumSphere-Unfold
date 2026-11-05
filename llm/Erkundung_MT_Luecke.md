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
