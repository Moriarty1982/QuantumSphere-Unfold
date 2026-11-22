# Methoden-Notiz: Erster Ansatz einer Feldgleichung für den gerichteten OP5-Vermittler (Erkundung, vor der Rechnung festgelegt)

22. November 2026. **Erkundung, nicht blind:** Die Koeffizientenbedingungen wurden beim Entwurf von Hand skizziert (κ = ½, Skalargewicht ½).
Keine H-Nummer. Auftrag des Autors: „wäre eine feldgleichung bzw. ein erster ansatz davon nicht erstmal sinnvoll?“ und „ja, anlegen und
rechnen“, nach Runde v4.10.0-r37.

## Vorwissen geprüft
- r32.0: Vermittlerterm des Vergleichsmodells −g_m²N_m/d_m mit N_m = ⅔(x² − a_⊥x + a_⊥²), d_m = m² + r_mq − x; gesetzt r_m = ½, g_m² = 3/100.
  r32.4: führender statischer Kontrast aus ⅔g_m²a_⊥²/m².
- r33.1: Higgs-Radialmodus von W2, L_η = (∂_tη)² − (∇η)² − m_H²η² + 𝒥_hη; minimal g₀ = 0 (kein Einstein-Kanal in diesem Ansatz).
- r35.2: führendes statisches Glied unabhängig von r_m. r36.1: ohne Hintergrund kein gerichteter Pol; r36.3: N_m mit positiver
  Spin-2-Summe erreichbar, Struktur gesetzt. r37: gespannter String gibt Residuum ∝ 2a_⊥² − 2a_⊥x + x² und einen Zusatzpol bei ω₁.

## Ansatz (im Ruhesystem u, Achse n = e_z, i, j ∈ {x, y})
L = (∂_tη)² − (∇η)² − m_H²η² + 𝒥_hη
  + ½[(∂_tX_ij)² − r_m(∇X_ij)² − m²X_ijX_ij] + g X_ij(∂_i∂_jη − κδ_ij∂_t²η)
  + ½[(∂_tS)² − r_s(∇S)² − m_s²S²] + g_s S ∂_t²η,
mit X_ij symmetrisch quer zur Achse und einem Skalar S. Feldgleichungen durch Variation; Austausch durch Ausintegrieren von X und S.

## Fragen und Rechnung (Wolfram, exakt; Skript `mediator_field_equation.wl`, Ausgabe `run/mediator_field_equation.txt`)
1. Feldgleichungen im Fourierbild; effektiver η-Operator nach Ausintegrieren von X und S.
2. Abgleich mit −g_m²N_m/d_m: Für welche (g, κ, g_s) und unter welcher Bedingung an d_s gilt Gleichheit identisch in x und a_⊥? Eindeutig?
3. Stabilität: (a) Matrix der Zeitableitungen positiv definit (geisterfrei), (b) statische Energie positiv für alle **k**, (c) alle
   Lösungen x der Dispersionsgleichung reell und positiv auf einem Raster in (a_⊥, k_z²) für die Modellwerte und zwei größere g_m².
4. Anschluss an r37: Welche (κ, g_s) gibt der String? Was fehlt?

## Raster (vorab)
- **trägt:** N_m exakt, Koeffizienten eindeutig, geisterfrei und stabil für die Modellwerte, und der Anschluss an r37 legt alle Kopplungen fest.
- **trägt teilweise:** N_m exakt und stabil, aber mindestens eine Kopplung (etwa der Skalar) folgt nicht aus dem String oder dem Bestand.
- **trägt nicht:** Kein stabiler Ansatz dieser Form gibt N_m.

Frames: alles im Materie-Frame M, Rahmen und Achse wie in r36/r37. Ein einzelner String ist kein Feld; X_ij steht für eine Dichte gleich
ausgerichteter Strings, deren Kopplung untereinander r_m festlegen würde (nicht Gegenstand dieser Rechnung). OP5 bleibt in jedem Fall offen.
