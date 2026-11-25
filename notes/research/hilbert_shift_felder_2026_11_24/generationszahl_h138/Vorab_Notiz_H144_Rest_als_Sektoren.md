# Vorab-Notiz H144: Trägt die Rest-Generation die anderen Sektoren (Licht, Tachyon) bzw. die anderen Frames?

**Stand:** 25.11.2026, vor der Rechnung festgelegt. **Teilweise nicht blind:** H144a und H144b folgen analytisch (Begründung unten) und
werden nur nachgerechnet; offen und gewertet sind H144c und H144d. Anlass: Autor (25.11.2026, 20:21): „was wäre, wenn diese Generation jetzt
quasi die Generationen für die anderen Sektoren hält?“ Lesart (über den Koordinator): Die drei Kopien bilden den Materiesektor, die
Rest-Generation aus H142/H143 trägt Licht bzw. Tachyon oder die Frames T, P. Vorgabe: Vorzeichen nicht setzen; vor einem „widerlegt“ prüfen,
ob richtig in den Materie-Frame übertragen ist.

## Vorwissen geprüft
- **Sektorregel (T3, v4.8.0-r06/r07):** s = z₁² + z₂² + z₃² (komplex bilinear, ohne komplexe Konjugation); Materie s > 0, Tachyon s < 0,
  Licht s = 0. Für das Riemann–Silberstein-Feld F = E + iB ist s = F·F = |E|² − |B|² + 2i E·B. Gesamtbild: Positive und negative s gleichen
  Betrags verbindet die Dualität; z ↦ iz ist die elektromagnetische Dualität (r07), keine Wick-Drehung.
- **Frame-Abbildungen wirken über den C-Faktor** (v4.9.0-r51/H35, zusammengefasst in `../../op3_frame_map_generations_2026_11_15/README.md`):
  Tachyon-Abbildung z ↦ iz lässt jeden Sektor, Ladung und Chiralität fest; Zeitumkehr z ↦ z̄ tauscht die Ports bzw. Chiralitäten.
  Frames und Generationen liegen auf verschiedenen Tensorfaktoren von C ⊗ H ⊗ O (Erkundung 15.11.); v4.10.0-r19: Die Frame-Abbildungen wirken
  auf gesetzten Kopien nicht, der Kopienanteil ist M_n(C).
- **„Eine Algebra je Frame, die vierte als Betrachter“** (`../../op3_frame_algebras_observer_2026_11_16/`, Erkundung): vier Kopien als Kleinsche
  Vierergruppe {1, R, T, J_B}. Andere Ebene (HS(8), Kopienindex), hier nicht übernommen, im Ergebnis eingeordnet.
- **H138–H143** (dieser Ordner): Kopien O_v ⊂ ℂ⊗A₅, Ladung Q_v = ½ − (i/6)L_u − (i/3)R_u; Rest = Kern K der Summenabbildung; ladungsstabiler
  Teil W = eine Generation (H142, H143); leckende Zustände mit gestauchter Ladung ½ bzw. irrational (H143).

## Setzung (offengelegt)
Der komplexe Faktor ℂ von ℂ⊗A₅ wird als der C-Faktor der Frames gelesen (wie r51): Ein Zustand x = E + iB mit reellen E, B ∈ A₅ (je Träger).
Zwei Lesarten der Sektorgröße, beide berichtet:
- **N(x) = Σ_a x_a²** über alle 2ⁿ Koordinaten (bilineare Norm q q̄ ohne komplexe Konjugation);
- **s(x) = Σ_{a≥1} x_a²** nur über den Imaginärteil (T3 wörtlich, F = Im-Vektor).
Für Kernzustände wird über die Träger summiert (im Bild Φx = 0 wäre alles trivial null). Eine Phase x ↦ e^{iφ}x (Dualität) dreht N, s um
e^{2iφ}; invariant sind nur |N|, |s| und „null oder nicht null“. Für einen entarteten Eigenraum mit Basis X werden die Takagi-Werte
(Singulärwerte von XᵀX) berichtet; alle null heißt: der Raum ist total lichtartig.

## Hypothesen und Kriterien
- **H144a (nicht blind, analytisch):** z ↦ iz und z ↦ z̄ wirken trägerweise und erhalten K. Daher bildet keine Frame-Abbildung eine
  Kopien-Generation (Träger auf einem C_k) auf die Rest-Generation (Kernzustände, Träger auf ≥ 3 Kopien) ab. z ↦ iz lässt W und alle Ladungen
  fest; z ↦ z̄ bildet W auf sich ab mit q ↦ 1 − q, und das ist genau der globale Vorzeichenwechsel der Orientierung (1 − Q_v = Q_{−v}).
  Bestätigt, wenn numerisch ‖P_{conj W} − P_W‖ < 10⁻¹⁰, Spektrum gespiegelt, und jeder W-Zustand Gewicht auf mindestens drei Trägern hat.
- **H144b (nicht blind, analytisch):** Exakte Ladungseigenzustände mit q, q′ haben N(x, y) = 0, außer q + q′ = 1 (aus der Antisymmetrie von
  L_u, R_u). Also ist jeder Zustand mit q ≠ ½ unter N lichtartig, in Kopien-Generation und Rest-Generation gleich; Quarks (Farb-Triplett) haben
  keinen e₀-Anteil, also auch s = 0. Bestätigt, wenn numerisch alle Takagi-Werte der q-Eigenräume ≠ ½ unter N < 10⁻¹⁰ sind (Kopie und W).
- **H144c (gewertet, die eigentliche Frage):** Unter s (Imaginärteil, T3) unterscheiden sich Kopien- und Rest-Generation im Leptonteil:
  Eine Kopie hat |s| = ½ für die Zustände q = 0 und q = 1 (analytisch, (e₀ ± iu)/√2). **Vorhersage:** Die Rest-Leptonen (q = 0, 1 in W) sind
  **lichtartig** (|s| < 10⁻⁶), weil sich die reellen Anteile der Träger im Kern aufheben (H142-Mechanismus, Σ c_k = 0). Bestätigt, wenn das in
  allen Generationsklassen (H142: 9 Auswahlen; H143: beide Klassen mit n_gen = 1) gilt; widerlegt, wenn |s| > 10⁻⁶ in einer Klasse.
- **H144d (gewertet, Leck als Sektor):** Die leckenden Zustände (K ⊖ W, gestauchte Ladung ½ oder irrational) sind **nicht lichtartig** unter N
  (jeder Takagi-Wert > 10⁻⁶) in allen geprüften Klassen (H141, H142, H143). Zusammen mit H144b hieße das: ladungsstabil ⇔ lichtartig (unter N),
  Leck ⇔ s ≠ 0. Widerlegt, wenn ein leckender Zustand lichtartig ist.

## Folge, vorab festgelegt
- c bestätigt: Unter der wörtlichen Sektorregel liegt die Rest-Generation ganz im Lichtsektor (s = 0), die Kopien-Generationen haben dagegen
  nicht lichtartige Leptonen. Das wäre eine Lesart „Rest = Lichtsektor-Generation“, keine Herleitung; Tachyon und Materie unterscheidet die
  Größe ohnehin nur bis auf die Dualitätsphase (Vorzeichen offen).
- c widerlegt: Die Rest-Generation hat dieselbe Sektorsignatur wie die Kopien; sie ist dann unter dieser Setzung kein eigener Sektor.
  Vor dem Urteil wird geprüft, ob die Übertragung in den Materie-Frame der Kopie stimmt (gleiche Träger, gleiche Ladungskonvention).
- d bestätigt: Das Ladungsleck lässt sich als Austritt aus dem Lichtsektor lesen (Lesart). d widerlegt: Leck und Sektor sind unabhängig.
- Was in keinem Fall folgt: die physikalische Gleichheit der Sektoren (T1 bleibt Vermutung), Massen, Mischung, ein Vorzeichen. OP3, OP4 offen;
  kein Guard berührt.
- Werkzeuge: Python (numpy) für alle Klassen; Wolfram Language exakt für die Leptonwerte einer Auswahl je Klasse. Qiskit nicht eingesetzt
  (keine Schaltung).
- Vergeben: H144, k327.
