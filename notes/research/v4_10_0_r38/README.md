# v4.10.0-r38: Feldgleichungen für den gerichteten OP5-Vermittler, erster Ansatz (Stand 22.11.)

22. November 2026. Auftrag des Autors: „wäre eine feldgleichung bzw. ein erster ansatz davon nicht erstmal sinnvoll?“, „ja, anlegen und
rechnen“. Die Runde ist die Quelle für die Ergänzungen in Physik-Paper 6.9, Preprint-Anhang B.1 und Preprint 5.6. Erkundung, nicht blind;
Methoden-Notiz vorab (6bad83cb). Keine neue H-, k- oder CT-Nummer.

| Eintrag | Inhalt |
|---|---|
| Ansatz | Tensor X_ij quer zur Achse und Skalar S, gekoppelt über g X_ij(∂_i∂_j − κδ_ij∂_t²)η und g_s S∂_t²η; η wie in W2 |
| r38.1 | Austausch = −g_m²N_m/d_m exakt für g² = ⅔g_m², κ = ½, g_s² = ⅓g_m² bei d_s = d_m; eindeutig |
| r38.2 | geisterfrei für g_m² < 3; statisch stabil genau für g_m² ≤ 3r_m; Raster bestätigt (8/5 instabil bei r_m = ½) |
| r38.3 | trägt teilweise: κ = ½ ist der Wert des Strings aus r37; Skalar und Entartung gesetzt |

Rechnung: `../op5_mediator_field_equation_2026_11_22/` (Skript, Ausgabe, README).

OP1–OP5, C5, C6/T2 offen.
