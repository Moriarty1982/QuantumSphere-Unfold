# OP5: stärkere Gewichtung großer Punktfehler

29.10.2026. Unverändert quadratische Zweimodenfamilie und Region Radius .01. Zwei Zweige aus OP5_Boundary_Fair_Balanced_Check.json mit denselben401 tatsächlich aktiven Anpassungspunkten, drei äußere gedämpfte Gauss-Newton-Schritte je Zweig. Ausführbare Kontrolle401*24=9624 Residualkomponenten bestätigt. Keine Modelländerung.

Kontrollzweig minimiert ungewichtete Summe der quadratischen Punktnormen. Neuer Zweig verwendet iterativ neu bestimmte Punktgewichte w=max(||F_point||,.1*RMS), normalisiert auf mittleres w²=1. Alle24 reellen Komponenten eines Punktes werden gleich gewichtet. Der lineare Schritt minimiert somit lokal eine an der vierten Potenz orientierte Fehlerfunktion. Gewichte bleiben innerhalb eines äußeren Schritts fest; Schrittannahme prüft tatsächliche gegen vorhergesagte Reduktion dieses gewichteten quadratischen Surrogats und Geometrie. Das ist kein exakt gelöstes Minimaxproblem und keine monotone Garantie für eine unverändert definierte globale Viertpotenz-Zielfunktion.

Abschließende unangetastete Prüfmengen seed291046:1024 gleichmäßig auf8 Flächen verteilte Randpunkte sowie4096 Innenpunkte. Beiden Zweigen identisch und nicht zur Schrittannahme benutzt.

Rand: Kontrollzweig RMS .000156881, Maximum .000411706. Gewichteter Zweig RMS .000174291, Maximum .000321192. Das beobachtete Randmaximum sinkt gegenüber der normalen Fortsetzung um etwa22%, der RMS steigt um etwa11%.

Innen: Kontrollzweig RMS .000109764, Maximum .000332919. Gewichteter Zweig RMS .000142893, Maximum .000308807. Maximum etwa7% niedriger, RMS etwa30% höher. Gegenüber dem gemeinsamen Ausgangsfeld verbessert die gewichtete Variante die Maxima ebenfalls, verschlechtert aber die mittleren Restnormen. Deshalb ersetzt sie den bisherigen besten RMS-Stand nicht stillschweigend.

Geometrische Kennzahlen, Zustandsprojektionen und einzelne Flächenkontrollen vollständig in OP5_Peak_Weighted_Validation.json. Positive Normierungsgröße und invertierbare Coframe sowie raumartige t-Schnitte an geprüften Punkten sind Teil des Vergleichsvertrags; keine Uniformgarantie oder regionale Existenzbehauptung. Numerische Optimierungsverbesserungen sind keine physikalischen Genauigkeitszusagen.

Ergebnis: Der Zielkonflikt zwischen Mittelwert und beobachtetem Maximum ist explizit. Stärkere Gewichtung kann Fehler umverteilen und Stichprobenmaxima reduzieren, schließt die Gleichungen aber nicht. Ein kontrollierter nächster Test wäre eine moderate Mischung beider Zielfunktionen oder ein weicher Maximalfehler mit dokumentierter Schärfe, immer unter denselben unabhängigen Kontrollen. Nicht allein durch Wahl einer anderen Norm einen physikalischen Fortschritt behaupten.

Artefakte OP5_Peak_Mean_Control.py/.json, OP5_Peak_Weighted_Check.py/.json, OP5_Peak_Weighted_Validation.py/.json, lokale Vorläuferdaten und Evaluatoren erforderlich. Lokal gespeichert, nicht committed. Beide Kandidaten separat erhalten; Paper-Grafik unverändert, OP5 offen.
