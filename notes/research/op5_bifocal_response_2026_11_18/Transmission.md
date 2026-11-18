# Schließt der Transport mit dem Casimir-Spalt?

Analytische Erkundung nach [Vorab-Notiz](Transmission_Vorab.md), Commit b6dcd0cfc8e6a3ef83963b4c94c21f5e704c68d4. Endliche 1D-Dirac-Massenbarriere gleicher Breite wie der mechanische Spalt als Kontrollmodell. Kein Nahkontaktmodell.

Setze ħ=c=1, H=−iσ_x∂_x+mσ_z im Spalt, masselose gleichartige Leitungen außen. Bei 0<ω<|m| gilt ∂_xψ=Bψ mit B=iωσ_x−mσ_y und B²=κ² Id, κ=√(m²−ω²). Die Transfermatrix ist cosh(κd) Id+(sinh(κd)/κ)B. Im Außenkanal tragen die σ_x-Eigenvektoren die nach rechts/links gerichteten Ströme gleichen Betrags. Die Transfermatrix hat Determinante eins; ohne von rechts einfallende Welle hat die Transmissionsamplitude Betrag 1/|M_22|. Daraus folgt T=[1+(m²/κ²)sinh²(κd)]⁻¹.

Bei fester endlicher Masse ist T(d)>0 für endliches d und wächst bei kleiner werdendem Spalt. Bei d→0 folgt T→1. Kontrolle m=1, ω=1/2, d₀=1: T(1)=0,439293; T(4/5)=0,571695; T(1/10)=0,990074. Damit liegt bei der mechanischen Casimir-Schwelle keine Transmissionsnullstelle vor. Bei wachsender Masse und festem ω liefert m d→a endliches T→sech²(a); eine echte Sperre im betrachteten Grenzfall verlangt |m|d→∞ oder andere Rand-/Kopplungsphysik. Diese Aussage über m(d) bezieht sich auf genau den konstanten Slab pro d.

Die einfache Deutung des Spalts als endliche Massenbarriere bewirkt also mechanisch eine Öffnung des Transportkanals statt einer Sperre. Casimir-Schwelle aus Casimir.md und ideale Leitwertsperre aus Gate.md sind damit in diesem gemeinsamen Modell nicht vereinbar. Eine separate Zustandsabhängigkeit des Massenspalts oder ein anderer Kontaktoperator müsste aus einem physikalischen Kandidaten folgen; bloß feinere Spaltgeometrie genügt nicht. OP5 und H96 bleiben offen.
