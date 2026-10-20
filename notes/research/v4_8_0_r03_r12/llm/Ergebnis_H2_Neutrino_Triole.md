# Ergebnis H2: Neutrinos als lichtartige Triole (r = 1)

Vorab-Notiz: `Vorab_Notiz_H2_Neutrino_Triole.md`, Commit 434c5a8 (2026-10-20 00:01 UTC), vor der Rechnung.
Skript: `k15_test_h2.py`. Daten und Kriterium unverändert wie festgelegt.

## Vorbefund bestätigt

Mit ausschließlich positiven Wurzeln: K = 0,585 (NO) bzw. 0,500 (IO) im hierarchischen Grenzfall, also nie 2/3.
H2 braucht ein negatives Vorzeichen.

## Lösungen

Pro Ordnung gibt es genau eine physikalische Lösung (die zwei gefundenen Phasen δ sind Spiegelbilder mit
identischen Massen). In beiden Fällen trägt die **leichteste** Komponente das negative Vorzeichen.
Kontrolle: K = 0,666667 für alle Lösungen.

| Ordnung | m_leicht | m_mittel | m_schwer | Σm_ν (MC, 1σ) | 95 %-Bereich Σ | Kriterium |
|---|---|---|---|---|---|---|
| NO | 0,00036 eV | 0,00866 eV | 0,05013 eV | 0,05916 ± 0,00023 eV | 0,0587–0,0596 eV | < 0,0642: **verträglich** |
| IO | 0,00292 eV | 0,04917 eV | 0,04993 eV | 0,10201 ± 0,00042 eV | 0,1012–0,1028 eV | > 0,0642 auch bei 2σ: **disfavorisiert** |

## Urteil nach dem festgelegten Kriterium

**H2 ist verträglich.** Festgehaltene Vorhersage:

- normale Massenordnung,
- Σm_ν = 0,0592 ± 0,0002 eV,
- m₁ ≈ 0,36 meV, m₂ ≈ 8,66 meV, m₃ ≈ 50,1 meV.

## Einordnung (ehrlich)

- Die Vorhersage ist **schwach trennend**. In normaler Ordnung liegt das Minimum von Σ bei etwa 0,0588 eV (m₁ = 0).
  H2 sagt 0,0592 eV, nur etwa 0,4 meV darüber. Jedes Modell mit fast masselosem leichtestem Neutrino sagt
  praktisch dasselbe. Künftige Kosmologie (Empfindlichkeit etwa 0,015–0,02 eV) kann diesen Unterschied nicht
  auflösen.
- Klar prüfbar ist: **Ordnung** (JUNO, DUNE) und **Σ deutlich über 0,06 eV**. Eine invertierte Ordnung oder ein
  gemessenes Σ ≳ 0,07 eV würde H2 widerlegen. Ebenso ein kosmologisches Σ klar unter 0,058 eV, das allerdings
  auch die Standard-Oszillationsphysik in Bedrängnis brächte.
- Das Ergebnis deckt sich mit der Literatur (Brannen 2006, ähnliche Werte). Es ist **keine neue Vorhersage**,
  sondern eine unabhängige Bestätigung, dass die Triolen-Form mit r = 1 und freiem Vorzeichen auf die
  Neutrinodaten passt.
- Strukturell neu für das Projekt: Bei den geladenen Leptonen sind alle v_k positiv, bei den Neutrinos ist die
  leichteste negativ. Ob das Vorzeichen eine Bedeutung im Modell hat (z. B. Phase π im Triolenkern), ist offen.

## Status

[P] H2 verträglich, nicht bestätigt. Vorhersage gilt als festgeschrieben. Guards unberührt.
