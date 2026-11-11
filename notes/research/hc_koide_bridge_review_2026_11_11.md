# HC-Abstieg zu Koide: bedingte Verbindung

Datum: 2026-11-11. Quellengebundene Codex-Selbstprüfung einer bereits im
Paper formulierten Implikation; keine neue Hypothese, kein blinder Test.

## Quellen und Vorwissen

- `hc-mass-identification.tex`, SHA256
  `4a2cecf409f75355ea3c49e8191993a4cb4019d8c997eb0a64e4674a62301f4c`:
  Proposition `v480:hc-mass-descent` und anschließender Absatz ab
  „If an independently supplied seed“ bis vor „Obstructions“.
- `koide-and-kernel.tex`, SHA256
  `63fe03eb53ec883292ac09935f65fc04bb4a9f6e7a32870743471cdc294336c7`:
  Proposition `v480:koide-hc-mixing` samt Originalbeweis.
- Die beiden Selbstprüfungen vom selben Datum nennen die Zusatzbedingungen
  bereits. Die QAM-Registersuche nach `hc-mass` liefert keinen Treffer;
  es wird kein MMA-Beleg als Nachweis beansprucht.

## Aussage und Typen

H ist ein reeller Hilbertraum, J eine orthogonale Involution und
B:H→R³ eine beschränkte Koisometrie mit J-invariantem Kern.
R³ trägt das euklidische Skalarprodukt und dieselbe geordnete
Generationenbasis wie der Koide-Vergleichsraum. Der abstrakte Übergang
identifiziert ausschließlich diese beiden reellen Wurzelräume.
Er identifiziert weder M/T/P-Sektoren noch Generationen mit Sektoren.

Zusätzlich: Ein unabhängig gelieferter Seed erfüllt Bf₀=e mit
e=(1,1,1)/sqrt(3); alpha>0 und x=alpha BCf₀ ist ein nichtnulliger,
komponentenweise nichtnegativer Vektor physikalischer Hauptwurzeln.
Die letzten physikalischen Identifikationen sind Voraussetzungen.

## Prüfung der Implikation

Der Abstiegssatz liefert J_m=BJB*, eine orthogonale Involution, und
BC=C_m B. Daher x=alpha C_m e. Damit sind sämtliche Voraussetzungen
der Koide-HC-Proposition erfüllt. Mit h=<e,J_m e> folgt
K=2/[3(1+h)] und h>-1. Nach Definition des adjungierten Operators ist
h=<B*e,JB*e>. Somit gilt K=2/3 genau dann, wenn dieser Ausdruck null ist.
Die Norm von B*e ist eins, weil BB*=I. Ein Wechsel der Wurzelraummetrik
oder eine beliebige nichtorthogonale Koordinatentransformation wäre
keine gültige Anwendung dieses Arguments.

**Urteil: proved as written** als bedingte mathematische Implikation
des Originalabsatzes. **Die native physikalische Anwendung bleibt
conditional on a named input:** B, Seed, Wurzelgesetz, Positivität und
unabhängige Orthogonalitätsselektion fehlen.

## Grenzfälle und Gegenprobe gegen eine stärkere Aussage

J=I und B=I erfüllen den Abstieg, f₀=e liefert positive gleiche Wurzeln.
Dann h=1 und K=1/3: Der Abstieg allein erzwingt Koide nicht.
J=-I ergibt C=0; der Fall scheitert an der ausdrücklich geforderten
nichtnulligen Auslesung. Eine global nichtnegative lineare Auslesung
auf ganz H wäre wegen f und -f null. Zulässigkeit muss deshalb auf
einer eingeschränkten Zustandsmenge geprüft werden.

## Registrierung und Grenzen

Der Originalabsatz wird als Erklärung mit geprüften Abhängigkeiten zu
beiden Originalbeweisen registriert, nicht als zusätzlicher unabhängiger
Beweis. Der Argumentationsbaum behält beide abstrakten Frames. Der
Exporter meldet weiterhin `frame-bridge-required`, da der Store noch
keinen maschinell verifizierten Typ für solche Abbildungen besitzt.
Die mathematische Identifikation ist hier dokumentiert; diese technische
Meldung wird nicht durch Umbenennen der Frames unterdrückt.

Offene Guards: native Abbildung und Seed/Wurzelgesetz; unabhängig
begründete Orthogonalität; maschinenprüfbare typisierte Frame-Abbildung.
Bestehende Guards bleiben unverändert. Keine OP-Schließung.
