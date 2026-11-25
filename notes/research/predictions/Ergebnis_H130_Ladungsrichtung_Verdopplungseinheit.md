# Ergebnis H130: Die Ladungsrichtung liegt senkrecht zur Verdopplungseinheit, das Verhältnis 9/10 ist festgelegt

**25.11.2026. Vorab-Notiz `Vorab_Notiz_H130_Ladungsrichtung_Verdopplungseinheit.md` (Commit 3137c5f, 10:23 UTC, vor der Rechnung; teilweise nicht blind).
Skripte `notes/research/hilbert_shift_felder_2026_11_24/ladungsrichtung_h130/k258_test_h130.py` (Ausgabe `k258_out.txt`), `k258b_exakt.wl` (`k258b_out.txt`),
`k258c_nachkontrolle.py` (`k258c_out.txt`). Status: H130a bestätigt, H130b bestätigt.**

Werkzeuge: Python (numpy, scipy) für die Suche (kleinste Quadrate, 600 Zufallsstarts); Wolfram Language exakt für Abschluss, Alternativität und Normmultiplikativität
der gefundenen Klassen mit symbolischen Koeffizienten. Qiskit nicht eingesetzt (keine Schaltung).

## Kontrollen
| Kontrolle | Messwert | Schranke | |
|---|---|---|---|
| (i) dim su(3)_c, Singuletts, Stabilität von V | 8; genau span(1, e₇, e₈, e₁₅); Rest 1·10⁻¹⁴ | 8; Q; < 10⁻¹¹ | erfüllt |
| (ii) O_0, O_120, O_240 gefunden | Defekt 0, 2·10⁻²⁹, 1·10⁻²⁸; in der Suche 128 + 255 Treffer | < 10⁻²⁰ | erfüllt |
| (iii) Wolfram exakt | alle fünf Klassen nachgerechnet (unten) | | erfüllt |

Offengelegt: Eine der 600 Lösungen (Klasse O_0) meldete zwei flache Richtungen. Die Nachkontrolle an den exakten Punkten (k258c) gibt 0 flache Richtungen für
O_0, O_120 und B_+; der Ausreißer kam von nicht normierten Parametern in der Differenzenbildung. Ein erster Wolfram-Aufruf scheiterte an einem Tippfehler und rechnete nichts.

## Ergebnis
Alle 600 Starts enden in einer abgeschlossenen, farbstabilen Unteralgebra. Es gibt genau drei Klassen:

| Klasse | u (Ladungsrichtung) | u₈² | Treffer | alternativ, normmultiplikativ (Wolfram) |
|---|---|---|---|---|
| O_0 | e₇ | 0 | 128 | ja, ja |
| O_120, O_240 | −½e₇ ± (√3/2)e₁₅ | 0 | 255 | ja, ja |
| B_± | e₈, V = {x ± (e₇x)e₈} | 1 | 217 | **nein, nein** (12 Alternator-Komponenten ≠ 0) |

| Teil | Messwert | Kriterium | Entscheidung |
|---|---|---|---|
| H130a | oktonionische Lösungen nur bei u₈² = 0; keine flache Richtung (k258c) | ≤ 6 Werte, keine Schar | **bestätigt** |
| H130b | u₈² = 0,000000 in 383 von 383 oktonionischen Lösungen | u₈² < 10⁻⁸ | **bestätigt** |

## Warum es trägt
- Verlangt man, dass eine Generation in 𝕊 so gebaut werden kann wie bei HS(3), also mit einer Ladungsrichtung u und einem oktonionischen Träger, auf dem die Farbe als
  1 ⊕ 1 ⊕ 3 ⊕ 3̄ wirkt, dann bleiben genau die drei Oktonion-Kopien aus k254. Sie gehen durch die S₃ ineinander über, und in allen ist u₈ = 0.
- Der Hinweis aus der Vorab-Notiz traf halb zu: Bei u = e₈ gibt es tatsächlich abgeschlossene farbstabile Algebren B_±. Sie sind aber weder alternativ noch
  normmultiplikativ, also kein Träger im Sinn von HS(3). Zwischen 0 und 1 gibt es keinen Wert von u₈².

## Lesart
- **Zusammen mit H128:** Der Schritt 𝕆 → 𝕊 lässt G₂ × SU(3) übrig, die SU(3) hängt an e₈. Eine Generation verlangt eine Ladungsrichtung senkrecht zu e₈. Damit ist
  SU(3) → SO(3) erzwungen, und das Massenverhältnis von Spin 1 zu Spin 2 in der Form K ist **9/10, ohne Wahl von u**. Welche der drei Kopien gewählt wird, ist für das
  Verhältnis gleich (S₃ ist Symmetrie).
- **Nachträglich bemerkt:** Die Ladung, die die Farbe auswählt (G₂ → SU(3)_c), und die Brechung der Familiensymmetrie (SU(3) → SO(3)) hängen an derselben Bedingung
  u ≠ ±e₈. Für u = e₈ wäre die Familien-SU(3) ungebrochen, es gäbe dann aber keinen oktonionischen Träger.
- **Grenzen:** Gesetzt bleiben die Forderung „Generation wie bei HS(3)“, die Form K und ihr Vorzeichen im Potential (offen bis zur Feldgleichung, H128). Gesucht wurde
  in der vorab festgelegten Parametrisierung; Vollständigkeit beruht auf 600 Zufallsstarts, nicht auf einem Beweis. Nicht gezeigt ist, dass die Plätze Generationen sind.
  OP3 und OP4 bleiben offen, kein Guard ist berührt.
- **Mögliche nächste Frage (nur mit neuer Vorab-Notiz):** Tragen die drei Kopien O_0, O_120, O_240 selbst eine Dreierstruktur für das Feld (drei Ladungsrichtungen im
  Winkel von 120°), und was macht die Form K daraus?
