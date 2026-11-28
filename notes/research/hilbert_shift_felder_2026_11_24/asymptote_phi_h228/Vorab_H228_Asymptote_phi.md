# Vorab-Notiz H228 (k442): φ als Asymptote

Stand 28.11.2026, vor der Rechnung festgeschrieben. Der Autor hat gefragt: „was wäre wenn du das als asymptote behandelst?“ (11:41 UTC) und auf
der Entscheidungskarte „Beides rechnen“ gewählt (11:42 UTC). Gerechnet werden also zwei Lesarten.

- **Teil A, Grenzwert einer Schleife:** φ ist der anziehende Fixpunkt einer iterierten Abbildung aus Operationen des Rahmens, so wie H215
  es für β_sym geprüft hat.
- **Teil B, Zwischenstand auf dem Fluss:** φ ist kein Endpunkt, sondern der Stand des Gradientenflusses der gemeinsamen Vakuumenergie (H225)
  auf dem Weg von 0 zum Minimum π/8, abgelesen zu einer natürlichen Uhrzeit. Ohne vorab festgelegte Uhr gibt es keinen Test.

Ziel: φ = x = π/12 − δ*_Im = 0,0395773407, σ_φ = 7,8·10⁻⁷ (H221/H225). Der gemeinsame Versatz gilt für beide Lepton-Sektoren (H213:
x_ν = 0,04336 ± 0,00213 ist verträglich), getestet wird daher nur x.

## Vorwissen geprüft

- H215/k428 (`stabilitaet_rueckwaerts_h215/`): Schleifensuche für β_sym, 9 Operationen, Länge ≤ 5, widerlegt; Methode und Kontrollen
  werden hier übernommen. H216–H220: Umkehrschleifen, Flächenvarianten, χ/Λ und Endzahlen tragen nicht.
- H221/k434: Der gemeinsame Versatz ist ein Winkel, keine Skala. H222/k435, k436, H223/k437: Zweigwahl skalenfrei, Vorzeichen gesetzt.
- H224/k438: φ als Wigner-Drehung, kein Treffer (nächster 118σ). Wigner-Winkel kommen deshalb hier nicht in die Operationsklasse.
- H225/k439: E(φ) = −2 + q·S(φ) in führender Ordnung, S = |cos(π/4 − 3φ)| + |sin 3φ|, q < 0 gesetzt; Minimum genau π/8,
  Sektortausch V_Re(−δ; π/4 − φ) = V_Im(δ; φ) exakt. H226/k440: Tauschbruch widerlegt. H227/k441: Massenbilanz, φ bleibt Messzahl.
- r73 (PR #412): fasst H213–H227 zusammen.

## Teil A: Schleifenklasse (fest)

Bereich θ ∈ [0, π/4]. Faltung F: y ↦ y mod π/2, danach π/2 − y, falls y > π/4 (Diedergruppe des Quadrats; gesetzt, weil die
Sektorpotentiale in 2δ mit Versatz π/4 laufen). Zehn Grundoperationen:

| Zeichen | Abbildung | Herkunft |
|---|---|---|
| h | θ ↦ θ/2 | halber Winkel |
| d | θ ↦ F(2θ) | Doppelwinkel |
| s | θ ↦ θ/3 | Generationsdrittel |
| t | θ ↦ F(3θ) | kubische Invariante cos 3δ (H222) |
| X | θ ↦ π/4 − θ | Sektortausch (H225) |
| Y | θ ↦ F(π/12 − θ) | Im-Phase δ_Im = π/12 − φ |
| Z | θ ↦ F(π/6 − θ) | Re-Phase δ_Re = π/6 − φ |
| B | θ ↦ arctan(β_sym tan θ) | Maske tanh ε = β_sym (H45) |
| U | θ ↦ F(arctan(tan θ / β_sym)) | Umkehrung von B |
| G | θ ↦ arctan(tan θ / γ_L) | Winkelkontraktion im Materie-Frame |

β_sym = 0,549405640974529, γ_L = 1,864699764609373 (r67). Schleifen sind alle Wörter der Länge 1 bis 5 (111 110 Wörter). Wörter mit
Identitätsanteil > 1 % auf dem Gitter werden ausgeschlossen. Fixpunkte über Gitter (8001 Punkte) und Bisektion, anziehend heißt |f′| < 1.

**Fenster:** Trefferfenster W₂ = x ± 2σ_φ = ± 1,56·10⁻⁶. Häufungsfenster W_c = x · (1 ± 10⁻³).

**Kontrollen:** 2000 Zufallswerte gleichverteilt in [0,02; 0,06] (Startwert des Generators 228), gleiche Fensterbreiten.

**Kriterium Teil A:**
- *trägt:* mindestens ein anziehender Fixpunkt in W₂, und die Poisson-Wahrscheinlichkeit, so viele Treffer in W₂ zufällig zu erhalten
  (Erwartung aus der mittleren Dichte der Kontrollen), ist < 1 %.
- *trägt teilweise:* kein Treffer mit dieser Signifikanz, aber die Zahl N_c(x) in W_c liegt über dem 99. Perzentil der Kontrollen.
- *widerlegt:* sonst.

Hinweis vorab: Wörter nur aus h, d, s, t, X, Y, Z sind stückweise linear; ihre Fixpunkte sind rationale Vielfache von π. Ein Treffer
solcher Wörter wird getrennt ausgewiesen.

## Teil B: Fluss und Uhr (fest, ausdrücklich nicht blind)

Führende Ordnung (H225): Für 0 < φ < π/4 ist S = 2 cos(π/8) cos(3(φ − π/8)). Der Gradientenfluss dφ/dt = −dE/dφ hat mit u = π/8 − φ
die Form du/dt = −k sin 3u, k = 6|q| cos(π/8). Mit der Relaxationszeit am Minimum τ = 1/(3k) folgt geschlossen

  φ(t) = π/8 − (2/3) arctan( tan(3π/16) · e^(−t/τ) ),  φ(0) = 0.

q fällt in der Einheit τ heraus. φ = 0 ist ein Knick von S (|sin 3φ|), kein stationärer Punkt, der Fluss läuft also sofort los.

**Nicht blind:** Diese Form und der Wert t_x/τ = 0,132105 (σ_t ≈ 2,7·10⁻⁶) sind bei der Planung schon ausgerechnet worden. Ebenso fiel auf,
dass k·t_x = 3t_x/τ = 0,39632 nahe π/8 = 0,39270 liegt (0,92 %). Teil B ist deshalb eine Erkundung mit festem Kriterium, kein blinder Test.

**Uhren (fest):** Einheit τ. Kandidaten t*/τ ∈ {1, ½, ⅓, ⅛, ln 2, ε = artanh β_sym, β_sym, β_sym², 1/γ_L, 1/γ_L²}. Zusätzlich die bei der
Planung aufgefallene Lesart k·t* = π/8 (Einheit 1/k), ausgewiesen als nachträglich.

**Kriterium Teil B:** *trägt* nur, wenn eine Uhr φ(t*) innerhalb 2σ_φ trifft. *trägt teilweise* gibt es hier nicht, weil die Uhr nicht
blind gewählt ist. Sonst *widerlegt*, mit Abstand jeder Uhr in σ.

**Prüfung der Ordnung:** Mit der exakten Minimierung in δ (H225-Modell, endliches q ∈ {−0,01; −0,0852; −0,3}) wird t_x/τ numerisch
bestimmt; τ dann aus der Krümmung von E am Minimum. Weicht es von 0,132105 ab, gilt das Urteil für jedes q getrennt.

## Werkzeuge

Python `k442_test_h228.py` (numpy/mpmath, Ausgabe `k442_out.txt`) für beide Teile. Wolfram `k442b_gegenprobe.wl` (Ausgabe `k442b_out.txt`):
DSolve des Flusses und Vergleich mit der geschlossenen Form, t_x/τ, Uhren-Abstände; unabhängige Zählung der Fixpunkte für alle Wörter der
Länge ≤ 3 im Fenster W_c. Qiskit ist nicht geeignet (keine Quantenschaltung definiert).

## Gesamturteil

trägt, wenn A oder B trägt; trägt teilweise, wenn nur A teilweise trägt; sonst widerlegt. Vergeben: H228, k442.
