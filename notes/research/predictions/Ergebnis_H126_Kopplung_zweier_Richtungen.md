# Ergebnis H126: nicht prüfbar. Die Konstruktion ist überall entartet, und die Nicht-Assoziativität trägt exakt nichts bei

Vorab-Notiz: `Vorab_Notiz_H126_Kopplung_zweier_Richtungen.md`, Commit 0a1bd3aa (24.11.2026, 10:54 UTC), vor der Rechnung. Skripte unter `../hilbert_shift_felder_2026_11_24/h126/`: `k257_test_h126.py`,
Ausgabe `k257_out.txt`; Wolfram-Kontrolle `k257b_wolfram.wl` (`k257b_out.txt`); Nachkontrolle `k257_nachkontrolle.py` (`k257_nachkontrolle_out.txt`,
nach der Auswertung, kein Kriterium). Verfahren und Kriterium unverändert.

## Stufe A (Strukturprüfung)
| Prüfung | Ergebnis |
|---|---|
| A1 Entartung von H = MM† | **überall entartet**: 16 380 von 16 380 Gitterpunkten. Wolfram exakt: Eigenwerte {0, 2cos²χ, 2cos²χ} für alle χ, δ_ν |
| A2 Grenzfälle χ = 0, 180° | Eigenwerte {0, 2, 2}; die Spalte zum Eigenwert 0 hat \|U\|² = (⅓, ⅓, ⅓), der Rest ist durch die Entartung unbestimmt |
| A3 Nicht-Assoziativität | **exakt null**: Wolfram symbolisch M − M_assoz ≡ 0. Numerisch ≤ 10⁻¹⁶ außer bei χ = 90°, wo M selbst verschwindet (0/0) |

## Urteil nach dem festgelegten Kriterium
Die Vorab-Notiz sagt: „Gilt A1 überall entartet oder A3 null, wird Stufe B nicht gewertet, und H126 ist ‚nicht prüfbar‘.“ Beides trifft zu.
**H126 ist nicht prüfbar.** Stufe B wurde gerechnet, zählt aber nicht. Das Minimum χ² = 858 (sin²θ₁₂ = 0,66) ist ein Artefakt der willkürlichen
Basis im entarteten Eigenraum.

## Warum (Lesart, nach der Auswertung)
- Das Skalarprodukt ⟨x, y⟩_ℂ liest nur die Komponenten bei 1 und e₈. Mit e₈ als i ist V_w ein **zweidimensionaler komplexer Raum** (k255:
  komplexe Gram-Matrix vom Rang 2). M hat deshalb höchstens Rang 2, und ein Eigenwert ist immer 0.
- Auf diesem Raum wirkt Ψ_ν(Ψ_ν ·) wie eine Drehung mal cos χ (Eigenwerte 2cos²χ doppelt). Das ist ein Vielfaches einer unitären Abbildung und
  hat keine bevorzugte Basis. δ_ν geht nicht ein.
- Der Assoziator von Ψ_ν, Ψ_ν, g_k fällt ganz aus den gelesenen Komponenten (1, e₈) heraus. Die Nicht-Assoziativität, die der Test nutzen
  sollte, sieht diese Lesart gar nicht.

## Einordnung
- Gescheitert ist die Konstruktion, nicht die Idee. Mit e₈ als i und einer Paarung, die nur 1 und e₈ liest, kann keine nicht-assoziative
  Kopplung sichtbar werden. Ein neuer Versuch bräuchte eine Lesart, die Komponenten außerhalb von span{1, e₈} auswertet, also eine andere
  Paarung oder einen anderen Massenoperator. Das wäre eine neue Hypothese mit neuer Nummer und eigener Vorab-Notiz.
- Bestätigt ist nebenbei die Zwei-Generationen-Struktur aus r13: Unter e₈ als i trägt jedes V_w nur zwei komplexe Zustände. Der dritte ist der
  Nullraum.
- OP3/OP4 offen; kein Guard berührt; H8, H125 unberührt.
