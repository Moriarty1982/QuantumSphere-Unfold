# Ergebnis H24: Unter Hilbert-Shift-Zoom überlebt nur der Generationenkreis; gemischte Masken geben verschiedene Lesarten

Vorab-Notiz: `Vorab_Notiz_H24_Ketten_Module_Readouts.md`, Commit 8c89481 (2026-10-23 19:39 MESZ), vor der Rechnung.
Skript `k80_test_h24.py`, Ausgabe `k80_out.txt`. Kriterium unverändert. Elementare Zahlentheorie; der Gehalt liegt in der Modellwahl
(Zoomstufe j = Schritt 2^j, gemischte Maske = Σ oder ∨).

## Ergebnisse

| Hypothese | Ergebnis | Befund |
|---|---|---|
| H24a ungerade Ketten | **bestätigt** | Ungerade Ketten behalten auf jeder Stufe ihre Länge. τ^{2^j} = τ für gerades j, τ⁻¹ = ρτρ für ungerades j: Der Generationenkreis bleibt vollständig, seine Orientierung wechselt mit der Stufe, die Umkehrung ist das ρ-Spiegelbild |
| H24b Zweierketten | **bestätigt** | Ketten der Länge 2^a verschwinden ab Stufe a. Sichtbare Ordnungen in G: Stufe 0 {1, 2, 3, 4, 6, 12}, Stufe 1 {1, 2, 3, 6}, ab Stufe 2 nur {1, 3}; dort liegt jedes g^{2^j} in ⟨τ⟩ |
| H24c gemischte Masken, m = 3 | **bestätigt** | Lesart Σ: 21 von 63 Masken (3 \| k, z. B. Bits {0, 1}) sehen eine Generation, die übrigen drei. Lesart ∨: jede Maske sieht drei |
| H24d allgemeine Länge | **bestätigt** | Σ: ℓ = m/gcd(m, k); ∨: ℓ = m/gcd(m, 2^{min S}); unter ∨ bleibt der ungerade Anteil von m immer erhalten (m ≤ 64, alle Masken) |
| H24e Ebenen | **bestätigt** | Stufe 0 zeigt Frames (2, 4) und Generationen (3) zugleich, ab Stufe 2 nur die Generationen |

## Einordnung (zur Autoridee)

1. **„Wenn man oft genug zoomt, bilden die Generationen einen Kreis“** stimmt im Modell, und zwar als einziges, was übrig bleibt:
   - Von der ganzen Struktur S₃ × D₄ ist ab Zoomstufe 2 nur noch der Triality-Kreis der Länge 3 sichtbar.
   - Frame-Wechsel (Periode 2) und Dualitätsdrehung (Periode 4) verschwinden.
   - Das löst im Modell die Spannung aus H23: Frames und Generationen liegen auf verschiedenen Zoomstufen, grob die Frames, tief die
     Generationen.
2. **Orientierung:** Auf ungeraden Stufen läuft der Kreis rückwärts, und das ist genau das Frame-Spiegelbild ρ. Zoom und Frame sind
   so verbunden: Jede zweite Stufe liest die Generationen im gespiegelten Frame.
3. **Verschiedene Moduln:** Was beim Zoomen überlebt, ist der **ungerade Anteil** der Kettenlänge.
   - Eine Kette der Länge 6 (3 Generationen × 2 Frames) oder 12 (× 4 Dualitätsphasen) zeigt tief gezoomt 3.
   - Eine Kette der Länge 2^a verschwindet ganz.
   - In G entsteht keine Generationenkette der Länge 4 oder mehr. Eine andere ungerade Länge, etwa 5 oder 7, bräuchte eine andere
     Gruppe.
4. **Gemischte Readouts geben verschiedene Lesarten**, je nachdem, wie die Maske aggregiert:
   - Liest sie als ein Schritt (Σ), sieht ein Drittel der Masken nur eine Generation, die übrigen drei.
   - Liest sie die Komponenten gemeinsam (∨), sieht jede Maske drei.
   - Welche Aggregation μ gemeint ist, legt der Text (`def:guarded-mixed-qam-readout`) nicht fest. Hier liegt eine Autorentscheidung.
5. **Grenze:** Das ist Arithmetik zyklischer Gruppen. Es zeigt, was das Modell aus Zoom und Masken macht, nicht, dass die Natur so
   ausliest. Die Wahl „Zoom = Schritt 2^j“ folgt der Bit-Registrierung β_j = 2^j, ist aber eine Lesart.
