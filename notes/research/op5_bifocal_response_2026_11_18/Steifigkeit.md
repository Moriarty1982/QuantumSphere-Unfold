# Bifokale Reparatur und Rückstellenergie

Analytische Erkundung mit numerischer Kontrolle gemäß [Vorab-Notiz](Steifigkeit_Vorab.md), Commit 4bce6650b589243fe1dafead2d634fb5c40de827. Modell-Einheiten und gleiche euklidische Chartkoordinate. Die Umfangsenergie ist ein zusätzlicher Ansatz.

Setze r=c/b, B(t)=∂_b G=2ab sin²t/(a²−c²cos²t), A=⟨B²⟩>0. Dann ist G=B(t)(v+ru)+O((|u|+|v|)²). Für den Umfang gilt ℓ_b=∫₀^{2π} b cos²t/(a²sin²t+b²cos²t)^{1/2} dt>0. Eine feste Ruhelänge erzeugt S=κℓ_b² und die führende Energie E₂=[A(v+ru)²+Sv²]/2. Ihr Minimum liegt bei v*=−Ar u/(A+S). Der Restanteil des linearen Defekts ist S/(A+S); der minimale quadratische Energieterm ist χu²/2 mit χ=ASr²/(A+S). Jede positive feste Rückstellung mit c>0 hinterlässt deshalb in diesem Modell beides: lineares Restresiduum und positive quadratische Energie.

Kontrolle mit einer Ruhelänge ℓ(b+du)+O(u²): Ersetze Sv² durch S(v−du)². Dann χ=AS(r+d)²/(A+S). Für d=−r verschwindet die quadratische Energie trotz positiver Steifigkeit. Wird die Ruhelänge exakt als ℓ(√(a²−(c+u)²)) mitgeführt, besitzt die reparierte Form sogar exakt Energie null in beiden Anteilen. Diese Mitführung ist eine zusätzliche Kopplungsregel; weder das geometrische Nullresiduum noch die P-Bedingung erzwingt sie.

Für a=√2, b=c=1, κ=1 ergibt periodische Quadratur A=0,928932, ℓ_b=2,847835, S=8,110162, v*/u=−0,102768, χ=0,833467. Rund 89,7 % des linearen Defekts bleiben. Die direkte Minimierung der nichtlinearen Modellenergie auf 512 Winkelpunkten ergab 2E_min/u²=0,834318, 0,833893 und 0,833680 bei u=0,001, 0,0005 und 0,00025. Für κ=0 liefert die bekannte exakte Reparaturellipse Energie null.

OP5: Nur wenn u in einer physikalischen Reduktion proportional zur erhaltenen Eigendichte wäre und E in die effektive Energiedichte einginge, entspräche die quadratische Energie dem Zusatzdruck des bisherigen Fluidmodells. Der Befund verschiebt die Frage vom bloßen Vorhandensein einer Formmode zur nativen Bestimmung ihrer Ruhelänge und der Quelle u. OP5 und H96 bleiben offen.
