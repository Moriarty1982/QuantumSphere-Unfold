# Übergabe: Stand der letzten Sitzung

13. November 2026, ca. 01:20 (Claude). Wird pro Arbeitsblock überschrieben.

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

## Nächster Schritt (Autorentscheidung)

- Offen ist die Herkunft des Rückwegs: Gibt es im Companion ein zweites Element mit entgegengesetzter Hyperladung (oder einen Frame-Wechsel M/T), das den zweiten Umlaufsinn eichinvariant liefert? Ohne das bleibt K <= 1/2.
- Alternativ die Platzstruktur selbst prüfen: ob die drei Generationen überhaupt als zyklisch gekoppelte gleiche Kopien (Modell I) zu lesen sind.
- Ein Test mit Kriterium bekäme H99 und eine Vorab-Notiz.
- Offen daneben: W-a, W-c der Stringfrage; Statusvermerke für die gemeldeten älteren Stellen in einer neuen Runde.

## Pflichten in jeder Sitzung

- `AGENTS.md`, `wiki/Gesamtbild.md` und die einschlägige Anleitung unter `notes/anleitungen/` lesen; Auslöser in `notes/research/v4_10_0_w1/Zurueckgestellte_Ideen.md` prüfen.
- Vorwissen-Pflicht, Vorab-Notizen, Suchrichtung prüfen. Merges nur nach ausdrücklicher Freigabe. Wiki im selben PR.
- `.codex/environments/` bleibt unversioniert.
