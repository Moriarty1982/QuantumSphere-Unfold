# P-Rand: Nullbedingung und Energiekrümmung

Analytische Erkundung gemäß [Vorab-Notiz](P_Vorab.md), Commit 5f8b0668db8e84a733e6556beb50d236b4ac7877. Auf einen festen Beobachter bezogen; die betrachteten Felder sind homogene Werte bzw. lokale Plane-Wave-Amplituden, keine geschlossene M–T–P-Zelllösung.

Setze z0=E0(e1+i e2) mit E0>0, S(z)=z·z und u(z)=z†z/2. Dann S(z0)=0 bei u0=E0²>0. Die Ausbreitungsrichtung ist e3.

- Dualitätspfad z_rot(t)=exp(it) z0: S=0, u=u0, u''(0)=0. Die reellen E/B-Vektoren drehen transversal; die Richtung und der freie Maxwell-Energie-Impuls-Tensor bleiben erhalten.
- Amplitudenpfad z_amp(t)=(1+t²/2+it) z0: S=0 und dieselbe Richtung. u=u0(1+2t²+t⁴/4), u'(0)=0, u''(0)=4u0>0. Beide Pfade besitzen am Start sogar dieselbe Feldtangente iz0; der Energievergleich bei stationärer Energie entlang des jeweiligen Pfads ist daher kein Nachweis unterschiedlicher intrinsischer Hesse-Richtungen. Er zeigt ausdrücklich, dass die bloße Randbedingung die Fortsetzung des Pfads nicht bestimmt.

Eine energieflache Fortsetzung ist im freien Maxwell-Modell möglich. Die Nullbedingung allein erzwingt sie nicht. Für den Verbund ist offen, ob die tatsächliche Schnittstellenverschiebung auf diese fortgesetzte Dualitätsbahn abgebildet wird und ob die gesamte Kopplungsenergie die entsprechende gemeinsame Drehung respektiert. Eine Symmetrie nur des Maxwell-Anteils genügt nicht. Daher kein Wert für die physikalische Rückstellkonstante; OP5 und H96 bleiben offen.
