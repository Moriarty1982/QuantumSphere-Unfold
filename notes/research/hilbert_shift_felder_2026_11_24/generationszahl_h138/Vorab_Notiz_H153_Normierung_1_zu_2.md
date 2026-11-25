# Vorab-Notiz H153: Zieht eine algebraisch begründete 1:2-Normierung den skalenfreien Fluss auf K = ⅔?

**25.11.2026, vor jeder Rechnung committet.** Anlass: Autor „erst die normierung“ (nach H152). Skalenfrei; die Normierung muss aus der Algebra begründet sein und darf nicht
angepasst werden; Vorzeichen werden nicht gesetzt; der Term sechster Ordnung bleibt zurückgestellt. Vergeben: H153, Skripte k336 (Python) und k336b (Wolfram). Qiskit nicht
vorgesehen. Kein HDL/MMA-Vergleich.

## Vorwissen geprüft
- H150 (k333): Bei gleicher Komponentenzahl n_A = n_B ist der Tausch eine Symmetrie des Flusses; Start auf λ_A = λ_B, κ < 0 gibt K = ⅔ exakt (n = 1 und n = 2).
  Bei 1 gegen 2 Komponenten: K 0,6667 … 0,6778, startabhängig.
- H151 (k334): Fixstrahlen (1, 2): 10/9 (κ = 0), 1 (κ = 2λ, volle Norm), 0,8008; kein Fixstrahl mit κ < 0; Grenzwert K* = 1/3 + √10/9.
- H152 (k335): vollständiger Ansatz, δ nur 0 oder π/3.
- H149: Ψ = cos θ + sin θ·U mit einer einzigen Einheit U = w⊗n(δ); die Unteralgebra {1, U} ≅ ℂ; der Tausch J ist dort exakt.
- r13/k255: Auslesung g_k = 1/√3 + √(2/3)·w⊗f_k; die g_k sind orthonormal, (φ, y) ↔ (c₀, c₁, c₂) ist eine Drehung.

## Vorüberlegung (vor der Rechnung festgehalten)
Eine Normierung kann zweierlei sein: (i) eine Umparametrisierung der Felder bzw. Kopplungen. Sie ändert die Physik des Flusses nicht, sondern nur, welche Startwerte
„symmetrisch“ heißen; das ist eine Wahl der Anfangsbedingung. (ii) Eine Änderung, über welche Komponenten die Schleife läuft, also der Freiheitsgrade. Nur (ii) ändert
die β-Funktionen.

## Kandidaten (vorab fest, keine Anpassung)
- **N1 Komponentenzahl:** Kopplungen je Komponente normiert, A/n_A und B/n_B; symmetrischer Start heißt λ_A·n_A² … also λ_A^phys = λ, λ_B^phys = λ/4, κ^phys = κ̂/2.
- **N2 Spur der Auslesung:** Gewichte 1/3 (Einheit) und 2/3 (Kopien) aus g_k; symmetrischer Start in A/(1/3) und B/(2/3): λ_A^phys = 9λ, λ_B^phys = (9/4)λ, κ^phys = (9/2)κ̂.
- **N3 dritte Kopie:** Die Kopien-Norm über alle drei Kopien gezählt, Σ_k (y·f_k)² = (3/2)B; symmetrischer Start in A und (3/2)B: λ_B^phys = (9/4)λ, κ^phys = (3/2)κ̂.
- **N4 Unteralgebra {1, U}:** Die Schleife läuft nur über die von Ψ erzeugte Unteralgebra ℂ (n_A = n_B = 1); die Richtung in der Ebene (δ) ist dabei fest. Das ist eine
  Änderung der Freiheitsgrade (Art ii).

## Hypothesen und Kriterien
- **H153a (nicht blind, analytisch):** N1–N3 sind Umparametrisierungen (Art i): Der Fluss der physikalischen Kopplungen und die GW-Richtung sind dieselben wie in H150;
  nur die Startlinie ändert sich. *Kriterium:* symbolisch (Fluss kovariant unter der Umskalierung). Bestätigt, wenn exakt.
- **H153b (gewertet):** Für N1, N2, N3 je Gitter λ ∈ {0,05; 0,1; 0,2; 0,3}, κ̂/λ ∈ {−1,9; −1,5; −1,0; −0,5; −0,2; −0,1}: K am GW-Punkt. *Kriterien:* (1) startunabhängig,
  wenn Streuung < 10⁻³; (2) Treffer, wenn |K − 0,666661| < 2,1·10⁻⁵ (3σ); (3) θ stabil, wenn |θ − π/4| < 0,01. Vorhersage: keine der drei ist startunabhängig oder
  trifft; die Mittelwerte liegen bei verschiedenen K, weil die Startlinie den Kondensationspunkt verschiebt.
- **H153c (gewertet):** N4 (n_A = n_B = 1): Vorhersage K = ⅔ exakt und startunabhängig auf der ganzen Klasse κ < 0, θ = π/4 exakt (H150c). *Kriterium:* alle Punkte innerhalb
  10⁻⁹. Dazu ehrlich: N4 friert δ ein und ist eine Setzung über die Freiheitsgrade.
- **H153d (gewertet):** δ. Vorhersage: Keine Normierung wirkt auf δ, weil alle nur die Normen A und B umgewichten und die Z₃-Struktur der Ebene nicht berühren.
  *Kriterium:* mit ξ ≠ 0 (H152) landet δ für N1–N3 weiter auf 0 oder π/3; Stichprobe je Normierung 12 Punkte.

## Grenzen
- Eine Schleife, ohne Eichfelder. Die vier Kandidaten sind die, die sich ohne Anpassung aus der Algebra begründen lassen; weitere sind nicht ausgeschlossen.
- OP3 offen; kein Vorzeichen gesetzt; kein Guard wird berührt.
