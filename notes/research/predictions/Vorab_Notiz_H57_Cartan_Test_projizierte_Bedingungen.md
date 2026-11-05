# Vorab-Notiz H57: Cartan-Test mit projizierten Bedingungen (nicht blind)

Festgeschrieben vor der Rechnung (3. November 2026). **Nicht blind:** Die Zahlen aus H56 (ungültig) sind bekannt. Der Test
prüft, ob sie bei sauberer Numerik bestehen bleiben. Betrifft nur das OP5-Vergleichsmodell. OP5 bleibt offen.

## Änderung gegenüber H56

σ_k wird vor der Fortsetzung auf die gespeicherte Faser projiziert: σ'_k = P·σ_k, wobei P der Orthogonalprojektor auf
g'_6 ist (Kern von J, θ und Eichung bei p = 6, gespeichertes Symbol). Auf g'_6 wirken σ'_k und σ_k gleich, bis auf die
gemessene Abweichung der Fasern (4,4e-7). Alles andere wie in H56 (`k146_cartan_erweitert.py`).

## Hypothese H57

Mit σ'_k gilt, in allen drei Koordinatensystemen (Seeds 1, 2, 3):

- dim g''_p = 477, 594, 723, 865 für p = 6, 7, 8, 9;
- nicht involutiv bei p = 6 und 7, involutiv bei p = 8;
- dim g''^{(k)}_8 = 723, 130, 12, 0.

## Kriterium

- **Bestätigt:** alle drei Aussagen.
- **Widerlegt:** eine Aussage gilt nicht, bei gültigem Lauf.
- **Ungültig:** ein verwendeter Rang mit Lücke unter 1e4; Widerspruch zwischen den Koordinatensystemen; Verletzung von
  dim g''_{p+1} ≤ Σ.

## Grenzen

Nur das Symbol. Die formale Integrabilität des erweiterten Systems (gibt es weitere versteckte Bedingungen?) ist der
nächste Schritt. θ vom älteren Keim.
