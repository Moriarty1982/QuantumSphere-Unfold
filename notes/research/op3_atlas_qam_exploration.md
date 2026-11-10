# OP3: Paarstruktur des historischen Hüllenatlas

Erkundung, 10. November 2026. Die Kodierung verwendet die Zustände 0 bis 3 mit Blatt als niedrigem Bit und Parität als hohem Bit. Drei feste Paare mit gemeinsamem Anker 4 fixieren die Hilfsmarken 4 bis 7. Die beiden Quellpaare sind {0,1} und {0,2}. Jedes ihrer Zielpaare durchläuft unabhängig alle sechs Zweiermengen in {0,1,2,3}.

Der verifizierte MMA-Bericht hat den Hash `9e9f4963eb091dbd3ea6369381ddc97479349f3cd45ed2e67a14f3e990a80a537e0aab21eaed1d739ded57fe3e68ec826e2a8ae8ee45c4d0d4af6b59fa190a87`.

Von 36 Zielpaarkombinationen führen 12 zu keinem Treffer und 24 zu genau einer Permutation. Von diesen 24 erhalten vier beide Paararten, vier nur die Blattpaarart, vier nur die Paritätspaarart und zwölf keine der beiden. Jede einzelne Strukturprüfung akzeptiert damit acht Permutationen. Erst beide zusammen akzeptieren genau die vier Atlaswechsel.

Auf den drei Paarzerlegungen wirkt jede der sechs möglichen Umordnungen genau viermal. Das folgt auch analytisch. Die Paartypen entsprechen der Differenz der beiden Zustände unter bitweisem XOR. Jede Permutation der vier Zustände kann als affine Abbildung auf zwei Bits geschrieben werden. Der lineare Anteil permutiert die drei von null verschiedenen Differenzen. Der freie Translationsanteil hat vier Möglichkeiten. Er ergibt genau die vier Atlaswechsel, wenn der lineare Anteil die Identität ist.

Unter den 576 geordneten Zweischrittfolgen der 24 rekonstruierten Permutationen haben 96 eine Zusammensetzung im Atlas. Nur 16 davon bestehen aus zwei Atlaswechseln. Bei den anderen 80 liegt jeder Einzelschritt außerhalb des Atlas. Die linearen Anteile sind dort nichttrivial und invers zueinander. Daher verschwindet die Umordnung der Paararten in der Zusammensetzung. Beispiel: Erst (2 3), dann (0 1). Beide sind einzeln außerhalb des Atlas, zusammen bilden sie den Blattwechsel (0 1)(2 3). 480 Folgen haben eine Zusammensetzung außerhalb des Atlas.

Für eine Folge der Länge n ≥ 1 gibt es genau 4·24^(n−1) Folgen mit Endpermutation im Atlas. Nach freier Wahl der ersten n−1 Schritte gibt es für jede der vier gewünschten Endpermutationen genau einen letzten Schritt. Nur 4^n Folgen bleiben an jedem Einzelschritt im Atlas. Unter den Folgen mit passendem Ende beträgt ihr Anteil daher 6^(1−n). Die exakte Kompositionszählung der MMA-Kandidaten bestätigt die Formel bis n = 6.

Der Atlas ist der Kern der Wirkung auf den drei Paarzerlegungen. Daher genügt es, die induzierte Umordnung der Paarzerlegungen nach jedem Präfix festzuhalten. Sind alle Präfixe in diesem Quotienten die Identität, sind es auch alle relativen Einzelschritte. Ein Endprotokoll allein kann Rückkehr zur Identität mit durchgehender Erhaltung verwechseln.

Bei k geprüften Zwischenständen einschließlich des Endes bleiben 4^k·24^(n−k) Folgen übrig. Für jeden Abschnitt darf man alle Schritte bis auf den letzten frei wählen. Der letzte muss zu einer der vier Atlaspermutationen führen. Der Anteil vollständig atlaserhaltender Folgen unter den akzeptierten Folgen ist 6^(k−n). Die Auszählung für n = 3 ergibt 2304 akzeptierte Folgen bei reiner Endkontrolle, 384 bei genau einer zusätzlichen Zwischenkontrolle und 64 bei Prüfung aller drei Präfixe.

Ein weiterer Paarstapel prüft die Abhängigkeit zwischen Präfix und Ende. Der ungesicherte Endvergleich erkennt den Blattwechsel mit einem Treffer. Mit `depends_on` und `requires_match` wird dieselbe Anfrage nach dem strukturell widersprüchlichen Präfix blockiert und nach einem gültigen Präfix ausgeführt. Der gespeicherte Bericht hat den Hash `a003296a59f86c389eac23f6186a96b2c973e44aefbf5ba4f9fc89d18ee0c18468b4d732dcf72a7d061c0c96312b007825a501cb166b3577240fff79134c3fbb`.

Trefferabhängigkeiten allein koppeln die Endpermutation nicht an die konkreten Treffer der beiden Schritte. Im Kontrollstapel sind Blattwechsel und Paritätswechsel einzeln eindeutig. Der ungebundene Endvergleich akzeptiert trotzdem den Blattwechsel als Ende. Werden die vier Zustandsbilder der extern berechneten Zusammensetzung zusätzlich als Paarbedingungen vorgegeben, hat das falsche Ende keinen Treffer und das richtige Ende genau einen. Berichtshash `486be80346493cba81bd4663b1416a191b4a33df5acc2dd0849acac883a4df7809a97faf0086bf9933f209f30baf2b23c70d13d2d944d47ac88b3c0ed8a7f8bf`.

Der [gespeicherte Zusammensetzungsstapel](op3_atlas_composition_batch.json) umfasst alle 16 geordneten Paare. Für jedes Paar findet der korrekte Endwechsel genau einen Treffer und die durch einen zusätzlichen Blattwechsel verfälschte Kontrolle keinen. Die vier Einzelwechsel finden ebenfalls je einen Treffer. Verifizierter Berichtshash `332d9a9067c60458b7d6268c0b6bf2c7143af9cdc43fdcc8ddc12852c117c66039c3de9416b9169feaa9a1a1e8e1611d9c0b9bfa3458a46d8d19191f3cf048b3`.

Das ist eine Auswertung der endlichen Kodierung des historischen Hüllenatlas. Ein nativer Hüllenübergang und die geometrische Persistenzbedingung werden dadurch nicht zertifiziert.
