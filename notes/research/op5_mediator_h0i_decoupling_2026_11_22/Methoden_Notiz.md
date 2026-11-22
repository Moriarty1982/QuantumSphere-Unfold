# Methoden-Notiz: Warum koppeln die Zeit-Quer-Komponenten H_0i nicht? (Erkundung, vor der Rechnung festgelegt)

22. November 2026. Auftrag des Autors: „H_0i-Entkopplung begründen“, nach Runde v4.10.0-r39. Keine H-Nummer.
**Teilweise nicht blind:** Beim Entwurf wurde von Hand skizziert, dass (K1) der Fierz–Pauli-Austausch die erhaltene Quelle auf dem
dreidimensionalen Unterraum gar nicht sieht und dass (K4) eine Mittelung über die relative Zeitorientierung das Gewicht w = 2p − 1 gibt.
K2 und K3 sind nicht vorab gerechnet.

## Vorwissen geprüft
- r39: Ein Tensor H_ab auf (t, x, y), eine Masse, Kopplung g′H^abJ_ab mit J_ab = ∂_a∂_bη − cη_ab□_∥η, Gewicht w der H_0i.
  N = λN_m genau für w = (3c+1)(c−1)/2; Erhaltung (c = 1) verlangt w = 0, dann g′² = g_m²/3. Die Entkopplung ist gewählt; Lesart dort:
  Fierz–Pauli-artige Hilfsfelder, nicht gerechnet.
- r36.1: Lorentz-invariantes Vakuum: Proca und Fierz–Pauli mit Ableitungskopplung geben keinen Pol, nur Kontaktterme.
- `../op5_bifocal_response_2026_11_18/OP5_J_Massiver_Tensorvermittler.md`: Fierz–Pauli-Austausch zwischen erhaltenen Quellen; die
  longitudinalen Terme fallen weg.
- r31.1 / H118: Die Orientierung des Oktanten ist eine Zeitorientierung der Auslese; die Zeitumkehr (komplexe Konjugation) kehrt sie um,
  kein Kandidat des Bestands legt sie fest. OP3 ruht.
- r37: Der String hat nur räumliche Auslenkungen; sein Vertex enthält keine Zeit-Quer-Komponente.
- Konvention: Zeitumkehr z ↦ z̄ (hier ω ↦ −ω) und Tachyon-Abbildung z ↦ iz werden nicht verwechselt (r51, r81).

## Werkzeug
Wolfram Language, exakt symbolisch (Fourierbild, Matrixinversion, Koeffizientenvergleich in x = ω² und a = a_⊥). Qiskit ist hier nicht
geeignet: Es gibt keine explizit definierte Quantenschaltung, sondern einen klassischen Feldaustausch. Skript `h0i_decoupling.wl`,
Ausgabe `run/h0i_decoupling.txt`.

## Kandidaten und Rechnung
Basis wie r39: Fourierbild mit x = ω², a = |k_⊥|², Quelle bei c = 1 erhalten, Ziel −g_m²N_m/d_m mit N_m = ⅔(x² − ax + a²).
- **K1 Fierz–Pauli auf dem Unterraum.** Massiver Spin-2-Propagator in D = 3 mit Projektor P_ab = η_ab − p_ap_b/m². Austausch mit J_ab
  für allgemeines c; ist er ∝ N_m für irgendein c?
- **K2 H_0i als Hilfsfelder.** H_0i ohne Zeitableitung, über das elektrische Feld E_ij = ∂_tH_ij − ∂_iH_0j − ∂_jH_0i an H_ij gekoppelt, mit
  eigener Steifigkeit μ ≥ 0 (L ⊃ −½μH_0iH_0i); H_00 und H_ij sonst wie r39. H_0i herausintegrieren, Austausch berechnen. Gibt es ein μ
  (endlich oder als Grenzwert), für das der Austausch genau λN_m/d_m mit einem einzigen Pol ist?
- **K3 Zeitumkehr-Parität.** Paritäten der Vertizes J_ab unter ω ↦ −ω für allgemeines c. Ist H_0i T-gerade, verbietet die Zeitumkehr-
  Invarianz die Kopplung an J_0i. Welche Annahme über H steckt darin?
- **K4 Mittel über die relative Zeitorientierung.** Austausch zwischen einem Vertex und seinem Bild mit gleicher Orientierung (Gewicht p)
  und mit umgekehrter (Gewicht 1 − p). Effektives w als Funktion von p; N_m genau für welches p? Gegenprobe: Die Tachyon-Abbildung
  (ω ↦ iω) an einem Vertex statt der Zeitumkehr.

## Raster (vorab)
- **trägt:** Ein Kandidat gibt w = 0 und damit N_m mit einem einzigen Pol aus einer Struktur, die im Projekt bereits steht, ohne neue Wahl.
- **trägt teilweise:** w = 0 folgt aus einer benannten Bedingung, die selbst nicht hergeleitet ist (etwa einer Zeitumkehr-Parität von
  H_0i oder gleichen Gewichten beider Orientierungen).
- **trägt nicht:** w = 0 bleibt eine Setzung; die dynamischen Kandidaten K1, K2 geben N_m nicht, und K3, K4 formulieren nur um.

Frames: alles im Materie-Frame M, Rahmen und Achse wie in r36–r39. OP5 bleibt in jedem Fall offen; OP3 ruht und wird nicht berührt.
