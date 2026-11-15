"""Schritt 2 (Erkundung): null, ein, zwei Kerne. Phasenbuchhaltung ueber Holonomien (Spin 1/2: Phase = Fluss).
Monopol: Flussdichte 1/2 pro Steradiant, Gesamtfluss 2 pi. Dreieck = Oktant (pi/2 sr), Kern = Kappe Omega im Dreieck.
Auf S^2 ohne n Kappen ist der Rest fuer n = 1 einfach zusammenhaengend (Scheibe), fuer n = 2 ein Ring (H^1 = Z),
allgemein hat er n - 1 unabhaengige Schleifen um Loecher, also n - 1 freie Aharonov-Bohm-Holonomien."""
import math
G = 0.2375330
OCT, SPH = math.pi / 2, 4 * math.pi
def wrap(p):
    return (p + math.pi) % (2 * math.pi) - math.pi
# Ein Kern: die Dreiecksschleife beraendet im Rest die Aussenflaeche O (ohne Loch); Holonomie = -Fluss(O) mod 2 pi
outside = SPH - OCT
cases = {
    "Kern ausgeschnitten, Zusammenhang unveraendert": 0.5 * outside,
    "Kern flussfrei, verdraengter Fluss gleichmaessig verteilt (B)": outside * 2 * math.pi / (SPH - G),
    "Kern flussfrei, verdraengter Fluss ausserhalb des Dreiecks, z. B. am Gegenpol (A)": 0.5 * outside + G / 2,
    "Kern flussfrei, verdraengter Fluss im Dreieck abgelegt": 0.5 * outside,
}
print("Ein Kern im Dreieck (Raumwinkel gamma_M), Bargmann-Phase der Dreiecksschleife:")
for k, flux_out in cases.items():
    print(f"   {k:78s} phi = {wrap(-flux_out):.6f}")
print("   Ziel (Leptonen) 2/3 =", round(2 / 3, 6), "; Oktant pi/4 =", round(math.pi / 4, 6))
print("Kein Kern: geschlossene Kugel, Gesamtfluss 2 pi fest, phi = pi/4 starr (keine Biegung).")
print("Zwei Kerne: Rest ist ein Ring; eine freie AB-Holonomie t um den Ring verschiebt phi beliebig:")
for t in (0.0, 0.1, -0.1):
    print(f"   t = {t:+.1f}: phi = {wrap(math.pi / 4 - G / 2 + t):.6f}")
print("n Kerne: n - 1 freie Holonomien. Genau ein Kern ist die einzige Zahl, die Biegung erlaubt und keinen freien Parameter hat.")
