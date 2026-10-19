# Lokales Sphaera-LLM — Datensatz und Anleitung

Stand: Kernkarte v2.0, Companion bis v4.8.0-r07 (2026-10-19).

## Inhalt

| Datei | Zweck |
|---|---|
| `build_dataset.py` | erzeugt `train.jsonl` (82 Paare) und `eval.jsonl` (11 Paare) |
| `train.jsonl`, `eval.jsonl` | Chat-Format (`system`/`user`/`assistant`), Antworten mit Ebenen-Tags [V]/[M]/[S]/[P] |
| `guard_linter.py` | findet verbotene Aussagen in LaTeX, Text oder Modellantworten |
| `eval_ollama.py` | bewertet ein lokales Modell auf `eval.jsonl` |
| `make_modelfile.py`, `Modelfile` | erzeugt das Ollama-Modell „sphaera“ mit der Kernkarte als Kontext (Stufe 1) |

Themen im Datensatz: Definitionen (18), Lesart B (15), Rechnungen/Zahlen (14), Status (14),
Guard-Fallen (17), Riemann-Arbeit (9), Offenes (6). Alle Antworten bestehen den Guard-Linter.

## Stufe 1 — ohne Training (empfohlen zuerst)

Die Kernkarte (rund 13.000 Tokens) wird als Systemkontext mitgegeben.

1. Ollama installieren: https://ollama.com
2. Modell holen. Auf der RTX 2060 mit 6 GB: `ollama pull qwen2.5:3b`.
   Mit mehr Speicher oder gemieteter GPU: `qwen2.5:7b`.
3. Im Ordner `llm/training` das Modelfile aus der aktuellen Kernkarte erzeugen und das Modell bauen:

   ```
   python make_modelfile.py qwen2.5:3b
   ollama create sphaera -f Modelfile
   ollama run sphaera
   ```

   `make_modelfile.py` schreibt die Kernkarte als Systemkontext ins Modelfile. Nach jeder neuen
   Kernkarte beide Befehle erneut ausführen.
4. Prüfen: `python eval_ollama.py sphaera`. Ausgegeben werden Tag-Disziplin, Guard-Verstöße und
   Stichwort-Abdeckung.

Hinweis zur 2060: Die volle Kernkarte braucht rund 13.000 Tokens, `num_ctx` steht deshalb auf 16384.
Das belegt beim 3B-Modell einen großen Teil der 6 GB. Wird es zu langsam oder bricht ab, die Kurzfassung
nehmen: `python make_modelfile.py qwen2.5:3b --kurz` (nur Abschnitte 0–6, rund 6.000 Tokens,
`num_ctx` 8192). Die Arbeitsergebnisse K1–K9 fehlen dann im Kontext; das Feintuning (Stufe 2) gleicht
das teilweise aus.

## Stufe 2 — Feintuning (QLoRA)

Nur, wenn Stufe 1 bei den Guard-Fallen oder der Tag-Disziplin versagt.

- Hardware: gemietete RTX 4090 (24 GB), etwa 0,35–0,70 $/Std. Ein Lauf über 82 Paare × 3 Epochen
  dauert Minuten, nicht Stunden.
- Werkzeug: Unsloth oder Hugging Face TRL (`SFTTrainer`) mit QLoRA (4-Bit), LoRA-Rang 16, Lernrate 2e-4,
  2–3 Epochen. Das Chat-Format von `train.jsonl` wird von beiden direkt gelesen.
- Ergebnis als GGUF exportieren und mit einem Modelfile (`FROM ./sphaera-lora.gguf`) in Ollama laden.
- Danach `eval_ollama.py` erneut laufen lassen und mit Stufe 1 vergleichen.

**82 Paare sind wenig.** Sie reichen, um Tag-Disziplin und Guard-Reflexe anzutrainieren. Fachwissen
liefert weiterhin die Kernkarte im Kontext. Am besten kombiniert man beides: feingetuntes Modell plus
Kernkarte.

## Regeln für neue Paare

- Jede Antwort beginnt mit einem Ebenen-Tag und trennt Vermutung, Mathematik und Stand.
- Zahlen nur aus nachgerechneten Skripten (`llm/k*.py`).
- Für jede neue Runde mindestens eine Guard-Falle: eine Frage, die eine verbotene Aussage voraussetzt,
  mit korrigierender Antwort.
- Vor dem Training: `python guard_linter.py train.jsonl --jsonl` muss 0 Treffer melden.

## Wichtig

Ein kleines Modell bleibt eine Hilfe zum Nachschlagen und Formulieren. Mathematische Aussagen werden
weiterhin gerechnet (SymPy/NumPy-Skripte), und jede neue Runde läuft durch `qs.py guards` und den
Guard-Linter.
