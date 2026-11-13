# Ergebnis H101: Die Maske aus r47 in Form K hebt das Elektron nicht aus dem Oktanten

**13. November 2026, spät. Vorab-Notiz `Vorab_Notiz_H101_Maske_hebt_Elektron.md` (Commit f470817). Skript `k223_test_h101.py`,
Ausgabe `k223_out.txt`. Status: H101 widerlegt (keine Lösung für ε). Nicht blind gegenüber den Daten.**

## Ergebnis
- Form K, M = D C D mit D = exp(ε W_l): Für keinen Wert von ε (beide Vorzeichen, |ε| bis 3) und keinen Maskenplatz wird
  m_e/m_τ = 2,876·10⁻⁴ erreicht. Der kleinste Eigenwert bleibt exakt null (Kontrolle bei ε = 0,05; 0,3; −0,4).
- **Grund (nachträglich erkannt, hätte vorab auffallen können):** Form K ist eine Kongruenz mit invertierbarem D. Nach dem
  Trägheitssatz von Sylvester behält sie Rang und Signatur; der Oktant hat Rang 2, also bleibt das Elektron masselos.
  Form S (Ähnlichkeit, r57) ändert die Eigenwerte gar nicht. Keine der beiden Formen aus r57 kann den A_4-Bruch liefern.
- Kriterium: H101a widerlegt (keine Lösung), damit H101 widerlegt.

## Nebenrechnung (nicht Teil des Kriteriums, nachträglich)
Die lineare Form aus r47, M = C + ε(W C + C W), ist keine Kongruenz und hebt den Rang:
- ε = +0,0870: m_μ/m_τ = 0,05967 (Daten 0,05946, +0,35 %), K = 0,666343;
- ε = −0,1796: m_μ/m_τ = 0,04826 (−18,9 %), K = 0,685659.
Die erste Lösung sieht gut aus, verfehlt aber die Genauigkeit der Pol-Koide-Beziehung deutlich: K weicht um 3,2·10⁻⁴ ab,
bei einer Unsicherheit von 5·10⁻⁶ (aus m_τ) etwa das 60-Fache. Dass m_μ/m_τ nahe am Messwert liegt, ist zudem keine
unabhängige Vorhersage: Jede kleine Anhebung, die K nahe 2/3 lässt, gibt bei festem m_e/m_τ fast das richtige m_μ, weil
Koide m_μ aus m_e und m_τ bestimmt. Das vorab festgelegte K-Kriterium (10⁻³) war gemessen an dieser Genauigkeit zu weit.

## Lesart
- Der A_4-Bruch, der das Elektron hebt, muss den Rang ändern; Kongruenz- und Ähnlichkeitsformen scheiden aus.
- Die lineare r47-Form tut das, bricht aber Koide auf der Genauigkeitsskala der Polmassen. Eine Anhebung, die K = 2/3 auf
  10⁻⁵ erhält, ist damit nicht gefunden.
- OP3/OP4 offen; OP1–OP5, C5, C6/T2 unverändert; H100 unberührt.
