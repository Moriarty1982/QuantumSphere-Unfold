# Ergebnis H186: Kein einzelner Ladungsterm gibt den Unterschied zwischen Up und Down

**Stand:** 27.11.2026. Vorab-Notiz `Vorab_Notiz_H186_Ladungsterm_fuer_drei_Generationen.md` (Commit c8ab85d, vor der Rechnung). Skripte
`k389_test_h186.py` (`k389_out.txt`) und `k389b_gegenprobe.wl` (`k389b_out.txt`).

Werkzeuge: Python (numpy, scipy) wie k388: zweite Variation von elf Invarianten mit dem Ladungsoperator D = Q₀ − ½ auf den 36 Farbrichtungen,
Eigenwerte je Ladung und je Paar von Vakuum-Eigenrichtungen, Monte-Carlo für die Datenfehler. Wolfram Language exakt im reduzierten Modell
(Quaternion-Unteralgebra {1, U, n, Un} mit komplexen Koeffizienten, Vakuum diagonal): dieselben Formeln wie die Anpassung in Python. Qiskit nicht
eingesetzt. Warnungen in Wolfram: nur Hinweise der Auswerteumgebung.

**Ergebnis in einem Satz:** Die Terme mit dem Ladungsoperator spannen alle drei Richtungen auf (keine Vorhersage aus Symmetrie und Grad), und kein
einzelner Term trifft den gemessenen Unterschied zwischen Up und Down; der nächste liegt gut 1000σ daneben.

## Ergebnisse gegen die Kriterien
| Teil | Befund | Kriterium | Urteil |
|---|---|---|---|
| H186a | Singulärwerte 6,63; 0,64; 0,35 (relativ kleinster 5,3·10⁻²): Rang 3 | Rang 3 | **bestätigt** |
| H186b | 33 Paare (Kandidat, Lesart); kleinster größter Abstand 1018σ (c7, X = √m) | beide Verhältnisse < 3σ | **widerlegt** |

Daten (M_Z, k376), Verhältnisse r₁ = ΔX₁/ΔX₃, r₂ = ΔX₂/ΔX₃ mit ΔX = X(Up) − X(Down): für X = √m r₁ = −0,001485 ± 0,000045, r₂ = 0,049285 ± 0,000616;
für X = m r₂ = 0,0034; für X = m² r₂ = 0,000013. Die Kandidaten geben r₂ zwischen 0,67 und 1.

## Form der Verschiebungen (Python über vier Vakua; Wolfram exakt)
Frequenzquadrat der Mode zum Paar (i, j), ladungsungerader Anteil (Up − Down)/2:

| Kandidat | Verschiebung |
|---|---|
| c1 Re Tr(W̄ ∘ DW) | ⅔ |
| c2 Re Tr((W̄ ∘ DW) ∘ W_U) | ⅓(l_i + l_j) |
| c4, c5 Re Tr((W̄ ∘ DW) ∘ (W_U ∘ W̄_U)), Re Tr((W̄ ∘ DW) ∘ W_U²) | ⅓(l_i² + l_j²) |
| c7, c9 Re Tr((W̄ ∘ W_U) ∘ (DW ∘ W̄_U)) und gespiegelt | ⅙(l_i + l_j)² |
| c11 Re Tr((W̄ ∘ DW) ∘ (W ∘ W̄)) | ½(l_i² + l_j²) + ⅓ l_i l_j (dazu ein ladungsmischender Anteil) |
| c3, c6, c8, c10 (Imaginärteile) | 0 |

Der ladungsgerade Anteil aller Kandidaten ist null: Die Terme mit D wirken rein als Unterschied zwischen den Ladungen.

## Lesart
- **Woran es scheitert.** Jede Verschiebung hängt nur an den zwei Eigenwerten (l_i, l_j) des Paars und ist in ihnen symmetrisch. Die zwei Moden,
  die die schwerste Vakuumrichtung enthalten, sind deshalb fast gleich schwer (r₂ nahe 1), die Daten verlangen r₂ ≈ 0,05. Eine Hierarchie wie bei
  den Quarks gibt unter den symmetrischen Funktionen nur das Produkt l_i l_j.
- **Keine Vorhersage aus der Symmetrie.** Mit drei unabhängigen Richtungen lässt sich jeder Unterschied einstellen (zwei freie Verhältnisse von
  Koeffizienten).
- **Die Zuordnung der Generationen ändert nichts** (nachträglich): Für die anderen fünf Zuordnungen ist der kleinste Abstand größer (ab 1638σ).

## Zusatz (nachträglich, Erkundung): wo die Daten im erlaubten Raum liegen
In der Basis 1, (l_i + l_j), l_i l_j ist der gemessene Unterschied, auf die dritte Generation normiert:
- X = √m: −0,0178 · 1 − 0,0017 · (l_i + l_j) + 0,7408 · l_i l_j
- X = m: +0,0001 · 1 − 0,0299 · (l_i + l_j) + 0,7884 · l_i l_j
- X = m²: +0,0013 · 1 − 0,0319 · (l_i + l_j) + 0,7919 · l_i l_j

Der Unterschied liegt in allen drei Lesarten fast ganz auf dem Produkt l_i l_j der zwei Lepton-Eigenwerte des Paars. Das reine Produkt
(= 3·c7 − 1,5·c4) gibt r₁ = +0,0170, r₂ = +0,0695 gegen −0,0015 und 0,0493 der Daten (X = √m): r₂ 1,41-fach, r₁ mit falschem Vorzeichen, nach σ weit
daneben (413σ, 33σ). Das ist **kein Treffer**, sondern ein Hinweis auf die Form: Wenn ein Term den Unterschied trägt, dann einer, der die zwei
Vakuum-Eigenwerte multipliziert (im Albert-Rahmen: die Adjunkte W^# oder die Determinante), nicht einer aus Potenzen der Spur. Nachträglich gefunden,
an denselben Daten abgelesen; als Hypothese nur mit eigener Vorab-Notiz prüfbar.

## Bilanz der Setzungen
| | gesetzt | hergeleitet | offene Wahl wandert nach |
|---|---|---|---|
| Träger, Vakuum | wie H185; Farbphase als Symmetrie | – | Grund für die Farbphase |
| Ladungsterm | elf Kandidaten bis Grad 4 mit einem D | Verschiebungen als Funktionen von (l_i, l_j); Rang 3 | Koeffizienten (zwei Verhältnisse frei) |
| Zuordnung | Paar ↔ Generation nach l_i + l_j | andere Zuordnungen schlechter (nachträglich) | – |
| Frequenz ↔ Masse | X = √m, m, m² als Lesarten | – | welche Lesart gilt |

## Grenzen
Kandidatenliste nicht vollständig (insbesondere keine Terme mit der Adjunkten oder der Determinante und keine mit zwei D); ladungsgerader Anteil
frei und nicht geprüft; Massen bei M_Z ohne Laufen; Grad ≤ 4, ohne Ableitungsterme. Kein Vorzeichen gesetzt. OP3 und OP4 bleiben offen.

## Nächster Schritt (Vorschlag)
Terme mit der Adjunkten W^# (Freudenthal-Produkt) und der Determinante der Albert-Algebra als Kandidaten festschreiben und mit Vorab-Notiz gegen
dieselben Daten prüfen, zusammen mit dem ladungsgeraden Anteil (sechs Massen statt nur der Unterschied). Vergeben: H186, k389. Nächste frei: H187, k390.
