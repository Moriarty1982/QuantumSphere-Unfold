# Vorab-Notiz H113: Farbauslese des Generationsrasters

22. November 2026. Nicht blind. Prüft den Vorschlag des Autors mit den wörtlichen Spalten e4,e5,e6. Der Farbtyp ist vor dem Lauf aus der vorhandenen Einbettung bekannt. Neu gegenüber der direkten Kommutantenprüfung ist der Test beider Auslesekanäle im konkreten Raster und die Kontrolle am konjugierten Farbträger.

## Vorwissen geprüft

- [OP3-Einbettung](../notes/research/op3_generation_embedding_gate_2026_11_12.md) ordnet e4,e5,e6 mit ihren I7-Partnern einer fundamentalen Farbdarstellung zu. Die farberhaltende Closure ändert ihren Farbtyp nicht.
- [Dixon-Kopien r25](../notes/research/op3_dixon_copies_2026_11_16/README.md) zählt drei Generationsrichtungen und eine Kopien-Singulettlinie im Kopienindex. Diese Rollen sind von der Farbdarstellung zu unterscheiden.
- [Gesamtbild](../wiki/Gesamtbild.md), T5 und T8. Geprüft wird die Einbettung der Zustände, ohne Massenhierarchie oder OP5-Dynamik vorauszusetzen. Die Vorab-Notizen zur Massenmaske und das OP5-Vergleichsmodell liefern keinen zusätzlichen dualen Farbfaktor für dieses Raster.

## Ansatz und Kriterien

Im Vergleich ist G = C^3 farbtrivial, mit Basis g_i. Unter dem in OP3 verwendeten SU(3)_c ist A = A_0 ⊕ A_c die innere komplexe Oktoniondarstellung mit A_0 = span_C(1) unter I7 (reell span_R(1,e7)) und A_c = span_C(e4,e5,e6). Ein farbtrivialer Zusatzfaktor darf die Multiplizität erhöhen. Auslese bedeutet eine lineare farbäquivariante Abbildung in einen farbtrivialen Zustandsraum.

- **H113:** Im literal belegten Raum G ⊗ A können eine diagonale Auslese mit den drei Eingängen g_i ⊗ e_(i+3) und eine davon unabhängige Restspaltenauslese mit den drei Eingängen g_i ⊗ 1 jeweils Rang drei erreichen. Entscheidung: Das Diagonalbild und die Restspalte werden unter dem nichttrivialen SU(3)-Zentrum geprüft. Rang null für mindestens einen der beiden Kanäle widerlegt H113.
- **Kontrollen:** Die Restspalte muss unter demselben Zentrum einzeln invariant sein. Ein zyklischer SU(3)-Farbwechsel verschiebt das Diagonalfeld aus der Diagonale. Die Konjugationswirkung auf 3̄ ⊗ 3 erlaubt die Spur; die drei Diagonal-Matrixeinheiten sollen dabei eine eindimensionale Auslese ergeben. Mit einem zusätzlichen unabhängigen Generationsindex soll dieselbe Spur je Generation getrennt anwendbar sein (Rang drei). Die Spurprobe kontrolliert nur die Farbe, ohne elektroschwache Zuordnung.

Exakte symbolische Wolfram-Prüfung. Ein reproduzierbarer Gegenbeweis über ein Element der Farbgruppe genügt für den negativen Teil.
