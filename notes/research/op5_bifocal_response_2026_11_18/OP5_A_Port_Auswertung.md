# OP5 – Auswertung des optischen A-Vorversuchs

21. November 2026. Analytische Erkundung im Materieframe M mit synthetischer Softwarekontrolle. Der [optische Kontrollversuch](OP5_J_Optischer_Kontrollversuch_Ansteuerungsfenster.md) gibt das Zweilastmodell, den unabhängigen Direktvergleich und das gewöhnliche Ansteuerungsfenster vor. Hier werden die A-Auswertung ausführbar gemacht und die mechanischen Kenngrößen normiert. Im [Gesamtbild](../../../wiki/Gesamtbild.md) betrifft dies die lokale Auslese. I3 benötigt eine eigenständige kosmologische Bestandsdynamik.

## Messdaten und Akzeptanzregeln

[op5_a_port_check.py](op5_a_port_check.py) verwendet Python ohne zusätzliche Bibliotheken. Pro Bandende sind genau vier Zustände zu erfassen. Die Namen sind `blank_off`, `blank_on`, `marker_off` und `marker_on`. Jeder Zustand braucht zwei unterschiedliche tatsächlich gemessene Lasten `loads`, einen zusätzlichen Lastpunkt `check_load` und einen unabhängigen Direktstandard `reference`. Alle komplexen Werte werden als `[Realteil, Imaginärteil]` angegeben. Jeder Lastpunkt enthält `x`, `y` und ihre absoluten komplexen Fehlerradien `x_error`, `y_error`. Der Standard liefert `value`, den absoluten Radius `error` und eine eindeutige `calibration_id`. Beide Beobachtungswege beziehen sich auf dieselben physikalischen Ebenen. Die Kennung verweist auf eine separat verfügbare Kalibrierung, deren Unabhängigkeit die Software nicht überprüfen kann. Optional darf je Zustand ein separater reiner, bereits entfalteter Phasenrest `extra_phase_error_rad` angegeben werden. Bereits im komplexen Radius enthaltene Fehler gehören nicht nochmals in dieses Feld.

Der dritte Lastpunkt testet die affine Verträglichkeit bei passivem $|r|\le1$. Aus den beiden Fit-Lasten berechnet das Programm den Interzept und dessen absolute Grenze aus gemessenen baryzentrischen Gewichten. Bei gemessenem Direktstandard $\widehat B$ und absolutem Fehler $\epsilon_B$ ist der Zellenradius
$$
r_{\rm Zelle}=\frac{|\widehat t-\widehat B|+\epsilon_t+\epsilon_B}{|\widehat B|-\epsilon_B}.
$$
Der Nenner ist eine untere Grenze für den wahren Referenzbetrag. Bei positivem Nenner und $r_{\rm Zelle}<1$ begrenzen $-\log(1-r_{\rm Zelle})$ den komplexen Logfehler und $\arcsin(r_{\rm Zelle})$ den Phasenfehler. Die Radien der vier Zustände werden je Bandende addiert. Die Endphasendifferenz trägt im konservativen Fall alle acht Zustandsgrenzen. Wirklich gemeinsame multiplikative Körper- oder Schaltfaktoren kürzen sich im Kreuzquotienten auch dann, wenn sie vom Frequenzende abhängen. Ein gemeinsamer additiver Fehler hat diese Eigenschaft nicht. Der Code nimmt ohne unabhängigen Beleg keine Fehlerkorrelation an.

Das Eingabeformat enthält oben `kind` als `synthetic` oder `measured`, `log_budget` pro Endpunkt und `endpoints` mit je `frequency_hz` und `states`. Das synthetische Eingabegerüst lässt sich ausgeben. Beispielbefehle aus der Repo-Wurzel:

```powershell
python notes/research/op5_bifocal_response_2026_11_18/op5_a_port_check.py --example-input
python notes/research/op5_bifocal_response_2026_11_18/op5_a_port_check.py --demo nominal
python notes/research/op5_bifocal_response_2026_11_18/op5_a_port_check.py --demo affine
python notes/research/op5_bifocal_response_2026_11_18/op5_a_port_check.py --demo curvature
python notes/research/op5_bifocal_response_2026_11_18/op5_a_port_check.py --input messung.json
```

Der Exitstatus 0 bedeutet, dass beide Endpunkte innerhalb der angegebenen Modell- und Fehlerhülle liegen. Status 1 bedeutet, dass die Daten mindestens einen Endpunkt nicht zertifizieren, auch bei widersprüchlicher affiner Prüfung. Status 2 meldet ungültige Daten, etwa zwei Fit-Lasten, deren Abstand nicht durch ihre Messradien abgesichert ist. Bei nicht nachgewiesenem von null verschiedenem Referenzbetrag bleibt die Loggrenze offen. Beobachtete zentrale Logwerte dienen als Diagnose und ersetzen die garantierte Hülle nicht.

## Synthetische Kontrollen

Alle drei Datensätze sind synthetisch und prüfen die Implementierung. Das gemeinsame illustrative Endpunktbudget ist $5\cdot10^{-7}$ im komplexen Logwert. Die Hüllen am oberen Bandende wurden tatsächlich so ausgegeben.

| Datensatz | Loggrenze am oberen Ende | Dritter Lastpunkt | Ergebnis |
| --- | ---: | --- | --- |
| Nominell | $3{,}8181\cdot10^{-7}$ | konsistent | innerhalb des Budgets |
| Affiner Interzeptfehler | $1{,}0853\cdot10^{-6}$ | konsistent | Direktstandard nicht eingehalten |
| Quadratische Lastantwort | $7{,}4563\cdot10^{-7}$ | Rest $4\cdot10^{-7}$ bei Grenze $4\cdot10^{-8}$ | affines Modell widersprochen |

Der affine Fehler zeigt, warum ein dritter Lastpunkt den unabhängigen Direktstandard nicht ersetzen kann. Der JSON-Rundlauf und die Zurückweisung zusammenfallender Fit-Lasten wurden ebenfalls ausgeführt. Die Prüfung gibt eine Auswertung für einen späteren realen A-Vorversuch. Gewöhnliche Messdaten, reale Referenzebenen und freie J-Ausbreitung sind hier noch nicht belegt.

## Dimensionsloses gewöhnliches Ansteuerungsfenster

Für $\Phi_*=G|D_\rho|\ell_z R_c^2$, $q=|\Phi_0|/\Phi_*$ und $e=\eta_\Phi/\Phi_*$ lautet das notwendige Fenster der vorigen robusten Garantie bei $\beta>\rho_K$ und positivem absoluten Messfehler
$$
\frac{(1+\rho_K)e}{\beta-\rho_K}
\le q\le
\min\left(
\frac{U_{\rm eff}}{C_uR_c},\
\frac{\epsilon_{\rm eff}}{C_\epsilon},\
\frac{\sigma_{\max}}{C_\sigma|D_\rho|\ell_z},\
\frac{R_c\bar F_{\max}}{C_F(\lambda+2\mu)\ell_z},\
\frac{A_{\rm eff}T^2}{4C_uR_c}
\right).
$$
Der Kraftterm gilt für die elastische Route. In der [spannungsfreien Endlage](OP5_J_Spannungsfreie_Ruhelagen.md) kann er entfallen, wenn die kompatible Zielmetrik materiell erreicht wird. Für die Zweikomponentenfahrt ist etwa $U_{\rm eff}=\min(U_1,cU_2)$ anzusetzen und analog bei Dehnung und Beschleunigung. Bei positiver Untergrenze gibt der Quotient aus kleinstem oberen Wert und unterem Wert die dimensionslose Reserve. Unter eins bleibt kein robustes Fenster. Über eins liefert der Vergleich eine notwendige Vorprüfung, solange die tatsächlichen Profilnormen und Werkstoffgrenzen unbekannt sind.

Wird das gewöhnliche Achsenpotential aus einem gewöhnlich-selektiven radialen Hubsignal rekonstruiert, kostet ein gleichmäßig begrenzter absoluter Hubfehler $\eta_u$ im Flächenannulus $[a,b]$ dimensionslos höchstens $4\pi(\sqrt b-\sqrt a)\eta_u/R_c$, zusätzlich zur Außen- und Längsreferenz. Wenn allein dieser Fehler und der mechanische Hub das Fenster begrenzen, muss im isolierten Ein-Prozent-Beispiel $\eta_u/U_{\rm eff}\lesssim1{,}043\cdot10^{-7}$ gelten. Das ist eine Anforderung der gewählten Worst-Case-Hülle. Ein direkt kalibriertes Integral oder korrelierte Fehler erfordern ein eigenes Budget.

Eine weitere notwendige Bedingung gilt für Aktoren mit **ortsfesten lokalen Antworttensoren** in der spannungsfreien longitudinalen Route. Für ein nichttriviales kompaktes Potential $\varphi$ spannen die Werte von $\operatorname{Hess}\varphi$ den ganzen Raum symmetrischer $3\times3$-Matrizen. Ein konstanter Annihilator $M$ würde im Fourier-Raum $(k^{\mathsf T}Mk)\widehat\varphi(k)=0$ erzwingen; auf einer offenen Menge mit $\widehat\varphi\ne0$ muss das quadratische Polynom daher verschwinden. Die lokale Aktorfamilie benötigt in diesem Fall sechs unabhängige Tensorrichtungen bereits am Endplateau. Räumlich wechselnde Antworttensoren und ableitungsgekoppelte Aktoren fallen außerhalb dieses Arguments. Das ist ein Rangtest, keine materielle Realisierung.

Für das Fenster sind mindestens Geometrie und Längsträger, die Gegenhubrelation beider Komponenten, Dichtedifferenz, zulässiger Hub, Dehnung, Säulendichte, Fahrzeit und Beschleunigung sowie bei elastischer Stützung Lamé-Modul und projizierte Kraftgrenze zu vermessen. Referenzpotential, Transferrest und Modellreserve brauchen unabhängige Eingaben. Freie J-Ausbreitung, HCl/H-Portkondition, native Metrik und H96 bleiben offen.

## Rechenkontrolle

Wolfram prüfte Zweilastidentität, Faktorkürzung, komplexe Referenzgrenze, dimensionslose Fenstergrenzen und das lineare Rangbeispiel. Python führte die drei Datenfälle und den JSON-Prüfpfad auf demselben Kommandozeileneinstieg aus. Qiskit wurde für diese klassischen Phasen- und Kontinuumsrechnungen erwogen.

[Wolfram-Skript](op5_a_port_evaluation.wl) · [Tatsächliche Wolfram- und Python-Ausgabe](op5_a_port_evaluation.txt) · [Laufmanifest](op5_a_port_evaluation.json)
