# Bestandsaufnahme: Wirkungs- und Dynamikansätze bis r80

**4. November 2026. Status: Bestandsaufnahme, keine Rechnung, keine Hypothese.** Anlass: Abschluss des Vergleichsmodell-Zweigs in r80.3 (Autorentscheidung). Ziel: Alle bisherigen Versuche, eine gemeinsame Dynamik aufzuschreiben, an einer Stelle sammeln; je Ansatz festhalten, woran er gescheitert ist; daraus ableiten, was eine Wirkung mindestens leisten muss. Die Fundstellen liegen unter `analysis/` (GitHub und lokal), im Hauptkorpus und in den Runden.

## 1. Was der Companion selbst anbietet
| Stelle | Inhalt | Stand |
|---|---|---|
| `thm:variational-form` (Teil 10) | S = ∫ (Ψ̄iΓD Ψ − Ψ̄ΩΨ − ¼ Tr F² − U_C7 − U_HC), mit U_C7 = λ_C ‖(1 − P_C7)Ψ‖², U_HC = λ_H ‖H_C − Λ[M₁₆, P_C7]‖² | Gliederung. Ω, P_C7 und Λ[M₁₆, P_C7] sind nicht konkret; die Geometrie ist fest (Γ^μ wird nicht variiert); der Text selbst nennt die Konkretisierung als nächste Aufgabe |
| `eq:toe_master_semiconcrete` (Teil 16) | R[Ψ] + Σ D_aΨ_a + Σ Λ_abΨ_b + λ_HC(I − C)Ψ + λ_cl R_cl + λ_β(Ψ − U_βΨ) = 0 | ausdrücklich nur „semi-konkreter Vertreter“; Differentialsymbole und gemischte Kinetik nicht angegeben (`OP5_Common_Cone_Kinetic_Criterion.md`) |
| Runden r27–r31 | Dynamikmodell: Dualitätsdrehung plus Kompensator-Messung, Tachyon-Reservoir, Markov-Kaskade | diskrete Zustandsdynamik, keine Feldwirkung; kein endlicher Nullpunkt für C5 |

## 2. Ansätze aus der HC- und OP5-Serie und ihr Scheitern
| Ansatz | Was er versucht | Woran er scheitert | Fundstelle |
|---|---|---|---|
| Koframe aus Bilinearen E = C[Ψ] im selben Frame | Geometrie aus den Spinoren | Spurhindernis: verlangt verschwindende gemischte Frame-Spur, schließt Koframes nahe der Identität aus | `HC_Bilinear_Geometry_Bridge.md`, `HC_Two_Frame_Action_Bridge.md` |
| Multiplikatorwirkung für das Wörterbuch | gemeinsame Variation explizit | Multiplikator kann den Einstein-Teil ausgleichen; keine unabhängige Einstein-Gleichung | `HC_Two_Frame_Action_Bridge.md` |
| affines Wörterbuch E = θ + C[Ψ] | lokale Lösung | nur in einem geänderten neutralen Elternmodell; mit Masse/Yukawa, Ladung und Kompensator zurück offen | `HC_Two_Frame_Action_Bridge.md`, `OP5_Massive_Affine_Branch.md` |
| massiver affiner Zweig mit Potential W(h) | Vakuumterm abschirmen | bei festem Impuls nur endlich viele C; kein offenes Intervall abgeschirmt | `OP5_Massive_Affine_Branch.md` |
| ebene Wellen als Quellen | Koframe vom Rang 4 | Rang ≤ N − 1 bei N Moden; zwei oder drei Wellen reichen nie | `OP5_Flat_Reference_Clock_And_Signals.md` §4 |
| geboostete Triade, feste Verbindung | Strom und Spin zugleich | induzierter Koframe bricht die Stromerhaltung (Ward) | `OP5_Boosted_Triad_And_Coframe_Feedback.md` |
| exakter Kreuz-Koframe, gemeinsame Elternwirkung | Kreuzauslesung variationell | existiert, bewahrt aber die Flachheit; Krümmung braucht eine nicht-exakte Auslesung | `OP5_Cross_Readout_Common_Action.md` |
| unabhängige Lorentz-Verbindung, Zwangsbedingung | Torsion | torsionsfrei nur mit Multiplikator vom Rang ≤ 1; ein volles Volumenglied passt nicht | `OP5_Connection_Reaction_Followthrough.md` |
| Phase/Amplitude/versteckte Partner | Trägheit herleiten | nur bedingt; eingeschränkte Wirkung verliert Normalgleichungen (Dreimoden-Gegenbeispiel) | `HC_Collective_Action_Reduction.md` |
| Kompensator-Krümmung auf der Nullachse | kinetischer Term für H_C | gedruckte komplexe Gleichung überbestimmt (w = v = 0); reelle Lesarten verschieden | `HC_Null_Axis_Action_Check.md`, `HC_Null_Axis_Dynamical_Closure.md` |
| Quellen und Rückwirkung, positive H_C | Phasenauswahl | Matching-Strafe auf H_C = Λ identisch null; Auswahl nur in einem anderen, beschränkten Modell, mit Formabstieg zu Skala null | `HC_Source_Backreaction.md` |
| endliche Strafe U_C7 | Schließung | endliche Strafe ist keine Projektion; sie kann eine Normalquelle QHPΨ nicht aufheben | `OP5_Native_Action_Closure_Penalty_Audit.md` |
| Vergleichsmodell R = (F, G, dg), r71–r80 | lokale Struktur | Hintergrund A, h vorgegeben und nicht von den Spinoren erzeugt (H68) | Runden r71–r80 |

## 3. Wiederkehrende Muster
1. **Ein Teil der Felder wird festgehalten.** Fester Hintergrund (r80), feste Verbindung (Triade), feste Geometrie (`thm:variational-form`). Jedes Mal scheitert die Rückkopplung genau an dem, was nicht variiert wurde.
2. **Das Wörterbuch Ψ → Koframe ist die Engstelle.** Spurhindernis, Rangschranke, Flachheit des exakten Kreuz-Koframes, Bruch der Stromerhaltung: Alle vier Hindernisse sitzen dort.
3. **Strafen statt Bedingungen.** Endliche Strafen (U_C7, U_HC) erzwingen die Schließung nicht und sind auf der Lösung oft identisch null.
4. **Adjungierte, reelle oder komplexe Stationarität bleiben ungeklärt.** Mehrere Notizen erhalten je nach Wahl andere Gleichungen.
5. **Quellen und Eichalgebra passen nicht zusammen.** H68: A lebt in span(λ₂, λ₄, λ₆), die Spinorströme fast nur in den diagonalen Richtungen.

## 4. Mindestanforderungen an eine gemeinsame Wirkung (abgeleitet, zur Entscheidung)
- **(W1) Alle Felder unabhängig variiert:** Ψ, Eichverbindung, Skalar bzw. H_C, Koframe (oder Metrik), gegebenenfalls Lorentz-Verbindung. Kein Hintergrund von außen.
- **(W2) Erklärte Stationarität:** Adjungierte, reelle Form und Variationsregel vor der Rechnung festlegen.
- **(W3) Koframe:** entweder unabhängiges Feld mit eigener Kinetik oder Zwangsbedingung mit Multiplikator, dessen Rückwirkung mitgerechnet wird. Die Stromerhaltung im induzierten Volumen muss folgen (Ward-Identität aus der Eichinvarianz).
- **(W4) Schließung als exakte Bedingung** (Projektor, Multiplikator), nicht als endliche Strafe; Normalgleichungen nicht weglassen.
- **(W5) Ein gemeinsamer Kegel:** Das Hauptsymbol aller Sektoren ist proportional zu einer Lorentz-Form (`OP5_Common_Cone_Kinetic_Criterion.md`).
- **(W6) Verträglichkeit von Quelle und Eichalgebra:** Die Ströme, die die Spinoren tragen, müssen in der Algebra der Verbindung liegen, sonst gibt es keine Feldgleichung mit Quelle (Lehre aus H68).
- **(W7) Vakuumterm nicht frei:** sonst bleibt OP5 unberührt (r69.1, `OP5_Massive_Affine_Branch.md`).
- **(W8) Frame-Typisierung nach Konvention F** (M, T, P), damit keine Ein-Frame-Artefakte entstehen (r22, r61).

## 5. Offene Entscheidungen des Autors (vor jeder Rechnung)
1. Ist der Koframe ein eigenes Feld oder eine Funktion von Ψ (mit Multiplikator)?
2. Komplexe oder reelle Wirkung, und welche Adjungierte?
3. Gravitation: Einstein–Hilbert/Palatini-Term oder rein induziert?
4. Welche Eichgruppe: volle su(3) (dann braucht der Hintergrund diagonale Anteile) oder eine Untergruppe, deren Ströme die Spinoren tatsächlich tragen?
5. Wird P_C7 als exakte Nebenbedingung gesetzt oder dynamisch ausgewählt?

## Entscheidungen des Autors
- **4.11.2026, Entscheidung 1: Variante B.** Der Koframe ist ein eigenes, unabhängig variiertes Feld (Einstein–Cartan–Dirac-Art). Ob auf den Lösungen E ≈ C[Ψ] gilt, die Geometrie also wie aus den Spinoren gebaut aussieht, wird später als eigener Test mit Vorab-Notiz geprüft. Ziel laut Autor: „versuchen und schauen, was man daraus lernen kann“.
- **4.11.2026, Entscheidung 2: R als Hauptlinie, K parallel.** Reelle Wirkung mit Dirac-Adjungierter Ψ̄ = Ψ†γ⁰ und symmetrischer Kinetik, festgelegt im Materie-Frame M, klassische (kommutierende) Spinoren; Frames T und P danach über die Frame-Abbildungen. Die komplexe Lesart K wird nicht verworfen (Autorhinweis: nie systematisch untersucht). Da S komplex stationär ⇔ Re S und Im S stationär, ist K = R plus die Gleichungen aus Im S; diese werden aus derselben Lagrangedichte mitgerechnet und darauf geprüft, ob sie die Schließung exakt erzwingen (W4) und ob nichttriviale Lösungen bleiben. Vorbefund: In `HC_Null_Axis_Dynamical_Closure.md` erzwingt die komplexe Stationarität harte Projektor-Transporte D P = 0, die reellen Wirkungen nicht; dafür schließt sie dort bestimmte Wellen aus (w = v = 0). Korrektur zu §2 dieser Notiz: Die Zeile „Kompensator-Krümmung auf der Nullachse“ nannte nur die Kehrseite.
- **4.11.2026, Entscheidung 3: Einstein–Cartan ohne Λ, vorerst ein System.** Koframe und Lorentz-Verbindung unabhängig, Term (1/2κ)∫e·R(ω); kein Λ-Term von Hand, damit sich zeigt, ob die übrigen Teile (Skalarpotential, Kompensator, Schließung, Im S) einen Vakuumterm festlegen (W7, OP5). Induzierte Gravitation später höchstens als Frage, ob κ von der Materieseite festgelegt wird. Autoridee „mehrere LQG-Systeme, über einen String verbunden“ als I1 in `llm/Zurueckgestellte_Ideen.md` mit Auslösern zurückgestellt.

## Nächster Schritt (Vorschlag)
Nach diesen Entscheidungen die kleinste Wirkung aufschreiben, die (W1)–(W8) erfüllt, und zuerst nur ihre Euler–Lagrange-Gleichungen und Identitäten (Bianchi, Ward) symbolisch prüfen, noch ohne Lösung. Ein Test mit Kriterium erst danach, mit Vorab-Notiz.
