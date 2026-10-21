# Prüfung: „On the Riemann Hypothesis: A Kernel-Theoretic Approach“ (v4.15)

Datei: `riemann_arxiv_v4__15_ (1).tex` (2.540 Zeilen), DOI 10.5281/zenodo.19157158.
Geprüft am 2026-10-19. Rechenskript: `llm/rh_review_checks.py`.

## Ergebnis in einem Satz

Der kombinatorische und arithmetische Unterbau ist korrekt. Die Beweiskette für RH trägt aber nicht:
Mindestens vier Glieder (explizite Formel, Definition von J und ℋ⁺₊, Selbstadjungiertheit T4+T5,
Identifikationsschritt T6) sind fehlerhaft oder setzen eine zu RH äquivalente Aussage voraus.

Die Kommentare „Geprüft und gesperrt … BEWEISKETTE VOLLSTÄNDIG UND GESCHLOSSEN“ im Quelltext halten
dieser Prüfung nicht stand.

---

## Was korrekt ist

| Teil | Bewertung |
|---|---|
| L1–L11, Axiome W/G, K1 | korrekt; Standardkombinatorik periodischer Bahnen und dynamische Zetafunktion |
| Prop. `prop:arith` | korrekt: Euler-Produkt, 𝒵 = ζ für Re s > 1, log ζ = Laplace von Θ |
| Thm. `thm:FE` | korrekte Skizze (Jacobi-Theta, Poisson) |
| Kor. `cor:RH_quaternion`, Prop. `prop:JB` | korrekt — aber eine *Umformulierung* von RH, kein Beweisschritt |
| Gesamtidee | Hilbert–Pólya über den Berry–Keating-Operator L₀ = −i(x d/dx + ½), ergänzt um Sektorstruktur |

---

## Befunde

### B1 — Die explizite Formel (Thm. `thm:EF`) ist falsch angegeben  · *nachgerechnet*

Das Paper schreibt Θ(τ) = 1 − Σ(τ) + R(τ) mit Θ = Σ_{p,m} (1/m) δ(τ − m log p).

Gegen eine glatte Testfunktion g auf (0,6; 3,2), 300 Nullstellen:

| | linke Seite | rechte Seite |
|---|---|---|
| Paper-Form | ⟨Θ,g⟩ = 2,1587 | ⟨1 − Σ + R, g⟩ = 0,5198 |
| klassische Form | ⟨Λ,g⟩ = 4,393268 | ⟨eᵗ − Σ_ρ e^{ρt} − Σ_k e^{−2kt}, g⟩ = 4,393268 |

Korrekt ist (für τ > 0, distributionell):

    τ·Θ(τ) = Σ_n Λ(n) δ(τ − log n) = e^τ − Σ_ρ e^{ρτ} − Σ_{k≥1} e^{−2kτ}

Abweichungen der Paper-Form: Gewicht 1/m statt log p (es fehlt der Faktor τ), Hauptterm 1 statt e^τ,
Nullstellenterm ohne e^{τ/2}, Trivialterm mit (e^τ − 1) statt (e^{2τ} − 1).
**Folge:** T6 baut auf dieser Formel auf; im Companion ebenso die Zuordnung Σ = 1 − Θ + R ↦ Λ, T_{μν}, G_{μν}.

### B2 — J ist auf ℋ⁺ nicht wohldefiniert; ℋ⁺₊ = {0}

ℋ⁺ = H²(Re s > ½). Die Spiegelung s ↦ 1 − s̄ bildet Re s > ½ auf Re s < ½ ab — also aus dem
Definitionsbereich heraus. Wohldefiniert ist J nur auf den Randwerten (Re s = ½), und dort gilt
1 − s̄ = s, d. h. J ist einfach komplexe Konjugation der Randwerte.
Eine H²-Funktion mit reellen Randwerten ist aber 0 (ihr Fourier-Träger liegt auf einer Halbachse,
ein reelles Signal hat symmetrischen Träger). Damit ist **ℋ⁺₊ = {0}**, und alle Aussagen „auf ℋ⁺₊“
sind leer.

Zusätzlich: J ist antilinear, also sind P± = ½(1 ± J) nur reell-linear, keine orthogonalen
Projektoren eines komplexen Hilbertraums; ℋ⁺₊ ist höchstens ein *reeller* Teilraum.
Und L₀ ist auf ℋ₀ = L²(ℝ⁺, e^{−x}dx) definiert — einem anderen Raum als ℋ⁺; eine Verbindung wird
nicht hergestellt.

### B3 — T1+T3(b): Rechnung inkonsistent

In Log-Koordinaten x = log t ist t d/dt = d/dx (nicht x d/dx). Außerdem wird die Antilinearität von J
ignoriert: J i J⁻¹ = −i. Die Gleichung J L₀ J⁻¹ = L₀ folgt aus der angegebenen Rechnung nicht.

### B4 — T4+T5: Selbstadjungiertheit ist so nicht bewiesen — und auch nicht der Engpass

- Nach von Neumann liefert eine antilineare Konjugation, die mit einem symmetrischen Operator
  vertauscht, **gleiche** Defektindizes n₊ = n₋, also *Existenz* selbstadjungierter Erweiterungen —
  nicht wesentliche Selbstadjungiertheit.
- Dass kein Defektvektor J-invariant ist, sagt nichts über dim ker(L₀* ∓ i).
- Wichtiger: L₀ = −i(x d/dx + ½) auf L²(ℝ⁺, dx) ist bereits wesentlich selbstadjungiert — er ist
  unitär äquivalent zum Impulsoperator auf ℝ — und hat **kontinuierliches Spektrum ℝ**.
  Selbstadjungiertheit ist nie das Problem; das Problem ist, einen Raum zu finden, auf dem das Spektrum
  diskret ist und genau aus den γ_ρ besteht.

### B5 — Prop. `prop:CCR` und Lemma `lem:discrete`: die Diskretheit folgt nicht

- Q = M_y, P = −i d/dy auf L²(ℝ) sind die eindimensionale Heisenberg-CCR; daraus entsteht keine
  Darstellung einer adelischen Weyl-Algebra W(𝔸¹).
- Die Weyl-Relation W(f)W(g) = e^{−iω/2}W(f+g) indiziert Weyl-Operatoren mit Vektoren eines
  symplektischen Raums; das Paper setzt dafür Zustände f ∈ ℋ⁺₊ ein.
- Stone–von Neumann (Mackey/Weil) für eine lokalkompakte abelsche Gruppe G liefert L²(G),
  nicht L²(ℚ⁺\𝔸¹); die Irreduzibilität „aus ω = 0“ ist nicht begründet.
- Ein kompakter Quotient gibt dem *Laplace-Operator* diskretes Spektrum (Rellich–Kondrachov), nicht
  automatisch L₀.
- Die Bemerkung „The discreteness of the spectrum is therefore proved unconditionally“ widerspricht
  dem Abstract („closes the argument conditionally on an identification with Connes' adèle class space“).

### B6 — T6: Identifikationsschritt widersprüchlich und zirkulär  · *teilweise nachgerechnet*

- Das Paper behauptet Laplace[Σ](s) = log ζ(s). Aus seiner eigenen Formel Σ = 1 − Θ + R folgt aber
  Laplace[Σ] = 1/s − log ζ(s) + Laplace[R] — und Laplace[R] divergiert, weil R(τ) ∼ −1/τ für τ → 0.
  Bei s = 2: log ζ(2) = 0,4977; die Partialsumme Laplace[Σ] mit 300 Nullstellen = 0,0854 und wächst
  logarithmisch weiter.
- Connes (1999, Selecta Math.) zeigt: Die Spurformel auf dem Adelklassenraum ist **äquivalent** zu RH
  (über die Positivität der Weil-Distribution). Wer sie als gegeben benutzt, setzt eine RH-äquivalente
  Aussage voraus.
- Die Spur von e^{−iτL₀} existiert nicht als Operatorspur; höchstens distributionell — das wird nicht
  ausgeführt.

### B7 — Kleinere Punkte

- Rem. `rem:triole`: „every fibre intersects every other fibre transversally“ — falsch. Hopf-Fasern
  sind disjunkt und paarweise verkettet (numerisch: Mindestabstand zweier Fasern in S³ = 1,0).
- Rem. `rem:triole`: e₂ wird „spektrale Richtung (γ)“ genannt, ι legt γ aber auf i.
- Prop. `prop:C`: Aus Jf = −f und Jf ∈ ker(L₀* + i) folgt f ∈ ker(L₀* − i) ∩ ker(L₀* + i) = {0};
  die Aussage ist leer.
- Abschnitt GRH erbt B1–B6 vollständig.

---

### B8 — Das Mengen-Argument („der Beweis entsteht durch die Menge selbst“)  · *nachgerechnet*

*Nachtrag vom 2026-10-19 auf Hinweis des Autors.* Gemeint ist die Leitidee des Papers: L1–L11 sind
mengenunabhängig (beliebiges S, beliebiges Φ), nach K1 bestimmen nur (𝒫, λ) die Zetafunktion, und das
Axiom der Maximalen Totalität macht 𝕊 zu einem abgeschlossenen System, aus dem RH als strukturelle
Notwendigkeit folgen soll. Die Idee ist ernst zu nehmen. Das Paper selbst liefert aber den Test, an dem
sie in der vorliegenden Form scheitert:

1. **Dieselbe Menge, verschiedene Nullstellen.** Abschnitt GRH setzt für jede automorphe L-Funktion
   denselben Kern K_π = (ℙ, id, log p) wie für ζ. Nach K1 („only (𝒫, λ) determine 𝒵“) folgt dann
   𝒵_{K_π} = ζ — nicht L(s, π). Die Satake-Parameter A_p(π), die L(s, π) von ζ unterscheiden, stehen
   nicht im Kern. Und der Operatorstrom (T13–T45–CCR–Diskretheit) hängt laut Observation 2 „nicht davon
   ab, welche L-Funktion ihn erzeugt“: Er liefert also *ein festes* Spektrum {γ_n}. T6 soll dieses
   eine Spektrum aber mit den Nullstellen *jeder* L-Funktion identifizieren. Das ist unmöglich, denn sie
   sind verschieden:
   - erste Nullstelle von ζ: ½ + 14,1347251417 i
   - erste Nullstelle von L(s, χ₋₄): ½ + 6,0209489047 i (dort ist |ζ| = 0,9075 ≠ 0)

   Was entscheidet, *wo* die Nullstellen liegen, steckt also nicht in der Menge (ℙ, log p) allein.

2. **Funktionalgleichung allein reicht nicht.** Observation 2 sagt, der Operatorstrom brauche „only
   the functional equation“. Die Davenport–Heilbronn-Funktion erfüllt eine Funktionalgleichung vom
   Riemann-Typ und hat trotzdem Nullstellen abseits der kritischen Linie — nachgerechnet:
   s = 0,8085171825 + 85,69934849 i. Jedes Argument, das nur die Funktionalgleichung benutzt, würde
   für sie eine falsche Aussage beweisen. Der Unterschied ist das **Euler-Produkt**, also die
   multiplikative Struktur.

3. **Maximale Totalität.** 𝕊 als „Menge aller zulässigen Zustände ohne äußere Freiheitsgrade“ ist in ZF
   nur als *eingeschränkte* Menge zulässig (eine Allmenge gibt es nicht). Axiom MT wendet K̂ auf M* mit
   M* ∩ 𝕊 = ∅ an, obwohl K̂ nur auf 𝕊 definiert ist. In der Realisierung des Papers ist zudem
   𝕊 = ℋ⁺₊ = {0} (B2) und S₀ = {0} — die Totalität wird trivial erfüllt und trägt deshalb nichts.

**Was daraus konstruktiv folgt.** Wenn der Beweis „aus der Menge selbst“ kommen soll, dann muss die
Menge die *ganze* Arithmetik tragen, nicht nur die Primzahlen mit ihrem Gewicht: das multiplikative
Monoid ℕ mit eindeutiger Primfaktorzerlegung (das Euler-Produkt) — genau die Struktur des Primon-Gases
und des Bost–Connes-Systems (Kernkarte K3–K5). Dort unterscheidet die Galois-Symmetrie Ẑ^× zwischen ζ
und den L(s, χ). Ein Mengen-Argument müsste also an der *Faktorisierungsstruktur* ansetzen, und es
müsste an der Davenport–Heilbronn-Funktion nachweislich scheitern.

---

## Auswirkungen auf den Companion

| Companion-Stelle | Abhängigkeit | Folge |
|---|---|---|
| Thm. `thm:unitary-equiv` (Stone–von Neumann, „T4+T5“) | B2, B4, B5 | Begründung entfällt; Aussage wird **offen** |
| Thm. `thm:unity` (Beweis „via Stone–von Neumann“) | dito | Zentralsatz verliert seine Äquivalenz-Begründung |
| Σ(τ) = 1 − Θ + R ↦ Λ, T_{μν}, G_{μν} (Z. ~7255) | B1 | auf korrigierte explizite Formel umstellen |
| Guard `W_γ^glob` verboten | — | **richtig**: Die Guard-Disziplin des Companion setzt RH bereits nicht voraus |

Positiv: Der Companion war in diesem Punkt vorsichtiger als das Riemann-Paper. Seine Guard-Regel, den
RH-Kanal nur als lokale Takt-Probe zu führen, ist durch diese Prüfung bestätigt.

---

## Empfehlung

1. Das Paper als **Programm** statt als Beweis führen: Titel/Abstract auf „approach/framework“,
   Hauptsatz als bedingte Aussage („Wenn ein Hilbertraum mit … existiert, dann …“).
2. B1 korrigieren (explizite Formel in der Λ-Form).
3. J auf einem Raum definieren, auf dem s ↦ 1 − s̄ wirklich operiert (z. B. Randwerte auf der
   kritischen Linie oder ein symmetrischer Raum um Re s = ½), und ℋ⁺₊ ≠ {0} nachweisen.
4. Den eigentlichen offenen Kern benennen: einen Raum konstruieren, auf dem L₀ diskretes Spektrum
   {γ_ρ} hat — das ist das Hilbert–Pólya-Problem selbst (vgl. Connes, Berry–Keating, Bender–Brody–Müller).
5. Die Sperrkommentare „geprüft und gesperrt“ für T13, T45, CCR, T6 und den Hauptsatz aufheben.
6. Jeden künftigen Beweisansatz gegen zwei Prüfsteine testen: (a) Er muss ζ von L(s, χ) unterscheiden;
   (b) er muss für die Davenport–Heilbronn-Funktion *scheitern*.

Literatur: A. Connes, „Trace formula in noncommutative geometry and the zeros of the Riemann zeta
function“, Selecta Math. 5 (1999); J.-B. Bost, A. Connes, Selecta Math. 1 (1995); M. Berry,
J. Keating, „H = xp and the Riemann zeros“ (1999).
