# Vermittler-Suche für den OP5-Fall: kein Vakuumfeld des Bestands trägt; zwei Teilkandidaten (Erkundung, nicht blind, 22.11.2026)

**Ergebnis in einem Satz:** Kein Feld des Bestands erfüllt als Vakuumfeld alle fünf Anforderungen an den gerichteten Vermittler. Der
gegenläufige Paar-Konnektor aus k185 ist massiv, unterluminal und gerichtet, hat aber weder Feldgleichung noch eine nachgewiesene lineare
Kopplung an den Higgsradius. Die optische Mode des zweikomponentigen Materials erfüllt alle fünf, ist aber eine Mode der Präparation; mit
ihr wäre der gerichtete Kontrast eine Eigenschaft des Materials, kein Signal eines neuen Feldes.

Auftrag des Autors: „Vermittler-Suche starten“. Verfahren vorab: `Methoden_Notiz.md` (Commit a3443d99). Skript `mediator_search.wl`, Ausgabe
`run/mediator_search.txt`, Wolfram exakt. Keine H-Nummer.

## Rechnung
- **Konnektoren (k185)** bei gemeinsamer Rapidität η, Materie p_M = m(cosh η, sinh η), Tachyonbild p_T = m(sinh η, ±cosh η):

  | Konnektor | q² | Geschwindigkeit q¹/q⁰ | bei η_sym |
  |---|---|---|---|
  | Paar, gegenläufig | +2m² sinh 2η | −e^{−2η} | 3,148 m², \|v\| = 0,291 |
  | Übergang, gegenläufig | −2m² sinh 2η | e^{2η} | tachyonisch, \|v\| = 3,44 |
  | mitlaufend (beide) | 0 | ±1 | lichtartig |
- **Optische Mode** zweier überlagerter Kontinua mit Paarfeder (longitudinal): Lücke ω₀² = k(ρ₁ + ρ₂)/(ρ₁ρ₂), v_opt² = K(c_σρ₁² + ρ₂²)/(ρ₁ρ₂(ρ₁ + ρ₂)),
  Schwerpunkt ruht (ρ₁u + ρ₂w = 0). Die Higgsquelle δ𝒥_h = Y₁∂u + Y₂∂w koppelt an diese Mode genau dann, wenn Y₁/ρ₁ ≠ Y₂/ρ₂
  (Y_a = Σ y n₀ der Komponente a).

## Einordnung
| | Kandidat | V1 massiv | V2 unterluminal | V3 linear an h_W | V4 gerichtet | V5 Feldgleichung |
|---|---|---|---|---|---|---|
| K1 | Paar-Konnektor gegenläufig | ja | ja (e^{−2η}) | offen | ja (Achse der Gegenläufigkeit) | nein |
| K2 | Übergangs-Konnektor gegenläufig | nein (tachyonisch) | nein | (W2-Lesart: das ist Φ selbst) | ja | nein |
| K3 | Konnektor mitlaufend | nein | nein | – | ja | nein |
| K4 | Z, W in W2 | ja | nein (Lorentz) | nein (quadratisch, r33.2) | nein | ja |
| K5 | abelsches Eichfeld (W1) | nein | nein | nein (Vektorstrom) | nein | ja |
| K6 | Graviton | nein | nein | nein bei minimaler Kopplung (r33.2) | nein | ja |
| K7 | Kondensat I4 | offen | offen | offen | nein | nein |
| K8 | optische Mode des Materials | ja | ja | ja, falls Y₁/ρ₁ ≠ Y₂/ρ₂ | nur mit gerichteter Präparation | ja (r32.2) |

## Lesart
- Kein Vakuumfeld trägt. Der aussichtsreichste Kandidat für ein **neues Feld** ist der gegenläufige Paar-Konnektor: Er bringt Masse,
  Unterluminalität und Richtung schon kinematisch mit. Ihm fehlen eine Wirkung und eine lineare Kopplung an den Higgsradius; liest man Φ
  mit W2 als Übergangs-Konnektor, tragen Paar- und Übergangs-Konnektor bei gleichen ebenen Wellen verschiedene Impulse, sodass eine lineare
  Mischung nicht von selbst entsteht. Die Geschwindigkeit e^{−2η} ist nicht die im Vergleichsmodell gesetzte (r_m = 1/2).
- Die optische Mode erfüllt alles, macht aber den gerichteten Kontrast zu einer **Materialeigenschaft**. Das trennt die Lesarten
  deutlich: Ein Signal, das nur bei Y₁/ρ₁ ≠ Y₂/ρ₂ auftritt und mit der optischen Lücke skaliert, wäre der Präparation zuzuschreiben.
- OP5 und H96 bleiben offen. Ein nächster Schritt wäre eine Wirkung für den Paar-Konnektor mit Kopplung an Φ, vorab festgelegt.
