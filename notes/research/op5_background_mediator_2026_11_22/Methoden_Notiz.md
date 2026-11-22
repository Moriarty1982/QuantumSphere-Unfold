# Methoden-Notiz: Ein Vakuumhintergrund als Träger des gerichteten OP5-Vermittlers (Weg B; Erkundung, vor der Rechnung festgelegt)

22. November 2026. **Erkundung, nicht blind:** Teile der Antwort sind analytisch absehbar. Keine H-Nummer. Auftrag des Autors: „weg b“,
nach Runde v4.10.0-r35 (Materialweg trägt teilweise; Zähler a_⊥ statt ⅔a_⊥²).

## Vorwissen geprüft
- r32.0: Vermittlerterm −g_m² N_m / d_m, N_m = ⅔(x² − a_⊥x + a_⊥²), a_⊥ = |P**k**|², P = diag(1, 1, 0); d_m = m² + r_m q − x.
- r33: Vergleichsfeld = Higgs-Radialmodus von W2; Kopplung an Z, W nur quadratisch.
- r34, Rückwärtssuche (22.11.), r35: Ein gerichteter Vermittler braucht ein ausgezeichnetes Bezugssystem; das führende statische Glied hängt
  nicht von r_m ab (r35.2); Dichtekopplung eines Materials gibt den Zähler a_⊥ (r35.3).
- `../op5_bifocal_response_2026_11_18/OP5_J_Massiver_Tensorvermittler.md`: Fierz–Pauli-Austausch zwischen konservierten Quellen; für
  konservierte Quellen fallen die longitudinalen Terme weg. N_m dort als gesetzte Eingabe (`OP5_J_Luminaler_Einstein_Kanal.md`,
  `OP5_J_Metrische_Kegelgrenze.md`).
- `../v4_10_0_r80/llm/Erkundung_Fierz_Hintergrund.md` (k168): Der OP5-Keim hat eine zeitartige Strömung u^a (Counterflow ±x/t) und einen
  raumartigen Spinvektor s^a entlang φ̂ = e_y. Lesart: Hintergrund mit Achse.
- Zurückgestellte Ideen: I4 (Kondensat) ohne Feldgleichung (r34); I1 nicht Gegenstand dieses Wegs.

## Ansatz
Neues Feld X mit linearer, eichinvarianter Kopplung an |Φ|², also an den Higgs-Radialmodus η (|Φ|² = v² + 2vη + …). Drei niedrigste
Formen: Spin 0, X|Φ|²; Spin 1, X_μ∂^μ|Φ|²; Spin 2, X_μν∂^μ∂^ν|Φ|². Ausintegrieren gibt den Vermittlerterm im η-Operator; sein Residuum
am Pol ist das Gegenstück zu g_m² N_m.

## Fragen und Rechnung (Wolfram, exakt; Skript `background_mediator.wl`, Ausgabe `run/background_mediator.txt`)
1. **Lorentz-invariantes Vakuum:** Residuum am Pol für Spin 0 (Klein–Gordon), Spin 1 (Proca) und Spin 2 (Fierz–Pauli) mit den
   Ableitungskopplungen oben. Entsteht ein Pol, und ist er gerichtet?
2. **Hintergrund mit Rahmen u = (1, 0, 0, 0) und Achse n = (0, 0, 0, 1):** Felder, deren Polarisationssumme aus den Projektoren
   T = uu und S = Querprojektor zu n und u gebaut ist (Raum quer zur Achse). Zähler für Spin 1 quer, Spin 2 quer und für eine allgemeine
   symmetrische Polarisationssumme auf dem (2+1)-Unterraum senkrecht zu n. Gibt es Koeffizienten, die N_m exakt ergeben? Eindeutig?
   Positivität der Residuen im physikalischen Bereich x ≥ 0, a_⊥ ≥ 0.
3. **Herkunft des Hintergrunds:** nur Einordnung, keine neue Rechnung: Spinvektor und Strömung des OP5-Keims (k168); Tachyonbild eines
   ruhenden Materiezustands (raumartig, k185).

## Raster (vorab)
- **trägt:** Eine Konstruktion mit Vakuumhintergrund liefert Pol, gerichteten Zähler N_m in exakter Form und die lineare Kopplung an η,
  und Achse wie Polarisationsstruktur folgen aus dem Bestand.
- **trägt teilweise:** Form und Kopplung lassen sich erreichen, aber Achse, Rahmen oder Polarisationsstruktur sind gewählt, nicht hergeleitet.
- **trägt nicht:** Auch mit Hintergrund entsteht kein gerichteter Pol mit Zähler a_⊥².

Frames: alles im Materie-Frame M; der Hintergrund wird dort angegeben. OP5 bleibt in jedem Fall offen.
