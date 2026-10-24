# Vorab-Notiz H42: Vorhersage sin²θ₂₃ ≤ 0.54 aus der korrigierten TM2-Lesart

Festgelegt am 2026-10-24, **vor** jedem Vergleich mit Daten, die nach diesem Datum veröffentlicht werden. Autor: „merge und leg es fest“. Bezug: r55/H39 (Lesart je
Teilchenart: Dirac ℤ₃, Majorana ℤ₂ aus A₄ ⇒ TM2), r57/H41 (Maske als Korrektur; bei θ₁₂ im JUNO-2σ-Bereich und θ₁₃ im NuFIT-3σ-Bereich gilt sin²θ₂₃ ≤ 0.537 in
Variante A und ≤ 0.515 in Variante B).

## Offenlegung

Die Grenze wurde in r57 **nach** der Auswertung bemerkt (k97_out.txt, Commit ad1375d). Sie gilt deshalb erst ab dieser Notiz als Vorhersage; Daten, die vor dem
2026-10-24 veröffentlicht waren, zählen nicht als Prüfung. Stand dieser Daten (NuFIT 6.0, normale Ordnung): ohne SK-atm sin²θ₂₃ = 0.561 (+0.012/−0.015), mit SK-atm
0.470 (+0.017/−0.013); der Oktant ist offen. Die Vorhersage liegt also zwischen den beiden heutigen Lösungen und ist durch sie weder bestätigt noch widerlegt.

## Vorhersage

Unter der Lesart von r55 mit der Maskenkorrektur von r57 gilt **sin²θ₂₃ ≤ 0.54** (normale Ordnung). Die Grenze ist eine gerundete obere Schranke aus beiden Varianten;
sie hängt an den dort festgelegten Modellwahlen (zirkulante Dirac-Kopplung, ℤ₂-invariante Majorana-Kopplung, Maske W_l = diag(0, 0, −3), Formen S bzw. K).

## Prüfdaten

Die erste globale Auswertung (NuFIT oder gleichwertig) oder die erste Einzelmessung von DUNE oder Hyper-Kamiokande, die nach dem 2026-10-24 erscheint und für
sin²θ₂₃ in normaler Ordnung ein 2σ-Intervall angibt. Bei mehreren Varianten (etwa mit und ohne atmosphärische Daten) zählt die von den Autoren als Hauptergebnis
bezeichnete.

## Entscheidungskriterium (verbindlich)

- **Widerlegt**, wenn das 2σ-Intervall ganz über 0.54 liegt.
- **Bestätigt**, wenn das 2σ-Intervall ganz unter 0.54 liegt.
- **Offen**, wenn 0.54 im 2σ-Intervall liegt; dann zählt die nächste Auswertung.
- Eine Bestätigung prüft nur die Grenze, nicht die Lesart als Ganzes: Auch andere Modelle sagen den unteren Oktanten oder θ₂₃ nahe 45° voraus.

Nach dem Commit dieser Notiz wird daran nichts mehr geändert.
