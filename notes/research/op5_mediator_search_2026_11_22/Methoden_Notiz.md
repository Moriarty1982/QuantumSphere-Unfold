# Methoden-Notiz: Gibt es im Bestand den gerichteten Vermittler des OP5-Falls? (Erkundung, vor der Rechnung festgelegt)

22. November 2026. **Erkundung, nicht blind:** Für die meisten Kandidaten steht die Einordnung analytisch fest. Keine H-Nummer. Auftrag des
Autors: „Vermittler-Suche starten“, nach Runde v4.10.0-r33 (der gerichtete Kontrast braucht einen unterluminalen, linear an den Higgsradius
gekoppelten massiven Vermittler, den W2 nicht enthält).

## Anforderungen (aus dem OP5-Vergleichsmodell, r32.0, r33.3)
- **V1 massiv:** positives Massenquadrat.
- **V2 unterluminal:** Ausbreitungsgeschwindigkeit kleiner als eins (im Modell gesetzt r_m = 1/2).
- **V3 linear an den Higgsradius oder an 𝒥_h gekoppelt** (Kopplung g_m im Modell).
- **V4 gerichtet:** eine ausgezeichnete Achse (Quellform N_m mit P = diag(1, 1, 0)).
- **V5 im Bestand mit Feldgleichung oder Wirkung.**

## Kandidaten (vor der Auswertung festgelegt, vollständig)
| | Kandidat | Quelle |
|---|---|---|
| K1 | Paar-Konnektor Materie–Tachyonbild, gegenläufig (q = p_M + p_T) | `../v4_10_0_w1/Erkundung_Konnektor_Kinematik.md` (k185) |
| K2 | Übergangs-Konnektor, gegenläufig (q = p_M − p_T) | ebenda; W2 liest ihn als Herkunft von −μ² |
| K3 | Konnektor mitlaufend | ebenda |
| K4 | massive Vektoren von W2 (Z, W) | r33.2 |
| K5 | abelsches Eichfeld der Dixon-Ablage (W1) | `../v4_10_0_w1/Wirkung_W1_Dixon_U1.md` |
| K6 | Graviton (Einstein-Kanal) | r33.2 |
| K7 | Kondensat aus Tachyon-Moden (I4) | `../v4_10_0_w1/Zurueckgestellte_Ideen.md` |
| K8 | optische Mode des zweikomponentigen Materials der OP5-Präparation | r32.2 |

## Rechnung (Wolfram, exakt)
Skript `mediator_search.wl`, Ausgabe `run/mediator_search.txt`.
1. K1–K3: Massenquadrat und Geschwindigkeit q¹/q⁰ der Konnektor-Impulse bei gemeinsamer Rapidität η, Wert bei η_sym.
2. K8: Dispersion der beiden Zweige zweier überlagerter Kontinua mit Paarfeder (eindimensional, longitudinal): Lücke und
   Geschwindigkeit des optischen Zweigs; Bedingung, unter der die Higgsquelle 𝒥_h an die optische Mode koppelt.
3. K4–K7: Einordnung nach Quellenlage (V3 aus r33.2; K7 ohne Feldgleichung).

## Einordnung
Je Kandidat und Anforderung: erfüllt, nicht erfüllt, offen. Ein Kandidat **trägt**, wenn V1–V5 erfüllt sind. Erfüllt ein Kandidat V1–V5 nur
als Eigenschaft des Materials, nicht des Vakuums, wird das ausdrücklich benannt: Dann wäre der gerichtete Kontrast eine Eigenschaft der
Präparation, kein Signal eines neuen Feldes. OP5 bleibt in jedem Fall offen.
