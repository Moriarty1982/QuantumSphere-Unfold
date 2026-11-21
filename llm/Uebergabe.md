# Übergabe: Stand der letzten Sitzung

## 21.11.2026 (Codex)

- **GitHub:** [PR #215](https://github.com/Moriarty1982/QuantumSphere-Unfold/pull/215) (SystemVerilog) ist als `89b2dc93e730deb12784a96f57e2b874ea6936e1` auf `main` gemergt. [PR #216](https://github.com/Moriarty1982/QuantumSphere-Unfold/pull/216) (MCP) ist als `e503bb7a497c520a6ec8fcb64cb946457b367998` gemergt. Beide PR-Zweige wurden lokal und auf GitHub gelöscht.
- **Prüfung:** Lean, TeX und QAM unter Linux und Windows bestanden auf beiden geprüften PR-Köpfen. Der Linux-Lauf zu #216 prüfte den neuen MCP-Aufruf über stdio. Die Wiki-Abgleiche waren erfolgreich. [HDL-Wiki-Lauf](https://github.com/Moriarty1982/QuantumSphere-Unfold/actions/runs/44883144993) · [MCP-Wiki-Lauf](https://github.com/Moriarty1982/QuantumSphere-Unfold/actions/runs/44892988023)
- **HDL:** Die direkte und die zyklische SystemVerilog-Steuerung stimmen in 209 begrenzten Fällen mit MMA überein. `7 + 1` braucht vier beziehungsweise 24 Takte. Yosys 0.9 zählt vor dem FPGA-Mapping 564 beziehungsweise 613 generische Zellen. Der Bericht enthält die Randfehlerprobe und die Vorlage für 19K–19L. [Laufbericht](../qam/examples/zuse_machine/hdl/verification.md) · [Textbaustein](../qam/examples/zuse_machine/hdl/README.md#verwendung-im-companion)
- **MCP:** `run_qam_hdl_check` ist am vorhandenen lokalen Server `qsc-qam-batch` registriert. Der Aufruf liefert nach lokalem Test über Windows und WSL die 209 Fälle und mit `synthesis=true` auch die generischen Yosys-Zellzahlen. Ein frischer Codex-Chat lädt das Werkzeug. [MCP-Anleitung](../mcp/README.md#hdl-and-mma-comparison-in-codex)
- **OP5 als nächster Forschungsauftrag:** Die Annahme gleicher freier Wellenzahl und Impedanz aufheben. Für einen getrennten H-Marker Vorwärts- und Rückstreuung bei unterschiedlichen A/J-Wellenzahlen berechnen und die Auswirkung auf die Rang-eins-Referenz prüfen. Die geometrische Anschlussschranke separat mitführen. Stand der elf Erkundungen in [PR #212](https://github.com/Moriarty1982/QuantumSphere-Unfold/pull/212) und `notes/research/op5_bifocal_response_2026_11_18/`.
- **Buchführung:** Keine neue H-, k-, Runden- oder CT-Nummer. Kein Dokumentbuild.

## Davor am 21.11.2026 (Codex)

- [PR #214](https://github.com/Moriarty1982/QuantumSphere-Unfold/pull/214) brachte `RUN_TAPE` mit QAM-Operator und Startzustand, MMA-Guards und Replay. Das Beispiel `7 + 1` hielt nach vier Schritten mit `[0,0,0,1]`. Wolfram reproduzierte die Spur und Qiskit den Endzustand auf vier vorab bereitgestellten Zellen.
- Der danach gespeicherte lokale MMA-Beleg `56a5aac83eee663a1b52627f1b05f336541504ff608eaa257c51e84c7ac62f26b79ccb4ae838a1a71181967f8a3c2ad1dc5eb6b86b8eaf367cecec4571a94f47` war im selben Checkout hashgleich replaybar.

## Inhaltlicher Stand

Die spinorielle Bandrealisierung, die HC-Rückkehr und die unbeschränkte Erweiterbarkeit mit stabiler Dekodierung bleiben Voraussetzungen des Companion. Freie J-Ausbreitung, gemessene Vorwärtsantwort, reale Anschlussreferenz, native Higgs–OP5-Kopplung und H96 bleiben offen. Öffentliche Baseline v5.2.0, DOI 10.5281/zenodo.24294648.
