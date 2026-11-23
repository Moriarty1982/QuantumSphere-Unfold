# Methoden-Notiz: Zweig B, Rahmen, Achse und Orientierung als Daten der Auslese (Erkundung, vor der Rechnung festgelegt)

23. November 2026. Auftrag des Autors: „Zweig B: Auslese“ nach der Bilanz in Runde v4.10.0-r45. Keine H-Nummer.
**Teilweise nicht blind:** Von Hand ist absehbar, dass u in der Kopplung quadratisch steht (B2) und dass der führende statische Term nicht von
r_m abhängt (r35.2). Die Zerlegung (B1) und die Abhängigkeit von der Detektorbewegung (B4) sind nicht vorab gerechnet.

## Strenges Raster (aus r45)
Zweig B zählt nur als Fortschritt, wenn die Zahl der gesetzten Eingaben sinkt, ohne dass eine neue dazukommt, und wenn er etwas vorhersagt,
das über N_m hinausgeht. Gesetzte Eingaben nach r45: (i) gerichtete Kopplung mit Rahmen u und Achse n, (ii) verlangsamte Ausbreitung r_m,
(iii) Zahlenwerte (r_m, g_m, m); dazu die offene Frage der Zeitorientierung (r40–r44, H118).

## Vorwissen geprüft
- `../op5_bifocal_response_2026_11_18/OP5_J_Lokale_Antriebswirkung.md`: Kopplung 𝓛_γ = −hP^{ij}R⁽¹⁾_{0i0j}[γ] mit Vorzeichenkonvention und
  δT^{00} = P^{ij}∂_i∂_jh, δT^{0i} = −P^{ij}∂_t∂_jh, δT^{ij} = P^{ij}∂_t²h; dort schon der Hinweis auf eine kovariante Fassung
  −hU^μU^ρP^{νσ}R_{μνρσ} („ein möglicher“ Vergleich).
- r45.1: Der kovariante Fierz–Pauli-Zähler dieser Quelle ist genau N_m; die Zeit-Quer-Komponenten koppeln.
- r35.2: Das führende statische Glied hängt nicht von r_m ab. r32.4: Der gerichtete Kontrast wird im statischen massiven Vergleich
  f = Δ_⊥H/m² ausgelesen. r38.2: geisterfrei für g_m² < 3, statisch stabil genau für g_m² ≤ 3r_m.
- OP1, Lesart (B): Die Breite ist eine Beobachtereigenschaft; H118: Das Oktant-Vorzeichen ist eine Zeitorientierung der Auslese.

## Werkzeug
Wolfram Language exakt (linearisierte Krümmung, Fourierbild, Fierz–Pauli-Kontraktion, Lorentz-Boosts). Qiskit nicht geeignet.
Skript `readout_branch.wl`, Ausgabe `run/readout_branch.txt`.

## Rechnung
- **B1 Auslese-Form:** Kovariante Kopplung 𝓛 = −h Π^{μν}u^αu^βR⁽¹⁾_{μανβ}[γ] mit Π^{μν} = −η^{μν} + u^μu^ν − n^μn^ν (räumlicher Projektor quer
  zu n im Ruhesystem u). Quelle S^{μν}(u, n, p) als Koeffizient von γ_{μν}. Prüfen: (a) im Ruhesystem gleich der Quelle der bifokalen Notizen,
  (b) Zerlegung Π^{μν}u^αu^βR_{μανβ} = Ricci-Anteil R_{uu} plus Achsen-Gezeitenanteil E_{nn} = R_{μανβ}n^μu^αn^νu^β (Vorzeichen nach
  Rechnung), (c) Fierz–Pauli-Zähler beider Anteile einzeln und gekreuzt: Woher kommt N_m?
- **B2 Orientierung:** Quelle und Zähler unter u ↦ −u und unter ω ↦ −ω.
- **B3 Rolle von r_m:** statischer Zähler g_m²N_m/d_m bei x = 0 für allgemeines r_m, Entwicklung für q ≪ m²; Stabilitätsbedingungen aus
  r38.2 bei r_m = 1 mit g_m² = 3/100.
- **B4 Vorhersage, Bewegung des Detektors:** Quelle im Ruhesystem der Präparation statisch (ω = 0, Wellenvektor k), Detektor mit
  u = γ(1, βe), e parallel zu n und e senkrecht zu n. Fierz–Pauli-Zähler N(β) und seine Entwicklung bis β². Im Zweig (H) ist u an ein
  Medium gebunden und hängt nicht vom Detektor ab; eine nichtverschwindende β-Abhängigkeit unterscheidet die Zweige messbar.

## Raster (vorab)
- **trägt:** B1 (a) gilt und N_m lässt sich einem Auslese-Anteil zuordnen; B2: Die Orientierung fällt heraus; B3: r_m ist für den
  führenden Kontrast entbehrlich und r_m = 1 ist zulässig; B4: Die Abhängigkeit von der Detektorbewegung ist nicht null. Dann sinken die
  Setzungen auf {Existenz der Kopplung, g_m, m}, mit u und n als Auslesedaten, und es gibt eine unterscheidende Vorhersage.
- **trägt teilweise:** B1 gilt, aber mindestens eine der Bedingungen B2–B4 nicht (etwa r_m wesentlich oder keine β-Abhängigkeit).
- **trägt nicht:** Die Kopplung lässt sich nicht als Auslese-Funktional von (u, n) schreiben, oder N_m braucht eine Struktur der Feldseite.

Frames: Materie-Frame M; u ist der Rahmen der Auslese (Detektor), n seine Messachse. Tachyon-Abbildung und Zeitumkehr werden nicht verwechselt.
OP5 bleibt offen.
