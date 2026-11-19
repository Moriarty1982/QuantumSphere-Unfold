# Dritter Sondenkanal und stationäre Phasenbindung

Analytische Erkundung gemäß [Vorab-Notiz](OP2_Lock_Vorab.md), Commit 8a0728bb85c86ffb6806525815dc2282aa45043e. Das Modell ist kanonisch, lokal und homogen; das Ziel der Bindung und die Beiträge zur Energiedichte werden gesetzt.

Für das kanonische Paar (φ,N) gilt Ṅ=−∂H/∂φ. Soll N für alle Zustände strikt erhalten sein, ist H unabhängig von φ. Ein direktes Potential für φ kann die Phase in diesem Modell dann nicht binden. Eine freie Frequenzgleichheit wäre möglich, wählt aber keine Zielphase aus.

Mit einem dritten Kanal (θ,J) ist die gemeinsame Ladung Q=N+J erhalten, wenn H nur von der relativen Phase abhängt. Prüfe H=V0+mQ+J²/(2I)+K[1−cos ψ], ψ=φ−θ−αQ, I,K>0. Dann gilt exakt:
- Ṅ=−K sin ψ, Ĵ=+K sin ψ, Q̇=0;
- ψ̇=−J/I;
- Bei J=0 und ψ=0 modulo 2π besteht stationäre relative Bindung, N=Q. Linearisierung: ψ̈=−(K/I)ψ. Das Gleichgewicht ist stabil im reduzierten System bei festem Q, ohne Attraktor: allgemeine Nachbarzustände oszillieren. Beim Einregeln wäre eine geeignete Kopplung an weitere Freiheitsgrade oder an ein dissipatives Medium nötig. Vorzugsweise wäre deren Ladungstransfer eigens zu bilanzieren.

Am Minimum ist H_min(Q)=V0+mQ. Interpretiert man Q als Eigendichte einer im effektiven homogenen Fluid erhaltenen Gesamtladung, liefert die lineare Zusatzenergie über p=Q dρ/dQ−ρ keinen Zusatzdruck. Das ist ein Modellresultat, keine Herleitung des kovarianten Tensors aus OP2. Außerhalb der stationären Lösung tauscht der dritte Kanal mit N Ladung aus und kann Zusatzenergie tragen. Die Annahmen einer Q-unabhängigen Untergrundenergie, der linearen Ladungsenergie und des durch αQ verschobenen Phasenminimums wurden nicht aus dem Zellgesetz abgeleitet.

Der orthogonale Sondenkanal des Companion motiviert eine dritte Variable, instanziiert aber diese kanonische Paarung, die gemeinsame Erhaltungsgröße und die Kopplung an den Geometriemonitor noch nicht. Der P-Frame ist hier nicht mit dem dritten Sondenkanal identifiziert. Die Wahl der Gesamtladung liefert auch nicht ihren heutigen Wert. OP2, OP5 und H96 bleiben offen.
