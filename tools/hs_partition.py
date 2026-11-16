"""Hilfskonstruktion fuer verschachtelte Tensor-Shift-Stufen (HS-Turm des Atlas, Verdopplungsregel v4.10.0-r26.1).

Idee des Autors (16.11.2026): Man uebergibt, welche HS-Stufe wie aufgeteilt ist (z. B. HS(8) = HS(7) + HS(6) + HS(6)) und welche
Beziehungen zwischen den Teilen gelten (Gewicht eines Teils, Normierung in einem uebergeordneten Teil); das Werkzeug rechnet die
Generationszustaende, die Ueberlappungsbedingung und die Phase einheitlich und zaehlt die moeglichen Mechanismen einer Aufteilung.

Begriffe
- Stufe HS(n) ueber dem Dixon-Traeger HS(6): k = n - 6 Kopien-Bits; Kopienindex (C^2)^{(x)k} mit 2^k Kaesten (Bitstrings).
- Basis: die Achse, in der die Kopien-Bits gelesen werden (Standard: Zyklusachse z); Bitreihenfolge legt die Halbierung fest
  (erstes Bit halbiert HS(n) in zwei HS(n-1), usw.).
- Knoten: jede Halbierung erzeugt Knoten; Name "HS(m)[praefix]" fuer den Teil, dessen erste (n-m) Bits gleich praefix sind.
- Generationszustaende: drei Richtungen n_k auf einem Kegel (Halbwinkel psi) um die Achse, Triplettanteil |n_k>^{(x)k} (Spin k/2),
  dazu optional eine gemeinsame Beimischung mit Gewicht w aus dem Komplement des symmetrischen Teils (k = 2: das Singulett).
- Mechanismus: eine Funktion der Knotengewichte des Triplettanteils, die w festlegt (selbstkonsistent mit psi).

Keine Physik wird hier entschieden; das Werkzeug rechnet nur, was eine Vorab-Notiz festlegt.
Aufruf zur Selbstpruefung: python tools/hs_partition.py --selftest
"""
import argparse
import itertools
import numpy as np


# ---------------------------------------------------------------- Kopienindex und Knoten
class ShiftTree:
    def __init__(self, stage, base=6, bit_order=None, axis=(0.0, 0.0, 1.0)):
        if stage < base:
            raise ValueError("Stufe unter dem Basistraeger")
        self.stage, self.base, self.k = stage, base, stage - base
        self.bit_order = list(bit_order) if bit_order is not None else list(range(self.k))
        if sorted(self.bit_order) != list(range(self.k)):
            raise ValueError("bit_order muss eine Permutation der Kopien-Bits sein")
        self.axis = np.asarray(axis, float) / np.linalg.norm(axis)
        self.boxes = ["".join(b) for b in itertools.product("01", repeat=self.k)]
        self.nodes = self._build_nodes()

    def _build_nodes(self):
        nodes = {}
        for depth in range(self.k + 1):                  # depth Bits festgelegt -> Stufe HS(stage - depth)
            for prefix in itertools.product("01", repeat=depth):
                prefix = "".join(prefix)
                members = [b for b in self.boxes
                           if all(b[self.bit_order[i]] == prefix[i] for i in range(depth))]
                name = f"HS({self.stage - depth})" + (f"[{prefix}]" if depth else "")
                nodes[name] = members
        return nodes

    def describe(self):
        return {name: members for name, members in self.nodes.items()}

    # Basiswechsel: Kaesten in der Basis der Achse lesen
    def _axis_unitary(self):
        a = self.axis
        th, ph = np.arccos(np.clip(a[2], -1, 1)), np.arctan2(a[1], a[0])
        u = np.array([[np.cos(th / 2), -np.exp(-1j * ph) * np.sin(th / 2)],
                      [np.exp(1j * ph) * np.sin(th / 2), np.cos(th / 2)]])
        U = np.eye(1)
        for _ in range(self.k):
            U = np.kron(U, u)
        return U                                          # Spalten = Achsenbasis

    def box_weights(self, state):
        amp = self._axis_unitary().conj().T @ state
        return {b: abs(amp[i]) ** 2 for i, b in enumerate(self.boxes)}

    def node_weights(self, state):
        p = self.box_weights(state)
        return {name: sum(p[b] for b in members) for name, members in self.nodes.items()}

    # symmetrischer Teil und Komplement auf dem Kopienindex
    def symmetric_projector(self):
        d = 2 ** self.k; P = np.zeros((d, d))
        for perm in itertools.permutations(range(self.k)):
            M = np.zeros((d, d))
            for i, b in enumerate(itertools.product((0, 1), repeat=self.k)):
                j = int("".join(str(b[perm[t]]) for t in range(self.k)) or "0", 2)
                M[j, i] = 1
            P += M
        return P / max(1, len(list(itertools.permutations(range(self.k)))))

    def complement_vector(self, seed_vector=None):
        """Normierter Vektor im Komplement des symmetrischen Teils (k = 2: das Singulett)."""
        d = 2 ** self.k
        Q = np.eye(d) - self.symmetric_projector()
        if np.allclose(Q, 0):
            raise ValueError("Komplement leer (k < 2)")
        v = Q @ (np.asarray(seed_vector, complex) if seed_vector is not None else np.eye(d)[1])
        return v / np.linalg.norm(v)


# ---------------------------------------------------------------- Generationszustaende und Auswertung
def coherent(n):
    th, ph = np.arccos(np.clip(n[2], -1, 1)), np.arctan2(n[1], n[0])
    return np.array([np.cos(th / 2), np.exp(1j * ph) * np.sin(th / 2)])


def cone(psi, axis=(0, 0, 1)):
    a = np.asarray(axis, float) / np.linalg.norm(axis)
    e1 = np.cross(a, [1, 0, 0] if abs(a[0]) < 0.9 else [0, 1, 0]); e1 /= np.linalg.norm(e1); e2 = np.cross(a, e1)
    return [np.cos(psi) * a + np.sin(psi) * (np.cos(2 * np.pi * j / 3) * e1 + np.sin(2 * np.pi * j / 3) * e2) for j in range(3)]


def triplet_part(tree, n):
    v = np.eye(1)
    for _ in range(tree.k):
        v = np.kron(v, coherent(n).reshape(-1, 1))
    return v.ravel()


def generation_states(tree, psi, w=0.0, admix=None):
    t = [triplet_part(tree, n) for n in cone(psi, tree.axis)]
    if w == 0:
        return t
    e = admix if admix is not None else tree.complement_vector()
    return [np.sqrt(1 - w) * x + np.sqrt(w) * e for x in t]


def overlap2(g):
    g = [x / np.linalg.norm(x) for x in g]
    return abs(np.vdot(g[0], g[1])) ** 2


def bargmann(g):
    g = [x / np.linalg.norm(x) for x in g]
    return abs(np.angle(np.vdot(g[0], g[1]) * np.vdot(g[1], g[2]) * np.vdot(g[2], g[0])))


def gram_det(g):
    g = [x / np.linalg.norm(x) for x in g]
    return np.linalg.det(np.array([[np.vdot(a, b) for b in g] for a in g])).real


def solve(tree, mechanism=None, target_overlap=0.5, grid=20001):
    """Alle psi mit |<g_j|g_k>|^2 = target_overlap; w = mechanism(knotengewichte des Triplettanteils) oder 0."""
    def w_of(psi):
        if mechanism is None:
            return 0.0
        return mechanism(tree.node_weights(triplet_part(tree, cone(psi, tree.axis)[0])))

    def h(psi):
        w = w_of(psi)
        if not (0 <= w <= 1):
            return np.nan
        return overlap2(generation_states(tree, psi, w)) - target_overlap
    xs = np.linspace(1e-4, np.pi - 1e-4, grid); vs = np.array([h(x) for x in xs]); out = []
    for i in range(len(xs) - 1):
        a, b = vs[i], vs[i + 1]
        if np.isfinite(a) and np.isfinite(b) and np.sign(a) != np.sign(b):
            lo, hi = xs[i], xs[i + 1]
            for _ in range(80):
                mid = (lo + hi) / 2
                if np.sign(h(mid)) == np.sign(h(lo)): lo = mid
                else: hi = mid
            psi = (lo + hi) / 2; w = w_of(psi); g = generation_states(tree, psi, w)
            out.append({"psi_deg": np.degrees(psi), "w": w, "overlap2": overlap2(g), "phase": bargmann(g), "detG": gram_det(g)})
    return out


# ---------------------------------------------------------------- Aufzaehlung der Mechanismen einer Aufteilung
def enumerate_relations(tree, include_unnormalised=True):
    """Alle Beziehungen 'Gewicht von Knoten A' und 'Gewicht von A normiert in einem Vorfahren B' (A echte Teilmenge von B).
    Die Zahl der Eintraege ist die Versuchszahl einer Familie, die alle diese Beziehungen zulaesst (Look-elsewhere)."""
    names = list(tree.nodes)
    rel = []
    for a in names:
        A = set(tree.nodes[a])
        if include_unnormalised and len(A) < len(tree.boxes):
            rel.append((a, None))
        for b in names:
            B = set(tree.nodes[b])
            if A < B and len(B) < len(tree.boxes):
                rel.append((a, b))
    return rel


def relation_function(a, b=None):
    if b is None:
        return lambda W: W[a]
    return lambda W: W[a] / W[b] if W[b] > 0 else np.nan


# ---------------------------------------------------------------- Selbstpruefung an bekannten Ergebnissen
def selftest():
    print("Selbstpruefung an bekannten Ergebnissen (keine neue Rechnung):")
    t7 = ShiftTree(7)
    r = solve(t7)
    print(f"  HS(7), Spin 1/2, Ueberlappung 1/2: Phase {r[0]['phase']:.6f} (pi/4 = {np.pi/4:.6f}), det G {r[0]['detG']:.1e}  [r25.2]")
    t8 = ShiftTree(8)
    print("  Knoten von HS(8):", t8.describe())
    r = solve(t8)
    print(f"  HS(8), Spin 1 (M0): Phase {r[0]['phase']:.6f} (0.679042), det G {r[0]['detG']:.6f} (0.050253)  [r15.3, r25.3]")
    W = t8.node_weights(triplet_part(t8, cone(np.radians(r[0]['psi_deg']))[0]))
    print(f"  Kastengewichte: 00 {W['HS(6)[00]']:.4f}, 01 {W['HS(6)[01]']:.4f}, 10 {W['HS(6)[10]']:.4f}, 11 {W['HS(6)[11]']:.4f}"
          f"  (0.7927 / 0.0976 / 0.0976 / 0.0120)  [r25.5]")
    r = solve(t8, mechanism=lambda W: 0.25)
    print(f"  HS(8), Singulettgewicht 1/4 (M1): Phase {r[0]['phase']:.6f} (0.640384)  [H106]")
    print(f"  Beziehungen in HS(8) (Gewicht, Gewicht normiert in Vorfahre): {len(enumerate_relations(t8))}")
    print(f"  Beziehungen in HS(9): {len(enumerate_relations(ShiftTree(9)))}")


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--describe", type=int, metavar="STUFE", help="Knoten einer Stufe ausgeben")
    args = ap.parse_args()
    if args.selftest:
        selftest()
    elif args.describe:
        for name, members in ShiftTree(args.describe).describe().items():
            print(f"{name:14s} {members}")
    else:
        ap.print_help()
