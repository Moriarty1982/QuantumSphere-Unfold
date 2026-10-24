# Ergebnis H39: Lesart je Teilchenart als Untergruppe der A₄ gibt die bekannte TM2-Mischung; θ₁₂ scharf, θ₂₃ nicht

Vorab-Notiz: `Vorab_Notiz_H39_Restsymmetrie_Lesarten.md`, Commit 5c916b8 (2026-10-24 05:11 MESZ), vor der Rechnung. Vorab offengelegt: Klein → alle |U_ij|² = 1/3,
ℤ₂ → TM2 mit sin²θ₁₂ = 1/(3 cos²θ₁₃); korrigiert wurde die Ankündigung „tribimaximal ohne Parameter“ (braucht S₄, nicht A₄). Skript `k95_test_h39.py`, Ausgabe
`k95_out.txt`; der erste Lauf (`k95_out_erstlauf.txt`) hat dieselben Kriteriumswerte, danach wurde nur die Nachkontrolle angehängt.

## Regel

Dirac-Sektoren (u, d, e) lesen mit G_D = ⟨τ⟩ ≅ ℤ₃ (zirkulante Kopplungen, r44), Neutrinos (Majorana-Term möglich, r44) mit einer anderen Untergruppe G_M. A₄ hat
Untergruppen der Ordnung 1 (1), 2 (3), 3 (4), 4 (1), 12 (1).

## Ergebnisse

| Hypothese | Ergebnis | Befund |
|---|---|---|
| H39a G_M = Klein | **bestätigt** (Prüfung) | kein Treffer; alle \|U_ij\|² = 1/3 |
| H39b G_M = ℤ₂ | **bestätigt** | 1 176 Treffer je ℤ₂ (alle drei ℤ₂ gleichwertig): sin²θ₁₂ ∈ [0.3402, 0.3413], sin²θ₂₃ ∈ [0.451, 0.574] |
| H39c G_M = andere ℤ₃ | **bestätigt** (Prüfung) | kein Treffer |
| H39d Quarks | qualitativ | gleiche Lesart für u und d ⇒ V = 1 in führender Ordnung, CKM nur aus Korrekturen |

**Schärfe nach dem Kriterium:** Über alle Zuordnungen mit passendem θ₁₃ streut sin²θ₁₂ von 0.340 bis 0.660 und sin²θ₂₃ von 0.399 bis 0.601. Das ist breiter als
die festgelegten Grenzen (0.02 bzw. 0.1): nach dem Wortlaut eine **Anpassung mit einem Winkel**.

## Nachkontrolle (nach der Auswertung, kein Kriterium)

1. Getrennt nach Zuordnung: Treffer gibt es nur, wenn die feste Spalte ν₂ ist (TM2). Dort ist sin²θ₁₂ ∈ [0.3402, 0.3414] **scharf** (1/(3 cos²θ₁₃) = 0.3408),
   sin²θ₂₃ ∈ [0.399, 0.601] dagegen nicht. Die feste Spalte als ν₁ gäbe sin²θ₁₂ ≈ 0.66, als ν₃ sin²θ₁₃ = 1/3.
2. Vergleich mit neueren Daten, nicht in der Notiz: JUNO misst sin²θ₁₂ = 0.3092 ± 0.0087 (arXiv:2511.14593). Der TM2-Wert 0.3408 liegt 3.6 σ darüber; der NuFIT-
   Bestwert ist 0.307.

## Einordnung

1. **Die Lesart-Regel trägt qualitativ.** Dirac-Sektoren mit ℤ₃, Neutrinos mit ℤ₂ aus derselben A₄ der Ablage: Quarks mischen in führender Ordnung nicht, Leptonen
   stark. Das ist der Unterschied zwischen CKM und PMNS, den die bisherigen Tests (H34–H38) nicht ergaben.
2. **Quantitativ ist es die bekannte TM2-Mischung** der Literatur zu A₄ (keine neue Vorhersage der Struktur, aber die Struktur liefert die Gruppe und die Regel). Sie
   legt sin²θ₁₂ ≈ 0.341 fest; das liegt im NuFIT-3σ-Bereich, aber JUNO (2025) liegt 3.6 σ darunter. θ₂₃ bleibt frei.
3. Nach dem Kriterium eine Anpassung mit einem Winkel; inhaltlich die erste Lesart, die die Größenordnung beider Mischungen richtig ordnet. Die scharfe Aussage
   (θ₁₂) steht unter Druck durch JUNO. Korrekturen (etwa aus der Maske) könnten θ₁₂ senken; das wäre ein eigener Test.
