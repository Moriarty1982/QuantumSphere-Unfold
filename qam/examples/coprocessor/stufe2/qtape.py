"""Quanten-Coprozessor, Baustufe 2 als Software-Referenz: Band mit Drehung, Messung im Lauf, Schleife, Rueckfuehrung.

Kein HDL und nicht exakt: Der Zustand ist eine Dichtematrix in Gleitkomma (im Bauplan: Ausfuehrung "nicht exakt").
Die Maschine liest ein Band (Textzeilen), rechnet ohne Zutun des Hosts bis zu einem Stopgrund und fuehrt ein Protokoll:
je ausgefuehrter Zelle, was sie getan hat und warum (welche Regel griff), dazu einen fortlaufenden SHA-512-Hash.

Zustand: eine Menge von Baendern k = 0, 1, 2, ... Band k traegt einen Spin j = k/2 (symmetrischer Zustand von k Qubits),
als Block rho_k der Groesse (k+1) x (k+1); die Summe der Spuren ist 1. Band 1 ist das einzelne Qubit (Dublett).

Zellen (eine je Zeile, '#' leitet Kommentar ein):
  QTAPE 2                    Kennung und Formatversion (erste Zeile)
  BUDGET n                   hoechste Zahl ausgefuehrter Zellen (Stopgrund step_limit)
  KMAX n                     hoechstes Band (Vorgabe 40)
  ALLOW op op ...            erlaubte Befehle; alles andere fuehrt zu reject
  INIT k b                   Start: Band k, Spin entlang x polarisiert mit Blochlaenge b (nur k = 1 erlaubt b < 1)
  SET reg = ausdruck         Register setzen; Ausdruck aus Registern, Zahlen, + - * / **, sqrt atan cos sin log
  READ reg groesse           Auslese in ein Register: b (mittlere Polarisation <S_x>/j), p<k> (Gewicht von Band k), kbar
  ROT ausdruck               Drehung um die y-Achse, Blochwinkel 2*alpha (Spin-Drehung um 2*alpha)
  HC                         HC nicht selektiv: Messung von S_x auf jedem Band, Ergebnis verworfen
  MEASURE bit                HC selektiv: S_x-Messung mit Zufall (SEED), Vorzeichen des Ergebnisses in ein Bit-Register
  SWAP ausdruck              Austausch mit frischem Band |+> der Staerke x (nur wenn alles Gewicht auf Band 1 liegt)
  ADD ausdruck               Bandwechsel nach oben/unten: mit Gewicht mu wird ein frisches Qubit |+> angekoppelt und der
                             Gesamtspin gemessen (nicht selektiv): k -> k+1 oder k-1 nach Clebsch-Gordan
  DROP ausdruck              mit Gewicht lambda verliert das Band ein Qubit (Teilspur): k -> k-1
  NOISE reg modus eps        Register reg um eps * Rauschwert aendern; modus: prime_gap, prime_mod<m>, random
  LOOP n ... END             Schleife (verschachtelbar)
  JUMP_IF bit d              springt um d Zellen, wenn das Bit-Register 1 ist
  HALT                       Ende
Stopgruende: halted, boundary, step_limit, guard, reject.  Status: continue, guard, reject (wie MMA).
"""
from __future__ import annotations
import ast, hashlib, json, math, operator
import numpy as np

# ---------------------------------------------------------------- Spin-Hilfen
def spin_ops(k):
    j = k / 2.0; m = np.arange(j, -j - 1, -1)
    sz = np.diag(m); sp = np.zeros((k + 1, k + 1))
    for i in range(1, k + 1): sp[i - 1, i] = math.sqrt(j * (j + 1) - m[i] * (m[i] + 1))
    return (sp + sp.T) / 2, (sp - sp.T) / 2j, sz

def cg_maps(k, q):
    """Koppelt Spin j = k/2 mit einem Qubit im Zustand q = (q_auf, q_ab). Liefert (U, D): rho -> U rho U^+ (Band k+1), D rho D^+ (Band k-1)."""
    j = k / 2.0; m = np.arange(j, -j - 1, -1)
    U = np.zeros((k + 2, k + 1), complex); D = np.zeros((max(k, 1), k + 1), complex)
    Mu = np.arange(j + 0.5, -j - 1.5, -1); Md = np.arange(j - 0.5, -j + 0.5 - 1, -1) if k >= 1 else np.array([])
    for a, mm in enumerate(m):
        for s, qs in ((0.5, q[0]), (-0.5, q[1])):
            M = mm + s
            iu = int(round(j + 0.5 - M)); cu = math.sqrt((j + 0.5 + (M if s > 0 else -M)) / (2 * j + 1)) if True else 0
            # <j+1/2, M | j m; 1/2 s> = sqrt((j + 1/2 +- M)/(2j+1))  (oberes Zeichen fuer s = +1/2)
            U[iu, a] += qs * cu
            if k >= 1 and abs(M) <= j - 0.5 + 1e-9:
                idn = int(round(j - 0.5 - M))
                # <j-1/2, M | j m; 1/2 s> = -+ sqrt((j + 1/2 -+ M)/(2j+1))
                cd = (-1 if s > 0 else 1) * math.sqrt((j + 0.5 - (M if s > 0 else -M)) / (2 * j + 1))
                D[idn, a] += qs * cd
    if k == 0: D = np.zeros((0, 1), complex)
    return U, D

def drop_maps(k):
    """Teilspur ueber ein Qubit eines symmetrischen k-Qubit-Zustands: Kraus-Operatoren Band k -> Band k-1."""
    j = k / 2.0; m = np.arange(j, -j - 1, -1); A = [np.zeros((k, k + 1)), np.zeros((k, k + 1))]
    for a, mm in enumerate(m):
        if j + mm > 0: A[0][int(round(j - 0.5 - (mm - 0.5))), a] = math.sqrt((j + mm) / (2 * j))
        if j - mm > 0: A[1][int(round(j - 0.5 - (mm + 0.5))), a] = math.sqrt((j - mm) / (2 * j))
    return A

# ---------------------------------------------------------------- Primzahl-Rauschen
class PrimeNoise:
    """Gibt die Primzahlen der Reihe nach aus (Sieb, deterministisch) und macht daraus kleine Stoerwerte."""
    def __init__(self, limit=2_000_000):
        s = np.ones(limit + 1, bool); s[:2] = False
        for i in range(2, int(limit ** 0.5) + 1):
            if s[i]: s[i * i::i] = False
        self.p = np.flatnonzero(s); self.n = 0
    def next(self, mode):
        p, q = int(self.p[self.n]), int(self.p[self.n + 1]); self.n += 1
        if mode == "prime_gap": v = (q - p) / math.log(q) - 1.0          # normierte Luecke, Mittel nahe 0
        elif mode.startswith("prime_mod"): mm = int(mode[9:]); v = (p % mm) / mm - 0.5
        else: raise ValueError(mode)
        return p, v

# ---------------------------------------------------------------- Ausdruecke
_OPS = {ast.Add: operator.add, ast.Sub: operator.sub, ast.Mult: operator.mul, ast.Div: operator.truediv, ast.Pow: operator.pow, ast.USub: operator.neg}
_FN = {"sqrt": math.sqrt, "atan": math.atan, "cos": math.cos, "sin": math.sin, "log": math.log, "min": min, "max": max, "pi": math.pi}
def evaluate(expr, reg):
    def ev(n):
        if isinstance(n, ast.Constant) and isinstance(n.value, (int, float)): return float(n.value)
        if isinstance(n, ast.Name):
            if n.id in reg: return reg[n.id]
            if n.id == "pi": return math.pi
            raise KeyError(n.id)
        if isinstance(n, ast.BinOp): return _OPS[type(n.op)](ev(n.left), ev(n.right))
        if isinstance(n, ast.UnaryOp): return _OPS[type(n.op)](ev(n.operand))
        if isinstance(n, ast.Call) and isinstance(n.func, ast.Name) and n.func.id in _FN: return _FN[n.func.id](*[ev(a) for a in n.args])
        raise ValueError("Ausdruck nicht erlaubt")
    return ev(ast.parse(expr.strip(), mode="eval").body)

# ---------------------------------------------------------------- Maschine
class QTape:
    OPS = {"INIT", "SET", "READ", "ROT", "HC", "MEASURE", "SWAP", "ADD", "DROP", "NOISE", "LOOP", "END", "JUMP_IF", "HALT"}
    def __init__(self, text, seed=1, trace_every=1):
        self.cells = [l.split("#")[0].strip() for l in text.strip().splitlines()]; self.cells = [c for c in self.cells if c]
        self.budget, self.kmax, self.allow = 100000, 40, set(self.OPS)
        self.reg, self.bands, self.trace, self.loops = {}, {}, [], []
        self.status, self.stop, self.steps, self.head = "continue", None, 0, 0
        self.hash = hashlib.sha512(); self.rng = np.random.default_rng(seed); self.seed = seed; self.primes = None; self.trace_every = trace_every
        self._cache = {}
    # -- Hilfen
    def weights(self): return {k: float(np.real(np.trace(r))) for k, r in self.bands.items()}
    def pol(self):
        tot = 0.0
        for k, r in self.bands.items():
            if k >= 1: tot += float(np.real(np.trace(r @ spin_ops(k)[0]))) / (k / 2.0)
        return tot
    def _log(self, cell, did, why):
        self.hash.update((cell + "\n").encode())
        if self.trace_every and (self.steps % self.trace_every == 0 or cell.split()[0] in ("HALT", "INIT")):
            w = self.weights()
            self.trace.append({"schritt": self.steps, "kopf": self.head, "zelle": cell, "getan": did, "warum": why,
                               "b": round(self.pol(), 12), "baender": {str(k): round(v, 10) for k, v in sorted(w.items()) if v > 1e-10}, "hash": self.hash.hexdigest()[:16]})
    def _stop(self, reason, status=None):
        self.stop = reason
        if status: self.status = status
    def _put(self, new, k, r):
        if r.size and abs(np.trace(r)) > 1e-300: new[k] = new.get(k, 0) + r
    # -- Lauf
    def run(self):
        c0 = self.cells[0].split()
        if c0[:1] != ["QTAPE"] or c0[1:2] != ["2"]: self._stop("reject", "reject"); self.trace.append({"zelle": self.cells[0], "getan": "nichts", "warum": "Kennung QTAPE 2 fehlt: reject, es wird nichts gerechnet"}); return self
        self.head = 1
        while self.stop is None:
            if self.head >= len(self.cells): self._stop("boundary"); break
            if self.steps >= self.budget: self._stop("step_limit"); break
            cell = self.cells[self.head]; t = cell.split(); op = t[0]; self.steps += 1; nxt = self.head + 1
            try:
                if op == "BUDGET": self.budget = int(t[1]); did, why = f"Budget {self.budget}", "Kopfzeile: Obergrenze fuer ausgefuehrte Zellen"
                elif op == "KMAX": self.kmax = int(t[1]); did, why = f"hoechstes Band {self.kmax}", "Kopfzeile: Speichergrenze"
                elif op == "ALLOW": self.allow = set(t[1:]); did, why = "Opcode-Maske gesetzt", "Kopfzeile: nur diese Befehle sind erlaubt, alle anderen fuehren zu reject"
                elif op not in self.OPS or op not in self.allow:
                    self._log(cell, "nichts", "Befehl unbekannt oder nicht in ALLOW: reject"); self._stop("reject", "reject"); break
                elif op == "INIT":
                    k = int(t[1]); b = evaluate(" ".join(t[2:]), self.reg); sx = spin_ops(k)[0]
                    if k == 1: r = 0.5 * (np.eye(2) + b * 2 * sx)
                    else:
                        w, v = np.linalg.eigh(sx); r = np.outer(v[:, -1], v[:, -1].conj())
                    self.bands = {k: r.astype(complex)}; did, why = f"Start auf Band {k}, Polarisation {b:.6g} entlang x", "Startzustand (Ur-Seed) laden"
                elif op == "SET":
                    name, expr = cell[3:].split("=", 1); name = name.strip(); val = evaluate(expr, self.reg); self.reg[name] = val
                    did, why = f"{name} = {val:.12g}", f"Rueckfuehrung: {name} wird aus den Registern berechnet ({expr.strip()})"
                elif op == "READ":
                    name, what = t[1], t[2]
                    if what == "b": val = self.pol()
                    elif what == "kbar": val = sum(k * w for k, w in self.weights().items())
                    elif what.startswith("p"): val = self.weights().get(int(what[1:]), 0.0)
                    else: raise ValueError(what)
                    self.reg[name] = val; did, why = f"{name} = {val:.12g}", f"Auslese ({what}) in ein Register; steht der naechsten Runde zur Verfuegung"
                elif op == "ROT":
                    al = evaluate(" ".join(t[1:]), self.reg); new = {}
                    for k, r in self.bands.items():
                        if k == 0: new[0] = r; continue
                        sy = spin_ops(k)[1]; w, v = np.linalg.eigh(sy); u = (v * np.exp(-1j * 2 * al * w)) @ v.conj().T; new[k] = u @ r @ u.conj().T
                    self.bands = new; did, why = f"Drehung um alpha = {al:.10g} (Blochwinkel {2 * al:.10g})", "Drehbefehl: mischt Amplituden (fehlte der Bandmaschine laut H137)"
                elif op == "HC":
                    new = {}
                    for k, r in self.bands.items():
                        if k == 0: new[0] = r; continue
                        w, v = np.linalg.eigh(spin_ops(k)[0]); rr = v.conj().T @ r @ v; new[k] = v @ np.diag(np.diag(rr)) @ v.conj().T
                    self.bands = new; did, why = "S_x gemessen, Ergebnis verworfen", "HC nicht selektiv: loescht alles quer zur HC-Achse (r70.2)"
                elif op == "MEASURE":
                    ks = sorted(self.bands); pw = np.array([max(self.weights()[k], 0) for k in ks]); k = ks[self.rng.choice(len(ks), p=pw / pw.sum())]
                    r = self.bands[k] / np.trace(self.bands[k])
                    if k == 0: m = 0.0; self.bands = {0: r}
                    else:
                        w, v = np.linalg.eigh(spin_ops(k)[0]); pr = np.clip(np.real(np.einsum("ia,ij,ja->a", v.conj(), r, v)), 0, None); a = self.rng.choice(len(w), p=pr / pr.sum())
                        m = w[a]; self.bands = {k: np.outer(v[:, a], v[:, a].conj())}
                    self.reg[t[1]] = 1.0 if m > 0 else 0.0; did, why = f"Band {k}, Ergebnis m = {m:+.1f}, Bit {t[1]} = {int(m > 0)}", f"HC selektiv: Projektion mit Zufall (SEED {self.seed}); das Bit steht fuer JUMP_IF bereit"
                elif op == "SWAP":
                    x = evaluate(" ".join(t[1:]), self.reg); w = self.weights()
                    if not (0 <= x <= 1) or abs(w.get(1, 0) - 1) > 1e-9: self._log(cell, "nichts", "SWAP verlangt 0 <= x <= 1 und alles Gewicht auf Band 1: guard"); self._stop("guard", "guard"); break
                    plus = 0.5 * np.ones((2, 2), complex); r = self.bands[1]; c, s = math.sqrt(1 - x), math.sqrt(x)
                    self.bands = {1: (1 - x) * r + x * plus + 1j * c * s * (plus @ r - r @ plus)}
                    did, why = f"Austausch mit frischem Band |+>, Staerke x = {x:.10g}", "Teil-SWAP: ein Anteil x des Zustands wird durch das Bezugsband ersetzt"
                elif op == "ADD":
                    mu = evaluate(" ".join(t[1:]), self.reg); new = {}; q = (1 / math.sqrt(2), 1 / math.sqrt(2))
                    for k, r in self.bands.items():
                        self._put(new, k, (1 - mu) * r)
                        if k + 1 > self.kmax:
                            if abs(np.trace(r)) < 1e-10: self._put(new, k, mu * r); continue     # verschwindendes Gewicht am Rand bleibt liegen
                            self._log(cell, "nichts", f"Band {k + 1} ueber KMAX: guard"); self._stop("guard", "guard"); break
                        U, D = self._cache.setdefault(("cg", k), cg_maps(k, q)); self._put(new, k + 1, mu * U @ r @ U.conj().T)
                        if k >= 1: self._put(new, k - 1, mu * D @ r @ D.conj().T)
                    if self.stop: break
                    self.bands = new; did, why = f"Qubit |+> angekoppelt mit Gewicht {mu:.6g}, Gesamtspin gemessen", "Bandwechsel: Clebsch-Gordan verbindet Band k mit k+1 und k-1"
                elif op == "DROP":
                    lam = evaluate(" ".join(t[1:]), self.reg); new = {}
                    for k, r in self.bands.items():
                        if k == 0: self._put(new, 0, r); continue
                        self._put(new, k, (1 - lam) * r); A = self._cache.setdefault(("dr", k), drop_maps(k)); self._put(new, k - 1, lam * sum(a @ r @ a.T for a in A))
                    self.bands = new; did, why = f"ein Qubit abgegeben mit Gewicht {lam:.6g}", "Bandwechsel nach unten (Teilspur): k -> k-1"
                elif op == "NOISE":
                    name, mode, eps = t[1], t[2], evaluate(" ".join(t[3:]), self.reg)
                    if mode == "random": v = float(self.rng.standard_normal()); src = f"Zufallszahl (SEED {self.seed})"
                    else:
                        if self.primes is None: self.primes = PrimeNoise()
                        p, v = self.primes.next(mode); src = f"Primzahl Nr. {self.primes.n}: {p}"
                    self.reg[name] = self.reg.get(name, 0.0) + eps * v; did, why = f"{name} += {eps:.4g} * {v:+.6f} = {self.reg[name]:.10g}", f"Rauschen aus {src}, Modus {mode}"
                elif op == "LOOP":
                    self.loops.append([self.head, int(evaluate(" ".join(t[1:]), self.reg)), 1]); did, why = f"Schleife mit {self.loops[-1][1]} Runden beginnt", "Rolle Loop aus 19Q"
                elif op == "END":
                    start, n, i = self.loops[-1]
                    if i < n: self.loops[-1][2] += 1; nxt = start + 1; did, why = f"zurueck zum Schleifenanfang (Runde {i + 1} von {n})", "Runde beendet, Zaehler noch nicht erreicht"
                    else: self.loops.pop(); did, why = f"Schleife nach {n} Runden verlassen", "Zaehler erreicht (Rolle Return aus 19Q)"
                elif op == "JUMP_IF":
                    d = int(t[2])
                    if self.reg.get(t[1], 0.0) == 1.0: nxt = self.head + d; did, why = f"Sprung um {d:+d}", f"Bit {t[1]} ist 1 (Rolle Branch aus 19P)"
                    else: did, why = "kein Sprung", f"Bit {t[1]} ist 0"
                elif op == "HALT":
                    self._log(cell, "angehalten", "HALT gelesen"); self._stop("halted"); break
            except Exception as e:
                self._log(cell, "nichts", f"Fehler beim Ausfuehren ({type(e).__name__}: {e}): guard"); self._stop("guard", "guard"); break
            tr = sum(self.weights().values()) if self.bands else 1.0
            if abs(tr - 1) > 1e-8: self._log(cell, did, why + f"; Spur {tr:.12f} weicht von 1 ab: guard"); self._stop("guard", "guard"); break
            self._log(cell, did, why); self.head = nxt
        return self
    def result(self):
        return {"status": self.status, "stopgrund": self.stop, "schritte": self.steps, "kopf": self.head, "register": self.reg, "baender": self.weights(), "b": self.pol(), "hash": self.hash.hexdigest()}
    def write_trace(self, path):
        with open(path, "w") as f:
            for row in self.trace: f.write(json.dumps(row, ensure_ascii=False) + "\n")
