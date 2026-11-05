# Übergabe: Stand der letzten Sitzung

**Diese Datei wird am Ende jedes Arbeitsblocks überschrieben, nicht fortgeschrieben.** Sie ist der Einstiegspunkt für die nächste Sitzung, egal mit welchem Modell. Die Geschichte steht in `AGENTS.md` (Rundentabelle), in der Kernkarte und in den Runden.

## Stand vom 5. November 2026, ca. 21:45 (Claude)
- **Offen: PR #69** (`research/v4.10-r84-zweite-lesart`), Runde **v4.9.0-r84**: Geist-Kondensat auf FRW, Autorentscheidungen (zweite Lesart, holomorphe Adjungierte), H78–H81. Wiki im PR; Bestandsaufnahme und Zurückgestellte Ideen auf GitHub aktualisiert. ours-Merge der lokalen Historie bis 815da20 (Vorab-Commits ef3e1e0, 701f1ca, a5799ef). CI-Lauf 42105091376. **Merge nur nach „PR 69 mergen“.**
- **Lokal eingebaut (815da20):** 1328 Seiten, 3972 Labels, Overfull 45, harte Werte 0, Guard-Linter 0 (ein `\bsym` außerhalb des Mathemodus vor dem Build korrigiert). AGENTS-Zeile r84, Kernkarte K134 (v15.0). **Nächste Bundle-Basis: 815da20.**
- Nächste Schritte zur Wahl: Epoche τ* und Modenauswahl weiter (beobachtbare Folgen?), Zustand bei τ = 0 für δ = 0 (Boyle–Finn–Turok), Massenterme (Dirac, Majorana) unter der zweiten Lesart, I1, Skala.

## Davor (21:15)
- **PR #68 gemergt als e253208** (5.11., 21:01; `research/v4.10-r83-vakuumzerfall`), Runde **v4.9.0-r83**: H76 (Vakuumzerfall), H77 (Tachyonbild einer Wirkung nach Lesart B), Geist-Kondensation (Erkundung), Korrektur zu r82.1(b), (c). Wiki im PR (r82-Aussagen als zurückgezogen markiert). ours-Merge der lokalen Historie bis 5a23a7b (enthält Vorab-Commits 2b47e7f, d087d67). CI-Lauf 42099084932.
- **Lokal eingebaut (5a23a7b):** 1325 Seiten, 3967 Labels, Overfull 45, harte Werte 0, Guard-Linter 0. AGENTS-Zeile r83, Kernkarte K133 (v14.9). **Nächste Bundle-Basis: 5a23a7b.**
- Löschrecht für den lokalen Ordner in dieser Sitzung erteilt (git-Sperrdateien); alte `.git/stale-*lock*` aus früheren Sitzungen liegen noch dort und können weg.

- **Nach r83 (21:10), Erkundung `llm/Erkundung_Geistkondensat_Skala.md` (k193):** Geist-Kondensat auf FRW gibt ρ = 1/(16c) + C/(a³√c), also Λ plus Staub; Höhe und Staubanteil C frei, kein Zusammenhang mit H70 oder I4 ableitbar. Das Kondensat heilt nur das kondensierende Feld; masselose T-Bilder (Photonen, Fermionen) behalten negative Energie, H76 greift für sie. **Offene Autorentscheidung:** T-Anteil als eigenes Feld (dann Rahmen-Cutoff ≲ 14 MeV für den ganzen T-Sektor nötig) oder als zweite Lesart desselben Feldes (ψ_T = −iσ_n ψ_M(x + δ), passend zu T1; dann nächster Test: Dynamik der reduzierten Theorie, Hamilton-Funktion beschränkt?).

- **Autor (21:05): Variante 2 zuerst. H78 bestätigt (Vorab ef3e1e0, nicht blind, k194):** Mit reeller Wirkung fällt δ im flachen Raum heraus. Skalar: (a − b)X/2 − (a + b)V, stabil, m_eff² = γm², kein Zerfall. Weyl (k174-Form, nur Argument verschoben): Operator (a − b)(t, n) + (a + b)(⊥), Dispersion ω² = k_n² + γ²k_⊥² bei Materie-Gewichten → 86 % Lorentz-Verletzung, Laborgrenzen 10⁻¹³…10⁻¹⁵ → **für Fermionen ausgeschlossen**; Photon-Gewichte: keine Zeitentwicklung. Offenlegung: δ-Probe Lauf 1 mit nicht periodischem Testfeld. `llm/Ergebnis_H78_T_als_zweite_Lesart.md`. **Auslöser I1.1 getroffen** (zwei Lichtkegel), I3 berührt (Geist-Kondensat Λ + Staub). Offene Wege: (i) zweite Lesart mit Koordinatenabbildung (Λ(iπ) kehrt t um, Warnung r51/r81), (ii) Variante 1 mit Rahmen-Cutoff, (iii) I1.

- **Autor (21:17): alle drei Wege möglich; begonnen mit der Koordinatenabbildung. H79 bestätigt (Vorab 701f1ca, nicht blind, k195):** k174 hatte den komplexen Boost (iπ) nur auf den Spinor angewendet. Vollständig (Spinor S = −iσ_z und Argument Λ(iπ)x + δ) und mit **holomorpher** Adjungierter (ψ† ↦ ψ†S) ist der Bildterm −L_M: Wirkung (a − b)S_M, isotrop, stabil, K3 erfüllt, kein Zerfall. Hermitesch: (a + b)S_M, K3 verletzt. Im flachen Raum = Materie-Theorie mit umnormierter Kinetik (Skalare m_eff² = γm², Λ nicht aufgehoben). **Autor (21:23): holomorphe Adjungierte festgelegt** (Bestandsaufnahme, Entscheidungen). Nachträglich: Λ(iπ) spiegelt die Zeit; auf FRW sieht T die Expansion als Kontraktion (Autorfrage, Herkunft I4) → Kandidat H80 auf FRW. `llm/Ergebnis_H79_vollstaendiger_komplexer_Boost.md`.

- **Erkundung `llm/Erkundung_Zweite_Lesart_FRW.md` (21:30):** Auf FRW sieht der T-Term a(δ − τ). Skalare nur gerade Potenzen von a (Fortsetzung egal), konforme Felder (Weyl, Eichfelder) sehen nichts. δ = 0: wie flach, T = Universum vor dem Urknall (kontrahierend; Nähe zu Boyle–Finn–Turok, CPT-symmetrisches Universum). δ ≠ 0: Kinetik-Gewicht verschwindet bei a(τ)/a(|δ − τ|) = β_sym, Strahlung τ* ≈ 0,355δ. Autor (21:29): beide Wege getrennt durchgehen.

- **H80/H81 (Vorab a5799ef, nicht blind, k196):** H80a bestätigt (δ = 0: exakt Materie-Skalar mit m² ↦ γm², keine neue Dynamik; Vorhersagen nur über Zustand bei τ = 0, vgl. Boyle–Finn–Turok). H81a bestätigt (τ* = 0,3546 Strahlung, 0,4257 Materie), H81b bestätigt (τ* regulär singulär, allgemeine Lösungen ∝ ln|τ − τ*|, nur eine Mode je k regulär → Modenauswahl; Wahl k = m = 1 offengelegt), **H81c quantitativ widerlegt** (tachyonisches Vorzeichen ja, Wachstum nur ×1,57 statt > 10 bei m·δ = 3). `llm/Ergebnis_H80_H81_zweite_Lesart_FRW.md`. Nicht auf GitHub; nächste Runde r84 sammelt H78–H81, Autorentscheidungen, Erkundungen k193, FRW.

## Davor (19:45)
- **PR #67 gemergt als ebf5048** (5.11., 19:31; `research/v4.10-r82-higgs-stabilitaet`), Runde **v4.9.0-r82**: Higgs-Sektor W2, Stabilität der M–T-Aufhebung (H74, H75), Torsions-Paarkanal (k190). Inhalt: Runde in `parts/v490-post-release-layers.tex`, Notizen und Skripte k188–k190 unter `notes/research/v4_10_0_r82/`, H74/H75 unter `predictions/`, Wiki (6 Seiten), ours-Merge der lokalen Historie bis 2d5c6c2 (enthält die Vorab-Commits b24bb08, 6aa8477). CI-Lauf 42084679668.
- **Lokal eingebaut (2d5c6c2):** 1322 Seiten, 3961 Labels, Overfull 45, harte Werte 0, Guard-Linter 0. AGENTS-Zeile r82 und Kernkarte K132 (v14.8) nachgezogen. Nächste Bundle-Basis: 2d5c6c2.
- **Gemergt zuvor:** PR #64 (r80), #65 (W1-Notizen), #66 (r81, b3cf9f7), #59, #51.
- **Zuletzt vergebene Hypothese:** H81. Nächste freie Nummer H82.
- **Branches, die weg können** (Löschen über den Proxy gesperrt): `rechnen/h59`, `rechnen/h65`, `rechnen/h67`, `rechnen/hintergrund`, `research/v4.10-w1-wirkung-test`, nach dem Merge auch `research/v4.10-r81-…` und `research/v4.10-r82-higgs-stabilitaet`.

## Inhaltlicher Stand
- OP5-Vergleichsmodell-Zweig geschlossen (r80). Gemeinsame Wirkung W1 (r81), Higgs-Erweiterung W2 (r82, `llm/Wirkung_W2_Higgs.md`).
- Ergebnis bisher: Die Struktur liefert **Mechanismen, keine Skala**. Higgs-Vakuumenergie hebt sich mit dem Tachyonbild bei Photon-Gewichten exakt auf; bei direkter Kopplung instabil (H74), bei reiner Gravitation keine exponentielle Instabilität, aber Gleichtakt ∝ t² und Bondi-Durchgehen (H75). Torsions-Paarkanal anziehend, kondensiert nur an der Planck-Skala (ν^c-Majorana, See-saw m_ν ~ 10⁻⁶ eV).
- Zurückgestellte Ideen I1–I4 in `llm/Zurueckgestellte_Ideen.md` (I1 String-Brücke zwischen LQG-Systemen, I2 mod HC als chinesischer Restsatz, I3 Λ als Folge der Dunkle-Materie-Rechnung, I4 Kondensation tachyonischer Moden durch Expansion).

## Nach r82 erledigt (5.11., jetzt in Runde r83, PR #68 gemergt)
- **H76 (Vorab 2b47e7f, nicht blind):** Quanten-Zerfall 0 → φφ + χχ über das Graviton. a, b, c bestätigt: Lorentz-invariant divergiert die Rate ∝ L² (Boost-Volumen); mit Rahmen-Cutoff Γ/V = 2,25·10⁻⁵ Λ⁸/M_P⁴; Schranke Λ ≲ 14 MeV (grob). Lauf 2 nicht verwertbar, Lauf 3 halbanalytisch (k191c) offengelegt. Stabilität verlangt einen ausgezeichneten Rahmen (Kandidat: mitbewegter Rahmen aus H70) und einen Cutoff ≤ ~10 MeV; Kaplan–Sundrum ≲ 2 meV passt zu I4 (nachträglich). `llm/Ergebnis_H76_Vakuumzerfall.md`, Skripte k191, k191b, k191c.

- **Erkundung `llm/Erkundung_Lesarten_Tachyonbild.md`:** I4-Kondensat ⟨χ⟩ ist Lorentz-invariant, liefert keinen Rahmen, heilt H76 nicht. Zwei Lesarten des Tachyonbilds einer Wirkung: A (L_T = −L_M, Energieparität, r82.1) und B (p ↦ ip, X ↦ −X, Potential bleibt). B macht aus gesunder P_M = X/2 + cX² eine Geist-Kondensation (X₀ = 1/4c, stabil, w = −1, eigener Rahmen, Anregungen DM-artig), hebt aber V_min nicht auf. Autor (5.11.): erst prüfen. **H77 bestätigt (Vorab d087d67, nicht blind, k192, k192b):** Nur Lesart B ist mit r07.2, r20.2, H71, r81 und F3 verträglich; A gibt eine Geist-Kopie ohne Tachyon. Folge: **r82.1(b), (c) nicht gedeckt** (Higgs-Bild unter B um 0 stabil, kondensiert nicht, Summe a·V_min) → Korrektur in der nächsten Runde; H74, H75, H76, r82.4 bleiben gültig. Geist-Kondensation unter B ist die zur Struktur passende Erkundung (cX² Eingabe). `llm/Ergebnis_H77_Lesart_Tachyonbild.md`.

## Nächster Schritt (Optionen, Autor wählt)
1. Erledigt mit H76 (siehe oben). Folgefrage: Erzeugt die Struktur einen Cutoff im mitbewegten Rahmen?
2. Skalenfrage: Woher kommt eine Skala außer der Planck-Skala? Kandidaten: I1 (Stringspannung, Informationsmenge), I4 (Kondensation auf FRW).
3. Zusammengesetzte Lesart von Φ (Higgs als Paarkondensat statt Elementarfeld).
4. Prüfen, ob die Kopplungsformen der Ablage (r47, r52–r55) eine Yukawa-Kopplung zu einem T-Partner des Neutrinos enthalten.
- Offene Vorhersagen H15, H42, H46 warten auf Daten.

## Pflichten in jeder Sitzung
- Auslöser in `llm/Zurueckgestellte_Ideen.md` prüfen (beim Start und wenn ein Ansatz scheitert).
- Zuerst `AGENTS.md` lesen, dann die einschlägige Anleitung mit dem Abschnitt „Bereits beantwortet“, dann diese Datei.
- Vorwissen-Pflicht und Vorab-Notizen beachten. Merges nur nach „PR NN mergen“.
- Wiki im selben PR mitziehen.
- Am Ende diese Datei aktualisieren.
