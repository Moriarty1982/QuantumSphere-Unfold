# Ergebnis H129: Schleifen können die Skala erzeugen, aber nicht festlegen, dass sie im Anhang entsteht (Test k296, 25.11.2026)

**Urteil nach den vorab festgelegten Kriterien:** H129 ist **nicht bestätigt**. K-a (Skala entsteht von selbst) **trägt teilweise** (67,8 % des Gitters),
K-b und K-c (die Skala entsteht im Anhang) sind **widerlegt**. Das entspricht der Vorhersage der Vorab-Notiz; überraschend war nichts.
Vorab-Notiz: `notes/research/predictions/Vorab_Notiz_H129_Schleifen_erzeugen_Skala_im_Anhang.md` (Commit 6742639, vor dem ersten Skriptlauf).
**Teilweise nicht blind**, wie dort offengelegt: K-b stand durch die Tauschsymmetrie fest, für K-a und K-c gab es einen Überschlag im Kopf.
Offen waren die β-Koeffizienten, die Gitteranteile und die Größe von δZ.

Werkzeuge: Python mit sympy (β-Funktionen, Kontraktion) und scipy (Fluss, 3936 Gitterpunkte). Wolfram Language unabhängig: β-Funktionen, Klassifikation
auf einem Teilgitter von 361 Punkten mit NDSolve, Zusatzterme mit Quaternionen als 2×2-Matrizen (k296b). Alle drei Vergleiche stimmen genau überein.
Qiskit nicht eingesetzt (keine Schaltung). Kein HDL/MMA-Vergleich.

## Zahlen
**Stufe A (β-Funktionen, t = ln μ):**
16π²·dλ_A/dt = 4(κ² + 20λ_A²), 16π²·dκ/dt = 16κ(κ + 2λ_A + 2λ_B), 16π²·dλ_B/dt = 4(κ² + 20λ_B²).
Für λ_A = λ_B = λ und r = κ/λ: 16π²·dr/dt = −4λ·r·(r − 2)². Der Punkt κ = 2λ ist das Potential der vollen Norm λ(A + B)².

**Stufe B (Fluss ins Infrarote, 3936 Gitterpunkte):**
| Klasse | Bedeutung | Punkte |
|---|---|---|
| (i) | keine Skala bis τ = 10⁴ | 1268 |
| (ii) | flache Richtung im Anhang | 787 |
| (iii) | flache Richtung in der Vorstufe | 787 |
| (ii) = (iii) | Gleichstand bei λ_A = λ_B | 158 |
| (iv) | flache Richtung mit beiden Anteilen | 936 |

- **K-a:** 2668/3936 = 67,8 % mit Skala. Zwischen 50 % und 95 %, also „trägt teilweise“.
- **K-b:** 787/2668 = 29,5 % im Anhang (mit halben Gleichständen 32,5 %). Unter 50 %, widerlegt. (ii) und (iii) sind genau gleich groß, wie offengelegt.
- Die Punkte ohne Skala haben alle κ > 0, mit κ/√(λ_Aλ_B) zwischen 0,10 und 2,68. Für κ < 0 entsteht immer eine Skala, und zwar mit beiden Anteilen (iv).
- Die Gildener–Weinberg-Bedingung ist an allen Ereignissen erfüllt (787/787, 787/787, 936/936).

**Stufe C (Zusatzterme, Abschneidung):** K₁ gibt allen vier Komponenten dieselbe Korrektur (z = 9·c₁·J). K₂ gibt z = 0 für x₀ und 24·c₂·J für x₁, x₂, x₃.
- **K-c:** widerlegt. K₂ zeichnet die drei imaginären Richtungen aus, nicht den Anhang: x₁ gehört zur Vorstufe und hat dieselbe Korrektur wie x₂, x₃.

## Was das für die Vermutung des Autors heißt
1. **Ein Vorzeichen legen die Schleifen fest.** Wo im skalenfreien Ansatz überhaupt eine Skala entsteht, entsteht sie als feste Amplitude (in der Sprache von
   k295: wie μ² < 0). Die andere Möglichkeit, ein gewöhnliches massives Feld ohne feste Amplitude (μ² > 0), kommt in dieser Rechnung nicht vor.
   Das stützt die Vermutung „Vorzeichen folgen aus der Feldgleichung“ in diesem einen Punkt, mit der Einschränkung unter „Grenzen“.
2. **Wo die Skala entsteht, legen sie nicht fest.** Potential und kinetischer Term sind unter dem Tausch Vorstufe ↔ Anhang symmetrisch. Welcher Teil
   die feste Amplitude bekommt, entscheidet die kleinere der beiden Kopplungen λ_A, λ_B, also wieder eine freie Zahl. K₂ unterscheidet reell von
   imaginär, nicht Vorstufe von Anhang.
3. **Die Kopplung κ, die k295 gern null gehabt hätte, ist der Motor.** Ohne κ (und ohne Eichfelder) gibt es keine Schleifen-Skala. Mit κ > 0 und flacher
   Richtung im Anhang bekommt die Vorstufe die Masse m² = κ·⟨B⟩. „Masse im Anhang, Licht bleibt masselos“ (k295, κ = 0) und „Skala von selbst“
   schließen sich in diesem Modell aus. Offen bleibt der Weg über Eichfelder (k291 Punkt 6).
4. **κ < 0 gibt den Fall aus k292:** beide Kreisanteile ungleich null, Verhältnis A/B = √(λ_B/λ_A) an der flachen Richtung. Das ist die einzige Klasse,
   in der immer eine Skala entsteht.
5. **Das Potential der vollen Norm ist der Ruhepunkt ohne Skala.** Für 0 < κ ≤ 2λ läuft der Fluss auf κ = 2λ zu. Dort ist das Potential λ(A + B)²,
   die Unterscheidung zwischen Vorstufe und Anhang verschwindet im Infraroten, und nichts kondensiert.

## Nachträglich (nicht Teil des Kriteriums)
- Der obere Rand des Fensters ohne Skala (2,68) hängt an τ ≤ 10⁴. Im symmetrischen Fall wächst r oberhalb von 2 nur logarithmisch: r = 2,1 erreicht
  λ = 0 erst jenseits von τ = 10⁴. Asymptotisch ist das Fenster dort 0 < r ≤ 2.
- τ = 10⁴ heißt ln(μ₀/μ) ≈ 1,6·10⁶ und ist keine physikalische Spanne. Verlangt man die Skala innerhalb von ln(μ₀/μ) ≤ 39,5 (τ ≤ 0,25), bleiben
  1568/3936 = 39,8 %. Nach dem Maßstab von K-a wäre das „widerlegt“; das Kriterium war aber mit τ = 10⁴ festgelegt, das Urteil oben gilt.

## Grenzen
- Eine Schleife, ohne Eichfelder, nur ℂ → ℍ, nur Links- und Rechtsdrehung um i. Die zwei nur linksinvarianten Terme aus k295 sind nicht mitgenommen.
- Punkt 1 gilt für die skalenfreie Rechnung (keine quadratischen Divergenzen). Mit einer Abschneidung Λ entstehen Beiträge δμ² ∝ (4λ + κ)Λ²/(16π²)
  mit dem Vorzeichen der Kopplungen. Ob der Turm die skalenfreie Lesart verlangt, ist eine Setzung (sie passt zu „keine Masse auf HS(0), HS(1)“).
- Stufe C gilt nur für die Abschneidung; in dimensionaler Regularisierung ist δZ im masselosen Fall null. Mit der Stromvariante der Zusatzterme
  (volle so(4), k290) entfällt auch die Unterscheidung reell gegen imaginär.
- Das Gitter ist eine Wahl, die Anteile sind keine Wahrscheinlichkeiten.
- OP1, OP3, OP4, OP5 bleiben offen, kein Guard ist berührt.

## Möglicher nächster Schritt
Der Tausch Vorstufe ↔ Anhang ist die Rechtsmultiplikation mit j, also Teil der so(4) des Ansatzes. Der Term erster Ordnung (Linksdrehung um i) und eine
geeichte Rechts-U(1) (Ladungen +1 und −1) brechen ihn nicht. Brechen kann ihn nur etwas, das an der Vorstufe allein angreift. Der Kandidat aus dem Turm ist
der HC, der ab HS(1) die Form der Ellipse festlegt (k292): Er könnte λ_A gegen λ_B oder das Vorzeichen von κ festlegen. Das ist nicht gerechnet.

## Dateien
`k296_test_h129.py` (`k296_out.txt`, Laufzeit etwa eine Minute), `k296b_gegenprobe.wl` (`k296b_out.txt`).
