# OP3: Schließungsklasse und geometrische Verzerrung

Analytische Erkundung, 10. November 2026. Das Modell prüft, was aus den formalen Eigenschaften einer Verfeinerung allein folgt.

Auf der euklidischen Ebene sei die Modell-Schließungsklasse durch `K_cl(x,y) = y` gegeben. Für jeden reellen Parameter `a` setze

```text
J(x,y)   = (x,-y)
F_a(x,y) = (-x+a y²,y).
```

Direkt durch Einsetzen gilt: `J` ist eine orthogonale Involution, `F_a` ist eine Involution, `F_a J = J F_a`, und `K_cl ∘ F_a = K_cl`. Auf der sichtbaren Achse wirkt jede Variante als dieselbe Vorzeichenumkehr. Ihre Ableitung ist dort dieselbe orthogonale Spiegelung.

Am Punkt `(x,y)` ist der Scherparameter der Ableitung `b = 2ay`. Ihre Determinante ist −1, und die Spur des Produkts der transponierten Matrix mit der Matrix selbst ist `2 + b²`. Für das Singulärwertverhältnis `K ≥ 1` gilt deshalb `K + 1/K = 2 + b²`. An jedem festen Punkt mit `y ≠ 0` kann die Verzerrung durch die Wahl von `a` beliebig groß werden.

Folglich erzwingen Klassenerhaltung, J-Verträglichkeit, Involutivität und eine isometrische Wirkung samt Ableitung auf der sichtbaren Achse gemeinsam keine endliche einheitliche Verzerrungsgrenze für ein Fenster positiver Breite. Eine quantitative native Bedingung quer zur Achse wäre dafür erforderlich.

Die Modellklasse `K_cl` und das euklidische Singulärwertverhältnis sind explizite Vergleichsgrößen. Der Befund betrifft die logische Folgerung aus den genannten Eigenschaften. Die Identifikation mit der nativen Schließungsklasse und dem historischen Monitor bleibt offen. Der [OP3-Hüllensatz](../../sources/research/parts/v470/22_op_transport_arguments.tex#L491) und der [geometrische Zweischritt-Test](../../sources/research/parts/v470/19_local_op_entry.tex#L1825) verwenden diese nativen Größen.
