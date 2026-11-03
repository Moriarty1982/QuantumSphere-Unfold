# Erkundung: Spencer-Kohomologie des ϑ-geeichten Symbols (Abschätzung zu H53)

Stand: 3. November 2026. Erkundung ohne Vorab-Notiz. Skript `k141_spencer_geeicht.py` (Symbol aus J, θ und Eichzeile
w; nur Symbolränge, keine Linearisierung). Betrifft nur das OP5-Vergleichsmodell.

## Frage

H53 ließ offen, ob die 4 zusätzlichen Bedingungen an 6-Jets in F₈ (P₅₆ = 848 statt 852) echt sind oder ein Artefakt
der ungenauen Grad-3-Linearisierung. Hindernisse gegen die Fortsetzung von Jets liegen in der Spencer-Kohomologie
H^{k,2} des Symbols. Ihre Dimension ist eine Obergrenze für die Zahl solcher Bedingungen.

## Ergebnis

H^{k,2} = dim ker(δ: g_k ⊗ Λ² → S^{k−1} ⊗ Λ³) − rang(δ: g_{k+1} ⊗ Λ¹ → S^k ⊗ Λ²); alle Lücken ≥ 4e6.

| Symbol | H^{4,2} | H^{5,2} |
|---|---|---|
| ungeeicht g (Probe: Erkundung Symbolstruktur gibt 4) | 0 | 4 |
| geeicht g' | 0 | 4 |

## Lesart

- **H^{4,2}(g') = 0:** Für versteckte Bedingungen an 5-Jets ist kein Platz. Das passt zu P₅ = 371 in F₇ und F₈.
- **H^{5,2}(g') = 4:** Für versteckte Bedingungen an 6-Jets ist Platz für genau 4. Das ist die in F₈ beobachtete Zahl.
- Ein Rauschartefakt würde, wenn überhaupt, viele nahezu verschwindende Singulärwerte gleichzeitig anheben: Fehler
  in A, B vom Grad 3 treffen alle Kernvektoren mit c₅-Anteil (P₅ = 371). Beobachtet sind genau 4 Werte bei 1e-9,
  die übrigen bleiben bei 3e-14. Das spricht für echte Bedingungen.
- Die Eichung ändert H^{5,2} nicht. Die 4 Bedingungen hängen also nicht an der ϑ-Freiheit.
- Ob die 4 tatsächlich verwirklicht sind, entscheidet die Symbolrechnung nicht. Sie sagt nur, dass es höchstens 4 sein
  können. Das hängt von den Termen niederer Ordnung ab (Krümmungsabbildung R'_6 → H^{5,2}).

## Offen

Ein entscheidender Test (H54) braucht die genauere Grad-3-Linearisierung oder eine Rauschskalierung: absichtlich
eingebrachtes Rauschen der Stärke ε in A, B vom Grad 3. Bleiben die 4 Werte bei 1e-9, während die echten Nullwerte
mit ε wachsen, sind die Bedingungen echt.
