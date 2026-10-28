"""Exact finite qubit instrument controls; no native field dynamics claim."""
import json
import sympy as s

I = s.I
one = s.eye(2)
sx = s.Matrix([[0, 1], [1, 0]])
sy = s.Matrix([[0, -I], [I, 0]])
sz = s.diag(1, -1)
bx, by, bz, phase = s.symbols("bx by bz phase", real=True)
rho = (one+bx*sx+by*sy+bz*sz)/2
rz = (one+sz)/2
n = (sx+sz)/s.sqrt(2)


def zero(x):
    return all(s.simplify(s.trigsimp(t)) == 0 for t in x)


def P(axis, sign=1):
    return (one+sign*axis)/2


def D(axis, state):
    return sum((P(axis,j)*state*P(axis,j) for j in (1,-1)),s.zeros(2))


assert zero(D(sx,D(sz,rho))-D(sz,D(sx,rho)))
assert zero(D(sx,D(sx,rho))-D(sx,rho))
after_x_n = D(n,D(sx,rz))
after_n_x = D(sx,D(n,rz))
assert zero(after_x_n-one/2)
assert zero(after_n_x-(one+sx/2)/2)
p_x_n = s.simplify(s.trace(P(sx)*after_x_n))
p_n_x = s.simplify(s.trace(P(sx)*after_n_x))
assert p_x_n == s.Rational(1,2)
assert p_n_x == s.Rational(3,4)
assert after_x_n.det() == s.Rational(1,4)
assert after_n_x.det() == s.Rational(3,16)

Ut = s.cos(phase/2)*one-I*s.sin(phase/2)*sy
delayed = Ut*rz*Ut.H
p_delay = s.trigsimp(s.trace(P(sx)*delayed))
assert s.trigsimp(p_delay-(1+s.sin(phase))/2) == 0
measured_first = Ut*D(sx,rz)*Ut.H
assert zero(measured_first-one/2)
assert zero(D(sx,Ut.subs(phase,s.pi)*rho*Ut.subs(phase,s.pi).H)
            -Ut.subs(phase,s.pi)*D(sx,rho)*Ut.subs(phase,s.pi).H)
assert zero(Ut.subs(phase,s.pi)*P(sx)*Ut.subs(phase,s.pi).H-P(sx,-1))

# Generic fixed passive basis rotation: compare the whole instrument.
C = (sx+sz)/s.sqrt(2)
H = sx
Hp, rp, xp, np = C*H*C.H, C*rz*C.H, C*sx*C.H, C*n*C.H
assert zero(D(xp,D(np,rp))-C*after_n_x*C.H)
assert s.simplify(s.trace(P(xp)*D(xp,D(np,rp)))-p_n_x) == 0
assert s.simplify(s.trace(Hp*rp)-s.trace(H*rz)) == 0
for a in (1,-1):
    for b in (1,-1):
        branch = P(sx,b)*P(n,a)*rz*P(n,a)*P(sx,b)
        branchp = P(xp,b)*P(np,a)*rp*P(np,a)*P(xp,b)
        assert zero(branchp-C*branch*C.H)
        assert s.simplify(s.trace(branchp)-s.trace(branch)) == 0

# Controlled meter, ancilla |0>, followed by partial trace gives D_x.
V = s.kronecker_product(P(sx),one)+s.kronecker_product(P(sx,-1),sx)
assert zero(V.H*V-s.eye(4))
joint = V*s.kronecker_product(rho,s.diag(1,0))*V.H
reduced = s.Matrix(2,2,lambda i,j:sum(joint[2*i+a,2*j+a] for a in range(2)))
assert zero(reduced-D(sx,rho))
# Native counterpart changes a real disk axis only by sign: same full meter.
assert zero(sy*n*sy+n)
assert zero(D(-n,rho)-D(n,rho))
assert zero(P(-n)-P(n,-1))

# Order-dependent system energy under the separately declared H=sigma_x.
assert s.simplify(s.trace(H*after_x_n)) == 0
assert s.simplify(s.trace(H*after_n_x)) == s.Rational(1,2)
# General energy change under D_x: by and bz are erased.
h0,hx,hy,hz=s.symbols("h0 hx hy hz",real=True)
Hg=h0*one+hx*sx+hy*sy+hz*sz
assert s.simplify(s.trace(Hg*(D(sx,rho)-rho))+hy*by+hz*bz) == 0

# A different Hamiltonian can leave the source's real disk.
Uz=(one-I*sz)/s.sqrt(2)
rx=(one+sx)/2
assert zero(Uz*rx*Uz.H-(one+sy)/2)

print(json.dumps({
    "status":"all exact finite controls passed",
    "input":"rho_z pure; native x axis; n=(x+z)/sqrt(2)",
    "final_same_compensator_probability_x_then_n":"1/2",
    "final_same_compensator_probability_n_then_x":"3/4",
    "delay_probability":"(1+sin(omega*t))/2",
    "same_or_orthogonal_nonselective_axis_controls":"commute",
    "pi_delay_nonselective_channels_commute_but_labels_swap":True,
    "fixed_passive_complete_instrument_covariant":True,
    "controlled_meter_partial_trace_equals_dephasing":True,
    "system_energy_H_sigma_x_x_then_n":"0",
    "system_energy_H_sigma_x_n_then_x":"1/2",
    "general_H_requires_full_bloch_ball":True,
    "native_op5_physical_protocol_derived":False,
},indent=2))
