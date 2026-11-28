# k449: HS(−1), HS(0), HS(1) aus einem inneren und einem äußeren Feld (Erkundung, nicht blind)

28.11.2026. **Erkundung ohne Vorab-Notiz.** Die Rechnungen sind Standardmathematik und stehen vor der Rechnung fest; nicht blind.
Anlass ist Marcs Frage vom 28.11.: Angenommen, der Urknall hat nur einen abgetrennten Bereich des Ursprungsfelds neu geordnet. Das
äußere Feld ist noch da und stemmt sich mit Druck oder Vakuum gegen den Kollaps, das innere arbeitet dagegen, und dazwischen liegt eine
Vakuumschicht mit einem Casimir-Effekt. Wie könnten unsere Stufen HS(−1), HS(0) und HS(1) daraus entstehen?

Skript `k449_innen_aussen.py` (Ausgabe `k449_out.txt`), Gegenprobe `k449b_gegenprobe.wl` (Ausgabe `k449b_out.txt`).

## Vorwissen geprüft
- k405 (`../hs_minus_1_k405/`): Unter ℝ gibt es keine Algebrastufe. Was „unter“ HS(0) liegt, ist ℤ₂ = S⁰ = {±1}, die Einheitssphäre von
  HS(0). Die Gruppenalgebra ℝ[ℤ₂] ist split-komplex, ℝ⊕ℝj mit j² = +1 (Index −1).
- k407 (`../hs_minus_1_rueckkehr_k407/`): Auf der Clifford-Uhr (Periode 8) kehrt der Typ ℝ⊕ℝ bei HS(3) und HS(11) zurück.
- `op5_bifocal_response_2026_11_18/Casimir.md`: Platten mit Feder ergeben ein metastabiles Minimum, kritisches x = 4/5.
- `licht_vermittler_zeit_2026_11_24/README.md`, Punkt 10: Motorbild (Scheibendynamo/Bullard) mit Einstrom und Abstrahlung.
  Das ist der „abgedrehte Elektromotor“, auf den Marc sich bezieht.

## Was gerechnet wurde (alles exakt, zwei Werkzeuge)
1. **Wand.** Ein reelles Feld mit V = λ(φ²−1)² hat genau zwei Vakua, ±1. Das ist S⁰, also die Einheitssphäre von HS(0). Ein abgetrennter
   Bereich mit dem anderen Vakuum ist durch eine Wand (Kink tanh(√(2λ)x)) getrennt. Geprüft wurden der BPS-Rest (Wolfram exakt 0), die
   Wandenergie (4/3)√(2λ) und die topologische Ladung +1.
2. **Innen/außen als Algebra.** Zwei Bereiche ergeben zwei Projektoren e₊ und e₋ mit e₊² = e₊, e₋² = e₋, e₊e₋ = 0 und e₊ + e₋ = 1.
   Das Vorzeichen über die Wand ist j = e₊ − e₋ mit j² = +1. Die reellen Funktionen auf {innen, außen} bilden also genau ℝ⊕ℝj = HS(−1).
   In beiden Werkzeugen exakt geprüft.
3. **Casimir im Spalt.** Für Moden (n + a)π/d gilt E/A = −(π²/(12d³))·ζ(−3, a).
   - Gleiche Randbedingung auf beiden Seiten (DD, a = 1): ζ = 1/120, die Energie ist anziehend und der Spalt schließt sich.
   - Gemischte Randbedingung (DN, a = ½): ζ = −7/960, die Energie ist abstoßend und der Spalt bleibt offen.
   - Verhältnis: **−7/8** exakt.
4. **Verdrehung.** Hat das Feld beim Umlauf über den Spalt die relative Phase α, so ist E(α) ∝ −S(α) mit S(α) = Σ cos(nα)/n⁴ = π⁴/90 − π²α²/12
   + πα³/12 − α⁴/48 (0 ≤ α ≤ 2π). Die Form ist exakt über Re Li₄(e^{iα}) geprüft, die Differenz liegt unter 1e-29.
   - S(π)/S(0) = **−7/8**, also dieselbe Zahl wie DN/DD.
   - Kritische Punkte: nur α = 0, π, 2π.
   - Bei Bosonen-Vorzeichen liegt das Minimum bei α = 0, bei Fermionen-Vorzeichen bei α = π.
   - Der erste Python-Lauf wich bei α = π/4 um 1e-4 ab. Ursache war `nsum` an der oszillierenden Reihe; Wolfram-`NSum` ist ebenso
     ungenau. Die exakte Polylog-Form beseitigt die Abweichung.

## Zuordnung (Lesart, nicht hergeleitet)

| Zustand zwischen innen und außen | Casimir im Spalt | Was bleibt | Stufe |
|---|---|---|---|
| gleich (α = 0, DD) | anziehend, Spalt schließt | nur e₊ + e₋ = 1, ein Feld | **HS(0) = ℝ** |
| Vorzeichenwechsel (α = π, DN) | abstoßend, Spalt bleibt offen | e₊, e₋ getrennt, j² = +1 | **HS(−1) = ℝ⊕ℝj** |
| freie Phase α (U(1) ⊃ ℤ₂ = {0, π}) | dazwischen, Minimum nur bei 0 oder π | Drehung statt Spiegelung, j → i | **HS(1) = ℂ** |

Kurz gesagt beginnt die Leiter bei der Trennung, nicht beim einen Feld:
- Zwei Bereiche ergeben ℝ⊕ℝj (HS(−1)).
- Verschmelzen sie, bleibt die Diagonale ℝ (HS(0)).
- Wird das Vorzeichen zur stetigen Phase, entsteht ℂ (HS(1)).

Das passt zu k405, wo ℤ₂ = S⁰ unter HS(0) liegt: Die Spiegelstufe ist hier nicht abstrakt, sondern das Vorzeichen über die Wand.

## Hergeleitet, gesetzt, nachträglich
- **Hergeleitet (Mathematik):**
  - Zwei Bereiche erzeugen genau die split-komplexe Algebra.
  - Die Vakua eines reellen Felds bilden S⁰.
  - Im Spalt ist nur gemischte Randbedingung bzw. Phase π abstoßend, also stabil getrennt.
  - Das Verhältnis −7/8 = −(1 − 2⁻³) ist eine reine Zählzahl (η(4)/ζ(4)). Es ist derselbe Faktor 7/8 wie zwischen Fermionen und
    Bosonen im Stefan-Boltzmann-Gesetz, also bekannte Physik und keine neue Zahl.
- **Gesetzt:**
  - e₊ und e₋ werden als inneres und äußeres Feld gelesen.
  - Der Spalt ist eine ebene Schicht mit festem d (keine Kugelgeometrie, keine Expansion).
  - Für HS(1) wird ein komplexes Feld mit Phase angenommen, damit ist ℂ von Hand hineingesteckt. HS(1) wird also nur **zugelassen**,
    nicht **erzeugt**.
- **Nachträglich bemerkt:** Marcs Bild verlangt, dass sich das äußere Feld gegen den Kollaps stemmt. Im Casimir-Bild leistet das nur der
  abstoßende Fall, und der ist genau der Fall mit j² = +1. Eine stabile Trennung wählt also die Spiegelstufe HS(−1), nicht HS(0).
  Das war nicht vorab vermutet.

## Was das nicht leistet
- Es gibt keine Zahl und keine Vorhersage. φ = 0,0395773 bleibt offen (der Strang ruht).
- Woher die stetige Phase für HS(1) kommt, bleibt offen. Ein möglicher Weg ohne Handsetzung wäre eine Drehung der Wand selbst
  (Motorbild, Phasengeschwindigkeit ⇒ U(1)). Das ist nicht gerechnet.
- HS(2) und höher (ℍ, 𝕆) folgen daraus nicht. Die Rückkehr des Typs ℝ⊕ℝ bei HS(3)/HS(11) (k407) würde im Bild eine erneute Trennung
  bedeuten. Auch das ist nur eine Lesart.

## Urteil
Erkundung, nicht blind. Das Bild ist **tragfähig als Anschauung**:
- HS(−1) und HS(0) entstehen zwanglos aus „zwei Bereiche oder einer“.
- Die Casimir-Schicht unterscheidet die beiden über das Vorzeichen der Energie, und die Zahl −7/8 verbindet Spalt und Verdrehung.
- HS(1) braucht eine zusätzliche Annahme.

Nächster möglicher Test (H235, wartet auf Marc): Ob die Verdrehungsenergie im Im-Sektor (geladen, c = 1) und im Re-Sektor (neutral,
c = 0) verschieden zählt und so den exakten Sektortausch aus H225 bricht.
