# Ergebnis H172: Für Quarks gilt die Zuordnung Ladung ↔ Phasenlage nicht

**Stand:** 26.11.2026. Vorab-Notiz `Vorab_Notiz_H172_Quarks_Phase_und_Ladung.md` (Commit dbc30d1, vor der Rechnung). **Nicht blind bezüglich der Daten** (die
Quark-Phasen standen seit H1 im Repo; Erwartung „widerlegt“ war vorab notiert). Die Regel war festgelegt und wurde nicht angepasst. Skripte k367 (Python,
10⁶ Ziehungen, Seed 20261126) und k367b (Wolfram, Zentralwerte). Zentralwerte stimmen überein. Qiskit nicht eingesetzt.

**Ergebnis in einem Satz:** Die Regel χ(Q) = |Q|·π/4 mit dem Versatz x sagt für Down-Quarks δ nahe π/12 und für Up-Quarks δ nahe 0 oder π/6 voraus; gemessen
sind δ_d = 0,100 und δ_u = 0,052 (bei M_Z), in allen Varianten mindestens 25σ neben jedem Kandidaten. **H172a ist widerlegt.**

## Ergebnisse gegen die Kriterien
| Teil | Befund | Kriterium | Urteil |
|---|---|---|---|
| H172a, Down (\|Q\| = ⅓) | δ = 0,100129 ± 0,000953 (M_Z), 0,110119 ± 0,000424 (Standardskalen). Nächster Kandidat π/12 − x = 0,222222: −128σ bzw. −265σ. Mit negativer leichtester Wurzel δ = 0,152 bzw. 0,167: −71σ bzw. −133σ | primär kein Kandidat < 5σ | **widerlegt** |
| H172a, Up (\|Q\| = ⅔) | δ = 0,051806 ± 0,000483 (M_Z), 0,074555 ± 0,000183 (Standardskalen). Nächster Kandidat x = 0,039577: +25σ bzw. +191σ. Mit negativer Wurzel +35σ bzw. +212σ | primär kein Kandidat < 5σ | **widerlegt** |
| H172b | Leptonen: K − ⅔ = −2,2·10⁻⁶ (σ 5·10⁻⁶), δ − δ* = +2,7·10⁻⁶ (σ 6·10⁻⁶) | 10⁻⁵, 10⁻⁶ | K **erfüllt**; δ **knapp verfehlt** (2,7·10⁻⁶ statt 10⁻⁶), innerhalb 0,4σ des m_τ-Fehlers. Die Schranke war zu eng gesetzt, weil hier m_τ eingeht |
| H172c | δ wächst von M_Z zu den Standardskalen um 0,010 (Down) und 0,023 (Up). K_u = 0,888 / 0,849, K_d = 0,748 / 0,731. δ + x = 0,140 / 0,150 (Down), 0,091 / 0,114 (Up), gegen die Regelwerte 0,262 und 0,524 | Bericht | – |

## Lesart
- **Was widerlegt ist.** Die Ausdehnung der Lesart aus H168 bis H171 auf Quarks: Die Phasenlage folgt nicht linear der elektrischen Ladung. Die Quark-Phasen
  liegen nicht einmal in der Reihenfolge der Regel: Sie sind beide klein, und der Up-Typ (größere Ladung) hat die kleinere Phase.
- **Was nicht berührt ist.** Für Leptonen bleibt „neutral gegen geladen = Realteil gegen Imaginärteil“ eine Lesart unter H99. Der Test sagt nur, dass die Größe,
  die zwischen den beiden Lepton-Sektoren umschaltet, nicht |Q| mit linearem Gesetz ist. Bei den Leptonen unterscheiden sich die Sektoren in mehr als der Ladung
  (schwacher Isospin; Majorana- gegen Dirac-Charakter), und dafür sind die Quarks kein Prüfstein: Beide Quarktypen sind geladen und Dirac.
- **Zwei Einschränkungen des Tests.** Erstens setzt die Regel K = ⅔ voraus (Postulat J), und für Quarks ist K = 0,73 bis 0,89; die Brannen-Form mit festem K
  gilt dort nicht (H1). Zweitens hängt δ bei Quarks deutlich von der Skala ab (Up: 0,052 → 0,075), so dass kein scharfer Wert existiert. Beides ändert das
  Urteil nicht: Die Abstände sind ein Vielfaches der Skalenabhängigkeit.
- **Mögliche engere Lesart (nicht geprüft, nachträglich):** Die Achteldrehung könnte am Unterschied „eigenes Antiteilchen oder nicht“ hängen (σ als
  Ladungskonjugation, H169) statt an der Größe der Ladung. Dann wären alle geladenen Sektoren vom Typ c = 1, und die Quarks müssten wie die geladenen Leptonen
  bei π/12 − x liegen. Das ist für Down bereits oben mitgeprüft (−128σ) und für Up durch δ_u = 0,052 ebenfalls ausgeschlossen. Auch diese Lesart trägt also
  für Quarks nicht, solange K frei ist.

## Bilanz der Setzungen
| Schritt | gesetzt | hergeleitet | wohin die offene Wahl gewandert ist |
|---|---|---|---|
| H167 bis H171 | Skala, J, c = 1, H99 | Sektorschritt = Achteldrehung; Projektor = Lichtkegel; zwei Tauschsymmetrien | warum Cσ im geladenen Sektor; Versatz x |
| H172 | Regel χ = \|Q\|π/4 für Quarks | nichts: von den Daten widerlegt | die Quarks folgen der Lepton-Struktur weder in K noch in δ |

Der Befund trifft das Ziel selbst: K = ⅔ und δ ≈ 2/9 sind Eigenschaften der Leptonen, nicht der Dreiergruppen (das stand seit H1 fest). Eine Herleitung der
Lepton-Phase muss also erklären, warum sie für Quarks **nicht** gilt. Kandidat aus dem Projekt: Farbe (H127: Quarks bei exakter A₄ entartet; H125: Leptonen
und Quarks mit entgegengesetzter Orientierung). Das ist eine Frage für den Autor, kein Ergebnis.

## Grenzen
- Daten und Fehler aus k14 (H1) übernommen, nicht neu recherchiert. Massen bei M_Z aus der dort benutzten Tabelle.
- Nur die Phase geprüft. Kein Vorzeichen gesetzt; kein Guard berührt; OP3 und OP4 offen.
- Vergeben: H172, k367. Nächste frei: H173, k368.
