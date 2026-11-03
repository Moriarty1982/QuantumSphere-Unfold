# Hochgenaue Faser-Rechnungen auf GitHub Actions (H59)

`k159_hp_faser.py <Keim-Ordner> <q> <out.json>` bestimmt die Faser der q-Jets des erweiterten OP5-Vergleichssystems in arb (70 Stellen):
- fester Jet bis Grad q−1, Gleichungen bis Grad q+1;
- Elimination von c_{q+2} und c_{q+1};
- Gram der abgeleiteten Bedingungen auf dem Kern N_q.

Daten:
- `hp_work2/AB_taylor2.pkl` stammt aus k153b (mpmath, dps 160);
- die Eichreihe kommt aus den Keim-Dateien unter `analysis/op5-field-slices/state-sufficiency-2026-10-30/`.

Workflow `.github/workflows/hp-faser.yml`:
- Start durch einen Push auf `rechnen/**` mit Änderung unter `ci/hp/`;
- die Liste der q steht in `auftrag.txt`;
- ein Job je q, die großen zuerst.

Die Ergebnisse stehen im Job-Log (Zeilen `ERGEBNIS`) und im Artefakt.

Vorab-Notiz: `notes/research/predictions/Vorab_Notiz_H59_versteckte_Bedingungen_7_8_Jets.md`.
