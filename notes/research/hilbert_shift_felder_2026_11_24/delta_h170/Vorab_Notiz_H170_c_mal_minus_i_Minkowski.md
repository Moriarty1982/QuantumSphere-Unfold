# Vorab-Notiz H170: Was passiert, wenn c mit −i multipliziert wird? Wick-Drehung, Minkowski-Ebene und die beiden Sektoren

**Stand:** 26.11.2026, vor der Rechnung festgelegt. **Nicht blind:** a bis d stehen analytisch fest und sind von Hand überschlagen; die Rechnung ist eine
exakte Nachprüfung. e ist ein Zahlenvergleich; einige Differenzen sind vorab grob überschlagen (kein Treffer gesehen). Anlass: Autor, 26.11.2026, 18:42 UTC:
„was wäre wenn wir c mit −i multiplizieren?“ und „wenn er mit der zeit zusammenhängen würde, hätten wir den ersten teil eines minkowsky space“.
Einordnung: `wiki/Gesamtbild.md`, T8/T13, OP3/OP4; Frames nach Konvention F. Vergeben: H170, k365 (geprüft: frei).

## Vorwissen geprüft
- **H169** (`../delta_h169/`): Projektor = Punkt c = i; c = 0 und ±1 = feste σ-Parität; π/12 aus H99 = Paritätstausch.
- **v4.9.0-r51** (`../../v4_10_0_r48_r55/rounds/v490_r51_round.tex`): iL_e₇ = äußeres z ↦ iz (Tachyon-Abbildung) mal inneres z ↦ e₇z; die Tachyon-Abbildung lässt
  Sektoren und Chiralität fest; Ladungskonjugation ist der Zeitumkehr-Teil T (Tausch der Ports), **nicht** die Tachyon-Abbildung. Regel aus AGENTS.md:
  z ↦ iz und z ↦ z̄ nicht verwechseln.
- **r13 neu / k255** (`../r13/README.md`): Ψ = (1 + u)/√2 = exp(uπ/4), Achteldrehung; Koide folgt aus dieser Form. **r30, H118:** Oktantschritt, Phase π/4.
- **H45, r47** (Maske, ε₀ = artanh β_sym = 0,6175296) und Zählregel β_sym = 0,5494056410 (Postulat).
- **k270** (`../rueckwaerts/README.md`): C = ½(1 + iL_u) schneidet auf HS(1) einen Kreisanteil heraus.
- Suche nach „−i·c“, „c ↦ −ic“, „hyperbolische Einheit“, „Minkowski“ zusammen mit „Ladungsmischung“ in `notes/`, `wiki/`: kein Vorbefund.

**Suchrichtung:** rückwärts von H169: gesucht ist eine native Operation, die den Projektorpunkt c = i auf c = 1 bringt. **Werkzeugwahl:** Python (sympy, mpmath)
exakt; Wolfram unabhängig als Gegenprobe. Qiskit nicht geeignet.

## Aufbau (k365, `k365_test_h170.py`; Gegenprobe `k365b_gegenprobe.wl`)
Wie H169: inneres j = e₇, äußeres i, P = ½(1 + ij). Neu: k = ij (k² = +1), c′ = −ic, also 1 + cj = 1 + c′k. Feld z = s + jv, r, δ wie bisher.
Quadratische Form des Spin-1-Terms ohne Normierung: G_c = (cs − v)²; normiert F_c = G_c/(1 + c²) (H169d).

## Hypothesen und Kriterien
- **H170a (exakt): Die Abbildung c ↦ −ic.** Ordnung 4; Bahn {i, 1, −i, −1}; Fixpunkte 0 und ∞. Der Projektor P (c = i) geht auf c = 1, c = 1 auf den
  Projektor P̄ (c = −i). Die neutrale Lesart c = 0 ist Fixpunkt. Kriterium: Nullreste.
- **H170b (exakt): c ↦ −ic ersetzt die Drehung durch einen Schub, die Ebene bekommt Minkowski-Signatur.** 1 + c′k mit k² = +1; Norm (a + bk)(a − bk) = a² − b²
  (Signatur (1,1)) statt a² + b² auf span(1, j). 1 + c′k = √(1 − c′²)(cosh ε + k sinh ε) mit c′ = tanh ε. Der Projektor ist der lichtartige Punkt c′ = 1
  (ε → ∞); Tr Z² = 2(1 − c′²)|x|², Spin-1-Term (1 − c′²)v′². Zusammensetzung zweier Mischungen addiert ε (Geschwindigkeitsaddition
  (c₁′ + c₂′)/(1 + c₁′c₂′)), wie reelles c die Winkel χ addiert. Kriterium: Nullreste.
- **H170c (exakt): Am Projektorpunkt ist die Form holomorph und enthält beide Sektoren.** G_i = −(s + iv)² = −r²e^{2iδ} (äußeres i). Realteil = 2F₀ − (s² + v²)
  (die σ-gerade Form, c = 0), Imaginärteil = 2F₁ − (s² + v²) = −2sv (die σ-ungerade Form, c = 1). Allgemein −r² cos 2(δ − χ) = Re[e^{−2iχ}·G_i]: Die ganze
  reelle Familie besteht aus den Phasenlagen dieser einen Form. Kriterium: Nullreste.
- **H170d (exakt): Multiplikation mit −i ist der Schritt neutral → geladen.** Re[−i·G_i] ist die c = 1-Form; auf δ wirkt das als Verschiebung um π/4, gefaltet
  die Verschiebung π/12 aus H99. Auf dem Feld entspricht −i an der quadratischen Form einer Achteldrehung e^{−iπ/4} (Wurzel aus −i), **nicht** der vollen
  Tachyon-Abbildung z ↦ iz; diese gibt G ↦ −G (tauscht Minima und Maxima, lässt die σ-Parität fest). Kriterium: Nullreste; Minima gefaltet auf 10⁻¹².
- **H170e (Zahlenvergleich): Trifft das Wick-Wörterbuch den Versatz?** Im Schub-Bild ist die native Zahl ε₀ = artanh β_sym. Übersetzung Winkel ↔ Rapidität:
  Gudermann-Funktion gd(ε) = arcsin(tanh ε). Ziele: x = 0,0395773407, 2x, tan x, tan 2x. Kandidaten, vorab: gd(ε₀) − π/6, π/6 − arctan β_sym, ε₀ − gd(ε₀),
  ε₀ − π/6, π/4 − ε₀, gd(ε₀) − arctan β_sym, π/4 − gd(ε₀), jeweils auch halbiert und verdoppelt (21 Kandidaten, 84 Vergleiche). Treffer, wenn relativ näher
  als 10⁻³. **Vorhersage: kein Treffer** (Zufallserwartung < 0,2).

## Folge, vorab festgelegt
- a bis d bestätigt: Antwort an den Autor: Ja, die Multiplikation mit −i hat eine genaue Bedeutung. Sie macht aus der Drehebene (1, e₇) eine Ebene mit
  Minkowski-Signatur, in der die Ladungsmischung ein Schub und der Chiralitätsprojektor der Lichtkegel ist. An der quadratischen Form ist sie der Schritt vom
  neutralen zum geladenen Sektor. **Nicht hergeleitet** bleibt, dass die innere Richtung die Zeit ist: Die Rechnung gibt die Signatur (1,1), keine Zuordnung
  zur Raumzeit. Als Kandidat festzuhalten, nicht als Ergebnis. Ebenso bleibt offen, warum der geladene Sektor den Imaginärteil liest.
- e ohne Treffer: Der Versatz x folgt auch im Schub-Bild nicht aus β_sym. Mit Treffer: eigener Test nötig.
- Kein Vorzeichen wird gesetzt; kein Guard berührt; OP3 und OP4 bleiben offen. Keine neue Datenvorhersage.
