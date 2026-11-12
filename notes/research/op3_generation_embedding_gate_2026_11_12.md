# OP3: Farbtriplet, Closure und echter Generationenraum

12. November 2026. Analytische, nicht blinde Erkundung und Quellenprüfung.
Fortsetzung von `op3_inner_operator_terms_2026_11_11.md`. Keine neue
Simulation, H-/k-Nummer, Parameteranpassung oder Freigabe eines OPs.
Veröffentlichungsvorbereitung bleibt auf Autorenwunsch zurückgestellt.

## Ziel und Urteil

Prüfziel: Liefert die bestehende Zuordnung e_4,e_5,e_6 selbst einen
ausgezeichneten invarianten Raum für drei unterschiedliche Leptonmassen?

**Nicht als native Generationenidentifikation nachgewiesen.** Die Quellen
liefern ein Farbtriplet nach Festlegung der inneren komplexen Struktur.
Die spätere Seed-Konstruktion ist ausdrücklich eine bedingte Einbettung,
keine Beseitigung der bereits bekannten Farb-/Generationen-Doppelverwendung.
Unter unten genannten Farbinvarianzannahmen wird ihre direkte Kompression
sogar skalar. Damit ist eine enge Route ausgeschlossen, nicht jede denkbare
Realisierung von drei Generationen auf dem größeren Träger.

## Vorwissen geprüft

Einordnung: Gesamtkarte T7/T8/T13. Geprüfte Quellstellen:

- `v470/10_sphaera_and_physics.tex`, `thm:three-generations`, samt
  nachfolgendem Statusvermerk: Farbrotation und Generationen wurden auf
  dieselben Einheiten gelegt; eine zweite dreifache Struktur ist nötig.
- `v490-post-release-layers.tex`, r33.2 und H18: rechte Gram-Labels können
  vom linken Spinorwirken getrennt werden, liefern aber noch keine gelöste
  Massenfrage. Die historischen numerischen H18-Befunde werden hier nicht
  als neu ausgeführte Rechnung oder allgemeiner Unmöglichkeitssatz benutzt.
- Dort r35.1: innere Einheit L_e7, ihre Bildrichtungen und die expliziten
  Übersetzungsprojektoren zur äußeren komplexen Einheit.
- Dort r36.1 und Folgerungen: der Zyklus e4→e5→e6 liegt in der Farbgruppe;
  die Doppelverwendung wird nicht durch einen Framewechsel behoben.
  Bereits genannte Alternativen sind die drei Trialitätsslots von O³
  und die rechte Quaternion-/Dixon-Struktur aus r33.
- `generation-coupling.tex`, `v480:generation-states` und
  `v480:generation-closed-seeds`; `analysis/Generation_Closure_Coupling.md`:
  Metrik, Seed-Einbettung, generationenneutrale HC-Wirkung und gemeinsame
  Darstellung von P und den Operatoren sind zusätzliche Daten.
- `op3_original_question_operator_map_2026_11_11.md` und
  `op3_inner_operator_terms_2026_11_11.md`: Unterschied von Koide-Frage,
  Hüllenverträglichkeit, Übergangs-Gram-Matrix und innerer Kompression;
  die erforderliche Invarianz des Seed-Bildraums wurde separat benannt.

Die Auslöser der zurückgestellten Ideen wurden geprüft; diese lokale
Darstellungsprüfung löst keine neue der dortigen physikalischen Routen aus.
Rückwärtssuche statt weiterer Fits: Erst den Raum mit den richtigen
Symmetrierollen festlegen, dann einen Operator auf diesem Raum auswerten.

## 1. Welche drei Richtungen die ursprüngliche Tabelle tatsächlich benennt

In der inneren komplexen Struktur I_7=L_e7 gilt nach der vorhandenen
Quellenkonvention

$$I_7e_4=-e_3,\qquad I_7e_5=-e_2,\qquad I_7e_6=e_1.$$

I_7²=-I; es ist nicht die HC-Involution J mit J²=I aus dem späteren
Hilbertraumvergleich. Die reellen Richtungen e4,e5,e6 allein bilden daher
keinen unter I_7 abgeschlossenen komplexen Raum. Zusammen mit ihren
I_7-Bildern bilden sie die reelle sechsdimensionale Darstellung, die als
ein komplexes dreidimensionales Farbtriplet gelesen wird. Die Partner
e1,e2,e3 sind dort keine zweite unabhängige Generationenfamilie.

Die Übersetzung in die äußere komplexe Einheit verändert diese Rollen
nicht beliebig. r35 benutzt dazu die ausdrücklich deklarierten Pi_±,
hier anders benannt, um sie nicht mit dem Closure-Projektor P oder den
HC-Projektoren zu verwechseln. Dies sind Darstellungsabbildungen, keine
unbegründete Identifikation zwischen M-, T- und P-Frame.

Die spätere Wahl phi_- tensor e4,e5,e6 wird erst auf einem zusätzlich
festgelegten Tensorprodukt zur Seed-Isometrie. Selbst dann sind
„drei geschlossene odd Zustände“ und „drei Lepton-Generationen“
verschiedene Behauptungen.

## 2. Ein überprüfbares Symmetriekriterium statt eines Massenfits

Sei K ein positiver komplexer Hilbertraum, R_c(g) eine unitäre dargestellte
Farbwirkung und U_c(g) die fundamentale SU(3)-Wirkung auf C³. Es seien

$$T_0:\mathbb C^3\to K,\quad T_0^*T_0=I_3,\quad
 R_c(g)T_0=T_0U_c(g),$$

$$P=P^*=P^2,\quad [P,R_c(g)]=0,\quad G=T_0^*PT_0.$$

Dann ist G mit allen U_c(g) vertauschbar. Dies folgt durch Einsetzen
der Intertwinerbeziehung und von R_c(g)*P R_c(g)=P.

Warum muss ein solcher 3×3-Kommutant skalar sein? Die Vertauschung mit
allen Diagonalmatrizen diag(exp(iu),exp(iv),exp(-i(u+v))) zwingt alle
Außerdiagonaleinträge auf null. Die Vertauschung mit der zyklischen
Permutationsmatrix, die ebenfalls in SU(3) liegt, erzwingt gleiche
Diagonaleinträge. Damit gilt direkt

$$G=cI_3,\qquad 0\leq c\leq1.$$

Für c=0 gilt PT_0=0: kein Seed überlebt die Projektion. Für c>0 ist

$$S=c^{-1/2}PT_0,\qquad R_c(g)S=SU_c(g).$$

Die Closure-Normierung bewahrt also den Farbtyp. Sie verwandelt ein
Farbtriplet nicht in drei unabhängig farblose Generationen.
Dieser Schluss setzt Farbinvarianz von P ausdrücklich zusätzlich
voraus; [P,J]=0 aus der HC-Konstruktion allein reicht dafür nicht.

Sei nun Omega ein dargestellter farbneutraler Massenterm auf einem
farberhaltenden festgehaltenen Hintergrund, also

$$[\Omega,R_c(g)]=0.$$

Dann folgt für die direkte Kompression

$$A_G=S^*\Omega S,\qquad [A_G,U_c(g)]=0,\qquad A_G=aI_3.$$

Bei Hermitizität ist a reell. Selbst bevor die zusätzliche Invarianz
von im(S) geklärt ist, kann diese Kompression keine drei verschiedenen
Eigenwerte besitzen. Ist im(S) außerdem invariant und a>0 als Masse
identifiziert, ergeben sich drei gleiche Massen und K=1/3. Für a=0
ist der nichtnullige Koide-Quotient nicht definiert.

Ist im(S) nicht invariant, darf man aus dieser Kompression ohnehin
keine drei vollen Eigenmassen ablesen. Auch dann bleibt die Deutung
der drei Farbrichtungen als die drei Generationen unbegründet.

Grenze: Eine Operation oder ein Hintergrund, die Farbe nicht erhalten,
ist durch diesen bedingten Ausschluss nicht erfasst. Dann wäre aber
gerade die Annahme einer farbneutralen Massenauslesung geändert. Das ist
kein kostenfreier Ausweg durch Umbenennung von Farbe in Generation.

## 3. Welcher Raum stattdessen benötigt wird

Die strukturelle Trennung lautet

$$V_{\rm phys}\otimes G_{\rm gen},\qquad
 R(g)=R_{\rm phys}(g)\otimes I_{G_{\rm gen}}.$$

Auf dem Generationenraum wiederholt sich dabei derselbe physikalische
Darstellungstyp, statt dass seine drei Basisrichtungen drei Komponenten
eines Farbtriplets sind. Ein erlaubter innerer Vergleich kann dann
die Form I_phys tensor A_gen haben. Die Symmetrie auf V_phys erzwingt
keine Gleichheit der Eigenwerte von A_gen. Sie bestimmt A_gen aber auch
nicht. Insbesondere ist eine frei angehängte C³ keine Herleitung der
Anzahl oder der Massen der Generationen.

Für eine einzelne Farbtripletkopie ist der obige direkte Kommutant skalar;
bei mehreren gleichartigen Kopien kann er zwischen diesen Kopien wirken.
Für Lepton-Generationen ist insbesondere derselbe farblose und passend
geladene physikalische Darstellungstyp mehrfach zu realisieren. Diese
Rollen sind vor der Auslesung zu bestimmen, nicht aus den Eigenwerten
einer passenden Matrix nachträglich zu erschließen.

## 4. Zwei bereits vorhandene Ansätze: keine neue Verdopplung erfinden

| Vorhandener Ansatz | Welche Rollen trennt er? | Was noch nicht geliefert ist |
|---|---|---|
| Drei Trialitätsslots O³ | Slotindex kann von der diagonalen Farbwirkung innerhalb jedes Slots getrennt werden. | Native volle Symmetrie-/Operatorwirkung, Closure und ein ausgezeichneter invarianter Drei-Zustandsraum mit denselben physikalischen Quantenzahlen. |
| Rechte Quaternion-/Dixon-Labels, r33 | Bestimmte Gram-Labels können vom linken Spinorwirken getrennt werden; die Slot-Zyklik kommutiert mit Farbe. | Die Labels sind zunächst Funktionen von Zuständen. Sie sind damit noch keine drei linearen Eigenzustände, keine Isometrie S und kein hergeleitetes Massenspektrum. |

Beide Kandidaten stammen aus den vorhandenen Quellen. Keine dieser
Zeilen behauptet bereits eine native volle Tensorfaktorisierung oder
einen geschlossenen Generationenoperator. Dass eine Symmetrie kommutiert,
ist erst eine notwendige Rollenprüfung, keine Dynamik.

## Ergebnis, Status und nächster Auftrag

Der Ursprung der Lücke liegt vor der konkreten 3×3-Massenmatrix:
Die aktuelle Seed-Konstruktion bewahrt ihre deklarierten Hilbertraum-
Eigenschaften, rechtfertigt aber die geerbte Bezeichnung „Generationen“
nicht. Unter Farberhaltung kann die Benennung der Farbbasis auch
mathematisch keine nichtdegenerierte direkte Massenauslesung erzeugen.

Der nächste konkrete Quellenauftrag ist deshalb der bereits vorhandene
**Trialitätsslotraum O³**: Wie wirken dort der linke Spinor/Lorentzteil,
Farbe, Closure und die M-/T-Kopplung auf den Slotindex? Gesucht wird ein
nativer Mehrfachraum desselben physikalischen Zustands, nicht ein neues
Farbtriplet. Die rechte Gram-Lesart bleibt als alternative Vergleichsroute
erhalten; die beiden Routen werden nicht ohne Abbildung gleichgesetzt.

Beleggrenzen: Der schreibgeschützte QAM-MCP ist in dieser Sitzung nicht
verfügbar. Die lokalen schreibgeschützten CLI-Suchen nach generation,
triplet und e_4 ergaben keine passenden Ausgaben im geladenen Index.
Das ist kein Nachweis der Abwesenheit solcher Aussagen im gesamten Werk.
Kein gespeicherter MMA-Beleg wurde beansprucht oder neu ausgeführt.

Die Kommutantenrechnung ist im Text direkt hergeleitet, ohne numerischen
Test oder neue externe Theoremquelle. Es wird keine Neuheit behauptet.
Provenienz: Selbstprüfung am Quellenstand main 802c7af mit den lokalen
Notizen des Forschungszweigs. OP1–OP5 und alle wissenschaftlichen Guards
behalten ihren Status; historische Runden und Papertexte bleiben erhalten.
