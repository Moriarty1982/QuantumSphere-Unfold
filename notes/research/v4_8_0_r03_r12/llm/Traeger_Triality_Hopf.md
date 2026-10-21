# Träger der drei Triality-Plätze: die oktonionische Hopf-Faserung

Stand 2026-10-20. Modellbau, kein Datenvergleich, keine Vorhersage. Skript: `k29_hopf_triality_traeger.py`.
Bezug: K28 (Vorschlag Generationen = Triality-Plätze), `thm:hopf` (S₂ ≅ S⁸ = 𝕆P¹ „octonionic spinor,
3 generations“, Faser S⁷ → S¹⁵ → S⁸).

## Befunde (M, nachgerechnet)

1. **Die Hopf-Abbildung ist das Triality-Produkt.** h(x, y) = (|x|² − |y|², 2xȳ) bildet S¹⁵ normtreu auf S⁸ ab.
2. **Einheits-Tripel.** Die Menge {(a, b, c) : |a| = |b| = |c| = 1, (ab)c = 1} ist unter der zyklischen Vertauschung
   (Triole ℤ₃) und unter (a, b, c) → (ā, c̄, b̄) abgeschlossen, trägt also die Generationen-S₃ aus K28. Sie hat
   Dimension 14 (a, b frei, c = conj(ab)).
3. **Verbindung zur Faserung.** Über dem Äquator von 𝕆P¹ (|x| = |y| = 1/√2) ist (a, b, c) = (√2·x, √2·ȳ, v̄) mit
   v = 2xȳ genau ein Einheits-Tripel; die Faser über v ist {(a, ā·v)} ≅ S⁷. Die drei Triality-Plätze sind also
   die beiden Komponenten des Totalraums und der Basispunkt.
4. **G₂ diagonal** erhält die Tripel und ist mit der Hopf-Abbildung verträglich.
5. **Symmetrischer Punkt.** a = b = c ist genau dann ein Einheits-Tripel, wenn a³ = 1, also a = exp(2πu/3) für
   eine imaginäre Einheit u. Für u = e₇ liegt a in span(1, e₇), der komplexen Ebene am Ende der Kaskade, und ist dort
   ω. **Der Stabilisator dieses Punktes in G₂ hat Dimension 8 und ist die Farbgruppe SU(3).** Den symmetrischen
   Generationenpunkt zu wählen, legt also zugleich die Farbgruppe fest.

## Probe (M): Koide-Phasen als Tripel-Phasen

Liegen alle drei Plätze in span(1, e₇), wird (ab)c = 1 zu α₁ + α₂ + α₃ ≡ 0 (mod 2π), eine additive Triole der
Phasen. Die Koide-Phasen δ + 2πk/3 erfüllen das nur für 3δ ≡ 0 (mod 2π). Gemessen ist δ = 0,2222 bei den geladenen
Leptonen, also 3δ = 0,667. **Die direkte Lesart scheitert.** Dass 3δ ≈ 2/3 ist, ist die bekannte Zahl 2/9 · 3. Ihre
Allgemeingültigkeit hat H1 (r11) widerlegt; sie wird hier nicht als Befund gezählt.

## Einordnung

- **[S]** Die oktonionische Hopf-Faserung, die der Companion schon für S₂ benutzt, trägt die drei Triality-Plätze
  von selbst, mit der Triole als zyklischer Symmetrie und G₂ als Farbseite. Das ist ein natürlicher Träger für den
  Vorschlag aus K28, keine Herleitung der Generationen.
- **[S]** Die Wahl des symmetrischen Punktes bricht G₂ auf SU(3): Generationen-Symmetrie und Farbgruppe hängen über e₇
  zusammen. Die frühere Zuordnung „e₇ = Kaskaden-Ende, SU(3) = Stab(e₇)“ erhält damit eine zweite Lesart.
- **[V, offen]** Massen: Wie aus Abweichungen vom symmetrischen Tripel eine Massenhierarchie und K = 2/3 entstehen
  sollen, ist offen. Die einfachste Phasenlesart scheitert (s. o.).
