# Vorab-Notiz H37: Kopplungen aus der Triality-Form statt zirkulanter Kopplungen

Festgelegt am 2026-10-24, **vor** der Rechnung. Autor: „mach das“ (auf den Vorschlag, die zirkulante Kopplung C durch eine Kopplung aus der Struktur zu
ersetzen, etwa aus der Triality-Form). Bezug: r37 (t(x, y, z) = Re((xy)z) ist die Spin(8)-Triality-Form, Generationen auf den Plätzen), r44 (Massenterme
tragen H- bzw. H̃-Quantenzahlen), r47 (Maske), r50/r52 (H34, H36: zirkulante C mit Maske widerlegt), r51 (Tachyon-Abbildung lässt Sektoren fest, Zeitumkehr T
tauscht sie).

## Kopplungen aus der Struktur (Lesarten, nicht hergeleitet)

Die Triality-Form koppelt nur **verschiedene** Plätze. Eine Yukawa-artige Kopplung zweier Generationen mit einem Higgs-Wert v_k im dritten Platz ist dann
T(v) = [[0, v₃, v₂], [v₃, 0, v₁], [v₂, v₁, 0]], v reell (die Form ist reell). Die zweite Invariante der Struktur ist die Norm je Platz; sie gibt einen für alle
Plätze gleichen Diagonalteil α·1. Massen = Beträge der Eigenwerte, Mischung aus den Eigenvektoren (nach Masse geordnet).

## Offenlegung (vorab analytisch gesehen bzw. grob abgeschätzt)

T(v) ist spurfrei, also auch D T(v) D; die vorzeichenbehafteten Eigenwerte summieren sich zu null, das verlangt für die Beträge m₃ = m₁ + m₂. Für die geladenen
Sektoren offensichtlich falsch. Für Dirac-Neutrinos (normale Ordnung) gibt es genau ein m₁* mit m₃ = m₁ + m₂; grob geschätzt m₁* ≈ 0.035 eV, also Σm um 0.12 eV.
Die Spektren von α·1 + T(v) hängen nur von α, Σv² und v₁v₂v₃ ab; nach Anpassung der Massen bleibt je Sektor eine Kurve von Lösungen (ein freier Parameter).

## Daten

Wie H34/H36 (Massen bei M_Z nach Huang/Zhou 2021, NuFIT 6.0 normale Ordnung, PDG 2024, m₁ ∈ {0, 0.001, 0.003, 0.01, 0.02, 0.05, 0.1} eV), dazu
Σm_ν < 0.0642 eV (95 %, DESI DR2 BAO + CMB, arXiv:2503.14744).

## Hypothesen

- **H37a (reine Triality-Kopplung):** Mit C = T(v) (mit oder ohne Maske in Form K) lassen sich die Massen von u, d, e nicht darstellen (m₃ = m₁ + m₂ verletzt).
  Für Dirac-Neutrinos gibt es genau ein m₁*; dort liegt Σm **unter** 0.0642 eV.
- **H37b (Norm + Triality, ohne Maske):** C = α·1 + T(v), ε = 0. Über die Lösungskurven von u und d (je 2000 Punkte, alle Vorzeichenwahlen) gibt es Paare mit
  |V_us|, |V_cb|, |V_ub| innerhalb ±20 %; Anteil wird mitberichtet. Ebenso für e und ν (für ein m₁ der Liste) mit allen drei PMNS-Größen in den 3σ-Bereichen.
- **H37c (H/H̃-Lesart der zirkulanten Kopplung):** Zirkulantes C mit Maske wie in H36, aber Sektoren mit H̃ (u, ν) in der einen und mit H (d, e) in der anderen
  Form, weil H̃ eine Konjugation mehr enthält. Beide Zuordnungen (u, ν in S und d, e in K; und umgekehrt) werden gerechnet, ein gemeinsames ε, Kriterien wie
  H36a/b. Bestätigt, wenn eine der beiden Zuordnungen beide Kriterien erfüllt (die doppelte Wahl wird mitberichtet).

## Entscheidungskriterium (verbindlich)

- H37a: der Teil zu u, d, e ist eine Prüfung (vorab klar); zählt nur der Neutrino-Teil: Σm(m₁*) < 0.0642 eV ⇒ bestätigt, sonst widerlegt (dann ist auch die
  reine Triality-Kopplung für Neutrinos durch die Kosmologie ausgeschlossen).
- H37b bestätigt für Quarks **und** Leptonen ⇒ die beiden Invarianten der Triality-Struktur tragen Massen und Mischung, mit einem freien Parameter je Sektor
  (zwei freie für drei Winkel: eine Vorhersage je Sektor). Nur Quarks oder nur Leptonen ⇒ Teilbefund. Großer Anteil passender Paare ⇒ schwacher Befund.
- H37c bestätigt ⇒ die H/H̃-Lesart mit einem ε erklärt beide Mischungen; widerlegt ⇒ auch sie nicht.

Nach dem Commit dieser Notiz wird daran nichts mehr geändert.
