# Ergebnis H194: Die H188-Form teilt keine Gestalt zwischen den Sektoren, aber die leptonischen l_k sind spezifisch (Test, k402, 27.11.2026)

**Status:** Test mit Vorab-Notiz (`notes/research/predictions/Vorab_Notiz_H194_H188_Form_unabhaengige_Vorhersage.md`, Commit 615c984,
vor der Rechnung). H194a ist nicht blind (Kontrolle, der bekannte Fit aus k391c). **Werkzeuge:** Python (numpy) für Fits, ρ-Suche und
Zufallskontrollen (`k402_test_h194.py`/`k402_out.txt`, Zusatzkontrolle `k402c_kontrolle.py`/`k402c_out.txt`); Wolfram Language für die
exakten leptonischen Eigenwerte und die Fits als Gegenprobe (`k402b_out.txt`), bestätigt Python exakt. Qiskit nicht nötig.
**Anlass:** Kartenwahl des Autors „H188-Form testen" (27.11., 09:17).

## Die Form und die Frage
m ∝ (a·l_k + b·l_k²)/(l_i + l_j)², Zuordnung B, Lesart X = m. l = [0,040350, 0,580212, 2,379438] sind die Eigenwerte des
**Leptonvakuums** (K = ⅔, δ = 2/9 aus den geladenen Leptonen — nicht für die Quarks justiert). Je Sektor zwei Zahlen a, b. Ein
Zwei-Parameter-Fit an drei Massen trifft fast immer; die Form trägt nur, wenn sie darüber hinaus Inhalt hat. Zwei vorab festgelegte
unabhängige Vorhersagen:

## Ergebnis

**H194a (nicht blind, Kontrolle).** Der bekannte Fit je Sektor: Up a = −1,14·10⁻³, b = 6,61·10⁻², b/a = −57,9, χ² = 4,82
(Abstände −0,09; +2,13; −0,53 σ); Down a = 3,31·10⁻³, b = −2,81·10⁻⁴, b/a = −0,085, χ² = 3,09 (−1,12; +1,35; −0,11 σ).
Wie k391c, zwei Zahlen je Sektor.

**H194b (Test — gemeinsame Gestalt): widerlegt.** Ein **einziges** ρ = b/a für beide Sektoren (Skala je Sektor frei) bringt
keinen Sektor in die Nähe: bestes gemeinsames ρ = 24,4 gibt Up 80σ, Down 75σ. Die sektorweise optimalen ρ sind −57,9 (Up) und
−0,085 (Down) — ein Faktor **680** auseinander. Die Sektoren teilen **keine** Gestalt; Up läuft nahe an l_k²/z, Down nahe an l_k/z
(verschiedene Grenzfälle derselben Form, nicht eine gemeinsame Form). Kriterium „beide < 3σ mit einem ρ": nein.

**H194c (Test — Spezifität der leptonischen l_k): spezifisch.** Hier liegt das eigentliche Ergebnis:
- **Zuordnung.** Von den sechs Index-Permutationen trifft **nur** Zuordnung B (Up χ² = 4,82, Down χ² = 3,09). Alle fünf anderen
  geben χ² von 4·10³ bis 6·10⁴. Die Zuordnung ist hochspezifisch.
- **Eigenwerte.** 2000 zufällige l-Tripel (gleiche Normierung, Zuordnung B) durch denselben Fit: ein Sektor erreicht den
  beobachteten χ² in 0,4 %, **beide in 0,0 %**.
- **Faire Zusatzkontrolle (k402c).** Auch wenn jedes zufällige l-Tripel seine **eigene** beste der sechs Permutationen nutzen darf
  (so wie im echten Fall über Zuordnungen gesucht wurde), erreichen **beide** Sektoren den beobachteten χ² in **0,00 %** von 5000
  Fällen; der echte worst-χ² = 4,82 liegt am Rang 0,00 % (bestes Zufalls-l: 29, also 6× schlechter). Die leptonischen Eigenwerte
  sind für diese Form klar ausgezeichnet.

## Gesamturteil: teilweise
Nach dem vorab festgelegten Kriterium trägt die Form „als echter Kandidat" nur, wenn H194b **oder** H194c ihr Inhalt über den
Zwei-Parameter-Fit hinaus gibt. H194b scheitert (keine gemeinsame Gestalt), H194c trägt stark (die leptonischen l_k sind
spezifisch): **teilweise**. Die H188-Form ist **kein** beliebiger Fit — sie bindet die Quarkmassen gerade an die Eigenwerte des
Leptonvakuums (also an die geladenen Leptonen über δ = 2/9), und zufällige Eigenwerte reproduzieren das praktisch nie.

## Ehrliche Grenzen des Befunds
- **Die Form selbst ist nachträglich gewählt** (H188 verglich 324 Tripel). H194c kontrolliert die Wahl der **Zuordnung** und der
  **Eigenwerte**, nicht die Wahl der **Funktionsform** (l_k, l_k², (l_i+l_j)²). Die Spezifität gilt **bedingt** auf diese Form. Ein
  voller Befund bräuchte eine **Herleitung** der Form aus der Feldgleichung.
- **Je Sektor bleiben zwei Zahlen angepasst** (b/a frei und verschieden), und die Sektoren teilen keine Gestalt. Die Form sagt
  nicht, warum Up die Quadratform und Down die Linearform bevorzugt; allein treffen beide reinen Formen nicht (15σ, 34σ, H188).
- Die χ²-Werte (4,82 und 3,09 bei einem Freiheitsgrad, p ≈ 0,03 und 0,08) sind je für sich nicht spektakulär; das Gewicht liegt
  auf dem gemeinsamen Treffer mit **denselben** leptonischen l_k und der Seltenheit bei Zufalls-l.

## Lesart
Es gibt eine echte, spezifische Brücke von den geladenen Leptonen (deren Massen die l_k über δ = 2/9 setzen) zu den sechs
Quarkmassen: m_Quark ∝ (a·l_k + b·l_k²)/(l_i+l_j)² trifft beide Sektoren gerade mit den leptonischen Eigenwerten, nicht mit
beliebigen. Das ist der erste Weg im Quark-Strang, der mehr als einen reinen Fit zeigt. Was fehlt, ist die Herleitung der Form und
der Grund für die zwei verschiedenen b/a (Up quadratisch, Down linear). Das ist der nächste sinnvolle Schritt, wenn der Autor den
Strang weiterführt — und passt zur Linie „Massenquelle aus der Feldgleichung".

## Bilanz der Setzungen
| Größe | Status |
|---|---|
| Form (l_k, l_k², (l_i+l_j)²) und Zuordnung B | gesetzt (nachträglich in H188 gewählt; H194 kontrolliert Zuordnung + l_k, nicht die Form) |
| leptonische l_k (δ = 2/9) | Eingabe aus geladenen Leptonen; **spezifisch** (Zufalls-l treffen 0,0 %) — hergeleitet im Sinn „nicht beliebig" |
| b/a je Sektor | angepasst, und zwischen den Sektoren nicht teilbar (Faktor 680) |
| gemeinsame Gestalt ρ | widerlegt (80σ/75σ) |
| Herleitung der Form | offen (der eigentliche Befund) |

## Grenzen
Fester Funktionsansatz, keine Herleitung aus der Feldgleichung. OP3/OP4 (Quarkmassen) bleiben offen. Nächste frei: H195, k403.
