# Vorab-Notiz H122: Bestimmt die Auslese ihren Rahmen selbst? (Q1b, OP1 Lesart B und OP5 Ausleseseite)

**Stand:** 23. November 2026, vor der Rechnung festgelegt. Anlass, Autor (23.11.): „Q1 Auslesegesetz“, dann Wahl des Zweigs „Q1b Rahmen und
Achse“ (statt Q1a Orientierung). **Teilweise nicht blind:** H122a ist Lehrbuchwissen (Minimum der Energiedichte im Rahmen E ∥ B); für einzelne
Moden sind H122b und H122c aus r46.3 absehbar (Ordnung b² mit verschiedenen Vorzeichen; entlang der Achse ein Term −b²k_z²). **Blind** sind die
Aussagen für exakte Boosts in allen Ordnungen und für die Mittel über das Azimut und über isotrope Richtungen von k.

## Frage
Q1b fragt nach einem gemeinsamen Datum (Ruhesystem u, Achse n) der Auslesen von OP1 (Lesart B) und OP5 (Ausleseseite). r48.2 nennt beide
„verwandt, nicht gleich“: Bei OP1 gehören Ruhesystem R und Achse dem Feld, beim Vergleichsmodell die Achse dem Detektor. Schärfer gefragt:
**Legt die Auslese ihren Rahmen selbst fest**, als Extremum der in u quadratischen Auslese über alle Beobachter, entartet genau unter Boosts
entlang der Achse? Ist das bei beiden so, gehört der Rahmen in beiden Fällen dem ausgelesenen Feld; sonst ist er bei OP5 eine äußere Setzung.

## Vorwissen geprüft
- r46 (`notes/research/op5_readout_branch_2026_11_23/readout_branch.wl`, Ausgabe `run/readout_branch.txt`): Kopplung
  L = −h Π^{μν} u^α u^β R^{(1)}_{μανβ}, Π transversal zu n im Ruhesystem von u; Fierz–Pauli-Zähler N; statisch N = ⅔a² (a = k_⊥²); Detektorbewegung
  entlang der Achse: N = ⅔a(a − b²k_z²) + O(b⁴), quer: ⅓a²(2 + b² + b² cos 2φ) + O(b⁴); Zeitorientierung fällt heraus (r46.2).
- r48 (`notes/research/op1_op5_readout_compare_2026_11_23/`): OP1-Auslese |E′|² + |B′|² = (E₀² + B₀²) cosh 2η quer zur Achse, 1 entlang;
  φ = sech 2η; Zuordnung „n = E∥B-Achse, u bezogen auf R“ benannt, nicht geprüft.
- r49: R als Bezugssystem der Verlangsamung verlangsamt nur quer zur Achse; mit c_h² = 1 (W2) No-go der gerichteten Kopplung.
- r45.4: Weggabelung Feldseite (H) gegen Auslese (B); `notes/research/op_cross_map_2026_11_23/` (Querschnitt Q1); r53 (Q1a, Orientierung,
  hier nicht Gegenstand); `notes/research/op1_two_readings_2026_11_17/` (Lesart B: φ = sech 2η als Beobachtergröße).
- Zurückgestellte Ideen: I1 (String liefert Rahmen und Achse, r37) ist hier nicht Gegenstand; kein Auslöser neu getroffen.

## Aufbau
- **OP1:** F mit E ∥ B entlang z im Ruhesystem R, E₀, B₀ > 0. Beobachter u = Λ(η, d)·(1, 0, 0, 0) für jede Boostrichtung d (Einheitsvektor)
  und Rapidität η. Auslese Q_F(u) = |E′|² + |B′|² (= 2 T_uu).
- **OP5:** Funktionen von r46 unverändert (`Riem`, `src`, `fp`, `contr`, `PiProj`). Statische Mode der Präparation k = (0, k₁, k₂, k₃) im Ruhesystem
  u_p der Präparation; Detektorrahmen (u, n) = Λ(b, d)·(u_p, e_z), also u und n mit demselben reinen Boost. Auslese N(b, d; k).
- Mittel: (i) über das Azimut von k_⊥ bei festem k₃ und a; (ii) isotrop über die Richtungen von k bei festem |k|.
- Werkzeug: Wolfram Language (exakt, symbolisch; Reihen und exakte Ausdrücke in b). Qiskit nicht geeignet (keine Quantenschaltung); kein HDL-
  Vergleich (kein endlicher Auswahlablauf). Skript `llm/h122_readout_extremum.wl`, Ausgabe `llm/h122_readout_extremum.txt`.

## Hypothesen und Kriterien
- **H122a (OP1, nicht blind):** Q_F(u) − Q_F(R) ≥ 0 für alle u, mit Gleichheit genau für Boosts entlang z. Kriterium: exakter Ausdruck für
  beliebiges d; Hessesche bei η = 0 positiv semidefinit mit Kern genau in Richtung z.
- **H122b (OP5, Ruhesystem als Extremum):** u_p ist ein Extremum von N über Detektorboosts: N(b, d) − N(0) hat für alle b ∈ (0, 1) und alle d
  dasselbe Vorzeichen. Geprüft (i) mode-weise, (ii) im Azimutmittel, (iii) im isotropen Mittel. **Bestätigt** in einer Stufe, wenn das
  Vorzeichen dort für alle d gleich ist; **widerlegt**, wenn es zwei Richtungen mit verschiedenem Vorzeichen gibt (Sattel).
- **H122c (OP5, Achse als Entartungsrichtung):** Es gibt eine Richtung d*, für die N(b, d*) = N(0) für alle b gilt, und d* = e_z (die Achse).
  Geprüft in denselben drei Stufen. **Bestätigt** in einer Stufe, wenn d* = e_z das leistet; **widerlegt** sonst.

## Folge, vorab festgelegt
- **Trägt:** H122a bestätigt und H122b, H122c im isotropen Mittel bestätigt. Dann legt in beiden Fällen die Auslese ihren Rahmen als Extremum
  fest, und die Achse ist die Entartungsrichtung; die Zuordnung aus r48.2 wäre als gemeinsames Gesetz gestützt (nicht hergeleitet).
- **Trägt teilweise:** H122a bestätigt und genau eines von H122b, H122c im isotropen Mittel bestätigt.
- **Trägt nicht:** H122a bestätigt, H122b und H122c im isotropen Mittel widerlegt. Dann ist der Rahmen bei OP1 ein Extremum des Feldes, bei OP5 eine
  äußere Setzung des Detektors: ein struktureller Unterschied, schärfer als r48.2 („verwandt, nicht gleich“).
- H122a widerlegt (nicht erwartet): Lesart B von OP1 ist neu zu prüfen.
- In jedem Fall bleiben OP1, OP5 und Q1 offen; die Mode-weisen Ergebnisse werden berichtet, entscheiden aber nicht.
