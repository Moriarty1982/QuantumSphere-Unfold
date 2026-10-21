# Vorab-Notiz H2: Neutrinos als lichtartige Triole (r = 1)

Festgelegt am 2026-10-20, **vor** jeder Berechnung von Neutrinomassen aus diesem Ansatz.
Diese Datei wird committet, bevor das Prüfskript läuft.

## Herkunft

Nach r11 gilt r = |c|/t = 1 (K = 2/3) exakt nur für die geladenen Leptonen mit Polmassen. Lesart B ist im Kern
elektromagnetisch (r10); Leptonen spüren keine starke Kraft. Daraus folgt die Hypothese, dass
„jeder Kern lichtartig, r = 1“ ein Prinzip für **alle Leptonen** ist. Die Neutrinos sind die Leptonen, deren
absolute Massen unbekannt sind; das macht sie zum Test.

## Offenlegung vor der Festlegung

Beim Durchdenken wurde **vor** dieser Notiz bemerkt: Mit ausschließlich positiven Wurzeln √m kann K für die
Neutrinos bei den gemessenen Massendifferenzen 2/3 nicht erreichen (hierarchischer Grenzfall K ≈ 0,59 für
normale, ≈ 0,50 für invertierte Ordnung; Annäherung an Entartung senkt K gegen 1/3). Diese Variante wäre also
ohne weitere Rechnung ausgeschlossen. Die Triolen-Form v_k = t(1 + √2 r cos(δ + 2πk/3)) erlaubt jedoch für r = 1
negative Komponenten (bis −0,414 t); die Masse ist m_k = v_k². **H2 lässt deshalb das Vorzeichen der v_k frei.**
Die Idee, Koide auf Neutrinos mit einem negativen Vorzeichen anzuwenden, ist in der Literatur nicht neu
(u. a. Brannen 2006); neu ist hier nur die Begründung aus der Triolen-Struktur und die Vorab-Festlegung.

## Hypothese

**H2:** Die drei Neutrinomassen sind m_k = t² (1 + √2 cos(δ + 2πk/3))², k = 0, 1, 2, mit t > 0 und einer Phase δ,
also eine Triole mit r = 1. t und δ werden allein aus den zwei gemessenen Massendifferenzen bestimmt.

## Daten (verbindlich)

NuFIT 6.0 (Esteban et al., JHEP 12 (2024) 216, arXiv:2410.05380), Tabelle 1, Spalte „IC24 with SK atmospheric data“:

| | Wert | 1σ |
|---|---|---|
| Δm²₂₁ | 7,49 × 10⁻⁵ eV² | ± 0,19 × 10⁻⁵ |
| Δm²₃₁ (NO) | +2,513 × 10⁻³ eV² | +0,021 / −0,019 × 10⁻³ |
| Δm²₃₂ (IO) | −2,484 × 10⁻³ eV² | ± 0,020 × 10⁻³ |

Kosmologische Vergleichsgrenze: Σm_ν < 0,0642 eV (95 %), DESI DR2 BAO + CMB (Planck, ACT), ΛCDM
(DESI Collaboration, arXiv:2503.14744).

## Verfahren (verbindlich)

- Für jede Ordnung (NO, IO) alle Lösungen (t, δ) der zwei Gleichungen suchen; sortierte Massen a < b < c:
  NO: b² − a² = Δm²₂₁, c² − a² = Δm²₃₁. IO: c² − b² = Δm²₂₁, c² − a² = |Δm²₃₂|.
- Für jede Lösung angeben: m_leicht, Σm_ν, Vorzeichenmuster der v_k.
- Unsicherheit per Monte Carlo (10⁵ Ziehungen, Gauß; asymmetrische Fehler gemittelt).

## Entscheidungskriterium (verbindlich)

- **H2 ohne Lösung** (für beide Ordnungen keine Lösung innerhalb 2σ der Eingaben): **widerlegt**.
- **H2 im Konflikt mit der Kosmologie**: Wenn jede Lösung Σm_ν > 0,0642 eV hat, auch an der 2σ-Grenze der
  Eingaben: **durch Kosmologie disfavorisiert** (nicht widerlegt, da die Grenze modellabhängig ist).
- Sonst: **verträglich**; die vorhergesagten Werte von Σm_ν und m_leicht werden als Vorhersage festgehalten
  und an künftigen Messungen (Kosmologie, KATRIN/Project 8, Ordnung durch JUNO/DUNE) geprüft.

Nach dem Commit dieser Notiz wird daran nichts mehr geändert.
