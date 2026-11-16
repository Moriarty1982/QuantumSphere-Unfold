# v4.10.0-r22: Der Kollapszustand im ganzen Hauptkorpus typisiert

16. November 2026. Auftrag des Autors: „Ja, Runde r22“, nach der Erkundung
`../collapse_state_typing_2026_11_16/README.md`. Die Runde steht als Datei `rounds/v4100_r22_round.tex` und ist an
`sources/research/parts/v4100-post-release-layers.tex` angehängt. Lesart, nicht blind, ohne Rechnung und ohne Vorab-Notiz. Keine
H-Nummer, kein CT-Eintrag, kein Guard ausgegeben. Der Hauptkorpus wird nicht umgeschrieben.

| Eintrag | Inhalt | Quelle |
|---|---|---|
| r22.1 | Typisierung der 93 z⁻-Stellen in fünf Gruppen: Nullpunkt des Versatzes (R), invariantes Objekt (Rolle von P), Horizont (Ort von P), kein Punkt, Richtung der Kaskade (offen) | `../collapse_state_typing_2026_11_16/README.md`, `zminus_stellen.txt` |
| r22.2 | Die Koordinate z⁻ läuft von R (0) nach P (∞), wie die Rapidität in r21.8 (sech 2η); Lesart wegen wechselnder Skala | ebenda |
| r22.3 | Der Kollapszustand als Nullzustand ist das Horizont-Ende, nicht der Ursprung; passt zu r15.2 und r29.1(b) | ebenda |
| Berichtigung | zu r21.9, Zeile 3: „never fully reach z⁻ = 0“ ist R (bleibender Versatz), nicht P; keine Spannung mit r24.3 | ebenda |
| r22.4 | Offen: ob die Kaskade „zurück zu z⁻ = 0“ zu R oder zu P führt | ebenda |

## Prüfung
- Guard-Linter (`python tools/qs.py guards sources/research/parts/v4100-post-release-layers.tex --start 3074`):
  0 Kandidaten in den Zeilen 3074–3198.
- Kandidaten-Build (`python .github/scripts/qsc_latex_build.py --source-dir sources/research --output-dir <Pfad>`, MiKTeX):
  1442 Seiten, 0 Fehler, 0 undefinierte Verweise, 0 Overfull; r22 im Inhaltsverzeichnis.
