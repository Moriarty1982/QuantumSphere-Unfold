# Übergabe: Stand der letzten Sitzung

## 21.11.2026 (Codex)

- **GitHub:** [PR #214](https://github.com/Moriarty1982/QuantumSphere-Unfold/pull/214) ist als `368bddc48839817212836ff7e11e6908b295df71` auf `main` gemergt. Der geprüfte Kopf `98d4c586589a081c98ee947c9d1935d7702c00fe` ist enthalten. Der Zweig ist lokal und auf GitHub gelöscht. Beim Abgleich gab es keinen offenen PR.
- **Prüfung:** Lean, TeX und QAM unter Linux und Windows bestanden. Der [Wiki-Abgleich](https://github.com/Moriarty1982/QuantumSphere-Unfold/actions/runs/44881263858) war erfolgreich.
- **Rechenmodell:** `RUN_TAPE` führt einen deklarierten QAM-Operator mit QAM-Startzustand unter MMA-Guards aus. Das binäre Beispiel $7+1$ hielt nach vier Schritten mit dem Band `[0,0,0,1]` in der Reihenfolge vom niederwertigsten Bit. Wolfram reproduzierte die Spur und Qiskit den Endzustand bei vier vorab bereitgestellten Zellen. Der lokale [Aufruf](../qam/examples/zuse_machine/README.md#mit-qam-mml-und-mma-rechnen) bleibt der Einstieg.
- **Beleg auf dem lokalen `main`:** `56a5aac83eee663a1b52627f1b05f336541504ff608eaa257c51e84c7ac62f26b79ccb4ae838a1a71181967f8a3c2ad1dc5eb6b86b8eaf367cecec4571a94f47`. Ergebnis und Hash stimmen beim Replay überein. Die Windows-Zeilenenden beim Checkout änderten den Implementierungshash des vorherigen Belegs bei gleichem Ergebnis.
- **Buchführung:** Keine neue H-, k-, Runden- oder CT-Nummer. Kein Dokumentbuild. Die nächste OP5-Rechnung steht im vorigen Arbeitsblock.

## Davor am 21.11.2026 (Codex)

- **GitHub:** [PR #212](https://github.com/Moriarty1982/QuantumSphere-Unfold/pull/212) ist als `82a09e149ef695c9b7d2f6dcb738de125b520b47` auf `main` gemergt. Der geprüfte Kopf `8d422d780e988dd5095518bdaab5f9ff39da822f` ist enthalten. Der PR-Zweig ist lokal und auf GitHub gelöscht. Kein offener PR zum Zeitpunkt des Abgleichs.
- **Prüfung:** Elf Wolfram-Laufmanifeste einschließlich der Artefakthashes validiert. Der Diff ist frei von Whitespace-Fehlern. Die PR-Pfade lösen keine GitHub-PR-Prüfungen aus. Der [Wiki-Lauf](https://github.com/Moriarty1982/QuantumSphere-Unfold/actions/runs/44878591327) war erfolgreich. [OP5 #12](https://github.com/Moriarty1982/QuantumSphere-Unfold/issues/12#issuecomment-7059031894) und [Register #17](https://github.com/Moriarty1982/QuantumSphere-Unfold/issues/17#issuecomment-7059032254) wurden aktualisiert und sind offen.
- **Befund:** Elf Erkundungen unter `notes/research/op5_bifocal_response_2026_11_18/`. Die vorbereitete mechanische Schaltbahn ist im Vergleich bis zur zweiten Ordnung außenkompensiert. Das gewöhnliche Binnenfeld bleibt für die Messung relevant. Ringkalibrierung und markierte Phasenauslese haben bedingte Fehlergrenzen. Das illustrative schwach gekoppelte HCl/H-Beispiel verfehlt die Anschlussanforderung bereits geometrisch. Im passiven Einlinienmarker verlangt ein Pi-Hub bei höchstens einem Prozent Amplitudenverlust rund 313 Halbbreiten Verstimmung.
- **Nächster Schritt:** Die Annahme gleicher freier Wellenzahl und Impedanz aufheben. Für einen getrennten H-Marker Vorwärts- und Rückstreuung bei unterschiedlichen A/J-Wellenzahlen berechnen und die Auswirkung auf die Rang-eins-Referenz prüfen. Die geometrische Anschlussschranke separat mitführen.
- **Buchführung:** Keine neue H-, k-, Runden- oder CT-Nummer. Kein Dokumentbuild.

## Inhaltlicher Stand

Freie J-Ausbreitung, gemessene Vorwärtsantwort, reale Anschlussreferenz, native Higgs–OP5-Kopplung und H96 bleiben offen. Öffentliche Baseline v5.2.0, DOI 10.5281/zenodo.24294648.
