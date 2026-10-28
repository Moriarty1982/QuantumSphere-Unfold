"""Finite controls for the separate OP5 neutral-frame note; no physical fit."""

from fractions import Fraction as Q
import json
import math


def mul(a, b):
    return [[sum(x * y for x, y in zip(row, col)) for col in zip(*b)] for row in a]


def transpose(a):
    return list(map(list, zip(*a)))


def rho(z, x):
    return [[(1 + z) / 2, x / 2], [x / 2, (1 - z) / 2]]


def average(a, b):
    return [[(x + y) / 2 for x, y in zip(ar, br)] for ar, br in zip(a, b)]


sx = [[Q(0), Q(1)], [Q(1), Q(0)]]
rotation = [[Q(0), Q(-1)], [Q(1), Q(0)]]  # same conjugation as sigma_y
state = rho(Q(3, 10), Q(2, 5))
jb_state = mul(mul(sx, state), sx)
tachyon_state = mul(mul(rotation, state), transpose(rotation))
assert jb_state == rho(Q(-3, 10), Q(2, 5))
assert average(state, jb_state) == rho(Q(0), Q(2, 5))
assert average(state, tachyon_state) == rho(Q(0), Q(0))
assert average(state, jb_state) != rho(Q(0), Q(0))

eta1, eta2, chi = 0.2, 1.0, -0.7
mid = (eta1 + eta2) / 2
assert abs((eta1 - mid) + (eta2 - mid)) < 1e-15
assert abs((eta1 + chi + eta2 + chi) / 2 - (mid + chi)) < 1e-15

# Exact noncommuting boosts, signature (-,+,+,+), active convention.
c, s = Q(5, 4), Q(3, 4)
bx = [[c, s, 0, 0], [s, c, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
by = [[c, 0, s, 0], [0, 1, 0, 0], [s, 0, c, 0], [0, 0, 0, 1]]
metric = [[-1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
assert mul(mul(transpose(bx), metric), bx) == metric
assert mul(mul(transpose(by), metric), by) == metric
assert mul(bx, by) != mul(by, bx)

eplus, eminus = Q(4), Q(1)
v_com = (eplus - eminus) / (eplus + eminus)
assert v_com == Q(3, 5)
gamma_com = Q(5, 4)
assert gamma_com * (1 - v_com) * eplus == Q(2)
assert gamma_com * (1 + v_com) * eminus == Q(2)

v_landau = Q(1, 3)
g2_landau = 1 / (1 - v_landau * v_landau)
epsplus_new = g2_landau * (1 - v_landau) ** 2 * eplus
epsminus_new = g2_landau * (1 + v_landau) ** 2 * eminus
assert epsplus_new == epsminus_new == Q(2)
# Using packet COM velocity instead would not remove local energy flux.
epsplus_com = gamma_com**2 * (1 - v_com) ** 2 * eplus
epsminus_com = gamma_com**2 * (1 + v_com) ** 2 * eminus
assert epsplus_com == Q(1) and epsminus_com == Q(4)

null_dust_neutral = [[4, 0, 0, 0], [0, 4, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
assert sum(metric[i][i] * null_dust_neutral[i][i] for i in range(4)) == 0

print(json.dumps({
    "status": "all finite controls passed",
    "jb_average_b": ["0", "2/5"],
    "native_tachyon_average_b": ["0", "0"],
    "midpoint": mid,
    "noncollinear_boosts_commute": False,
    "packet_com_velocity": str(v_com),
    "packet_com_rapidity": 0.5 * math.log(4),
    "local_landau_velocity": str(v_landau),
    "local_landau_rapidity": 0.25 * math.log(4),
    "landau_frame_energy_density": str(epsplus_new + epsminus_new),
    "neutral_null_dust_trace": 0,
    "physical_lambda_derived": False,
}, indent=2))
