# Deutscher Preprint, Fassung 0.5.0: Release-Paket

**Status (28.11.2026): veröffentlicht**, [Record 24632440](https://zenodo.org/records/24632440) (Upload und Veröffentlichung Lauf 46169542735, Workflow „Zenodo Release“, Freigabe des Autors; 66 Seiten). Vorschau nach dem Veröffentlichen geprüft (Lauf 46169634007): `Quantum_Sphaera_Preprint_0.5.0.pdf`, korrekt. Der folgende Text hält die Vorbereitung fest.

**Reserviert am 28.11.2026 (Freigabe des Autors):** Zenodo-Entwurf 24632440, Version-DOI 10.5281/zenodo.24632440 (Workflow „Zenodo Release“, Lauf 46166762716, neue Fassung von 24563916). Ab jetzt `deposition_id=24632440`, nie `new_version_of`. Nichts hochgeladen. `\versiondoi` ist gesetzt. Der Preprint verweist auf Companion v5.6.0 (10.5281/zenodo.24632437; Entscheidung des Autors vom 28.11.2026); v5.6.0 erscheint vorher oder gleichzeitig.

**Status (28.11.2026): vorbereitet, nicht reserviert, nicht hochgeladen, nicht veröffentlicht.** Jeder Zenodo-Schritt (Reservierung,
Upload, Veröffentlichung) und die Entscheidung, dass diese Fassung erscheint, brauchen die ausdrückliche Freigabe des Autors (`AGENTS.md`).
Concept-DOI 10.5281/zenodo.24405552; Vorgänger 0.4.0 vom 26.11.2026, [Record 24563916](https://zenodo.org/records/24563916),
DOI 10.5281/zenodo.24563916. Ältere Fassungen bleiben sichtbar.

- Quelle: `paper/preprint-de/` (Fassung 0.5.0, Entwurf; `\versiondoi` leer bis zur Reservierung). Seitenzahl nach dem ersten Build eintragen
  (in der Vorbereitung stand kein pdfLaTeX zur Verfügung).
- Metadaten: `release/zenodo/metadata_preprint_de_0_5_0.json` (isVersionOf 24405552, isNewVersionOf 0.4.0 24563916, Bezug Companion v5.5.0
  und Repository). Ob zusätzlich v5.6.0 als „references“ eingetragen wird, entscheidet der Autor; dann muss v5.6.0 vor oder mit dem Preprint erscheinen.
- Payload: `Quantum_Sphaera_Preprint_0.5.0.pdf` (noch zu bauen, nach der Reservierung mit Version-DOI auf der Titelseite) und `SHA256SUMS.txt`.
- Beschreibung, Kurzfassung und Prüfliste: `paper/preprint-de/ZENODO.md`.

## Änderungen gegenüber 0.4.0

Quelle jeder Änderung ist eine Companion-Schicht (`sources/research/parts/v4100-post-release-layers.tex`, r69 bis r75); der Artikel gibt sie
verkürzt wieder. Kein offenes Problem ist geschlossen, kein Guard aufgehoben, keine Vorhersage entschieden.

- Abschnitt 1.3: Frames auf der Kugel der Feldzustände (r70, Korrektur Gewichte gegen Amplituden, k382) und die neuen Namen (r69).
- Neuer Abschnitt 5.9 „Die Leptonphase: ein Winkel, ein Vorzeichen, eine gemessene Zahl“ (r73, r74): Versatz als Winkel φ (H221), Zweigwahl ohne
  Skala, Vorzeichen gesetzt (H222, H223, k436), φ = 0,0395773 bleibt gemessen (H224–H235 widerlegt oder ohne Treffer, k449 Erkundung), H236 klärt
  die Doppelzählung, Bilanz H227.
- Neuer Abschnitt 5.10 „Vorhersagen dieser Fassung (Stand 28. November 2026)“ (r75) mit Einstufung hergeleitet / gesetzt / gemessene Eingabe /
  nachträglich und der Versionsregel des Autors.
- Bisheriger Abschnitt 5.9 („offen“) wird 5.11; in der OP2-Zeile ist ein beiläufiger Verweis durch „frühere Arbeit“ ersetzt.

## Nächste Schritte mit Freigabe des Autors

1. Merge der Vorbereitung (Dauerauftrag: bei grüner CI).
2. Reservierung (neue Fassung von 24563916), dann nur noch `deposition_id`.
3. `\versiondoi` setzen, Literaturlinks auf den Merge-Commit pinnen, PDF bauen (0 Overfull, besonders die Tabellen in 5.10), Prüfsumme.
4. Upload, Prüfung des Entwurfs und der Vorschau, Veröffentlichung mit endgültigem Datum, Vorschau erneut prüfen.
