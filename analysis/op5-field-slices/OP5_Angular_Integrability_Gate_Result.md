# OP5: prüft die Winkelstruktur die symmetrische Fortsetzungsobstruktion?

30.10.2026. Direkter Eliminationsvergleich, drei reparierte Kontrollpunkte aus OP5_Joint_Compatibility_Lower_Data.json. Feldwerte und erste Jets fest; ursprüngliche Kopplungen und Coframe-Definition unverändert.

Wolfram bestätigte auf rho>0 exakt s=rho dphi und d(dphi)=0. Daraus folgt die zuvor hergeleitete Struktur E^a=dj_a/2+B_a dphi. Sie ist eine geometrische Identität der Vergleichsauslese, kein zusätzlicher physikalischer Feldterm.

Untersuchte Freiheiten:384 reelle geordnete zweite Ableitungen ohne gemischte Symmetrie; diese erfüllen nach gemeinsamer erster Reparatur die96 differenzierten Spinorgleichungen bis ungefähr1e-9 bei Differenzschritt1e-5. Volle Symmetrie reduziert auf240 Variablen und hinterlässt die bekannten stabilen Reste .000878954,.02363114,.00949257.

Erster Test:12 unabhängige lineare Bedingungen dphi wedge dE^a=0 auf die geordneten zweiten Jets. Die Basisfreiheit wird vollständig durch einen Nullraum eliminiert, bevor die Feldgleichungen gelöst werden. Alle drei Punkte bleiben bis ungefähr1.5e-9 kompatibel. Die frei gewählte Minimum-Norm-Lösung ohne diese Bedingungen verletzt sie zwar deutlich, aber andere freie Lösungen erfüllen sie. Deshalb darf die Verletzung eines Einzelrepräsentanten nicht als Ursache der Obstruktion gelten.

Zweiter Test: volle Strom-Curl-Identität dE^a=dB_a wedge dphi. Nach Abzug der bereits bekannten ersten-Jet-/Hintergrundquelle verlangt sie Aread_a(z_mu_nu-z_nu_mu)=0, wobei Aread_a delta z=Re(Psi†Q_a delta z). Dies liefert24 unabhängige Bedingungen auf geordnete zweite Jets. Diese Matrix annihiliert den gesamten symmetrischen Zweitjetraum numerisch unter1e-10. Ergebnisse des vollständigen Nullraumtests stehen in OP5_Angular_Integrability_Gate_Check.json unter full_current_F_residual.

Auch die volle Strom-Curl-Identität lässt alle drei Systeme numerisch kompatibel: Restnormen bei Schritt1e-5 etwa1.59e-9,1.52e-9,1.58e-9. Die ausgelesene geometrische Curlstruktur erklärt somit den bisherigen großen Rest in diesem Test nicht. Die zusätzlichen Hindernisse treten erst auf, wenn die zugrunde liegenden Spinorableitungen selbst vollständig symmetrisch fortsetzbar sein müssen. Coframe-Integrabilität und Spinor-Integrabilität dürfen nicht gleichgesetzt werden.

Alle Systeme verwenden drei Differenzschritte1e-4,1e-5,1e-6. Restwerte nahe1e-9 sind von Differenz-/Rundungsfehlern begrenzt; keine exakte Rangzertifizierung oder regionale Lösung. Die Eliminationsvergleiche sind aussagekräftiger als bloße Dimensionszählung oder das Prüfen eines einzelnen freien Fits.

Artefakte OP5_Angular_Integrability_Gate_Check.py/.json mit gespeicherten Quellen und Vorläuferdaten erforderlich. Lokal gespeichert, nicht committed. OP5 und native physikalische Identifikation bleiben offen.
