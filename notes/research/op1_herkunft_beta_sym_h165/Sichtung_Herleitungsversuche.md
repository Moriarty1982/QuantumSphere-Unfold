# Sichtung: bisherige Versuche, β_sym herzuleiten oder zu erklären (Stand 26.11.2026)

Erstellt vor der Rechnung zu H165 als „Vorwissen geprüft“. Quelle: Durchsicht der Ordner `notes/research/op1_*`, `hopf_gap_2026_11_23`, `predictions/`,
der Companion-Schichten, des Physik-Artikels (Abschnitt 6) und des Wikis. Kein Versuch leitet β_sym her. „Trägt“ heißt hier: wurde als Lesart behalten.
Die Sichtung hat ein Subagent zusammengetragen; Stichproben (thm:bsym-hopf, r61.2, OP1 im Wiki, H164) sind vom Hauptagenten gegengelesen, die übrigen
Zeilen nicht einzeln.

## Zwei Zahlenwerte im Bestand
- 0,5493482 und γ_L = 1,86444 kommen aus den gerundeten Eingaben γ_BI = 0,2375 und γ_string = 0,1274.
- 0,549406 und γ_L = 1,864700 kommen aus den exakten Werten γ_M = 0,2375329580 (Meissner) und γ_T = ln 2/(π√3) = 0,1273840.
- r64.6(b) hält die Spaltung fest: keine Aussage hängt am Unterschied.

## Die Versuche
| Nr. | Versuch | Fundstelle | Idee | Wert | Befund |
|---|---|---|---|---|---|
| 1 | Hopf-Winkel | `thm:bsym-hopf`, `rem:bsym-hopf-gap` | β = sin(θ_H/2), ℤ/3-Bahn auf rundem S³ | 1/√3 = 0,5774, γ_L = 2 | 4,9 % daneben; liest R-Zustand als Materie-Versatz (r61.1) |
| 2 | Primgitter-Korrektur δ_CL (P3) | `conj:cl-correction`, v4.8.0-r09 | β = (1/√3)·exp(−γ₁/(4πγ_L⁵)) | Treffer auf 0,018 % | Exponent nachträglich gewählt; nach r19 verloren (−0,15 %); archiviert |
| 3 | Tribonacci-Fixpunkt | `thm:tribonacci` | γ_L = 1/β(γ_L) | 1,8392867552 | mischt Frames (r61.1a) |
| 4 | Hawking-Temperatur | `thm:dual-origin` | γ_L ≈ 1/β | 1,820 | 2,4 % daneben, gleicher Mangel |
| 5 | Kosmologisches β | `rem:omega-bsym` | β = √Ω_M | 0,5578 | nur Konsistenzvergleich |
| 6 | Alte Lorentz-Lesart | `thm:frame-offset` | γ_L = 1/√(1−β²) | β ≈ 0,844 | ersetzt; F11: beide Eingaben sind Literaturwerte |
| 7 | GUE-Selbstbestimmung (P1) | `thm:gue-selfdet`, v4.8.0-r08, Archiv | KS-Minimum der Entfaltung bei μ = γ_L | Minimum bei 1,00 (bzw. 2,85; 2,25) | an den Nullstellen 1–2000 widerlegt; archiviert |
| 8 | Kick der Dualitätsdrehung | v4.9.0-r27 | ein Kick aus R gibt den Hopf-Zustand bei 30° | gemessen 28,78° | Modell, Winkel angepasst |
| 9 | Zählverhältnis | H47, v4.9.0-r63, r68 | γ_L = γ_DL/γ_ABCK | 0,549406 | nicht blind; braucht U(1)-Zählung (SU(2): 0,604468); Zuordnung Regel↔Frame nicht hergeleitet |
| 10 | Einfrieren | H48 | β als eingefrorene Bloch-Länge | Hopf bei r = 1, Messwert bei r = 1,157 | widerlegt |
| 11 | Eindeutigkeit im Regelraum | H98, H104 | DL/ABCK einziges Paar von 36? | zweites Paar 1,864824 | H98 bestätigt (nicht blind), H104 widerlegt |
| 12 | Energie/Unruh (P1/P2) | v4.10.0-r09, r10 | T erreicht nur den Tachyon-Boden | — | P2 scheitert; Regel ≙ frame-abhängiges Flächenquant |
| 13 | Irreduzibilität (A) | v4.10.0-r17 | Frame-Abbildungen irreduzibel nur bei j = ½ | Kramers-Alternative 1,2559 | Brücke nicht hergeleitet |
| 14 | String-Endpunkte | I1, CT-004 | Endpunkt trägt j = ½ | — | Guard ohne Stütze |
| 15 | Statistik rückwärts | r24.1 | Austauschstatistik je Frame | — | nicht herleitbar |
| 16 | Kreuzungen | r24.4, H105 | T zählt Horizontkreuzungen | Stufe 4 ln 2 | Lesart; H105 offen |
| 17 | U1/U2-Zerlegung | `op1_u1_check`, `op1_counting_rule_data` | DL = U1 + U2 | — | ruht auf (S1) |
| 18 | (S1′) masselose Kreuzung | `op1_s1_check`, `op1_flux_lines` | Helizität gibt U1 und U2 | — | kippt (A) |
| 19 | Eine Auslese in R | `op1_r_readout_precheck` | Boosts, die Spinsektoren erhalten | — | keine M/T-Asymmetrie |
| 20 | Unscharfer HC | `op1_hc_blur` | achsengemittelte Maske | 0,237533; 0,274067 | offen: Zustandszahl oder Spur? |
| 21 | Register-Entropie | `op1_entropy_count` | Zählung aus dem Register | γ = 0,2342 | erklärt R und P, nicht M |
| 22 | Auslesefrequenz | `op1_readout_frequency` | quasinormale Frequenz | log₂3 = 1,584963 | 0 von 16; Nebenwert 2^(1−γ_L) = 0,549161, nicht verwendet |
| 23 | Moran-Dimension | `op1_moran_geometry`, r29, r53 | größte Kopienzahl in der Ebene | 1,8647 | nachträglich; für T zirkulär |
| 24 | Eine Zahl | `op1_one_number` | γ_L als Boost von (M, T) | — | zurückgezogen: Paar ist (M, M̄) |
| 25 | Zwei Lesarten | `op1_two_readings` | OP1 wird „warum Geschwindigkeit β“ | 0 von 9 | nächster 1/√3 |
| 26 | Gemeinsame Prämisse, T-Regel | k237–k239 | eine geteilte Prämisse | 0 von 47 Einheiten | keine gefunden |
| 27 | Flächenquant unter Boost | `op1_area_quantum_boost` | Rovelli–Speziale | — | unitärer Boost erhält das Spektrum |
| 28 | U2 unter (B) | k236 | Boost bei η = 0,6175 | — | bevorzugt, wählt nicht |
| 29 | J_B am Flächenoperator | H121 | transformierte Einfachheitsbedingung | — | widerlegt |
| 30 | Holst-Dualität | r31.3/r31.4 | Dualitätsdrehung der Krümmung | 0,981 | kann γ_L nicht geben |
| 31 | Oktant-Auslese | H123, r58 | Gewicht 2 nur bei getrennter Orientierung | β′ = 0,543379 | widerlegt (m_W −20,3σ) |
| 32 | Auslese legt Frame fest | H122 | Extremum der Auslese | — | Frame fest, Achse nicht |
| 33 | Halbklassisches Spektrum | k245 | j + ½ in beiden Frames | γ_L = 2 exakt | erklärt die Hopf-Lücke, verfehlt die Daten |
| 34 | Vergleich mit OP5-Auslese | r48 | zwei Auslesen | — | verwandt, nicht gleich |
| 35 | Feldgleichung auf dem Turm | r64.4 | rekursive Feldgleichung | κ = 1,2004 | legt β nicht fest |
| 36 | Überlapp, Himmelskugel | H161, H164 | β = Überlapp Hopf-Zustand/Gegenpol | — | Identitäten für jedes β |
| 37 | Maske ε = η | H45, H134 | Maskenstärke = Rapidität | — | nur Eingabe |

## Schon geprüfte geschlossene Kandidaten (γ_L oder β)
2 und 1/√3; 1,8392867552; 1,820; P3; 2,151501 und 0,604468 (SU(2)); 1,255868 und 0,336784 (Kramers); log₂3; 2,153 und 1,077 (nur T geändert);
√Ω_M = 0,5578; 1,864824 (H104); 1,837930 und 0,543379 (Oktant); 2^(1−γ_L) = 0,549161; Wurzel von β³+β²+β−1 (0,5437); neun Geschwindigkeiten
(1, ½, 1/√3, √(2/3), 1/√2, tanh(½ arcosh 2), tanh γ_M, tanh γ_P); 16 Horizontfrequenzen; 47 natürliche Einheiten; 24 Verhältnisse in r16.9(d).

## Was eine Herleitung nach dem Bestand leisten muss
1. Die Eingaben γ_BI und γ_string sind Literaturwerte, nicht hergeleitet (F11).
2. Der Wert braucht die U(1)-Zählung mit Gewicht 2 je Spin (m = ±j) für M und „nur j = ½“ für T.
3. Er braucht das Flächenspektrum √(j(j+1)) (H104, k245).
4. Die Regel ist gleichwertig zu einem frame-abhängigen Flächenquant (r10.3); weder unitäre Boosts noch J_B noch die Holst-Drehung erzeugen es.
5. γ_L ist der Faktor von (M, M̄), nicht von (M, T).
6. Das Leptonfenster [0,545; 0,570] ist nicht blind; die bisherigen Treffer sind mit Zufall verträglich.

## Zurückgestellte Ideen mit Bezug
I1 (mehrere LQG-Systeme, durch einen String verbunden): Auslöser 3 (Rechnung berührt β_sym als γ_BI/γ_string) hat am 15. und 16.11. schon gegriffen (Nr. 14–16).
I6 (kurze englische Notiz): Auslöser 2 lautet „OP1 bekommt eine Herleitung der M-Regel oder wird zurückgestellt“.
