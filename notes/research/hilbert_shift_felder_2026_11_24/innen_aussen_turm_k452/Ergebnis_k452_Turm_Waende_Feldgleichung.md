# k452: Die höheren HS-Stufen im Wand-Bild, ihr Vergleich und warum der Turm bei HS(3) anhält (Erkundung, nicht blind)

28.11.2026. **Erkundung ohne Vorab-Notiz.** Alle Rechnungen sind bekannte Mathematik (Cayley–Dickson, Hurwitz, Radon–Hurwitz, Adams) und standen
vor der Rechnung fest; nicht blind. Marc stellte drei Fragen nacheinander:
1. Wie entstehen die anderen HS-Stufen im Bild aus k449 (inneres und äußeres Feld)?
2. Was zeigen die Stufen, wie verändern sie sich, warum ändert das die Physik, und warum hält der Turm an, mit einem Grund abseits der Sedenionen?
3. Kann man jede Zahlstufe ℝ, ℂ, ℍ, 𝕆, 𝕊 als allgemeine Feldgleichung formulieren?

Skript `k452_innen_aussen_turm.py` (Ausgabe `k452_out.txt`), Gegenprobe `k452b_gegenprobe.wl` (Ausgabe `k452b_out.txt`). Alle gemeinsamen Zahlen
stimmen überein.

## Vorwissen geprüft
- **k449:** Zwei Bereiche ergeben ℝ⊕ℝj = HS(−1). Verschmelzen ergibt ℝ = HS(0). Eine stetige Phase ergibt ℂ = HS(1); sie ist gesetzt.
  Nur der abstoßende Fall j² = +1 hält eine Trennung stabil.
- **k253/k254 (`../hs4/`):** Feldregel ψ′ = u w ψ in A_n. Die Ableitungsalgebra hat die Dimensionen 0, 0, 3, 14, 14 (HS(0) bis HS(4)).
  HS(1) bringt die U(1)-Ladung, HS(2) die erste Holonomie (Berry −Ω/2), HS(3) g₂ mit Stabilisator su(3). Bei HS(4) kommt keine neue stetige
  Symmetrie dazu, nur eine endliche S₃, die drei Oktonion-Teilalgebren vertauscht. Nullteiler sind Lecks.
- **k405/k407:** Unter ℝ gibt es keine Stufe. Bei HS(3) kehrt der Typ ℝ⊕ℝ als Links/Rechts-Vorzeichen zurück (Clifford-Uhr). Größte
  antikommutierende Mengen von Einheiten: 0, 1, 3, 7, 8, 9, 10, 11, … (für HS(0) bis HS(4) gleich der Radon–Hurwitz-Zahl).
- **H138–H148:** In 𝕊 gibt es genau drei G₂-stabile Oktonion-Kopien. Ob die Kopien Generationen sind, ist offen.
- **Literatur (nur als Bezug, hier nicht nachgeprüft):** Gürsey und Günaydin (Oktonionen und Farbe), Dixon (ℝ⊗ℂ⊗ℍ⊗𝕆 als Algebra des
  Standardmodells), Furey (Ladungen und Generationen aus ℂ⊗𝕆).

## 1 Entstehung: jede Stufe ist eine weitere Wand um alles Bisherige
Die Verdopplung A_(n+1) = A_n ⊕ A_n·ℓ liest sich als Paar (innen, außen) = (a, b) mit dem Produkt
(a, b)(c, d) = (ac + g·d̄b, da + bc̄). Je Wand gibt es ein Vorzeichen g = ℓ²:
- g = +1: Vorzeichenwechsel über die Wand (wie HS(−1) in k449; das ist der abstoßende, stabile Fall).
- g = −1: Verdrehung beim Durchgang.

Gerechnet (Teil 1 bis 4):
- **Division braucht die Verdrehung an jeder Wand.** Bis HS(3) ergibt von den 2ⁿ Vorzeichenfolgen genau eine eine Divisionsalgebra, nämlich g = −1
  an jeder Wand (Normform definit, +2ⁿ). Jede einzelne Wand mit g = +1 macht die Normform indefinit (+2ⁿ⁻¹, −2ⁿ⁻¹) und erzeugt Nullteiler (split-Algebra).
- **Die neue Verdrehung steht senkrecht auf allen inneren.** ℓ antikommutiert mit allen Imaginäreinheiten der inneren Stufe, exakt für HS(2) bis HS(4).
- **Was jede neue Wand kostet:**
  - Bei zwei Wänden zählt die Reihenfolge der Durchgänge: e₁e₂ = +e₃, aber e₂e₁ = −e₃ (ℍ, nicht kommutativ).
  - Bei drei Wänden zählt die Klammerung: (e₁e₂)e₄ = +e₇, aber e₁(e₂e₄) = −e₇ (𝕆, nicht assoziativ, aber alternativ).
  - Bei vier Wänden geht Intensität verloren: (e₁+e₁₀)(e₄−e₁₅) = 0 bei N = 2 für beide Faktoren. Das ist ein Leck, und zwar auch mit Verdrehung an
    jeder Wand (𝕊).

**Spannung zu k449:** Eine stabile Trennung wählt g = +1 und führt damit zu split-Algebren, nicht zum Divisionsturm. Der Divisionsturm verlangt an
jeder Wand die Verdrehung, also an jeder Stufe dieselbe Zusatzannahme wie bei HS(1). Das Bild erklärt den **Aufbau** des Turms, aber nicht, **woher
die Verdrehung** kommt. Das ist jetzt eine einzige offene Frage statt einer je Stufe.

## 2 Vergleich der Stufen

| Stufe | Wände | was neu dazukommt | was verloren geht | stetige Symmetrie (dim Der) | Lesart im Projekt |
|---|---|---|---|---|---|
| HS(−1) ℝ⊕ℝj | 1, gespiegelt | zwei Bereiche, Vorzeichen | Division (Nullteiler e±) | — (ℤ₂) | Trennung, Spiegel M ↔ T (k405, k449) |
| HS(0) ℝ | 0 | ein Feld, Größe | — | 0 | neutral, zeitumkehrinvariant (k253) |
| HS(1) ℂ | 1, verdreht | Phase | Anordnung | 0 (Phase als U(1)) | Ladung (k253) |
| HS(2) ℍ | 2 | zweite, senkrechte Verdrehung | Kommutativität | 3 = su(2) | Spin ½, erste Holonomie (k253) |
| HS(3) 𝕆 | 3 | dritte Verdrehung | Assoziativität | 14 = g₂ ⊃ su(3) | Farbe (k253), Links/Rechts kehrt zurück (k407) |
| HS(4) 𝕊 | 4 | **keine neue stetige Symmetrie**, nur endliche S₃ | Alternativität, Norm, Division | 14 (wie 𝕆) | drei Oktonion-Kopien, Generationskandidat (H138, offen); Lecks |

**Warum das die Physik ändert (Lesart):** Jede verdrehte Wand fügt eine Schicht innerer Symmetrie hinzu, der Reihe nach nichts, U(1), SU(2) und
SU(3) ⊂ G₂. Danach kommt nur noch Vervielfältigung (drei Kopien) ohne neue Kraft. Diese Abfolge sieht aus wie die Eichstruktur U(1)×SU(2)×SU(3) des
Standardmodells mit drei Generationen. Das ist eine Lesart, keine Herleitung. Dieselbe Beobachtung steht in der genannten Literatur.

## 3 Warum der Turm anhält, physikalisch (Teile 5 und 7)
Drei Formulierungen, die sich als **dieselbe Bedingung** herausstellen:
1. **Feldgleichung (Marcs dritte Frage).** Jede Stufe hat eine Feldgleichung erster Ordnung D f = 0 mit D = ∂₀ + Σ eᵢ∂ᵢ: Cauchy–Riemann für ℂ, Fueter
   für ℍ, oktonionischer Dirac-Operator für 𝕆.
   - Sie ist genau dann eine Wurzel der Wellen- bzw. Laplace-Gleichung (D̄D f = Δf für **jedes** Feld f), wenn die Linksmultiplikationen eine
     Clifford-Darstellung bilden: LᵢLⱼ + LⱼLᵢ = −2δᵢⱼ.
   - Gerechnet: Für HS(1), HS(2), HS(3) ist die Abweichung exakt 0, für HS(4) ist sie 2.
   - **Für 𝕊 gibt es also keine Feldgleichung erster Ordnung, deren Quadrat die Wellengleichung ist.** Ein Feld dieser Stufe kann sich nicht lokal und
     mit Lichtgeschwindigkeit ausbreiten wie die Felder der Stufen darunter.
2. **Wand.** Die Wand zwischen innen und außen ist eine Sphäre S^(N−1) im Feldraum. Um in jede Richtung verdrehen zu können, braucht sie N−1 überall von
   null verschiedene, orthonormale Verdrehungsfelder (einen Rahmen).
   - Mit vᵢ(x) = eᵢx gibt es einen vollen Rahmen auf S¹, S³ und S⁷ (Gram-Abweichung ≤ 4·10⁻¹⁶). Auf S¹⁵ gibt es keinen (Gram-Abweichung 0,84,
     Richtungen fallen zusammen).
   - Allgemein trägt S^(N−1) nur ρ(N) − 1 unabhängige Felder (Radon–Hurwitz): für N = 16 sind das 8 von 15, für 32 sind es 9 von 31, für 64 sind es
     11 von 63.
   - Ein voller Rahmen existiert nur für N = 1, 2, 4, 8 (Adams 1960, Hopf-Invariante 1).
   - Die 8 Felder bei HS(4) sind genau die 8 antikommutierenden Einheiten aus k407.
3. **Erhaltung.** Die Intensität ist beim Durchgang durch alle Wände erhalten (Norm multiplikativ, Hurwitz). Das gilt bis HS(3) exakt (Wolfram
   symbolisch 0 für HS(2) und HS(3)) und bricht bei HS(4) (Leck).

**Antwort auf Marcs Einwand:** Der Abbruch muss keine Eigenheit der Sedenionen sein, an die sich das Universum „streng hält“. Er folgt aus einer
physikalischen Forderung: **Jede Stufe soll eine Feldgleichung erster Ordnung haben, deren Quadrat die Wellengleichung ist** (Dirac-Prinzip: lokale,
kausale Ausbreitung). Diese eine Forderung erzeugt den Turm ℝ, ℂ, ℍ, 𝕆 und beendet ihn danach zwingend. Das ist die gesuchte „Feldkonfiguration, die
genau das erzeugen muss“, in Form einer Bedingung an die Feldgleichung. Weitere Wände sind nicht verboten, sie bringen aber keine neue
wellenfähige Richtung mehr, nur Kopien und Lecks.

## Hergeleitet, gesetzt, nachträglich
- **Hergeleitet (Mathematik, nachgerechnet):**
  - Division nur bei Verdrehung an jeder Wand.
  - Verlust von Reihenfolge, Klammerung und Norm nach zwei, drei und vier Wänden.
  - Clifford-Bedingung erfüllt bis HS(3), gebrochen bei HS(4).
  - Rahmen auf S¹, S³, S⁷, nicht auf S¹⁵.
  - Radon–Hurwitz-Zahlen.
  - dim Der = 0, 0, 3, 14, 14.
- **Gesetzt:**
  - Lesart „jede Stufe eine weitere Wand“, (a, b) = (innen, außen).
  - Verdrehung g = −1 an jeder Wand (die offene Annahme aus k449, jetzt je Stufe).
  - **Der Feldwert lebt in der Stufe selbst** (Feldregel aus k253), und die Ableitungsrichtungen sind deren Einheiten. Mit allgemeinen
    Clifford-Algebren statt der Stufe selbst gibt es Dirac-Operatoren in jeder Dimension (Bott-Periode 8, k407); dann hält nichts an.
    Der Abbruch gilt also genau für die Forderung „Feld und Richtungen im selben Raum“.
  - Dirac-Prinzip als physikalische Forderung.
  - Zuordnung der Symmetrien zu Ladung, Spin und Farbe (frühere Lesarten).
- **Nachträglich:** Die 8 Rahmenfelder bei HS(4) stimmen mit den 8 antikommutierenden Einheiten aus k407 überein. Die Äquivalenz von Feldgleichung,
  Wandrahmen und Erhaltung wurde hier zusammengeführt.

## Was offen bleibt
- Woher die Verdrehung an jeder Wand kommt. Kandidat aus k449 ist eine drehende Wand (Motorbild), nicht gerechnet.
- Ob die drei Oktonion-Kopien in HS(4) Generationen sind (H140–H143, offen).
- **Möglicher Test (braucht H-Nummer):** Die Feldgleichung der Stufe auf die Feldregel ψ′ = u w ψ aus k253 anwenden. Dann prüfen, ob bei HS(4) die 8
  noch wellenfähigen Richtungen genau die drei Kopien tragen oder sie trennen.

Es gibt keine neue Zahl und kein Urteil über ein OP; OP1 bis OP5 bleiben offen. Vergeben: k452. Nächste frei: H237, k453.
