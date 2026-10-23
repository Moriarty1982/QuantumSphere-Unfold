# Ergebnis H28: Die Wahl aus r42 ist unter den Annahmen bis auf den Frame erzwungen

Vorab-Notiz: `Vorab_Notiz_H28_Warum_diese_Wahl.md`, Commit 9b8b360 (2026-10-23 20:27 MESZ), vor der Rechnung. Vorab von Hand gerechnet und
offengelegt: die Sektor-Zuordnung von iL_{e₇} und iR_{e₇}, der Fall J = iR_{e₇} und Tr Q = 4. Skript `k84_test_h28.py`, Ausgabe `k84_out.txt`.

## Ergebnisse

| Hypothese | Ergebnis | Befund |
|---|---|---|
| H28a Klassifikation | **bestätigt** | Der Kommutant von Farbe und Q auf ℂ⊗𝕆 ist 4-dimensional (die Sektor-Projektoren). Genau vier Projektoren haben als Bild ein Singulett und ein Triplett: J = iL_{e₇} → {0, 2/3}, −iL_{e₇} → {1/3, 1}, iR_{e₇} → {0, 1/3}, −iR_{e₇} → {2/3, 1} |
| H28b Versatz | **bestätigt** | Für alle vier gilt Tr Y = 0 genau bei s = −½ |
| H28c Auswahl | **bestätigt** | Bei s = −½ sind alle Anomalien nur für J = ±iL_{e₇} null. J = iR_{e₇}: Tr Y³ = 3/2, SU(2)²U(1) = −2; J = −iR_{e₇}: −3/2, 2 |
| H28d Frame | **bestätigt** | T (iL_{e₇}) T⁻¹ = −iL_{e₇}: die beiden zulässigen Wahlen sind Frame-Bilder |

Normierung: Die SU(2)²U(1)-Spur summiert über beide Zustände jedes Dubletts. Die Handrechnung in der Notiz (−1) zählte jedes Dublett einmal.

## Einordnung

1. **„Warum diese Wahl“ ist teilweise beantwortet: durch Konsistenz.** Unter den Annahmen ist die Wahl bis auf den Frame erzwungen:
   - Die Farbverträglichkeit und die Ladungserhaltung lassen vier Chiralitätsprojektoren zu.
   - Die gravitative Anomalie legt den Hyperladungs-Versatz s = −½ fest.
   - Die übrigen Anomalien wählen die **Linksmultiplikation** mit e₇ aus.
   - Übrig bleiben genau das Standardmodell und sein Frame-Spiegelbild.

   Bemerkenswert ist, dass die Auswahl wieder links gegen rechts trifft. Die Seitenstruktur, die den ganzen Abend über aufgetaucht ist,
   entscheidet auch hier.
2. **Was weiter Annahme bleibt:** dass die schwache SU(2) rechts auf ℍ sitzt, dass Q_em = T₃ + Q + s gilt und dass der Projektor auf ℂ⊗𝕆
   wirkt. Diese Annahmen sind nicht hergeleitet. Gezeigt ist: Sind sie einmal gemacht, gibt es keinen weiteren Spielraum.
3. **Keine Vorhersage:** Dass das Standardmodell anomaliefrei ist, ist bekannt. Neu ist nur, dass in dieser Struktur die Anomaliefreiheit
   allein zwischen links und rechts entscheidet.
