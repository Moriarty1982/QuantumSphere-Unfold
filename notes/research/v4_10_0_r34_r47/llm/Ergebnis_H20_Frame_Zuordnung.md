# Ergebnis H20: Die Farb- und ν_R-Zuordnung ist ein Frame-Unterschied, der Anti-Triplett-Satz eine Frame-Vermischung

Vorab-Notiz: `Vorab_Notiz_H20_Frame_Zuordnung.md`, Commit 7d95feb (2026-10-23 18:54 MESZ), vor der Rechnung.
Skript `k76_test_h20.py`, Ausgabe `k76_out.txt`. Kriterium unverändert.

## Zwei komplexe Einheiten

- **Innerer Frame:** J = L_{e₇} auf 𝕆 selbst (J² = −1). So liest der Companion `thm:octonion-SU3`.
- **Äußerer Frame:** i = ℂ-Faktor der Dixon-Ablage. So rechnet H19; erst hier gibt es den Ladungsoperator Q.

## Ergebnisse

| Hypothese | Ergebnis | Befund |
|---|---|---|
| H20a innerer Frame | **bestätigt** | Stab(e₇) ist J-linear; span(1, e₇) trivial, e₇^⊥ irreduzibel vom komplexen Typ (reeller Kommutant = ℂ); e₄, e₅, e₆ ist eine komplexe Basis, J e₄ = −e₃, J e₅ = −e₂, J e₆ = e₁ |
| H20b Anti-Triplett (e₁, e₂, e₃) | **widerlegt** | span(e₁, e₂, e₃) ist weder J-invariant noch Stab-invariant (0,41) noch Q-invariant (0,17); es ist J·span(e₄, e₅, e₆), also dasselbe Triplett mal i |
| H20c Brücke P_± = ½(1 ∓ iJ) | **bestätigt** | äquivariant, injektiv, P_±J = ±iP_±. **P₋:** e₇^⊥ → Triplett Q = 2/3, span(1, e₇) und e₇ → Singulett Q = 0. **P₊:** Triplett Q = 1/3, Singulett Q = 1. T vertauscht P₊ und P₋ |
| H20d U(1) | **bestätigt** | Q = ½ − (i/6)·L_{e₇} − (i/3)·R_{e₇} exakt; die Phase e^{iθ} des Skalars allein wirkt auf allen Sektoren gleich (trivialer Teil) |

## Einordnung

1. **Die Triplett-Basis e₄, e₅, e₆ und ν_R ↔ e₇ sind im inneren Frame richtig.** `thm:octonion-SU3` stimmt. H19c hat die
   *reellen* Vektoren als Zustände in ℂ⊗𝕆 genommen. Das ist eine Frame-Verwechslung, kein Fehler der Zuordnung. Die Übersetzung
   in den äußeren Frame ist P_±, und die Wahl des Vorzeichens (i = +J oder i = −J auf dem Bild) ist eine Frame-Wahl.
   - **Mit P₋ deckt sich die Companion-Zuordnung mit Furey:** e₇ geht in das Singulett Q = 0 (ν), e₄, e₅, e₆ in das
     Triplett Q = 2/3 (u).
   - Mit P₊ entsteht das konjugierte Bild: Q = 1 (e⁺), Triplett 1/3 (d̄).
   - Das ist genau H19d: T vertauscht P₊ und P₋, daher Q ↦ 1 − Q.
2. **Echter Fehler, durch Frame-Vermischung:** Der Satz „Anti-Triplett (e₁, e₂, e₃) trägt die konjugierte Farbdarstellung“
   (Beweis von `thm:three-generations`). Im inneren Frame gibt es nur *ein* Triplett, e₁, e₂, e₃ sind seine J-Bilder. Ein
   konjugiertes Triplett gibt es erst mit der äußeren Einheit (Bild von P₊ gegen P₋), und dann nicht auf span(e₁, e₂, e₃).
   Kleinere Unschärfe: „Im 𝕆 = ℂ ⊕ ℂ³“ ist nicht J-invariant; das Singulett ist span(1, e₇) (e₇ = J·1), als komplexe Gerade
   aber zu Recht durch e₇ benannt.
3. **`thm:SM`, U(1):** Die Ladung braucht **beide** Einheiten, die äußere i und die innere e₇, und dazu Links- und
   Rechtsmultiplikation: Q = ½ − (i/6)(L_{e₇} + 2R_{e₇}). Der komplexe Skalar it allein erzeugt nur eine globale Phase, die
   alle Zustände gleich dreht. Er ist also nicht der Elektromagnetismus. Die U(1)-Zeile ist auf einen Frame bezogen: Sie
   vermischt den äußeren Skalar mit einer Ladung, die es nur im Zusammenspiel beider Frames gibt.
4. **Bleibt unabhängig davon:** Die Doppelbelegung Gen_i ↔ e_{i+3}: Farbe und Generation auf denselben Einheiten
   (v4.8.0-r13). Sie ist kein Frame-Problem.
5. **Korrektur der Lesart von v4.9.0-r34(c):** Die Aussage selbst bleibt richtig. Die reellen Unterräume sind keine
   Eigenräume. Falsch war die Folgerung, der Companion lege Farbe und ν_R auf die falschen Unterräume. Richtig ist: Er legt sie im
   inneren Frame fest, ohne die Übersetzung P_± zu nennen.

## Regel (Vorschlag für Konvention F)

Aussagen über Farbe und Ladung nennen ihre komplexe Einheit: **innerer Frame** (J = L_{e₇}, ohne Ladung) oder **äußerer
Frame** (ℂ-Faktor, mit Q), und für die Übersetzung das Vorzeichen P₊ oder P₋.
