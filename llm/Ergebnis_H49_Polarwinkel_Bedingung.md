# Ergebnis H49: Versteckte Bedingung der Polarwinkel-Richtung abseits des Äquators

Vorab-Notiz: `Vorab_Notiz_H49_Polarwinkel_Bedingung.md`, lokaler Commit e2d3394 (2. November 2026, 20:22 UTC), vor der
Rechnung. Rechnung: `k133_test_h49.py`, Kontrollen `k134_kontrolle.py`.

## Ergebnis: widerlegt

| Art | Punkt | Rang (von 128) | Lücke | κ |
|---|---|---|---|---|
| Kontrolle | Keim (1; 0,6; 0; 0) | 113 | 1,7e-1 / 1,7e-9 | 2,0e-10 |
| Kontrolle | (1,02; 0,6; 0,03; 0) | 113 | 1,7e-1 / 2,1e-9 | 2,9e-10 |
| Kontrolle | Keimpunkt, andere Lösung 1 | 113 | 1,7e-1 / 2,1e-9 | 1,8e-10 |
| Kontrolle | Keimpunkt, andere Lösung 2 | 113 | 1,7e-1 / 2,2e-9 | 2,7e-10 |
| Test | z = 0,02 | 113 | 1,7e-1 / 1,8e-9 | 1,3e-10 |
| Test | z = 0,05 | 113 | 1,7e-1 / 2,0e-9 | 1,5e-10 |
| Test | z = 0,1 | 113 | 1,7e-1 / 2,1e-9 | 1,5e-10 |
| Test | z = 0,2 | 113 | 1,8e-1 / 2,0e-9 | 2,4e-10 |
| Test | (1,03; 0,58; 0,05; 0,1) | 113 | 1,7e-1 / 1,8e-9 | 1,7e-10 |

Das Kontrollmaximum liegt bei 2,9e-10. Alle Tests mit |z| ≥ 0,05 liegen darunter, also unter 10 × Kontrolle. Nach dem
Vorab-Kriterium ist H49 widerlegt.

**Empfindlichkeit des Tests (k134, Punkt z = 0,1):**
- ohne den expliziten Hintergrundgradienten: κ = 9,2e-2;
- mit 0,1 % Fehler in einer dg-Zeile: κ = 7,8e-5.

Der Test hätte eine Bedingung also erkannt.

## Lesart

- Der Bruch der ϑ-Freiheit (c·∇G ∝ z/ρ²) erzeugt beim Übergang zu den zweiten Ableitungen keine versteckte Bedingung,
  weder am Äquator noch abseits davon. Die Projektion R₂ → R₁ ist an allen getesteten Punkten surjektiv.
- Die Vermutung „Ω ist die Verträglichkeitsbedingung der ϑ-Richtung und erscheint abseits des Äquators früher“ ist
  in dieser Form nicht gestützt. Ob Ω mit der ϑ-Richtung zusammenhängt, bleibt offen. Prüfbar wäre das über den
  Übergang R₃ → R₂ abseits des Äquators.
- Die Symbolbefunde (freie ϑ-Richtung, Kegel, Ebenen; siehe `Erkundung_OP5_Symbolstruktur_Grad7.md`) sind davon
  unberührt.
