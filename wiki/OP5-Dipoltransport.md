# OP5: Dipoltransport und lokale Umlagerung

Arbeitsstand zu PR #190. Die Größen beziehen sich auf das geometrische Randmodell, nicht auf eine bereits hergeleitete kosmologische Ladung.

- Nachbardiffusion erhält den Mittelwert, lässt den Dipol aber abklingen. Ein eigens gewählter Generator mit geschützter erster Winkelharmonischer kann den Dipol erhalten.
- Eine reellwertige Umlagerung auf vier benachbarten Stellen kann Gesamtmenge und beide Dipolmomente exakt erhalten. Die getestete Blockprojektion dämpft höhere Winkelmoden langsam.
- Für ganzzahlige Änderungen in derselben Einheit auf einem 32er-Ring erzwingt exakte Dipolerhaltung gleiche Änderungen an antipodalen Punkten. Die kürzeste zusammenhängende Strecke für einen nichttrivialen Schritt umfasst 18 Plätze. Ein 6er-Ring erlaubt dagegen vier benachbarte Plätze. Damit ist die Einschränkung rasterabhängig.

Die physikalische Zuordnung des Randdipols, das native Übergangsgesetz und H96 bleiben offen.

[Herleitung zur Ganzzahligkeit](../notes/research/op5_bifocal_response_2026_11_18/Ganzzahl.md).
