# Ergebnis H80 und H81: Die zweite Lesart auf FRW

Vorab-Notiz `Vorab_Notiz_H80_H81_zweite_Lesart_FRW.md`, Commit `a5799ef` (nicht blind). Skript `k196_zweite_lesart_frw.py`, Ausgabe `k196_out.json`.

## H80 (δ = 0, Spiegelung um den Urknall)
- **H80a bestätigt:** Für Strahlung und Materie und für beide Fortsetzungen a(−τ) = ±a(τ) ist die Modengleichung exakt (a − b)-mal die des Materie-Skalars mit m² ↦ γ·m² (γ = 1,8645), sympy exakt.
- **Folge (wie vorab):** δ = 0 bringt keine neue Dynamik. Ein Bezug zum CPT-Bild (Boyle–Finn–Turok) kann nur über Randbedingungen bei τ = 0 entstehen, die die Wirkung nicht festlegt.

## H81 (δ ≠ 0, Versatz; δ = 1)
- **H81a bestätigt:** Die Kinetik verschwindet bei τ* = 0,354572 (Strahlung) bzw. 0,425680 (Materie), übereinstimmend mit β_sym/(1 + β_sym) und √β_sym/(1 + √β_sym) auf 15 Stellen. Vorher K < 0, danach K > 0.
- **H81b bestätigt:** τ* ist regulär singulär. Eine allgemeine Lösung (χ = 1, χ′ = 0,5 bei τ = 0,05; k = m = 1) wächst bei Annäherung linear in ln|τ − τ*|: Steigung −0,120, R² = 1 − 4·10⁻¹⁵ auf den letzten drei Dekaden. Die per Schießverfahren gewählte Lösung mit K·χ′ → 0 bleibt beschränkt (Steigung 9·10⁻¹⁰, max|χ|/|χ(Start)| = 1,0007). Die Wahl k = m = 1 stand nicht in der Vorab-Notiz und ist hier offengelegt.
- **H81c widerlegt (quantitativ):** P/K ist vor τ* negativ (bei τ*/2: −0,81), das Vorzeichen ist also tachyonisch. Das Wachstum der Mode k = 0, m = 3 im Intervall (0,05; 0,9·τ*) ist aber nur der Faktor 1,57, nicht über 10. Das Fenster ist für m·δ = 3 zu kurz. Nachträglich (nicht geprüft): Das Wachstum hängt an m·δ und wird für größere Massen bzw. größeren Versatz stark.

## Folge
- **δ = 0** ist die ruhige Variante: Das Bild ist das Universum vor dem Urknall, die Theorie ändert sich nur um die Umnormierung, Vorhersagen müssten aus der Wahl des Zustands bei τ = 0 kommen (wie bei Boyle–Finn–Turok).
- **δ ≠ 0** hat eine ausgezeichnete frühe Epoche τ*. Dort wechselt die Kinetik das Vorzeichen, allgemeine Lösungen divergieren logarithmisch, und nur eine Mode je k kommt regulär durch: Der Durchgang **wählt eine Mode aus**. Davor ist der Skalar tachyonisch; wie stark, hängt an m·δ.
- Die Lesart des Autors, beide Zustände getrennt zu betrachten, ist damit gestützt: δ = 0 und δ ≠ 0 sind physikalisch verschieden, und δ ≠ 0 enthält δ = 0 nicht als ruhigen Grenzfall, solange τ* > 0 ist (τ* → 0 nur für δ → 0).
- Konforme Felder (masselose Fermionen, Eichfelder) sehen in beiden Varianten nichts. Λ wird in keiner Variante aufgehoben. OP5 bleibt offen.
