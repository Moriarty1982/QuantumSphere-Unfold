# Dorau–Much in QAM: Beobachter, Zugang und Geometrie

7. November 2026. Übersetzung und Rechenbeispiel einer externen Theorie, keine neue QSC-Runde. Quelle: [Dorau und Much, PRL 136, 091602 (2026)](https://doi.org/10.1103/lmq8-nsty), Gl. (4), (10)–(13), (18), (20)–(28); [lesbare Formeln der Autorenfassung](https://arxiv.org/html/2510.24491). Das [QAM-Beispiel](../../qam/examples/dorau-much.tex) macht die Profil- und Map-Zuordnungen explizit. Im Gesamtbild gehört es zur QAM-Schnittstelle (T14) und zur Frage nach einer physikalischen Auslesung (T13), ohne eine Identifikation der Sektoren (T1/T3) oder einen OP5-Schluss.

## Drei verschiedene Vorgänge

1. **Beobachter und Uhr.** Im flachen Referenzmodell wähle einen gleichmäßig beschleunigten Beobachter im rechten Keil. Mit der Vorzeichenkonvention der Quelle ist die Dilatation auf den Horizontdaten $U\mapsto e^{2\pi t}U$. Der modulare Parameter $t$ ist dimensionslos. Für die zugehörige Boost-Parametrisierung ist die Rapidität bis auf die Orientierung des Flusses $2\pi t$; der Betrag entspricht $a|\tau|$ bei Eigenbeschleunigung $a$ und Eigenzeit $\tau$ ($c=1$). Das ist ein Vergleich von Flussparametern innerhalb derselben Raumzeit.
2. **Zugang.** Die Einbettung $\mathcal A(W)\hookrightarrow\mathcal A(\mathbb M)$ läuft auf Observablen vom Keil in die volle Algebra. Auf Zuständen läuft die zugehörige Einschränkung andersherum: $\omega_W(A)=\omega_{\rm M}(A)$ für $A\in\mathcal A(W)$. Das ist die explizite Map im Beispiel. Der Horizont-Skalierungsgrenzfall ist ein weiterer Schritt; die Zielgrößen der Rechnung leben auf der Horizont-Algebra. Die Restriktion ist im Allgemeinen nicht umkehrbar. Ein Koordinatenwechsel allein entfernt keine Observablen.
3. **Physikalische Auslesung.** Im Horizontprofil ist die relative Entropie der gewichtete Boost-Fluss in modularer Normierung. Der Übergang zur Flächenänderung gehört zum geometrischen Profil **desselben** Beobachters. Er setzt die Flächenregel voraus. Raychaudhuri, lokaler Abgleich in allen Nullrichtungen und Energie-Impuls-Erhaltung samt Bianchi-Identität ergeben die semiklassische Einstein-Gleichung in der Näherung der Quelle. $\Lambda$ bleibt frei.

Damit können zwei QAM-Profile auch denselben Beobachter verwenden. Der Profilname bezeichnet hier zusätzlich den Geltungskontext. Keiner der Übergänge identifiziert Rindler mit M, T oder P. Die QAM-Software erfasst Map, Zielausdruck und Herkunft; die mathematische Bedeutung der Map muss separat angegeben werden.

## Wertvergleich im Horizontprofil

Schreibe $x=-U>0$, $\phi(U,y)=A f(x)g(y)$ mit glattem kompaktem Querprofil, $\int g^2d\mathrm{vol}_{\mathcal S}=1$, und $f(x)=\exp[-1/((x-1)(2-x))]$ auf $1<x<2$, sonst null. Dies sind gewählte Horizontdaten, keine Messwerte des Artikels. Gl. (12) gibt $S_H=2\pi A^2 I$, während (18) auf der Flussseite $J_B=A^2 I$ ergibt, mit $I=\int_1^2 x f'(x)^2dx$. Somit liefert die Übersetzung für dieselbe Eingabe exakt dieselbe Relation wie (12)–(13). In Planck-Einheiten ist mit der Flächenannahme $\delta A=4S_H$.

| Amplitude $A$ | Boost-Fluss $J_B$ | Relative Entropie $S_H$ | $\delta A$ unter Flächenannahme |
|---:|---:|---:|---:|
| 1 | 0,003284169 | 0,020635042 | 0,082540167 |
| 2 | 0,013136676 | 0,082540167 | 0,330160669 |

Simpson-Quadratur mit 1000 und 2000 Teilintervallen liefert dieselben gezeigten Stellen; das Vierfache bei doppelter Amplitude folgt analytisch. Das ist eine Auswertung der importierten Formeln, keine unabhängige Simulation der modularen Theorie.

Ein echter Darstellungsvergleich: Unter $U'=bU$ mit $b>0$ und mittransformiertem Profil gilt $U' (\partial_{U'}\phi)^2 dU'=U(\partial_U\phi)^2dU$. Derselbe Horizont und dieselbe Anregung liefern also unabhängig von der affinen Skalierung denselben Wert. Dagegen ändert die Wahl eines anderen Keils, welche Algebra und welche Flussdaten zugänglich sind; eine Gleichheit der Entropien folgt daraus nicht.

Der frühere Anschluss an Gram-Register und Petz-Rekonstruktion bleibt als spätere Frage stehen. Dieses Beispiel braucht ihn nicht.
