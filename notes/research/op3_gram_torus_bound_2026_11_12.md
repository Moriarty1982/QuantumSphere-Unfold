# OP3: Exakte Koide-Schranke der H18-Auslesung auf dem farbfesten Torus

12. November 2026. Analytische Erkundung, nicht blind. Keine Datenanpassung,
Simulation, neue H-/k-Nummer oder Änderung historischer Runden.
Einordnung: T5/T7 Träger; T8 Massenauslesung. Selbstprüfung, kein unabhängiges Audit.

## Vorwissen und präzise Prüfbehauptung

Ausgangspunkt ist Revision ecd068a, insbesondere
`op3_dixon_gram_bridge_2026_11_12.md` und
`op3_triality_carrier_gate_2026_11_12.md`.
Quellen: r15 in `sources/research/parts/v480-post-release-layers.tex`,
r33.2/H18 in `notes/research/v4_10_0_r32_r33/rounds/v490_r33_round.tex`
und `llm/Ergebnis_H18_Links_invariante_Massen.md` desselben Ordners.
Suchen in predictions/, den bisherigen OP3-Notizen und analysis/ wurden
mit den dortigen Gram-/Dreiecksargumenten abgeglichen. Der verwandte
`v480:hc-mass-triole-bound` in `hc-mass-identification.tex` betrifft
Nullsummenvektoren und ein anderes Massengesetz; er wird hier nicht
ohne neue Trägerzuordnung angewendet. Keine neue Hypothese registriert.

Geprüft wird ausschließlich: Für alle farbfesten r15-Konfigurationen und
das gemeinsame H18-Gesetz m_i=kappa sqrt(mu_i), kappa>0, liegt der
Koide-Quotient bei nichtverschwindender Gesamtauslesung zwischen 1/3 und 1/2.
Die Slots sind reell normierte Oktonionen in L=span_R(1,e7), mit dem
euklidischen Skalarprodukt; keine komplex-bilineare Boost-Auslesung.

## 1. Explizite Einschränkung der vorhandenen Funktionen

Schreibe x_i=exp(e7 alpha_i), mit
alpha_1+alpha_2+alpha_3=0 modulo 2pi. Dann gilt

$$\langle x_j,x_k\rangle=\cos(\alpha_j-\alpha_k),\qquad
\mu_i=2\sin^2(\alpha_j-\alpha_k).$$

Mit alpha_1=alpha, alpha_2=beta, alpha_3=−alpha−beta wird daraus

$$ (\mu_1,\mu_2,\mu_3)
=2\bigl(\sin^2(\alpha+2\beta),
        \sin^2(2\alpha+\beta),\sin^2(\alpha-\beta)\bigr).$$

Es gibt also drei konkrete Funktionen zweier reeller Phasen. Sie müssen
nicht gleich sein: alpha=pi/12, beta=pi/6 liefert exakt
((2+sqrt(3))/2, 3/2, (2−sqrt(3))/2), drei positive verschiedene Werte.
Die Dimensionszählung des Torus allein schließt eine Dreifachauslesung
somit ausdrücklich nicht aus.

## 2. Die entscheidende zusätzliche Beziehung

Setze w_i=exp(2 e7 alpha_i), betrachtet als Punkte der euklidischen Ebene L.
Ihre Sehnenlängen erfüllen

$$d_i=|w_j-w_k|=2|\sin(\alpha_j-\alpha_k)|,\qquad
\sqrt{\mu_i}=d_i/\sqrt2.$$

Damit sind die H18-Massen m_i=(kappa/sqrt2)d_i gemeinsame Vielfache
der Seitenlängen eines möglicherweise entarteten Dreiecks. Folglich gilt

$$m_i\leq m_j+m_k.$$

Dieser Beweisschritt benötigt nicht einmal die Produktphasenbedingung;
er gilt für beliebige drei Einheitsphasen in L. Eine andere Auswahl
auf demselben Torus kann die Dreiecksbedingung daher nicht umgehen.

## 3. Exakte Koide-Schranke und Randfälle

Seien r_i=sqrt(m_i) und s=r_1+r_2+r_3>0. Aus der Massendreiecksbedingung
folgt r_i≤sqrt(m_j+m_k)≤r_j+r_k, also r_i≤s/2. Damit

$$\frac13\leq K=\frac{\sum_i m_i}{(\sum_i\sqrt{m_i})^2}
=\frac{\sum_i r_i^2}{s^2}\leq\frac12.$$

Die untere Schranke folgt aus Cauchy–Schwarz; die obere aus
sum r_i²≤(s/2)sum r_i. Beide Grenzen werden im zugelassenen Torus erreicht:

- Phasen (0,2pi/3,−2pi/3) ergeben gleiche positive mu_i und K=1/3.
- Phasen (pi/6,pi/6,−pi/3) ergeben mu=(2,2,0) und K=1/2.
- Bei mu=(0,0,0), etwa drei Nullphasen, verschwinden alle Massen;
  K ist undefiniert. Dies ist kein Gegenbeispiel und kein Koide-Treffer.

Damit ist K=2/3 unter den genannten Voraussetzungen exakt ausgeschlossen.
Es wird kein Messwert benötigt. Bei drei positiven Massen gilt sogar
K<1/2, da alle r_i<s/2 sind.

## Prüfspur und Reichweite

Abhängigkeiten: r15-Phasenträger → reelles Skalarprodukt → r33-mu-Formel
→ zusätzliches H18-Massengesetz → Sehnen-Dreieck → Wurzeldreieck → K-Schranke.
Die algebraischen Schritte und die Null-/Gleichheitsfälle sind oben direkt
geprüft. Das H18-Massengesetz bleibt eine Annahme, keine native Identifikation.
Keine numerische Rechnung trägt den Beweis; historische H18-Scans werden
nicht erneut ausgeführt oder als erschöpfender analytischer Beweis ausgegeben.

Dies ergänzt den historischen Potentialtest um einen analytischen Ausschluss
auf dem hier präzisierten farbfesten Einheitsphasen-Träger. Nicht geprüft
oder ausgeschlossen sind allgemeine O³-Konfigurationen, andere Massengesetze,
ungleiche Kopplungen oder ein neu definierter physikalischer Zustandsraum.
Solche Änderungen brauchen eine eigenständige native Begründung.

Rückwärtssuche: Eine reine Phasenauswahl, ein zusätzliches Auswahlpotential
oder eine gemeinsame Skala kann diese Route nicht zu K=2/3 führen.
Nächster Quellenauftrag ist deshalb die spätere Kopplungsroute r53:
Welche vom H18-Gesetz verschiedene native Operation ist dort tatsächlich
definiert, und welche Ausschlüsse sind bereits dokumentiert? Kein neuer Scan.

QAM-Leseserver nicht verfügbar; lokale read-only Suche `triole` ohne Ausgabe.
Keine MMA-Belege oder Hashprüfung behauptet. OP1–OP5/C5/C6/T2 und Guards
unverändert. Auslöser zurückgestellter Ideen erneut geprüft; aus diesem
Ausleseausschluss ergibt sich kein neuer einschlägiger Auslöser.
