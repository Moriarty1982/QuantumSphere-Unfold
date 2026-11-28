# Ergebnis H232 (k446): Die Rückwärtssuche findet keinen Brecher. Ein symmetrischer Term kann x nur zu einem lokalen Minimum machen

**Datum:** 2026-11-28. **Vorab:** `Vorab_H232_Rueckwaerts_Brecher.md` (Commit d1de5e2, vor der Rechnung). **Urteil: widerlegt.**
**Werkzeuge:** Python (`k446_test_h232.py` → `k446_out.txt`) und Wolfram unabhängig (`k446b_gegenprobe.wl` → `k446b_out.txt`). Die Wolfram-Rechnung löst das
geschlossene Gleichungssystem für (δ_Im, δ_Re, φ, r) mit FindRoot bei 40 Stellen. Python minimiert global in δ und φ. Beide geben r* = 0,045023087591 und
x_ν,pred = 0,091852 auf alle gezeigten Stellen. Qiskit ist nicht einschlägig. Teil A war nicht blind, B und C waren blind.

## Frage
Rückwärts gefragt: Was muss ein Term leisten, damit φ = x = 0,0395773 das globale Minimum der gemeinsamen Vakuumenergie beider Lepton-Sektoren ist? Und muss er den
Sektortausch (H225) überhaupt **explizit** brechen, oder genügt ein spontaner Bruch durch ein entartetes Paar (φ₀, π/4 − φ₀)?

## Ergebnis
| Teil | Messwert | Kriterium | Entscheidung |
|---|---|---|---|
| A1 (nicht blind, Wolfram symbolisch) | dE/dφ = −4 cos(off_Im − off_Re) · sin(off_Im + off_Re − 2φ). Für **jeden** Zusatz, der nur von δ abhängt, gilt an jedem stationären φ: off_Im + off_Re = 2φ | — | Daten: φ* = (x + x_ν)/2 = 0,04147 ± 0,00106 |
| A2 (nicht blind) | führende Ordnung: q cos 3δ + r cos 6δ macht x stationär für c₀ = −q/(4r) = 0,374590, also r/\|q\| = 0,667396; dort x_ν,pred = x | — | — |
| B1 (blind), q = −0,0852 | r* = 0,0450231 (r*/\|q\| = 0,52844): x ist stationär und in δ ein Minimum, aber **nicht global** (E bei φ = 7π/24 tiefer: −2,12925 gegen −2,11517). Außerdem x_ν,pred = 0,09185, also **+22,8σ** | global und x_ν innerhalb 2σ | **nein** |
| B2 (blind) | r*/\|q\| = 0,52844 liegt 20,7 % unter ⅔. Direkt bei r = ⅔\|q\|: off_Im = −0,0207 statt x. Nächste Rahmenzahl: 1/γ_L (−1,5 %) | ⅔ innerhalb 2σ_r | nein |
| C (blind, Bericht) | r*/\|q\| läuft von 0,66739 (q → 0) bis 0,4388 (q = −0,3). x_ν,pred liegt nur für \|q\| ≲ 0,003 innerhalb 2σ. Für **kein** q ist x global | — | — |
| C (blind, Bericht) | Expliziter Zusatz ε·cos 3δ nur im Im-Sektor bei r = ⅔\|q\|: kein ε in [−0,01; 0,01] gibt x | — | ein Ladungsterm der Größe α (≈ 0,0073) reicht nicht |

**Gesamturteil nach Vorab: widerlegt** (B1 nein, B2 nein).

## Lesart
- **φ ist der Mittelwert der beiden Versätze (A1, exakt).** Zusätze, die nur von δ abhängen, gehen nicht in die Bedingung für φ ein. Ob sie symmetrisch sind oder den Tausch
  brechen, ist dafür gleich: An jedem Gleichgewicht ist φ der Mittelwert der beiden Sektor-Versätze. Die Daten verlangen φ* = 0,0415 ± 0,0011, und der Abstand x_ν − x
  (1,78σ, H213) ist genau die doppelte Verschiebung der Versätze gegen φ. Ein Brecher müsste also in φ selbst eingreifen oder große Verschiebungen in δ erzeugen.
- **Spontaner Bruch geht nur lokal.** Ein symmetrischer Spektralterm (cos 3δ und cos 6δ mit passendem Verhältnis) kann x zu einem stationären Punkt mit Partner π/4 − x machen.
  Die Ergänzung zu H225: Dort hieß es, ein symmetrisches Potential könne x nicht wählen. Das gilt für das globale Minimum. Ein lokales Minimumspaar ist möglich.
  Global ist x aber in keinem geprüften Fall. Mit dem festgelegten q = −0,0852 liegt die Neutrino-Vorhersage zudem 22,8σ daneben.
- **Das ⅔ aus der führenden Ordnung trägt nicht.** Bei q → 0 liegt r/|q| bei 0,66739 (0,11 % neben ⅔). Bei endlichem q fällt das Verhältnis stark ab, auf 0,528 bei q = −0,0852.
  Es war ohnehin durch die führende Ordnung angeregt (in der Vorab offengelegt).
- **Ein kleiner Ladungsterm genügt nicht.** Ein Zusatz nur im Im-Sektor (geladene Leptonen) in der Größe der Feinstrukturkonstante verschiebt den Versatz nicht bis x.
- **Wiederkehrendes Muster.** Wie bei H226 (T1) wird x höchstens ein **lokales**, stabiles Minimum. Das stützt die Lesart „φ als metastabiles Vakuum oder Anfangsbedingung“
  (H226, H231). Eine Weggabel für den Autor ist offen, siehe unten.

## Hergeleitet, gesetzt, nachträglich
- **Hergeleitet/gerechnet:** A1 (symbolisch, exakt), führende Ordnung A2, r*(q), x_ν,pred, Globalität (numerisch, zwei unabhängige Rechnungen).
- **Gesetzt:** Modell H225 (Zirkulantensektor, Baumniveau, K = ⅔, H99, α′_ν = −1), q = −0,0852 (H167), q < 0, Spektralterme nur über cos 3δ, Grad ≤ 2 in c.
- **Nachträglich:** Dass x in **keinem** q global ist und der Ladungsterm nicht reicht, stand nicht als Kriterium in der Vorab-Notiz (nur Bericht unter C).
  Ein Hinweis zur Python-Kontrolle von A1: Sie ist nur auf den Datenzweigen aussagekräftig. Dort stimmt sie auf 2·10⁻¹⁶. In den anderen Zeilen liegen die Minima auf
  anderen Zweigen. Die Versätze sind dort gegen die Datenzweige gemessen und ohne Bedeutung.
- **Wolfram-Hinweis:** NMinimize (Differential Evolution) blieb im Re-Sektor einmal bei −1,0364 hängen. Das Datenminimum liegt tiefer, bei −1,06017. Die Globalität in δ
  prüft Python auf einem Gitter mit 8000 Punkten.

## Grenzen
Nur Spektralterme bis Grad 2 in cos 3δ und ein linearer Ladungsterm. Höhere Grade mit freien Koeffizienten können mehr Werte treffen und wären angepasst. Keine
Quantenkorrekturen. Kein Guard berührt; OP3/OP4 offen.

## Dateien
`Vorab_H232_Rueckwaerts_Brecher.md`, `k446_test_h232.py`/`k446_out.txt`, `k446b_gegenprobe.wl`/`k446b_out.txt`, `README.md`.

Vergeben: H232, k446. Nächste frei: H233, k447 (vor Vergabe gegen `main` prüfen).
