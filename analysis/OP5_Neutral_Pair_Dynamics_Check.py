"""Exact symbolic controls for the conditional neutral-pair dynamics note."""

import json
import sympy as s

I = s.I
eye = s.eye(2)
sx = s.Matrix([[0, 1], [1, 0]])
sy = s.Matrix([[0, -I], [I, 0]])
sz = s.diag(1, -1)
bx, by, bz = s.symbols("bx by bz", real=True)
k, t, tau = s.symbols("k t tau", positive=True)
theta = s.symbols("theta", real=True)


def zero(matrix):
    return all(s.simplify(s.trigsimp(x)) == 0 for x in matrix)


rho = (eye + bx * sx + by * sy + bz * sz) / 2
opposite = sy * rho * sy
assert zero(opposite - (eye - bx * sx + by * sy - bz * sz) / 2)
generator = k * (opposite - rho)
assert zero(generator + k * (bx * sx + bz * sz))


def channel(matrix, duration):
    p = (1 - s.exp(-2 * k * duration)) / 2
    return (1 - p) * matrix + p * sy * matrix * sy


solution = (eye + s.exp(-2*k*t) * (bx*sx + bz*sz) + by*sy) / 2
assert zero(channel(rho, t) - solution)
assert zero(s.diff(solution, t) - k * (sy * solution * sy - solution))
assert zero(channel(channel(rho, t), tau) - channel(rho, t+tau))
assert zero(channel((eye+by*sy)/2, t) - (eye+by*sy)/2)

# System-first ordering; trace over the second qubit after joint evolution.
coupling = s.kronecker_product(sy, sx)
W = s.cos(theta) * s.eye(4) - I * s.sin(theta) * coupling
assert zero(W.H * W - s.eye(4))
joint = s.kronecker_product(rho, s.diag(1, 0))
out = W * joint * W.H
reduced = s.Matrix(2, 2, lambda i, j: sum(out[2*i+a, 2*j+a] for a in range(2)))
expected = s.cos(theta)**2 * rho + s.sin(theta)**2 * opposite
assert zero(reduced - expected)
assert zero(reduced.subs({theta:s.pi/4, by:0}) - eye/2)
assert zero(reduced.subs(theta,s.pi) - rho)  # closed ancilla revival
assert zero(reduced.subs(theta,s.pi/2) - opposite)

E0, hx, hy, hz, C = s.symbols("E0 hx hy hz C", real=True)
H = E0*eye + hx*sx + hy*sy + hz*sz
energy_derivative = s.simplify(s.trace(H*generator))
assert s.simplify(energy_derivative + 2*k*(hx*bx+hz*bz)) == 0
assert s.simplify(s.trace((H+C*eye)*generator)-energy_derivative) == 0
assert s.simplify(s.trace(rho*(H+C*eye))-s.trace(rho*H)-C) == 0

a, b = s.symbols("a b", positive=True)
psteady = b/(a+b)
assert s.simplify(-a*psteady+b*(1-psteady)) == 0
assert s.simplify(2*psteady-1-(b-a)/(a+b)) == 0

# r27: rotation about y, then compensator x projection; not radial in general.
alpha = s.symbols("alpha", real=True)
rot = s.cos(alpha)*eye-I*s.sin(alpha)*sy
Cport, Aport = (eye+sx)/2, (eye-sx)/2
rotated = rot*rho*rot.H
r27 = Cport*rotated*Cport+Aport*rotated*Aport
assert zero(r27-(eye+(bx*s.cos(2*alpha)+bz*s.sin(2*alpha))*sx)/2)
assert zero(r27.subs({bx:0, by:0, bz:1, alpha:0})-eye/2)
# Radius factor cos(2 theta); score is its square, not selective survival.
assert s.simplify(s.cos(2*s.pi/6)**2-s.Rational(1,4)) == 0
assert s.simplify(s.cos(2*s.pi/12)**2-s.Rational(3,4)) == 0

print(json.dumps({
    "status":"all exact symbolic controls passed",
    "markov_disk_decay":"exp(-2*k*t)",
    "full_ball_stationary_axis":"sigma_y",
    "ancilla_disk_neutral_angle":"pi/4",
    "closed_ancilla_revival_angle":"pi",
    "unequal_rate_stationary_imbalance":"(b-a)/(a+b)",
    "energy_derivative":str(energy_derivative),
    "r27_is_general_radial_channel":False,
    "absolute_energy_offset_determined":False,
    "physical_lambda_derived":False,
}, indent=2))
