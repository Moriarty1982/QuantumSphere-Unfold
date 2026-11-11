# OP3: ursprüngliche Massenfrage und heutige Operatorroute

11. November 2026. Autorenauftrag: vor der Veröffentlichung inhaltlich
weiterarbeiten; ursprüngliche OP3-Frage und heutige Operatorformulierung
nebeneinanderlegen. Quellen- und Folgerungsprüfung, keine blinde Hypothese,
keine Simulation, keine H-/k-Neuvergabe. Veröffentlichungsvorbereitung ruht.

## Urteil und geprüfte Aussage

**Unvollständig: Es fehlt die Herleitung des physikalischen Auslesegesetzes
und der dazugehörigen gemeinsamen Operatormatrix.** Die ursprüngliche
Koide-/Phasenfrage, die spätere Hüllenverträglichkeit und der heutige
Closure-Defekt sind unterscheidbare Fragestellungen. Ihre Gleichsetzung
ist in den geprüften Quellen nicht bewiesen. Das betrifft die Verbindung
zwischen den Routen, nicht die Gültigkeit ihrer bedingten linearen Algebra.

Die historische Rekonstruktion benutzt die erhaltenen Quellsnapshots;
sie behauptet keine vollständige Sichtung sämtlicher früherer Versionen
oder den allerersten zeitlichen Gebrauch des Namens OP3.

## Vorwissen geprüft und Einordnung

Gesamtkarte: T8 (Massen/Mischung), T13 (Mastergleichung), T14/T15
(Belege/Guards). Gelesen wurden insbesondere:

- `sources/historical/01_historical_core_snapshot/03_op_closure_phase_and_formal_supplement.tex`,
  historischer Eintrag „Historical OP~3: Koide / $\theta_K$ formula“.
- Historischer Anhang `05_appendices_and_computational_completeness.tex`,
  Absatz A4 ab Zeile 2606: verlangte Härtung der Koide-Winkelherleitung.
- `sources/research/parts/v470/10_sphaera_and_physics.tex`,
  `thm:koide-triolic`, `thm:dirac-probe`, `prop:three-compatible-readings`,
  einschließlich späterer Statusvermerke.
- `sources/research/parts/v470/22_op_transport_arguments.tex`,
  `sec:op3-shell-theorem` und `sec:packet-phase-epsilon-compatibility`.
- `koide-and-kernel.tex`, `generation-coupling.tex`,
  `native-operator-link.tex` und `v470/16_master_model.tex`.
- Vorbefunde `koide_original_op3_cycle_phase.md`,
  `op3_closure_distortion_independence.md`, die einschlägigen Anfangsabschnitte
  von `op3_repair_connected_family_2026_11_10.md` und
  `hc_native_selection_gate_2026_11_11.md`.

Die Auslöser der zurückgestellten Ideen wurden geprüft; durch diesen
Quellenvergleich entsteht kein neuer physikalischer Auslöser. Es werden
keine neuen Parameterläufe auf derselben ungeklärten nativen Basis gestartet.

## 1. Drei Fragen statt eines über die Zeit unveränderten OP3

| Strang | Gefragte Aussage | Was daraus noch nicht folgt |
|---|---|---|
| Historische Koide-/Winkelfrage | Warum gelten der Wurzelquotient und die bestimmte Massenphase? | Eine dreifache Struktur allein legt weder Normverhältnis noch Phase oder Skala fest. |
| Spätere OP3-Hüllenfrage | Erhält ein Hüllen-/Residualübergang die native Closure-Klasse? | Eine zulässige Hülle liefert noch keinen Massenoperator und keine drei Messwerte. |
| Heutiger Defektvergleich | Welche Gram-Matrix erzeugt ein dargestellter Übergang aus geschlossenen Generationszuständen? | Positivität der Matrix identifiziert ihre Eigenwerte noch nicht mit physikalischen Massen. |

Der historische Snapshot bezeichnete den ersten Strang als strukturell
geschlossen. Das ist eine historische Statusbehauptung. Die aktuelle
Fassung bezeichnet die Herleitung ausdrücklich als offen und archiviert
die alte Winkelformel. Deren Datenabweichung wird hier nicht erneut
aus Messdaten berechnet.

Der spätere Hüllensatz definiert Zulässigkeit durch

$$K_{\rm ncl}(\mathfrak T_{r,s}c_3)=K_{\rm ncl}(c_3).$$

Unter seinen Transport-/Faktorisierungsannahmen bleibt dadurch der
zugehörige strukturelle Invariant erhalten. Es steht dort keine Gleichung,
die diesen Invariant als drei Leptonmassen oder deren Koide-Phase ausliest.
Auch der lokale Antiphasenkorridor des sichtbaren Hüllenquotienten ist
ohne weitere Abbildung nicht die Phase des dreidimensionalen Massenspektrums.

## 2. Was die heutige Massenroute zusätzlich einführt

Im positiven gemeinsamen Hilbertraum sei P der orthogonale
Closure-Projektor, J die getrennte orthogonale HC-Involution und S eine
isometrische Einbettung dreier geschlossener Seeds, PS=S. Für den
normierten dargestellten Taktoperator R werden definiert:

$$D=(I-P)RP,\qquad B=DS,\qquad Q=B^*B.$$

Die Definitions-/Abhängigkeitskette lautet:

1. J und C=(I+J)/2 bestimmen eine Zweiteilung, noch keine drei Generationen.
2. P und die drei Seeds benötigen eine gemeinsame Darstellung und Metrik.
3. R benötigt Matrixelemente relativ zu P und den Seeds.
4. Diese Daten bestimmen B und die positive Matrix Q.
5. Erst das zusätzliche Gesetz M_mass=kappa Q deutet deren Spektrum als
   Massen; kappa und die physikalische Identifikation bleiben zu begründen.
6. Koide verlangt zusätzlich ein bestimmtes Verhältnis der Wurzelnormen;
   danach bleiben die Phase und eine absolute Skala gesonderte Fragen.

Diese Kette ist ein nützlicher bedingter Vergleich. Sie ist keine bereits
nachgewiesene Übersetzung des historischen Hüllensatzes.

## 3. Die konkrete Stelle des Auslesewechsels

Die ältere Probe-Lesart verwendet ausdrücklich

$$m_{\rm comm}(\psi)={\hbar\over c}
 |\langle\psi,[R,P]\psi\rangle|.$$

Für P=P*=P² und P psi=psi gilt dagegen exakt

$$[R,P]\psi=(I-P)R\psi,\qquad
 \langle\psi,[R,P]\psi\rangle=0.$$

Der Übergangsvektor kann trotzdem nichtnullig sein. Beispielsweise für
P=diag(1,0), psi=(1,0)^T und R als Austauschmatrix erhält man
[R,P]psi=(0,1)^T: Erwartungswert null, Übergangsnorm eins.
Dies ist eine direkte endliche Gegenprobe, kein empirischer Test.

Der Vorbefund `generation-coupling.tex` benennt bereits genau diese
Unterscheidung. Hier wird sie als Verzweigung im Gesamtargument festgehalten:
Die Ersetzung des Erwartungswertes durch dessen Übergangsnorm repariert
die alte Formel nicht durch bloßes Umformen, sondern wechselt die Observable.
Das schließt andere Massemechanismen nicht aus.

Ebenso bereits bekannt: Für festes P und S fällt der globale Faktor in
R_beta=exp(i phi(beta))R_0 aus Q heraus. Eine solche Phase allein kann
in dieser Route keine beta-abhängige Massenhierarchie auswählen. Benötigt
würden echte relative Kanäle oder unabhängig bestimmte Änderungen von
Operator, Seeds oder Projektor; diese dürfen nicht nach dem Ziel eingesetzt
werden.

## 4. Rückwärtssuche: im Kern steht auch ein innerer Operator

Die bestehende Mastergleichung enthält bereits den erklärten Ansatz

$$\Omega=m_0I+\alpha PMP+\beta\mathcal T+\gamma\mathcal H_C.$$

Hier ist beta der dortige Koeffizient; er wird nicht mit beta_sym
gleichgesetzt. Die Formel ist ein formal organisierter effektiver Ansatz,
keine abgeschlossene eindeutige Herleitung seiner Kopplungen.

Bei einer gemeinsamen Darstellung ist der mögliche innere
Generationsoperator

$$A_{\rm gen}=S^*P\Omega PS=S^*\Omega S.$$

Ein geeignet hermitescher, kanonisch normierter innerer Massenterm kann
auch bei strikter Closure nichtnullig sein. Die triviale Gegenprobe
P=diag(I_3,0), S=(I_3,0)^T, Omega=diag(A,H) zeigt dies: Für jedes
hermitesche A gilt [Omega,P]=0 und A_gen=A. Closure setzt die innere
Massenmatrix also nicht automatisch auf null. Umgekehrt bestimmt sie
deren drei Eigenwerte nicht; A ist im Gegenbeispiel beliebig.

Das ist eine analytische Einordnung bereits vorhandener Möglichkeiten,
keine neue native Konstruktion. Der Sinn der Rückwärtssuche ist:
Nicht von vornherein alle Masse im äußeren Closure-Defekt suchen, wenn
der ursprüngliche Gleichungsansatz einen inneren Operator enthält.

## 5. Prüfpflichten und kleinster nächster Schritt

| Pflicht | Befund dieser Prüfung |
|---|---|
| Historische Koide-Frage von späterer Hüllenfrage unterscheiden | Quellenbelegt; keine Gleichsetzung bewiesen. |
| Aus orthogonalem P die Null des Kommutator-Erwartungswerts herleiten | Direkt nachgerechnet; gilt unter den genannten Annahmen. |
| Den Gram-Ansatz als identische alte Observable behandeln | Durch die endliche Gegenprobe ausgeschlossen. |
| Globalen Taktphasenfaktor zur Auswahl der Gram-Verhältnisse nutzen | Bei festem P/S ausgeschlossen; schon vorhandener Vorbefund. |
| Nichtnulligen inneren Massenterm mit Closure vereinbaren | Algebraisch möglich; noch keine native physikalische Identifikation. |
| Drei Massen aus dem tatsächlichen Kern bestimmen | Offen: gemeinsame Darstellung, Kopplungen, Auslesegesetz, Skala. |

Nächster konkreter Quellenauftrag: Die vier Beiträge zu S*Omega S einzeln
auf ihren Definitionsgrad prüfen. Gesucht sind erst einmal Matrixelemente
und relationsbedingte Freiheitsgrade auf derselben Generationseinbettung,
nicht eine neue numerische Anpassung. Falls diese Beiträge nur Platzhalter
sind, ist genau die fehlende Definition zu bearbeiten. Ein erfolgreicher
Hüllenmonitor oder ein passendes Zeta-Packet ersetzt diese Pflicht nicht.

## QAM-Abgleich und Grenzen

Der verfügbare schreibgeschützte QAM-Server wurde zuerst nach OP3 durchsucht:
kein Treffer im geladenen Index. Das beweist nicht das Fehlen aller
OP3-Aussagen im Projekt. Die anschließende Koide-Suche findet unter anderem
die Überlagerungsausgabe `09145C0397CAF9217491AEAE51233207` und deren
Moment-Prämisse `26EB7B270E0750C6BC8A587D34E2CF7D`; Status jeweils
conditional. Auch Präparation und Ausleseprofil bleiben Voraussetzungen.
Aus diesen Treffern wird keine neue allgemeine Gültigkeit oder eine
Verbindung zur nativen Hüllenklasse abgeleitet. Keine MMA-Neuausführung,
kein neuer Beleg und keine Änderung eines Aussage- oder OP-Status.

Provenienz: Selbstprüfung am Quellenstand main 802c7af; der Arbeitszweig
enthält zusätzlich die ruhende technische Payload-Vorbereitung. Es wurden
keine historischen Runden umgeschrieben und keine externen mathematischen
Sätze oder aktuellen Messdaten als neu geprüft beansprucht.
