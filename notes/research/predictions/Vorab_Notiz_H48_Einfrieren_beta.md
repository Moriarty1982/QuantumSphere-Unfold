# Vorab-Notiz H48: β_sym als eingefrorene Länge des M/T-Zustands (frühe dichte Phase mit Einstein–Cartan-Spinterm)

Festgelegt am 2026-10-28, **vor** jeder Rechnung dieser Notiz. Autor: „mach das“ (auf den Vorschlag, H48 als Einfrieren in der dichten
Frühphase mit Einstein–Cartan-Spinterm zu testen). Bezug: r17 (γ_L = 1/|b|), r24 (R rein, P = I/2), r27 (Drehung plus Kompensator,
ein Kick aus R gibt den Hopf-Zustand), r28/r29 (Austausch mit dem Tachyon-Bezugszustand aus dem Vakuum), r30 (Kompensator kohärent),
r40 (hermitesche Energie frame-blind), r42 (Kompensator = Chiralitätsprojektor), r67 (Λ frame-unabhängig), r69 (absoluter Vakuumterm
nicht festgelegt). Skizze der gemeinsamen Dynamik: Gespräch vom 28.10. (Punkte 1–7).

## Frage

Kann β_sym aus einer Dynamik folgen statt eingesetzt zu werden? Getestet wird die kleinste homogene Reduktion der Skizze: Das M/T-Dublett
eines Spinor-Kondensats wird in der dichten Frühphase von Drehung, Kompensator-Messung und Austausch bewegt und friert ein, wenn die
Dichte fällt. Die eingefrorene Länge |b_∞| bestimmt β über r17: γ_L = 1/|b|, β² = (1 − |b|)/(1 + |b|).

## Modell (verbindlich)

Einheiten c = ħ = 1, Zeiteinheit 1/ω (ω = 1), κ = 8πG.

**Zustand.** Bloch-Vektor b = (b_x, b_z) auf der reellen Scheibe, |b| ≤ 1. R = (0, +1) (rein, r24), Tachyon-Bezugszustand
b_T = (0, −1) (Bild von R unter z → iz, r28). Kompensator-Achse x: C = ½(1 + σ_x) (r05), nach r42 zugleich Chiralitätsachse.

**Innere Dynamik.**

ḃ = ω J b − Γ_C P_z b − Γ_R (b − b_T)

- J: Drehung in der (x, z)-Ebene, J(b_x, b_z) = (b_z, −b_x) (Dualitätsdrehung, r27).
- P_z b = (0, b_z): nicht-selektive Kompensator-Messung dämpft die z-Komponente (r27, r30).
- Austausch mit dem Tachyon-Bezugszustand (r28, r29).
- Beide Raten sind Wechselwirkungen im Medium und proportional zur Teilchendichte: Γ_C = g n, Γ_R = r g n. Das Verhältnis r ist je
  Lauf fest.

**Geometrie.** Flaches FLRW, unimodular: Λ ist Integrationskonstante.

H² = (κ/3) ρ + Λ/3,  ρ = m n − e_EC · (3κ/16) J_A²,  J_A = n b_x,  n ∝ a⁻³.

- Die Teilchenzahl bleibt erhalten (Austausch ist Tausch, keine Netto-Erzeugung); m n ist hermitesch und hängt nach r40 nicht von b ab.
- Der Einstein–Cartan-Kontaktterm (Hehl–Datta) koppelt über die axiale Dichte J_A an b_x; Vorzeichen und Koeffizient 3κ/16 aus
  der Literatur übernommen, e_EC ∈ {0, 1} schaltet ihn ab bzw. an. Bei abweichender Literaturkonvention gilt der Literaturwert;
  angepasst wird nichts. Fällt ρ dabei auf 0 (Bounce), wird der Lauf ab dort nicht fortgesetzt und so gemeldet.
- H wird in jedem Schritt aus der Nebenbedingung berechnet (offenes System; Energieaustausch mit dem Reservoir wird nicht bilanziert).

**Anfang und Ende.** Start bei b = R, in der dichten Phase mit g n₀ ≫ 1. Integration über N = ln a, bis Γ_C < 10⁻⁸ und sich |b| je
e-Faltung um weniger als 10⁻¹⁰ ändert. |b_∞| = Mittel von |b| über die letzten 20 Drehperioden.

**Parameterraster (vollständig, nichts wird nachgeschoben).**
- r ∈ {0.5, 1, 1.157, 2}
- g n₀ ∈ {10², 10³, 10⁴}
- H₀ (Startwert von H, in Einheiten von ω) ∈ {10⁻³, 10⁻¹, 10, 10³}; daraus κ m n₀/3 = H₀² bei Λ = 0
- e_EC ∈ {0, 1}, mit Kontaktstärke (3κ/16) n₀²/(m n₀) ∈ {10⁻², 1} bei e_EC = 1
- Λ/3 ∈ {0, 10⁻⁶ H₀²}

## Prüfungen und Kriterium

**A (Struktur, Hauptfrage).** Für jedes r: Liegen alle |b_∞| des Rasters innerhalb ±1 % (relativ) von r/(1 + r)?
- Ja für alle r: **H48 bestätigt** in dem Sinn, dass β nur noch von einem Ratenverhältnis abhängt: β² = 1/(1 + 2r). OP1 würde dann zu
  „r aus der Struktur herleiten“.
- Sonst: **H48 widerlegt** in dieser Form. Gemeldet wird, wovon |b_∞| abhängt (H₀, g n₀, e_EC, Λ).

**B (Einstein–Cartan).** Ändert e_EC = 1 |b_∞| um mehr als 1 % gegenüber e_EC = 0 bei sonst gleichen Parametern? Nur berichtet,
kein eigenes Kriterium.

**C (Λ).** Ändert Λ |b_∞| um mehr als 1 %? Nur berichtet. Erwartet nein (Λ wirkt erst spät).

**D (Zahl, nicht blind).** r = 1.157 entspricht |b| = 0.5363, also γ_L = 1.8644 und dem heutigen β_sym. Dieser Wert ist nachträglich
aus β_sym zurückgerechnet und **kein** Test. Eine Zahl für β wird nur geprüft, wenn r aus der Struktur folgt; dafür braucht es eine
eigene Vorab-Notiz.

## Offenlegung (Vorüberlegungen vor der Rechnung)

- Im dichten Grenzfall (Γ ≫ ω) ist der quasistationäre Zustand b* = (0, −r/(1 + r)) analytisch klar; |b*| = r/(1 + r), bei r = 1
  der Hopf-Zustand |b| = ½ (r27). Das ist die Erwartung, gegen die A prüft.
- Kopfschätzung: Fällt die Dichte, folgt b dem quasistationären Zustand, solange Γ ≫ H. Ist dann schon Γ ≲ ω, wird |b*| kleiner
  (≈ Γ_R/ω), und der eingefrorene Wert hängt davon ab, wann Γ ≈ H wird. Erwartet ist deshalb: A hält nur, wenn das Einfrieren
  vor dem Einsetzen der Drehung liegt (H ≫ ω beim Einfrieren), sonst hängt |b_∞| an H₀ und g n₀. Ich rechne eher mit **widerlegt**.
- Unbekannt ist mir, was der Einstein–Cartan-Term bewirkt: Er macht ρ bei hoher Dichte kleiner und kann H stark ändern; ob das den
  Einfrierpunkt strukturell festlegt, ist offen.
- Die Wahl Γ_R ∝ n (statt ∝ H) ist eine Modellentscheidung: Mit Γ_R ∝ H würde |b| wie a^(−const) gegen 0 laufen und nie einfrieren
  (P-Attraktor, r27). Diese Variante wird nicht gerechnet.

## Was ein Ergebnis bedeutet

Bestätigt A, ist β_sym in diesem Modell keine freie Zahl mehr, sondern eine Funktion von r; das Problem verschiebt sich auf r. Widerlegt A,
zeigt das, welche Größe den eingefrorenen Wert trägt, und dass ein dimensionsloser Wert wie β nicht aus dimensionsbehafteten Raten
allein folgt. Guards bleiben unverändert; nichts hiervon berührt C5, C6/T2 oder globale Abschlüsse.

Nach dem Commit dieser Notiz wird daran nichts mehr geändert.
