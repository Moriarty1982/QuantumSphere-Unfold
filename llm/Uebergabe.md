# Übergabe: Stand der letzten Sitzung

13. November 2026, ca. 04:10 (Claude). Wird pro Arbeitsblock überschrieben.

- Öffentliche Baseline v5.0.0 (DOI 10.5281/zenodo.24152615, Tag v5.0.0 auf 539b75b). PR #100, #101, #102 gemergt; main 1eed465; Läufe 43265308165 (Zwei-PDF) und 43265308144 (Wiki-Sync) erfolgreich. Keine weitere Veröffentlichung nötig.
- Lokaler Ordner des Autors (`Quantum Sphera`) stand noch auf dem 6.11. (93c3d21, r05) und wurde auf Autorenfreigabe per Fast-Forward auf 1eed465 gebracht. Der alte Stand ist als Tag `lokal-stand-2026-11-06` gesichert (dabei entfielen 58 verfolgte Dateien, u. a. `.claude/skills`, alte Zusammenfassungen; alle über den Tag erreichbar).
- Offener Zweig `research/v5-string-relaxation-rueckwaertssuche` mit PR #103: Rückwärtssuche zur Stringrelaxationsfrage, Notiz und Selbstprüfungsskript unter `notes/research/op3_string_relaxation_backward_2026_11_12.*`, Wiki (Forschungsstand, Wiki-Pflege). Merge nur nach „PR NN mergen“.
- Zuletzt vergebene Hypothese H98, letztes k219. In diesem Block keine neue H-/k-Nummer, kein MMA-Beleg.

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

## Nächster Schritt (Autorentscheidung)

- Entscheiden, ob die Eigenwert-Auslesung als Kandidat weiterverfolgt wird. Wenn ja, braucht sie vorab: (1) einen Grund, warum Massenwurzeln Eigenwerte sind; (2) eine Regel, die die Konfiguration festlegt oder über welche Menge gemittelt wird; (3) eine dritte farbneutrale Richtung für die Elektronmasse. Ein Test dazu bekäme H99 und eine Vorab-Notiz.
- Statusvermerke in einer neuen Runde: r33-Labels (Ladung), ältere Koide-Stellen (v470/17, „2/3 factor“, rem:koide-mass-discrepancy), thm:three-generations.
- Oder die OP3-Linie ablegen: offene Vorhersagen H15, H42, H46, H96; Stringfrage W-a, W-c.
- PR #103 wartet auf „PR 103 mergen“.

## Pflichten in jeder Sitzung

- `AGENTS.md`, `wiki/Gesamtbild.md` und die einschlägige Anleitung unter `notes/anleitungen/` lesen; Auslöser in `notes/research/v4_10_0_w1/Zurueckgestellte_Ideen.md` prüfen.
- Vorwissen-Pflicht, Vorab-Notizen, Suchrichtung prüfen. Merges nur nach ausdrücklicher Freigabe. Wiki im selben PR.
- `.codex/environments/` bleibt unversioniert.
