# Ganzzahlige Dipol-Umlagerung am Ring

Analytische Erkundung nach [Vorab-Notiz](Ganzzahl_Vorab.md), Commit bf6d425beb71f9fda9a798cb18ec863c7680e2d1. Festes regelmäßiges Raster, ganzzahlige Änderungen q_j in einer gemeinsamen Einheit. Das ist eine zusätzliche Modellannahme.

Sei ζ=exp(2πi/N) und P(z)=Σ q_j z^j, Grad <N. Die drei Erhaltungsbedingungen sind P(1)=0 und P(ζ)=0; die zweite fasst beide reellen Dipolkomponenten zusammen. Für N=2^m, m≥3, ist das Minimalpolynom von ζ gleich z^(N/2)+1. Die Irreduzibilität folgt durch Eisenstein bei 2 nach z↦z+1: die dazwischenliegenden Binomialkoeffizienten sind gerade, der konstante Term ist 2. Daher ist P ein Vielfaches von (z−1)(z^(N/2)+1). Insbesondere hat jede ganzzahlige zulässige Änderung die Form q_(j+N/2)=q_j mit Σ_(j<N/2) q_j=0; umgekehrt genügt dies.

Durch zyklische Verschiebung kann eine zusammenhängende Stütze am Index 0 beginnen. Ihr Grad beträgt dann höchstens Streckenlänge −1. Die kleinste mögliche Strecke hat N/2+2 Plätze, erreicht durch (1−z)(1+z^(N/2)). Nur vier Plätze sind dort aktiv: 0,1,N/2,N/2+1, mit Änderungen +1,−1,+1,−1. Für N=32 sind das 0,1,16,17 und eine Strecke von 18 Plätzen. Ein lokaler Vier-Nachbar-Schritt ist auf diesem Raster ausgeschlossen. Als Rasterkontrolle liefert N=6 mit h=π/3 exakt g=2; der Stencil (1,−2,2,−1) verschwindet bei 1 und ζ und ist ganzzahlig auf vier Nachbarplätzen.

Die reellwertige Vierpunktregel bleibt im kontinuierlichen Modell gültig. Ein ganzzahliger mikroskopischer Schritt auf einem dyadischen Winkelraster müsste im gegebenen Modell antipodale Stellen gemeinsam ändern. Der Befund hängt an gleicher Einheit, exakten Momenten und dem Raster. Er begründet keine Quantisierung des nativen QAM- oder OP5-Überschusses. OP5 und H96 bleiben offen.
