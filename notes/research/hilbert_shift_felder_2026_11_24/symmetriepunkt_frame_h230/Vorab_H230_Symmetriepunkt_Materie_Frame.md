# Vorab-Notiz H230 (k444): Symmetriepunkt π/8 (und 0) in den Materie-Frame übertragen

Stand 28.11.2026, vor der Rechnung festgeschrieben. Nach H229 hat der Autor um 13:43 UTC gefragt, ob sich ein Grund finden lässt, warum φ so sein muss.
Von den drei vorgeschlagenen Richtungen wählte er um 13:45 UTC die dritte: „dann erst was noch fehlt, dann können wir das zumindest schon mal ggf. anhaken“.
Gemeint ist der Symmetriepunkt π/8, der im Ruheframe R liegt. Er wurde bisher direkt mit dem Messwert verglichen, der im Materie-Frame M gemessen wird.
Die Regel des Projekts verlangt aber, vor einem Vergleich die Frame-Abbildung anzuwenden. Dieser Schritt wird hier nachgeholt.

## Vorwissen geprüft

- H225/k439: Minimum der gemeinsamen Vakuumenergie bei φ_R = π/8 (Sektortausch exakt). H229/k443: Minima bei π/12, π/6 oder π/8.
  0 ist der Punkt ohne Drehung (H221).
- H166d (`delta_h166/`): Die Maske D = exp(εW) mit W = diag(0, 0, −3) und festem ε₀ = artanh β_sym wurde in den Formen K (DCD) und linear auf die
  Brannen-Matrix mit δ₀ ∈ {0, π/12, π/6, π/4, π/3, φ₁/3} angewandt. Es gab keinen Treffer, und Form K verletzt K = ⅔ (K′ = 0,744). Form S (Ähnlichkeit)
  lässt δ in jedem Frame gleich. **Damit ist der Punkt φ_R = 0 für beide Sektoren (δ₀ = π/12 und π/6) mit ±ε₀ schon gerechnet.** Hier wird er nur zur
  Kontrolle wiederholt und nicht gewertet.
- H45/H134: Maske D = exp(εW_l) für die Mischung. H224/k438: Wigner-Drehungen aus Frame-Boosts, kein Treffer (nächster 118σ). H228/k442: Die Operationen
  B (tan θ ↦ β_sym tan θ) und G (tan θ/γ_L) kamen nur als Schleifenbausteine vor; ihre Bilder des Symmetriepunkts wurden nicht ausgewertet.
- Frames nach Konvention F; Tachyon-Abbildung z ↦ iz und Zeitumkehr z ↦ z̄ nicht verwechseln (r51, r81).

**Teilweise nicht blind:** Bei der Planung wurden vier Werte von Teil B im Kopf überschlagen: Aberration von π/8 mit β_sym ergibt 0,214 bzw. 0,706, die
von 2φ = π/4 ergibt φ′ = 0,220 bzw. 0,655. Keiner liegt nahe x. Alle übrigen Werte sind nicht vorab gerechnet.

## Ziel

x = 0,0395773407 (σ 7,8·10⁻⁷) im Im-Sektor, x_ν = 0,04336 ± 0,00213 im Re-Sektor. Datenzweige δ_Im = π/12 − φ und δ_Re = π/6 − φ (H222).

## Teil A: Spektrum-Abbildungen (Maske nach H166)

R-Spektrum je Sektor: Brannen-Matrix mit ρ² = ½ (K = ⅔) und δ₀ = π/12 − φ_R (Im) bzw. π/6 − φ_R (Re), für φ_R ∈ {π/8, 0}. Abbildungen: Form K, Form linear
und Form S, jeweils mit ε ∈ {+ε₀, −ε₀, +2ε₀, −2ε₀} (2ε₀ = arcosh γ_L). Auslesen von (K′, δ′) wie in H166 und Umrechnung in φ′ = π/12 − δ′ bzw. π/6 − δ′,
jeweils in der Spektralklasse.

*Treffer A:* |K′ − ⅔| ≤ 10⁻⁴ **und** φ′_Im innerhalb 2σ von x **und** φ′_Re innerhalb 2σ von x_ν.

## Teil B: Winkel-Abbildungen

Der Symmetriepunkt wird in drei Lesarten als Winkel genommen: θ = φ, 2φ (so tritt er in cos 2(δ − χ − φ) auf) und 3φ (kubische Invariante). Bei
φ_R = π/8 sind das π/8, π/4 und 3π/8. Abbildungen:

- Aberration cos θ′ = (cos θ ∓ β)/(1 ∓ β cos θ) mit β ∈ {β_sym, tanh 2ε₀}, also vier Abbildungen;
- Kontraktion tan θ′ = tan θ / γ mit γ ∈ {cosh ε₀, γ_L = cosh 2ε₀} und Streckung tan θ′ = γ tan θ, also vier;
- Maske tan θ′ = β tan θ mit β ∈ {β_sym, tanh 2ε₀} und die Umkehrung, also vier;
- Lichtpunkt P (β → 1) und Dual-Frame T (z ↦ iz, θ ↦ θ + π/2) als Grenzfälle; sie liefern nur 0, π oder rationale Vielfache von π und werden nur berichtet.

Das sind 12 Abbildungen × 3 Lesarten = 36 Kandidaten für φ′ = θ′/n. Der Punkt 0 ist unter allen Abbildungen fest (θ′ = 0) und wird nur vermerkt.

*Treffer B:* φ′ innerhalb 2σ von x. Da der Versatz gemeinsam ist, gilt dann auch x_ν (1,78σ, H213).

*Lockerer Treffer (nur Bericht):* φ′ innerhalb 1 % von x. Die Zufallserwartung wird aus der Verteilung der 36 Bilder angegeben.

## Urteil

- *trägt:* ein Treffer A oder B;
- *trägt teilweise:* kein strenger Treffer, aber mehr lockere Treffer als die Zufallserwartung (Poisson-Wahrscheinlichkeit < 5 %);
- *widerlegt:* sonst. Dann ist der Schritt „Symmetriepunkt in den Materie-Frame übertragen“ erledigt und abgehakt.

## Werkzeuge

Python `k444_test_h230.py` (numpy, Ausgabe `k444_out.txt`); Wolfram `k444b_gegenprobe.wl` (Ausgabe `k444b_out.txt`): Teil B exakt und symbolisch, Teil A
für Form K über die Eigenwerte von DCD unabhängig. Qiskit ist nicht geeignet.

Vergeben: H230, k444.
