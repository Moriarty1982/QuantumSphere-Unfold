# Vorab H232 (k446): Rückwärtssuche nach dem Brecher des Sektortauschs

**Datum:** 2026-11-28. Vor der Rechnung geschrieben und committet. Anlass: Marc 13:43 („Grund statt Zufall“), Koordinator nach H231:
„Rückwärtssuche nach dem Brecher danach“. Werkzeuge: Python (`k446_test_h232.py`) als Hauptrechnung, Wolfram (`k446b_gegenprobe.wl`)
unabhängig, symbolisch für Teil A. Qiskit nicht einschlägig.

## Frage
H225: Die gemeinsame Vakuumenergie E(φ) beider Lepton-Sektoren ist unter dem Sektortausch V_Re(−δ; π/4 − φ) = V_Im(δ; φ) spiegelsymmetrisch um π/8.
H226 suchte vorwärts nach einfachen tauschbrechenden Termen (ohne Erfolg). Jetzt rückwärts: Was muss ein Term leisten, damit der Messwert
x = 0,0395773 das globale Minimum ist? Muss er den Tausch überhaupt **explizit** brechen?

Modell wie H225/H226: V_Im = −cos 2(δ − π/4 − φ) + P_Im(cos 3δ), V_Re = +cos 2(δ − φ) + P_Re(cos 3δ); die Spektralterme hängen von δ nur über die
Spektralinvariante c = cos 3δ ab (Klasse δ ~ δ + 2π/3 ~ −δ). Versätze: off_Im = δ_Im − 5π/4, off_Re = δ_Re − π/2 (Klassenvertreter der Datenzweige).
Daten: off_Im = x (σ 7,8·10⁻⁷), off_Re = x_ν = 0,04336 ± 0,00213.

## Vorwissen geprüft
H221 (Versatz ist ein Winkel), H222/k436 (Zweigwahl über das Vorzeichen von cos 3δ, gesetzt), H225 (Minimum bei π/8; Grenzen-Abschnitt: „eine Mischung aus cos 3δ und
cos 6δ mit freiem Verhältnis kann jeden Wert treffen und wird nicht gewertet“), H226 (vier vorwärts gewählte Brecher, widerlegt), H229 (Ordnung 6 mit dem festen
Verhältnis aus N², c₀ = 1/√2, Minima nur bei π/12, π/6, π/8), H213 (x_ν − x = 1,78σ). Neu hier: die Rückwärtsbedingung und die Frage, ob ein **symmetrischer**
Term den Tausch spontan brechen kann (entartetes Paar φ₀, π/4 − φ₀), mit dem schon festgelegten q = −0,0852 (H167).

## Teil A (nicht blind, analytisch)
- **A1 Stationaritätsbedingung.** Für jeden Zusatz, der nur von δ abhängt (in einem oder beiden Sektoren, symmetrisch oder nicht), gilt nach dem Hüllkurvensatz an jedem
  stationären φ: sin 2(off_Im − φ) = −sin 2(off_Re − φ), also off_Im + off_Re = 2φ (mod π/2). Folge: φ* = (x + x_ν)/2 = 0,04147 ± 0,00107, und der Daten-Abstand
  x_ν − x ist genau der doppelte Abstand der Versätze vom Modulus. Mit Wolfram symbolisch prüfen.
- **A2 Führende Ordnung.** Für kleine Spektralterme ist E(φ) = −2 + P_Im(cos(3φ − π/4)) + P_Re(sin 3φ). Für P_Im = P_Re = P ist E symmetrisch um π/8. Ein quadratisches
  P(c) = κ(c − c₀)² (das ist q cos 3δ + r cos 6δ mit c₀ = −q/(4r)) legt ein entartetes Minimumspaar (φ₀, π/4 − φ₀) — spontaner Bruch ohne expliziten Brecher.
  Für φ₀ = x gilt in führender Ordnung c₀ = 0,374590, mit q = −0,0852 also r/|q| = 1/(4c₀) = 0,667396. In führender Ordnung ist off_Re = off_Im, also x_ν,pred = x.
- **Offenlegung:** Diese Zahlen habe ich vor dem Schreiben dieser Notiz ausgerechnet. Dabei fiel auf: r/|q| liegt 0,11 % neben ⅔ (= K), c₀ 0,11 % neben ⅜.
  Der Kandidat r = ⅔|q| ist also durch die führende Ordnung angeregt, nicht vorab unabhängig. Blind sind nur die Korrekturen höherer Ordnung bei endlichem q.

## Teil B (blind): exakte Rechnung bei q = −0,0852
Exakte Minimierung in δ (global je Sektor) und in φ (global über eine volle Periode). Gesucht r* > 0 mit off_Im = x am globalen Minimum.
- **B1:** Gibt es r*, bei dem x das globale Minimum ist (entartetes Paar zulässig), der Datenzweig in beiden Sektoren global ist und x_ν,pred innerhalb 2σ (0,00213) liegt?
- **B2:** Liegt r*/|q| innerhalb 2σ_r von ⅔? σ_r wird aus σ_x fortgepflanzt. Zum Vergleich werden ½, 1/√2, β_sym, 1/γ_L, ¾ und 1 mit Abweichung angegeben.

## Teil C (blind, nur Bericht)
- r*/|q| für q = −0,001 … −0,3 (wie stabil ist das Verhältnis?).
- Wie groß müsste ein expliziter Zusatz ε·c nur im Im-Sektor (geladene Leptonen) sein, damit bei r = ⅔|q| genau x herauskommt? Vergleich |ε| mit α = 1/137.

## Entscheidung
- **trägt:** B1 ja und B2 ja (r = ⅔|q| gibt x innerhalb 2σ_x, x_ν innerhalb 2σ, alles global).
- **trägt teilweise:** B1 ja, B2 nein (der spontane Mechanismus wirkt, aber mit einem angepassten r; die offene Zahl wandert von φ zu r/|q|).
- **widerlegt:** kein r > 0 macht x zum globalen Minimum mit x_ν innerhalb 2σ.

## Gesetzt
Modell H225 (Zirkulantensektor, Baumniveau, K = ⅔, H99, α′_ν = −1), q = −0,0852 (H167), Vorzeichen q < 0, Spektralterme nur über cos 3δ, Grad ≤ 2 in c.
