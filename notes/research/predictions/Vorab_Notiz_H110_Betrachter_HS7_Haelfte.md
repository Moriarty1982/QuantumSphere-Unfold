# Vorab-Notiz H110: Legt der Zustand der HS(7)-Hälfte {Betrachter, F} die Biegung fest?

Festgelegt am 2026-11-16, **vor** der Rechnung. Auftrag des Autors: „HS(7)-Hälfte für λ“, nach den Erkundungen
`../op3_frame_algebras_observer_2026_11_16/` (Idee des Autors: Algebra je Frame, Kopie 00 als Betrachter; Aufteilung HS(8) = HS(7) + HS(6) + HS(6)).
Einordnung OP3, r16.7, r25, H106–H109. Skript `k232_test_h110.py` (nach dieser Notiz geschrieben, ausgeführt erst nach dem Commit).

## Anlass
Die Kopien von HS(8) sind die Kleinsche Vierergruppe {1, R, T, J_B}; Kopie 00 ist der Betrachter, die Frame-Kopien tragen die Auslesungen
$e_F$ (Eigenzustände von $F$ auf $\chi$, der Oktant mit Phase $\pi/4$). Eine reine Lesart ist starr. Gemischte Auslesungen biegen die Phase; $K=2/3$
in der Frame-Operator-Lesart hält nur eine Dephasierung um die Zyklusachse (Nachtrag der Erkundung, nötig $\kappa=0{,}938459$). Die Aufteilung
7+6+6 des Autors setzt den Betrachter mit genau einer Frame-Kopie in eine HS(7)-Hälfte; dort können beide verschränkt sein.

## Vorwissen geprüft
- `../op3_frame_algebras_observer_2026_11_16/` (mit Nachtrag): Kleinsche Vierergruppe, Starrheit reiner Lesarten, $K=(9+|R|^2)/18$, Dephasierung.
- `../op3_dixon_times_sedenions_2026_11_16/`: Kopienregister von HS(8) = zweites H.
- `Ergebnis_H107_*`: Aufteilung 7+6+6 mit Generationen in den Kopien (anderer Gegenstand), widerlegt.
- `Ergebnis_H108_*`: Majorana-Paare im Kopienregister, Bezugspunkt am Pol der Zyklusachse → flacher Oktant (andere Rollen der Kopien).
- `Ergebnis_H109_*`: Drehungen lassen die Phase stehen.
- r25/r26: Zwei Kopien in HS(7) bilden Triplett ⊕ Singulett unter Kopientausch.
- **Vorab gesehen und nicht gezählt:** Betrachterzustände $o$, $Fo$ als Aufzeichnung geben $\kappa=1/\sqrt3$, Phase 0,197 (Nachtrag der Erkundung).

## Festgelegte Familie
Betrachter $o$ = kohärenter Zustand auf der Zyklusachse, Vorzeichen $s\in\{+n,-n\}$ (die einzigen generationssymmetrischen reinen Betrachter).
Auslesungen $e_k$ = +1-Eigenzustände von $R=\sigma_z$, $T=\sigma_x$, $J_B=\sigma_y$.

**Zustand der HS(7)-Hälfte {1, F}:** das Majorana-Paar unter Kopientausch, also der Triplett-Zustand aus r25/r26 mit den beiden Punkten $e_F$ und $o$:
$|\Phi_F\rangle\propto|e_F\rangle|o\rangle+|o\rangle|e_F\rangle$. Die Auslesung, die der Betrachter sieht, ist der reduzierte Zustand
$\rho_F=\operatorname{Tr}_{\rm Betrachter}|\Phi_F\rangle\langle\Phi_F|$.

**Aufteilung (wer sitzt beim Betrachter):**

| Variante | Auslesungen |
|---|---|
| A (7+6+6 wörtlich) | eine Frame-Kopie ($R$) beim Betrachter: $\rho_R$; die beiden anderen rein |
| B (jede gepaart) | alle drei $\rho_k$ aus ihrem eigenen Paar |
| C (Mittel über die drei Aufteilungen) | $\rho_k=\tfrac13\rho_k^{\rm Paar}+\tfrac23|e_k\rangle\langle e_k|$ |

Das ergibt **6 Versuche** (3 Varianten × 2 Vorzeichen). Bei A wird zur Kontrolle geprüft, dass $T$ oder $J_B$ statt $R$ dieselben Werte gibt (nicht
gezählt). Kontrollen ohne Zählung: Singulett statt Triplett (erwartet vollständig gemischt) und $o$ statt Paar (rein, $\pi/4$).

Vorhersagen je Versuch: Phase $\varphi=|\arg\operatorname{Tr}(\rho_0\rho_1\rho_2)|$ und $K=\operatorname{Tr}S^2/(\operatorname{Tr}S)^2$ mit $S=\sum\rho_k$.

## Entscheidungskriterium (vor der Rechnung festgelegt)
- Treffer: $|\varphi-0{,}666665|\le0{,}0002$ **und** $|K-2/3|\le0{,}001$.
- **bestätigt**, wenn genau ein Versuch trifft; **mehrdeutig** bei mehr als einem; **widerlegt** bei keinem.
- Zufallserwartung, vorab geschätzt: 6 Versuche, je etwa 0,7 % für die Phase, $K$ zusätzlich einschränkend, zusammen höchstens etwa 0,04.

## Offenlegung
- Der Zielwert war bekannt, auch der nötige Kohärenzfaktor $\kappa=0{,}938459$. Blind ist der Test nur in der Konstruktion, nicht im Zahlenwert.
- Die Wahl des Triplett-Paars als Zustand der HS(7)-Hälfte stützt sich auf die Kopientausch-Regel aus r25/r26; andere verschränkte Zustände
  (mit freien Parametern) werden nicht geprüft. Ein Kandidat ($o$, $Fo$) ist vorab gesehen und nicht gezählt.
- Die Frame-Operator-Lesart von $K$ ist eine Setzung (die natürliche Fortsetzung der Gram-Lesart; begründet im Nachtrag der Erkundung).

## Ablauf
1. Diese Notiz und das Skript committen.
2. `k232_test_h110.py` ausführen (Ausgabe `k232_out.txt`).
3. Ergebnis-Notiz `Ergebnis_H110_Betrachter_HS7_Haelfte.md`.
