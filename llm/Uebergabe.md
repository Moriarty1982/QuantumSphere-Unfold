# Übergabe: Stand der letzten Sitzung

13. November 2026, ca. 15:15 (Claude). Wird pro Arbeitsblock überschrieben.

- **Dieser Block:** H99b mit der NuFIT-6.1-Primärtabelle entschieden: **verträglich, +1,80σ** (nicht blind). Zweig `research/v5-h99b-nufit61`, **PR #104 offen**, noch nicht gemergt. Enthält auch den lokalen Übergabe-Commit 0504201.

- Öffentliche Baseline v5.0.0 (DOI 10.5281/zenodo.24152615, Tag v5.0.0 auf 539b75b). PR #100, #101, #102 gemergt; main 1eed465; Läufe 43265308165 (Zwei-PDF) und 43265308144 (Wiki-Sync) erfolgreich. Keine weitere Veröffentlichung nötig.
- Lokaler Ordner des Autors (`Quantum Sphera`) stand noch auf dem 6.11. (93c3d21, r05) und wurde auf Autorenfreigabe per Fast-Forward auf 1eed465 gebracht. Der alte Stand ist als Tag `lokal-stand-2026-11-06` gesichert (dabei entfielen 58 verfolgte Dateien, u. a. `.claude/skills`, alte Zusammenfassungen; alle über den Tag erreichbar).
- **PR #103 gemergt als 83b2551** (13.11., auf „pr 103 mergen“ des Autors; Merge-Commit, Vorab-Commit 5b23c5a bleibt erreichbar; Läufe 43370355406 Wiki-Sync und 43370355373 Zwei-PDF erfolgreich). Enthält alle Notizen und Skripte dieser Sitzung unter `notes/research/` sowie H99 unter `notes/research/predictions/`. Zweig `research/v5-string-relaxation-rueckwaertssuche` kann weg. Lokaler Ordner auf 83b2551 vorgespult; dieser Übergabe-Commit liegt nur lokal.
- Zuletzt vergebene Hypothese H99 (siehe unten), letztes k221. Kein MMA-Beleg.
- Unversioniert im lokalen Ordner: `llm/literatur/Dorau_Much_2026_arXiv_2510.24491v3.pdf` (seit 6.11., nicht angefasst).

## Inhaltlicher Stand

- Autorenentscheidung 12.11.: erst Rückwärtssuche, keine Netzsimulation.
- Ergebnis (analytisch, nicht blind): Bei fester Außenlänge und frei umverteilbaren Längen sind die Zugkräfte gleich. Konvexe Energie: Relaxationszeiten wählen nichts aus, gleiche Strings geben K=1/3. Reiner Maxwell-String: Endaufteilung r_i(0) plus Überschuss nach Fluidität, neutral und kraftfrei, kein Attraktor. Attraktor nur bei L proportional a (Anteile (1/eta_i+H/k_i)/Summe), im Widerspruch zur festen Außenlänge. Gleiche Strings: ungleiche Aufteilung nur mit nicht monotonem Kraftgesetz; ein Höcker gibt (lang, kurz, kurz), drei verschiedene Längen brauchen zwei Umkehrpunkte.
- Damit ist die v5-Frage für die Maxwell-Klasse bei fester Außenlänge negativ beantwortet; allgemein bleibt sie offen. Weder Lambda noch Koide 2/3 oder das Leptonspektrum folgen.
- Fehlende native Operation: nicht konvexe Energie des einzelnen Strings oder Herkunft ungleicher Moduln aus dem Companion.
- OP1–OP5/C5/C6/T2 unverändert. I3 durch den Lambda-Bezug berührt, nicht benutzt.

## Weg W-b (12.11., abends, Autor: „versuche erst W-b“)

- Notiz und Skript `notes/research/op3_string_energy_source_search_2026_11_12.*`, im selben PR #103.
- Quellenbefund negativ: keine Stringenergie als Funktion einer Länge im Companion (gamma_string ist ein Zählparameter; thm:spring linear und ungedämpft; W2-Higgs-Potential ist Eingabe für ein Feld).
- Kleinste passende Energie (quartischer Doppeltopf, kubische Kraft): gleiche Zugkraft bei drei verschiedenen Längen verlangt Topfmitte L/3 und gibt exakt die Brannen-Form, K=1/3+2v²/L², K=2/3 für v=L/sqrt(6) (entspricht |b|=a/sqrt(2) aus r44.1(e)). Phase theta exakt entartet, nicht gewählt. Höhere Terme legen theta fest, kosten aber je eine Formzahl.
- Ergebnis: W-b liefert keine native Operation und führt auf den offenen Punkt aus r44 zurück (|b|/a, theta). Stringfrage und OP3 bleiben offen.

## Quellensuche zur Koide-Phase (12.11., Autor: „such im companion“, ältere Bausteine haben das heutige Wissen nicht)

- Notiz und Skript `notes/research/op3_phase_source_search_2026_11_12.*`, im selben PR #103.
- Übersehenes Vorwissen zu W-b nachgetragen: r10–r12, r16 (H11), r26 (H16), r38, r44, r45, koide-and-kernel, generation-coupling, coupling-scale-candidate.
- Befund: tau wirkt als delta -> delta+2pi/3, rho als delta -> -delta. Symmetrische Größen sehen nur cos(3 delta) und wählen zwei gleiche Massen. Die Phase misst das Verhältnis rho-ungerade zu rho-gerade (tan 3delta). Feder-Satz, Slot-Norm-Potentiale und die v5-Stringfrage sind rho-symmetrisch und scheitern deshalb (Grund aus r45: Chiralität).
- Native rho-ungerade Größen: Chiralitätsprojektor, Assoziator [e4,e5,e6]=-2e7, Q_J=iL_e7, Vorzeichen des Frame-Versatzes. Keine trägt einen Betrag. Quellensuche negativ, Lücke benannt.
- Ältere Stellen ohne Statusvermerk (nur gemeldet): v470/17 Zeilen 18 und 194 („structurally closed“), Bemerkung „The 2/3 factor is everywhere“, rem:koide-mass-discrepancy.

## Erkundung rho-ungerade Platzkopplung (13.11., Autor: „mach das mal“)

- Notiz und Skript `notes/research/op3_rho_odd_coupling_2026_11_12.*`, im selben PR #103. Erkundung, kein Test.
- Kandidat: Trialitätsform t mit festem Element h des dritten Platzes gibt M = a + alpha P + beta P², alpha = t(u, conj w, h), beta = t(conj w, u, h). Nur Oktonionenfaktor gerechnet.
- Quarks: alpha = -2(h0 - i h7), beta = -2(h0 + i h7) für reelles h = h0 + h7 e7; hermitesch, Brannen-Form; Phase = Winkel von h in der Ebene (1, e7). Verhältnis nicht festgelegt.
- Leptonen: Kopplung über t verschwindet für jedes h ((1+ie7)(1-ie7) = 0). Kein Platz-Kopplungsterm.
- Stand: native rho-ungerade Kopplung existiert (e7-Komponente des dritten Platzes), ohne festen Betrag und nur für Farbe. OP3/OP4 offen.

## Erkundung Dixon-Platzkopplung (13.11., Autor: Lepton-Fall versuchen, Dixon-Raum auch auf Quarks)

- Notiz und Skript `notes/research/op3_dixon_slot_coupling_2026_11_13.*`, im selben PR #103. Erkundung, kein Test.
- Kandidat F_b(x,y,h) = <(x^ y) h> auf C⊗H⊗O (volle Dixon-Konjugation am ersten Eintrag), Zustände wie k85.
- Keine Lorentz-invariante zyklische trilineare Form auf drei Spinor-Plätzen; h muss Skalar sein. Nur neutrale h (1⊗1, 1⊗e7, e3⊗1, e3⊗e7) koppeln.
- Sektorformel: alpha_s ∝ (a0 + i sigma a3)(o0 + i lambda o7); sigma = +1 (e, d), -1 (nu, u); lambda = +1 Leptonen, -1 Quarks. Reell: hermitesch, Brannen-Form, theta_s = sigma phi_H + lambda phi_O, Beträge gleich.
- Spiegelung: Platzmatrix u = rho-Bild von e, d = rho-Bild von nu (für jedes neutrale h).
- Nachträglich, nicht blind: gemeinsames reelles h verlangt gleichen Phasenbetrag für u und e; r11 hat 0,0518 gegen 0,2211. Einfachste Form passt nicht.
- Stand: rho-ungerade Kopplung für Leptonen und Quarks vorhanden, zwei freie Winkel, kein festes Verhältnis. OP3/OP4 offen.

## Nachtrag Verbinder und Hyperladung (13.11., „weiter“)

- Skript `notes/research/op3_dixon_connector_link_2026_11_13.py`, Nachtrag in der Dixon-Notiz, im selben PR #103.
- F_b-Kopplung = antilinearer Verbinderblock aus r44.1(b) (Rang 8, Dubletts). Idempotente (1∓ie3)⊗(1∓ie7) koppeln je einen Sektor; Y/2 = +1/2 (e, d), -1/2 (nu, u).
- Hyperladung: Rückweg beta_s hängt am Koeffizienten des gespiegelten Sektors, nicht eichinvariant. Ein kovariantes Element gibt nur M_s = a_s + alpha_s P, also K <= 1/2; Koide nicht erreichbar. Gemeinsames Element: 1 : 1 : 2.
- Der hermitesche Brannen-Fall (reelles h) ist vor der Brechung nicht eichinvariant; Bewertung in der Notiz korrigiert.

## Nachtrag 2 Herkunft des Rückwegs (13.11., „weiter“)

- Nachtrag 2 in der Dixon-Notiz, Skript `op3_dixon_connector_link_2026_11_13.py` erweitert, im selben PR #103.
- Varianten des Elements im dritten Platz: h (alpha c_s, beta c_s'), h* (conj c_s', conj c_s), h~ (c_s', c_s), h+ (conj c_s, conj c_s'); s' gespiegelt (e↔u, nu↔d). Eichinvariant: Koeffizient c_s oder conj c_s'.
- Rückweg über h~ ist eichinvariant, trägt aber denselben Koeffizienten wie der Hinweg: keine Phase aus dem Element. Rückweg über h+ bräuchte eine unabhängige zweite Dublett-Komponente; W2 hat ein Dublett, zweite Lesart passt dazu.
- Stand: Brannen-Phase = relative Phase der Kopplungskonstanten von Hin- und Rückweg, frei (r45, jetzt verortet). Struktur allein liefert sie im heutigen Companion nicht.

## Weg C: Platzstruktur geprüft (13.11., Autor: „c“)

- Notiz und Skript `notes/research/op3_generation_carrier_review_2026_11_13.*`, im selben PR #103.
- Korrektur: r53 (H37) ist Vorbefund zur Platzkopplung über t (t allein verboten, keine Quarkmischung); r47–r60 Masken und A4-Auslesung. In den beiden Kopplungsnotizen nachgetragen.
- Träger: Farbtriplett ausgeschieden (12.11.); Quaternionen-Richtungen i, j, k (r33) ausgeschieden als Generationenlabel, weil mu_1, mu_2 unter Q_em nicht invariant sind (neu; Voraussetzung: derselbe H-Faktor wie r40–r43); Hopf-Träger K <= 1/2; Modell I widerspruchsfrei, ohne Vorhersage.
- Antwort: kein Träger liefert Zahl drei und Massen zugleich. Es fehlt ein Grund für die Wiederholung (nativer Mehrfachraum gleicher Quantenzahlen oder eichinvariante Dreifachauslesung), nicht ein weiterer Kopplungsansatz.

## Erkundung Eigenwert-Auslesung (13.11., „weiter“)

- Notiz und Skript `notes/research/op3_gram_eigen_readout_2026_11_13.*`, im selben PR #103. Erkundung, kein Test.
- Eigenwerte der Platz-Gram-Matrix S sind eichinvariant (unitäre Wirkungen; nicht Boosts). Für drei Einheitsvektoren: s_k = 1 + 2 rho cos(theta + 2pi k/3), rho² = mittlere quadratische Überlappung, cos 3theta = c12 c13 c23/rho³, K = (1 + 2 rho²)/3 (mit sqrt(m) ∝ s als Annahme).
- Koide ⇔ rho² = 1/2; Positivität gibt den Bogen |theta| <= pi/12; Rand = koplanare Plätze, leichtester Zustand masselos. Zahl der Massen = Rang. Farbfeste Ebene: immer ein Eigenwert null.
- Mittel von K über Einheitsvektoren im R^n: (1 + 2/n)/3; farbfester Hopf-Torus: K in [1/2, 1], Mittel genau 2/3. Mittel über Konfigurationen, keine Herleitung; Numerologie-Vorbehalt.
- Unterschied zum Ausschluss vom 12.11.: der galt für das H18-Gesetz (Diagonal-Labels), nicht für die Eigenwerte.

## Zusätzliche Bedingung „Überlappung 1/2 für Leptonen und Neutrinos“ (13.11., Autorwahl)

- Keine H99 vergeben, kein Test gerechnet: Die Frage ist durch H2 (v4.8.0-r12, Vorab 434c5a8, k15) beantwortet. K = 2/3 für Neutrinos geht nur mit negativer Wurzel (NO, Summe 0,0592 eV, verträglich, schwach trennend); mit positiven Wurzeln höchstens K = 0,585.
- In der Gram-Lesart (Eigenwerte nie negativ) ist die Bedingung für Neutrinos mit bekannten Daten nicht erfüllbar. Nachtrag in `op3_gram_eigen_readout_2026_11_13.md`.
- Zuletzt vergebene Hypothese bleibt H98.

## Indefinite Form und H99 (13.11., Autorwahl „Indefinites Skalarprodukt“)

- Quellenbefund `notes/research/op3_indefinite_form_2026_11_13.*`: bilineare Form x^T y auf C⊗H⊗O ist invariant unter Drehungen, Boosts, Farbe, Q_em; verschwindet auf Zuständen fester Ladung q ≠ 0, nicht auf neutralen (passt zu r44.1(d)). Lesart B: Re s hat Signatur (3,3). Negativer Gram-Eigenwert genau außerhalb des Bogens |theta| > pi/12.
- **H99** (Vorab 5b23c5a, nicht blind, k221 in `notes/research/predictions/`): rho² = 1/2 in beiden farbneutralen Sektoren, theta_nu = theta_e + pi/12 ⇒ dm21/dm31 = 0,030839. H99a (NuFIT 6.0) verträglich, +1,31 sigma. H99b (Nachtrag 13.11. nachmittags, Primärtabelle nu-fit.org `v61.tbl-parameters.pdf`, IC24 mit SK, NO: dm21 = 7,537 +0,094/−0,10e-5, dm31 = 2,511 +0,021/−0,020e-3): R_obs = 0,030016 ± 0,000457, **+1,80 sigma, verträglich**. Nachträglich: Spalte IC23 gäbe +2,03 sigma; Sekundärwerte aus arXiv:2601.18781 (2,519/2,529) weichen von der Primärtabelle ab, Ersatzrechnungen überholt. Verlangtes dm21 = 7,744e-5 gegen JUNO allein 7,50 ± 0,12: +2,0 sigma.
- **Zuletzt vergebene Hypothese: H99.** Nächste freie Nummer H100. Letztes k: k221 (k220 liegt auf einem lokalen Zweig des Autors).
- H99, H99a in PR #103 (gemergt); H99b-Nachtrag in PR #104 (Ergebnis-Notiz, k221_out.txt, predictions/README, Wiki Forschungsstand, Vorhersagen-und-Tests, Wiki-Pflege).

## Erkundung NuFIT-Verlauf (13.11., abends, Autor)

- Skript, Grafik und Ausgabe `notes/research/nufit_verlauf_2026_11_13.{py,png}`, `..._out.txt`. Werte aus den Parametertabellen v1.0 bis v6.1 (nu-fit.org). Matplotlib fehlt in der System-Python; gerechnet in einer venv im Scratchpad.
- Δm²₂₁ liegt seit 2012 flach bei 7,39 bis 7,54 (Fit konstant am besten, Mittel 7,47). Δm²₃₁ (NO) stieg bis etwa 2017 und ist seither bei 2,51 bis 2,52 (exponentielle Annäherung, Grenzwert 2,515). R driftet leicht nach unten (Trend 2030: 0,0294); H99 verlangt 0,030839. R lag 2013/14 bei 0,0305–0,0308 nur wegen des damals niedrigen Δm²₃₁ (2,42; NO nur Nebenminimum); Anstieg mit IceCube/DeepCore, NOvA, T2K, Daya Bay 1230 Tage (v2.1/v2.2). Nach JUNO bestimmt σ(Δm²₃₁) den Test; bei gleichen Mittelwerten etwa 3σ gegen H99.
- Vorbehalt: Die Versionen teilen fast alle Daten, chi²/ndf etwa 0,1; die Fehlerbänder der Ausgleichskurven sind zu eng. Für einen Bestwert ist der heutige Wert die beste Schätzung künftiger Werte (Martingal); ein Trend ist Beschreibung, keine Vorhersage. Committet in PR #104, Wiki-Abschnitt im Forschungsstand.

## Drei Erklärungsideen für die H99-Abweichung (Autor: „im Hinterkopf behalten“, ungeprüft)

Die Daten verlangen eine Verschiebung von 0,2580 statt π/12 = 0,2618 (1,4 % kleiner; dR/dθ ≈ 0,22).
1. Die Beziehung θ_ν = θ_e + π/12 ist nicht hergeleitet (Brannen); nur π/12 als Bogenrand ist nativ. Korrektur oder Zufall möglich.
2. Gesetzte Annahmen: K = 2/3 auch für Neutrinos, Massenwurzel = Eigenwert, negative leichteste Wurzel.
3. Skalenfrage: θ_e aus Polmassen, Neutrinos bei anderer Energie; Laufen von θ_e nie untersucht, 1–2 % denkbar.

## Erkundung Varianten zu H99 (13.11., abends, Autor: „Idee 3 im Kopf, weiter mit 1 und 2; vor allem in Kombination“)

- Notiz, Skript, Ausgabe `notes/research/op3_neutrino_phase_candidates_2026_11_13.*`. Nicht blind, kein Test, keine H-Nummer.
- Raster 24 Varianten: nur die H99-Form passt; Spiegelung am Rand, c -> -c, det-Spiegelung, m ~ |s|, Seesaw m ~ s^4 scheiden mit 49σ bis >1000σ aus. Skala allein: 29 %.
- **Kandidat (nachträglich aus Fit):** alle drei Bestandteile bei M_Z: rho_nu² = rho_e²(M_Z) (K = 0,6678), Verschiebung = eigener Bogenrand 0,26006, theta_e(M_Z) = 0,22112 ⇒ R = 0,030087, +0,16σ (NuFIT 6.1), dm21 = 7,555e-5 (+0,46σ JUNO). Erst die Kombination der drei Ideen schließt die Lücke. Offen: warum M_Z.
- Trennung von H99 (0,030840) gegen künftige JUNO-Werte etwa 3σ.
- **Nachtrag Skala (Autor: „Grund für M_Z suchen“):** M_Z nicht ausgezeichnet; jede Skala von 5 GeV bis 2e16 GeV gibt R = 0,03006–0,03012. Unterschied zu Pol = QED-Selbstenergie (Faktor 1 + (3α/2π) ln(m_i/m_j)). Wahl ist binär: Polmassen oder Kopplungen. Für Kopplungen: Brannen-Form entsteht in Kopplungen (Dixon-Platzkopplung, W2-Yukawas), Neutrinos ohne Photonwolke. Dagegen: Koide 2/3 exakt nur bei Polmassen (wie H1/r11 für 2/9).
- **Nachtrag Koide-Spannung (Autor: „Erst Koide-Spannung“):** Pol-Koide trifft 2/3 auf 0,2 % der QED-Verschiebung (K_pol − 2/3 = −2,2e-6 ± 5,1e-6) ⇒ Struktur eher auf der Polseite. Ausweg Sumino (arXiv:0812.2103): Familien-Eichkorrektur hebt QED bei geladenen Leptonen auf; bei Neutrinos wirkt sie allein. Mit Koide exakt: R = 0,03025 (c = 1, +0,5σ), 0,03055 (c = 1/2, +1,2σ), 0,02968 (c = 2, −0,7σ). Exponent c offen; nicht nativ (keine Familien-Eichsymmetrie, r14/r33). Neue offene Frage: kann die Platzkopplung eine Familien-Eichwechselwirkung tragen?
- **Nachtrag c und Familiensymmetrie:** c für z = 0: 1,3–1,4 ohne Mischung, 1,7–1,8 mit PMNS-Mittelung (richtige erste Näherung); c = 1 gibt +0,7σ bis +0,8σ. Sumino: ℓ_L in 3, e_R in 3̄, α_F = 4α, Vereinigung mit SU(2)_L bei 10²–10³ TeV; Weinberg-Term ℓℓ gleiches Vorzeichen wie geladen ⇒ Richtung stimmt, c = 1 natürlich. Companion: nur diskrete S_3 (Sedenionen r13, Trialität r14/r15), Δ(96) in der Farbe; keine Familien-Eichsymmetrie. Einziger stetiger Kandidat: globale U(3) auf dem Platzindex der Gram-Matrix (Gram-Matrix ↔ Suminos Φ). Fehlt: Eichung, Bosonenmassen aus S, α_F = 4α.
- **c als Integral (Autor):** c = 1,8 ± 1,0 (PMNS-gemittelt); c − 1 nur 0,8σ, c = 0 (H99) 1,8σ. c = Verhältnis der Log-Integrale (Familie auf Neutrinoseite / QED geladen); bei Sumino exakt 1, da α_F = 4α beide gleich macht. c ≠ 1 wäre Maß eines abweichenden Integrals; heute nicht verlangt. Künftig σ_c ≈ 0,5.

## Erkundung Eichung Platzindex-U(3) (13.11., spät, Autor: „Platzindex-U(3) eichen“)

- Notiz, Skript, Ausgabe `notes/research/op3_slot_u3_gauging_2026_11_13.*`. Nicht blind, kein Test.
- Feld X (drei Plätze), S = X†X, X → XU, D X = ∂X − i g X A. Bosonenmassen: s_i (diagonal), (s_i+s_j)/2 (je zweimal), alle massiv (numerisch 1e-14). S adjungiert gäbe drei masselose Bosonen ⇒ geladen muss X sein.
- Auslesung A (√m ∝ s, Gram, H99): M_ii² ∝ √m_i ⇒ Aufhebung bei α_F = 8α. Auslesung B (m ∝ s): X = Suminos Φ, α_F = 4α, Überlappungs-Lesart von Koide verloren.
- Sumino-Ladungen ⇒ Massenmatrix bilinear XᵀX; c für Neutrinos bleibt 1.
- **Auslesung entschieden: A** (√m ∝ s). Nur A erlaubt negative Wurzeln (Neutrinos, H2); B gibt K_ν ≤ 0,585. Bogen gilt in beiden. Sumino-Bedingung hängt am Feld: X ⇒ α_F = 8α; Überlappungsmatrix als Feld (Φ → UΦ oder M → U M Uᵀ) ⇒ α_F = 4α. Letzteres braucht Überlappungen zwischen zwei verschieden geladenen Tripeln (links/rechts), nicht nativ.
- Offen: Überlappungsmatrix als eigenes Feld begründen (zwei Tripel L/R); Potential (ρ² = 1/2); Vereinigung mit SU(2)_L.

## Nächster Schritt (Autorentscheidung)

- PR #104 (H99b-Nachtrag) prüfen und auf „PR 104 mergen“ des Autors mergen.
- H100 (Autorentscheidung): beide Fassungen (H99: R = 0,030840; eine Skala M_Z: R = 0,030087) vor dem nächsten JUNO-/NuFIT-Ergebnis als Vorab-Notiz mit Entscheidungskriterium festschreiben. Skalenfrage erledigt (binäre Wahl Pol/Kopplung); Koide-Spannung spricht für Pol + Sumino-artige Korrektur. Kandidaten für H100: H99 (0,030840), Kopplungsseite (0,0301), Sumino c = 1 (0,0302); Kriterium und Wahl vorab festlegen.
- Statusvermerke in einer neuen Runde: r33-Labels (Ladung), ältere Koide-Stellen (v470/17, „2/3 factor“, rem:koide-mass-discrepancy), thm:three-generations.

## Pflichten in jeder Sitzung

- `AGENTS.md`, `wiki/Gesamtbild.md` und die einschlägige Anleitung unter `notes/anleitungen/` lesen; Auslöser in `notes/research/v4_10_0_w1/Zurueckgestellte_Ideen.md` prüfen.
- Vorwissen-Pflicht, Vorab-Notizen, Suchrichtung prüfen. Merges nur nach ausdrücklicher Freigabe. Wiki im selben PR.
- `.codex/environments/` bleibt unversioniert.
