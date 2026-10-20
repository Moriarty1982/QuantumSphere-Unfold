# Ergebnis H5: Mischwinkel der erhaltenen Spalte aus der Hopf-Struktur

Vorab-Notiz: `Vorab_Notiz_H5_Hopf_Mischwinkel.md`, Commit 16eff15 (2026-10-20 02:57 UTC), vor dem Vergleich.
Skript: `k20_test_h5.py`. Kontrolle: An den Polen werden die H4-Werte reproduziert (TM1 4,432; TM2 14,724).

## Variante (i): kanonische Hopf-Winkel und Azimute

Polwinkel θ ∈ {66,64°; 70,53°; 113,36°; 109,47°}, Azimut b ∈ {0°, 90°, 180°, 270°}, beide Zuordnungen:
**0 von 32 Kombinationen verträglich**; bestes χ² = 92 (Grenze 5,99). Flächenanteil der S² mit χ² < 5,99:
f = 0,020, also wären bei 32 Zufallsversuchen etwa 0,6 Treffer zu erwarten.
**Variante (i) widerlegt.**

## Variante (ii): Azimut frei

Alle vier Polwinkel geben **dasselbe** Ergebnis: χ² = 3,74 (1 FG, verträglich), sin²θ₁₂ = 0,3082,
δ_CP = 262°, Spalte = ν₁. Grund (nachgerechnet): Jede Spalte in span(c₁, c₂) hat |w_μ| = |w_τ|, und ihr
Elektron-Anteil hängt nur vom Abstand γ zu einem festen Punkt E der Hopf-Sphäre ab:
|w_e|² = sin²(γ/2), E bei Polwinkel 70,53°, b = 0 (dort ist w_e = 0). Bei freiem b lässt sich jeder Polwinkel
auf denselben Abstand γ schieben. **Der Hopf-Winkel spielt in Variante (ii) keine Rolle**; sie ist formal
verträglich, aber kein Test der Hopf-Hypothese. Robust ist nur: Jede solche Spalte als ν₁ gibt δ_CP ≈ 262°.

## Urteil nach dem festgelegten Kriterium

- (i) widerlegt. (ii) verträglich, aber entartet: H5 sagt darin nichts, was nicht schon TM1 sagt.
- **H5 als Hopf-Hypothese ist damit gescheitert.**

## Nachbefund (nicht vorab registriert, wie P3 zu behandeln)

Die Geometrie zeigt: Die Daten verlangen für die Spalte als ν₂ den Abstand γ = 66,57° von E. Der Hopf-Winkel des
Companion ist θ_H = 66,64°. Gleichwertig: |U_e2|² = β_sym², also sin²θ₁₂ = β_sym²/cos²θ₁₃ = **0,3086**
(gemessen 0,308, Abweichung etwa 0,05σ).

Warum das **kein Beleg** ist:
- Gefunden nach dem Test, nicht vorab. Die vorab festgelegte Größe war der Polwinkel, nicht der Abstand zu E.
- β_sym ist eingesetzt (aus zwei Barbero–Immirzi-Werten), nicht hergeleitet (OP1 offen), mit 4,9 % Hopf-Lücke.
- Der Companion hat rund zehn solcher Konstanten und es gibt viele Mischungsgrößen; ein Treffer auf 1σ ist
  bei so vielen Kombinationen wahrscheinlich.

Was er **wert sein kann**: eine Vorhersage für die Zukunft. JUNO misst sin²θ₁₂ auf etwa 0,5 %. Die Relation
verlangt 0,3086, TM1 verlangt 0,318. Das trennt klar. Als echter Test müsste die Relation jetzt, vor JUNO, als
eigene Vorab-Notiz festgeschrieben werden.

## Status

[P] H5 gescheitert. Strukturbefund (M): Elektron-Anteil = sin²(γ/2) auf der Hopf-Sphäre, |U_μ| = |U_τ|
für alle Spalten der Familie. Nachbefund |U_e2|² = β_sym² nur als Kandidat für eine künftige Vorab-Notiz.
Guards unberührt.
