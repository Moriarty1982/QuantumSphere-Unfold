# Der Kollapszustand z⁻ = 0 im ganzen Hauptkorpus, mit heutigem Wissen typisiert

16. November 2026, Claude Opus 5.5. **Erkundung (Lesart), nicht blind, ohne Rechnung und ohne Kriterium.** Auftrag des Autors:
„PR 147 mergen dann weiter“. Der Autor hatte darauf hingewiesen, dass die Idee des Kollapszustands vom Anfang des Projekts stammt und
mit heutigem Wissen zu überprüfen ist. r21.9 hatte dafür vier Stellen gelesen; hier sind alle 93 Stellen mit z⁻ im Hauptkorpus
durchgesehen (Liste: `zminus_stellen.txt`). Der Hauptkorpus wird nicht umgeschrieben; die Zuordnung ist eine Typisierung wie in
v4.9.0-r23/r24.

## Vorwissen geprüft
- **v4.9.0-r22 (Konvention F):** M, T und der Photonpunkt P (b = 0, Fixpunkt).
- **v4.9.0-r23/r24:** Der Hauptkorpus arbeitet in einem einzigen Frame. Sein „Photon-Frame“ (Versatz null) ist der Bezugsframe R, der
  reine Zustand mit |b| = 1; P ist der maximal gemischte Zustand und wird erst für β → 1 erreicht. Es gilt |b| = sech 2η.
  Vorzeichen von β sind Orientierungscodes; J: z⁻ ↦ −z⁻ ist die Ladungskonjugation C.
- **v4.9.0-r29.1:** Das Vakuum z⁻ = 0 des Hauptkorpus ist R. Der Horizont β → 1 ist der Photon-Fixpunkt P der Konvention F.
- **v4.9.0-r61.1(b), r64:** Der Hopf-Wert liest einen reinen R-Zustand; `thm:hawking-triolic` ordnet das Hawking-Photon dem Frame R zu.
- **v4.8.0-r18:** z⁻ = 0,422 ist eine Halbierung in der Geschwindigkeit, in der Rapidität ist es β_sym; „permanent“ in
  `thm:dark-offset` heißt nicht verschwindend.
- **k220, v4.10.0-r21.8/r21.9:** zwei Klassen, Vertreter R (φ = 1) und P (φ = 0); φ = sech 2η_R; der Kollapszustand hat zwei Rollen.

## Die Typisierung
| Gruppe | Fundstellen (Label oder Datei:Zeile) | Was z⁻ = 0 dort ist |
|---|---|---|
| **1. Nullpunkt des Versatzes** | `thm:frame-offset` (Beweis), `thm:symmetric-frame`, `thm:dark-offset`, `thm:spring`, 10:1328–1333 (v/c), 10:1429–1453 (Beobachterposition), 10:1786–1793 (GUE-Taktgeber im Photon-Frame), 10:1866–1871 (k(c) = 0), `prop:shared-vacuum-planck`, `thm:dark-energy` (absorbierender Zustand S², Λ = 0), `thm:hawking-triolic` (Photon bei β = 0), 12:696–977, 13:179, 18:47 (θ_H = 0), 23:398–648, 08:28, 08:31 | **R**, der Bezugsframe mit Versatz null (r24.3, r29.1(a), r61.1(b), r64) |
| **2. Das invariante Objekt** | `thm:unity` und die Bemerkung danach, die Bemerkung „Sphaera as photon“ (10:103–118), 10:1318 („unique fixed point“), 10:1352–1364 (Licht als Kompensator des Universums), 10:1565, 10:1609 | die **Rolle von P** (frame-invariant, Fixpunkt), dem Punkt z⁻ = 0 zugeschrieben |
| **3. Der Horizont** | Definition des Schwarzschild-Horizonts, `prop:horizon-cascade-singularity`, `thm:core`, Bemerkung „Black hole as inverted Sphaera“ | z⁻ → ∞ bei β → 1: der **Ort von P** in der Koordinate des Hauptkorpus (r24.3, r29.1(b)) |
| **4. Kein Punkt** | Planck-Boden und Turm \|z⁻\|ₙ (`thm:origin`), Pauli („same z⁻ state“), J: z⁻ ↦ −z⁻ (10:243–581), Vorzeichen von Re z⁻ (10:372), Messung als Projektion von z⁻ (10:577–581), RH-Zeile (10:453, 08:81, zurückgezogen seit v4.8.0-r04) | Skala, Orientierung (C, r24.1) oder zurückgezogen |
| **5. Richtung der Kaskade** | 10:115, `thm:core`, „inverted Sphaera“, `thm:dark-energy` (Kaskade „collapses directly to the photon ground state“) | **ungeklärt**: Ziel ist der Koordinatenpunkt R; die Kaskade ist aber nicht umkehrbar (Markov, absorbierend), und nach k220 führen nicht umkehrbare Schritte zu P |

## Ergebnis
1. **Die Koordinate z⁻ des Hauptkorpus läuft von R nach P.** Bei z⁻ = 0 liegt R (Versatz null, reiner Zustand), bei z⁻ → ∞ (β → 1,
   Horizont) liegt P (Photonpunkt, maximal gemischt). Das ist dieselbe Linie wie die Rapiditätslinie von r21.8: Dort gilt
   φ = sech 2η_R mit R bei η_R = 0 und P bei η_R = ∞, hier |b| = sech 2η nach r24.3. Die Gleichsetzung von z⁻ mit einer Rapidität ist
   eine Lesart: Der Hauptkorpus benutzt z⁻ mit wechselnder Skala (±β_sym als Geschwindigkeit, β/2, ∞ bei β → 1; vgl. r18).
2. **Der Name „Kollapszustand“ steht am falschen Ende für seine Hauptrolle.** Gruppe 1 (rund zwei Drittel der Stellen) benutzt
   z⁻ = 0 als Nullpunkt des Versatzes, also R. Gruppe 2 schreibt demselben Punkt die Rolle des invarianten Objekts zu, und die gehört
   P. Gruppe 3 setzt P, ohne es so zu nennen, an das andere Ende, z⁻ → ∞.
3. **Für die Frage des Autors („liegt drin oder nicht“):** Die lichtartige Klasse, also der Nullzustand im Sinn von r21.8, ist in der
   Koordinate des Hauptkorpus nicht z⁻ = 0, sondern z⁻ → ∞, der Horizont. Der Kollapszustand als Nullzustand gelesen ist der
   Horizont-Endpunkt. Das passt zur Lesart „Kern als Schatten eines Horizonts“ (Erkundung vom 15.11.,
   `../op3_horizon_shadow_2026_11_15/`) und zu r29.1(b).
4. **Berichtigung zu r21.9, Zeile 3.** r21.9 hatte „we can never fully reach z⁻ = 0“ (`thm:dark-offset`) als Aussage über
   Erreichbarkeit gelesen und P zugeordnet. Im Zusammenhang (Versatz β_sym bleibt als Restterm; v4.8.0-r18: „permanent“ heißt nicht
   verschwindend) ist es eine Aussage über die Lage des Materie-Frames: Er hat einen bleibenden Versatz und ist nie der reine Zustand.
   Das ist **R**, nicht P. Die in r21.9 vermerkte Spannung mit r24.3 besteht damit nicht.
5. **Offen bleibt Gruppe 5.** Ob die Kaskade „zurück zu z⁻ = 0“ zum Koordinatenpunkt R oder zur Klasse P führt, entscheidet der
   Hauptkorpus nicht. Für einen absorbierenden Markov-Prozess liegt P (Mischung) näher, für „Versatz null“ R.

## Was das nicht ist
- Keine Umschreibung des Hauptkorpus; die Zuordnung ist eine Lesart an den genannten Stellen.
- Keine neue Zahl und kein Test.
- OP1–OP5, C5, C6/T2 und die Guards sind unverändert.
