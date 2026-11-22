# Methoden-Notiz: Ein gespannter String als Vermittler des OP5-Falls (Weg C, I1; Erkundung, vor der Rechnung festgelegt)

22. November 2026. **Erkundung, nicht blind:** Die Tensorstruktur des Ergebnisses wurde beim Entwurf dieser Notiz analytisch skizziert. Keine
H-Nummer. Auftrag des Autors: „weg c“, nach Runde v4.10.0-r36 (Vakuumhintergrund erreicht N_m, setzt aber Rahmen, Achse und
Polarisationsstruktur).

## Vorwissen geprüft
- I1 (`../v4_10_0_w1/Zurueckgestellte_Ideen.md`): mehrere Systeme, verbunden durch einen String; Eintrag 5.11.: Konnektoren aus k185 als
  Stufen N = 0, 1, 2; Autorpräzisierung „es reicht, wenn er entsprechend schwingt“.
- `../op3_i1_string_bridge_2026_11_14.md`, `../op1_i1_string_endpoints_2026_11_15/`, `../op1_i1_crossing_2026_11_16/`: String zwischen
  Sektoren als Lesart; Stringdynamik offen.
- r32.0: N_m = ⅔(x² − a_⊥x + a_⊥²). r35: Dichtekopplung gibt a_⊥. r36: Ohne Hintergrund kein gerichteter Pol; mit Rahmen und Achse erreicht
  eine Spin-2-Summe N_m; die Herkunft von Rahmen, Achse und Struktur ist offen.

## Ansatz (Annahmen ausdrücklich)
- **S1:** Ein Nambu–Goto-String ist zwischen den Endpunkten im M- und im T-System gespannt, Länge L entlang der Achse n, Endpunkte in Ruhe
  (Rahmen u), feste Enden. Statische Eichung, D = 4, Querauslenkungen X^i, i ∈ {x, y}.
- **S2:** Die Spannung hängt vom Higgsradius ab, T(h) = T₀(1 + τ η/v + …) (wie bei Flussröhren, deren Spannung am Vakuumwert hängt).
- **S3:** Langwellig längs der Achse, k_z L ≪ 1. Nur die Grundmode (ω₁ = π/L) und ihre Zwei-Quanten-Zustände werden betrachtet.
Lineare Kopplung an η aus der Entwicklung von −∫T(h(X))√(−γ) bis zur zweiten Ordnung in X: ein Ein-Quanten-Term (X^i∂_iη) und ein
Zwei-Quanten-Term ½η[k_ik_jX^iX^j + Ẋ² − X′²].

## Fragen und Rechnung (Wolfram, exakt; Skript `string_mediator.wl`, Ausgabe `run/string_mediator.txt`)
1. Matrixelemente der Kopplung zwischen Grundzustand und den Zuständen mit einem Quant (Energie ω₁) und zwei Quanten (2ω₁) im
   Fock-Raum zweier Oszillatoren; Summe der Betragsquadrate je Energie = Residuum des Vermittlerterms.
2. Tensorstruktur des Residuums bei 2ω₁ in a_⊥ und x am Pol (x = 4ω₁²); Vergleich mit N_m Koeffizient für Koeffizient.
3. Ein-Quanten-Pol bei ω₁: Zähler; Kopplung der Mode 2 (α₋₂) im langwelligen Grenzfall.
4. Einordnung in die Familie von r36.3.

## Raster (vorab)
- **trägt:** Der gespannte String liefert Rahmen, Achse und Polarisationsstruktur selbst und reproduziert N_m am Pol exakt, ohne weitere Pole.
- **trägt teilweise:** Rahmen und Achse folgen aus dem String, die gerichteten Anteile von N_m werden erreicht, aber ein ungerichteter Anteil
  weicht ab oder es entstehen zusätzliche Pole.
- **trägt nicht:** Der String gibt keinen gerichteten Zähler mit a_⊥².

Frames: alles im Ruhesystem der Endpunkte, im Materie-Frame M angegeben. S1–S3 sind Annahmen, keine Herleitung. OP5 bleibt in jedem Fall
offen.
