# OP5: Strahlungseinfang und Anzahl gebundener Paare

19. November 2026. Analytische Erkundung für OP5/T9 im M-Frame. Die [Tensorbilanz](OP5_Gebundener_Tensor.md) liefert die Energie eines gebundenen Paars. Rückwärts von [H96](../predictions/Vorab_Notiz_H96_Omega_M_beta2.md) verlangt die Materiedichte zusätzlich eine Dichte langlebiger Paare zur festgelegten Epoche. Die [Fokusbahn](W2_Fokusbahn.md) zeigte klassischen Strahlungsverlust. Der [Quantendipol](W2_Quantendipol.md) behandelte das Relativspektrum ohne Strahlungsmoden. Hier kombinieren wir die Coulomb-Grenze dieses Spektrums mit dem transversalen [J-Maxwell-Kanal](W2_J_Eichkanal.md) im nichtrelativistischen Punktquellenvergleich. Zwei entgegengesetzt geladene Konstituenten in den einlaufenden Zuständen werden vorausgesetzt. Es gibt keinen kosmologischen Datenvergleich.

## Einfang aus dem Kontinuum

Seien $M_1,M_2$ die renormierten Massen, $\pm q$ die J-Ladungen, $\mu$ die reduzierte Masse und $A=q^2/(4\pi)>0$. Ein einlaufender Zustand mit relativem Impulsbetrag $k>0$ hat $E=k^2/(2\mu)$. Der Grundzustand liegt bei $-1/(2\mu a^2)$ mit $a=(\mu A)^{-1}$. Beim Übergang kann ein transversales J-Quant die frei werdende Energie aufnehmen. Im Schwerpunkt gilt $E+1/(2\mu a^2)=\omega+\omega^2/[2(M_1+M_2)]$ auf führender Rückstoßordnung. Es gibt eine positive Lösung für $\omega$. Die elektrische Dipolkopplung $-\mathbf D\cdot\mathbf E_J$ mit $\mathbf D=q\mathbf r$ verbindet eine einlaufende Partialwelle $\ell=1$ mit dem Grundzustand $\ell=0$. Die Näherung setzt $k/\mu\ll1$, $A\ll1$ und $\omega a\ll1$ voraus.

Der Winkelanteil ist für geeignete Polarisation von null verschieden. Der Radialanteil verschwindet im Coulomb-Grenzfall für kein $k>0$. Schreibe $u=a^{-1}$, $\eta=-u/k$, $s=u+ik$ und $\theta=\arctan(k/u)$. Bei weggelassenen positiven Normierungsfaktoren gilt
$$
\begin{aligned}
I(k)&=\int_0^\infty r^4e^{-sr}\,{}_1F_1(2-i\eta;4;2ikr)\,dr\\
&=24s^{-5}\,{}_2F_1(2-i\eta,5;4;2ik/s)
=\frac{12u}{(u^2+k^2)^3}\exp(2\eta\theta)>0.
\end{aligned}
$$
Die Potenz $r^4$ enthält das Volumenmaß, den Dipolfaktor und die reguläre Coulomb-Radialfunktion $F_1(\eta,kr)/r$ nach Abtrennen von $C_1(\eta)k^2$. Für die letzte Gleichheit setze $b=2-i\eta$ und $z=2ik/s$. Die hypergeometrische Reihe und ihre Fortsetzung liefern
$$
{}_2F_1(b,5;4;z)=(1-z)^{-b-1}[1+(b/4-1)z].
$$
Die Klammer ist $u/(2s)$. Der Zweig wird von $k=0$ entlang positiver $k$ fortgesetzt. Funktionsdarstellung und Laplace-Transformation: [NIST DLMF §33.2](https://dlmf.nist.gov/33.2.ii), [§13.10](https://dlmf.nist.gov/13.10.ii).

Unabhängige numerische Kontrolle in Einheiten $a=1$: Setze $F_1/r=C_1 k^2 r w$ und löse $w''+4w'/r+(k^2+2/r)w=0$ mit $w(0)=1$ und $w'(0)=-1/2$ per Runge–Kutta vierter Ordnung, gestartet mit der regulären Taylorreihe bis zum kubischen Term. Integriere $r^4e^{-r}w$ auf $[0,35]$ mit Schritt $0{,}001$ per Trapezregel. Für $ka\in\{1/4,1/2,1,2\}$ lag die maximale relative Abweichung von der Formel bei $1{,}73\times10^{-12}$. Die Rechnung bestimmt das Matrixelement bis auf Normierung. Die thermische Einfangrate bleibt offen.

## Bilanz der langlebigen Paare

Im homogenen verdünnten M-Ensemble seien $n_\pm$ die physischen freien Anzahldichten, $n_b$ jene der gebundenen Paare, $S(t)$ der kosmische Skalenfaktor und $H=\dot S/S$. In einer lokalen kinetischen Beschreibung mit Ionisation und irreversiblen Verlusten gilt
$$
\dot n_b+3Hn_b=\langle\sigma_{\rm cap}v_{\rm rel}\rangle n_+n_-
-(\Gamma_{\rm ion}+\Gamma_{\rm loss})n_b.
$$
Für $N_b=S^3n_b$ und $\Gamma=\Gamma_{\rm ion}+\Gamma_{\rm loss}$ folgt
$$
N_b(t)=N_b(t_i)e^{-\int_{t_i}^t\Gamma\,du}
+\int_{t_i}^t S^3(s)\langle\sigma_{\rm cap}v_{\rm rel}\rangle(s)n_+(s)n_-(s)
e^{-\int_s^t\Gamma\,du}\,ds.
$$
Einlaufverteilungen, J-Strahlungshintergrund, Verlustraten und Expansion gehen als Eingaben ein. Bei bloßem Einfang und Rückionisation bleiben $S^3(n_\pm+n_b)$ einzeln erhalten. Das kleinere der beiden Inventare begrenzt $N_b$. In diesem Zweiartenensemble erzwingt J-Neutralität bei gleichen Ladungsbeträgen Gleichheit der freien Inventare und lässt ihre gemeinsame Höhe beliebig. Ohne anfängliche Konstituenten und ohne zusätzliche Quelle bleibt $N_b=0$. Mit freien Konstituenten, Überlappung mit dem Einfangkanal und endlichen Verlustraten kann $N_b>0$ entstehen.

Der konservative Grundzustand liegt unter der Dissoziationsschwelle. Seine Lebensdauer hängt von weiteren offenen Kanälen ab. Für Teilchen und Antiteilchen derselben Art ist insbesondere Annihilation zu berücksichtigen. Ein Paar aus verschiedenen Arten verlangt die Prüfung der erhaltenen Quantenzahlen und der übrigen Zerfallskanäle. Das J-Quant führt Energie innerhalb von M ab. Diese Rechnung enthält keine M–T-Kopplung.

## Bedingung für H96

Mit der [gebundenen Gesamtenergie](OP5_Gebundener_Tensor.md) $E_b$ pro Paar und den übrigen Materiebeiträgen $\rho_{\rm sonst}$ lautet die Bedingung für die Zuordnung zu H96 heute
$$
n_b(t_0)E_b(t_0)=\beta_{\rm sym}^2\rho_{\rm crit}(t_0)-\rho_{\rm sonst}(t_0).
$$
Die rechte Seite muss für eine positive Paarenergiedichte nichtnegativ sein. Der nächste offene Modellschritt ist die Wahl und Prüfung nativer langlebiger Konstituenten sowie die Herleitung ihrer anfänglichen Inventare. Native kompakte Foki und Randwirkung bleiben offen. I3 würde weiterhin eine eigenständige Überschussdynamik erfordern.
