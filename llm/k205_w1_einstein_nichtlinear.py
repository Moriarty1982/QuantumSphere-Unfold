"""k205: H90 - volle nichtlineare Einstein-Gleichung von W1, Bianchi-Vertraeglichkeit, Vorzeichen der Gravitationswirkung.

Vorab-Notiz llm/Vorab_Notiz_H90_W1_Einstein_nichtlinear.md (Commit e5d03d8).
Methode: Jets (abgeschnittene Taylor-Polynome bis Grad ORD in x^0..x^3) an einem allgemeinen Punkt eines
gekruemmten Hintergrunds. Konventionen wie k203/k204:
  eta = diag(1,-1,-1,-1), sigmabar^a = (1,-sigma_i), Sigma^{ab} = 1/4 (sigma^a sigmabar^b - sigma^b sigmabar^a),
  D_mu psi = d_mu psi + 1/2 omega_{mu ab} Sigma^{ab} psi + i q J A_mu psi,
  R_{mu nu}^{ab} = d_mu omega_nu^{ab} - d_nu omega_mu^{ab} + omega_mu^a_c omega_nu^{cb} - omega_nu^a_c omega_mu^{cb},
  S_grav = (sigma_g / 2 kappa) int e R ; W1 wie notiert: sigma_g = +1.
Aufruf: python llm/k205_w1_einstein_nichtlinear.py [ausgabe.json]
"""
import numpy as np, itertools, json, sys

ORD = 3
mon = [a for dg in range(ORD + 1) for a in itertools.product(range(dg + 1), repeat=4) if sum(a) == dg]
idx = {m: i for i, m in enumerate(mon)}
NJ = len(mon)
P = np.zeros((NJ, NJ, NJ))
for i, a in enumerate(mon):
    for j, b in enumerate(mon):
        c = tuple(x + y for x, y in zip(a, b))
        if sum(c) <= ORD:
            P[i, j, idx[c]] = 1
Dm = np.zeros((4, NJ, NJ))
for i, a in enumerate(mon):
    for r in range(4):
        if a[r] > 0:
            c = list(a); c[r] -= 1
            Dm[r, idx[tuple(c)], i] = a[r]
I1 = [idx[tuple(int(i == m) for i in range(4))] for m in range(4)]
I2 = [i for i, a in enumerate(mon) if sum(a) == 2]


def J(spec, *ops):
    """Jet-Produkt nach einsum-Spezifikation (Kleinbuchstaben = Tensorindizes; Jet-Achse implizit zuletzt)."""
    ins, out = spec.split('->'); ins = ins.split(',')
    res, cur = ops[0], ins[0]
    for k in range(1, len(ops)):
        later = set(''.join(ins[k + 1:])) | set(out)
        keep = ''.join(dict.fromkeys(c for c in cur + ins[k] if c in later))
        res = np.einsum(f'{cur}X,{ins[k]}Y,XYZ->{keep}Z', res, ops[k], P, optimize=True)
        cur = keep
    return np.einsum(f'{cur}Z->{out}Z', res)


def lift(c):
    c = np.asarray(c); a = np.zeros(c.shape + (NJ,), dtype=complex); a[..., 0] = c; return a


def d(f):
    """d(f)[r, ...] = d_r f (Ordnung um 1 kleiner gueltig)."""
    return np.einsum('rki,...i->r...k', Dm, f)


def val(f):
    return f[..., 0]


eta = np.diag([1., -1, -1, -1]); et = np.diag(eta)
s0 = np.eye(2); sx = np.array([[0, 1], [1, 0]]); sy = np.array([[0, -1j], [1j, 0]]); sz = np.diag([1., -1])
sig = np.array([s0, sx, sy, sz], dtype=complex); sbar = np.array([s0, -sx, -sy, -sz], dtype=complex)
Sig = np.array([[0.25 * (sig[a] @ sbar[b] - sig[b] @ sbar[a]) for b in range(4)] for a in range(4)])
eps = np.zeros((4, 4, 4, 4))
for p in itertools.permutations(range(4)):
    eps[p] = np.linalg.det(np.eye(4)[list(p)])          # eps_{0123} = +1 (untere Indizes)
ETA, SBAR, SIG, EPS = lift(eta), lift(sbar), lift(Sig), lift(eps)


def jinv_mat(e):
    e0 = val(e); i0 = np.linalg.inv(e0); n = e - lift(e0)
    m = J('ij,jk->ik', lift(i0), n); s = lift(np.eye(4)); pw = lift(np.eye(4))
    for k in range(1, ORD + 1):
        pw = J('ij,jk->ik', pw, m); s = s + (-1) ** k * pw
    return J('ij,jk->ik', s, lift(i0))


def jdet(e):
    e0 = val(e); i0 = np.linalg.inv(e0); m = J('ij,jk->ik', lift(i0), e - lift(e0))
    lg = np.zeros(NJ, complex); pw = lift(np.eye(4))
    for k in range(1, ORD + 1):
        pw = J('ij,jk->ik', pw, m); lg = lg + (-1) ** (k + 1) / k * np.einsum('iiZ->Z', pw)
    ex = lift(1.0); t = lift(1.0)
    for k in range(1, ORD + 1):
        t = J(',->', t, lg) / k; ex = ex + t
    return np.linalg.det(e0) * ex


def geometry(e):
    E = jinv_mat(e)                                     # E[mu,a] = E^mu_a
    g = J('am,ab,bn->mn', e, ETA, e)
    gi = J('ma,ab,nb->mn', E, ETA, E)
    dg = d(g)                                           # dg[r,m,n]
    X = np.einsum('msn...->smn...', dg) + np.einsum('nsm...->smn...', dg) - dg
    Gam = 0.5 * J('ls,smn->lmn', gi, X)                 # Gam[l,m,n] = Gamma^l_{mn}
    elow = J('bc,cn->bn', ETA, e)
    nab = np.einsum('mbn...->mbn...', d(elow)) - J('lmn,bl->mbn', Gam, elow)
    om = J('na,mbn->mab', E, nab)                       # omega_{mu a b}
    dG = d(Gam)                                         # dG[m,r,n,s] = d_m Gamma^r_{ns}
    Rc = (np.einsum('mrns...->rsmn...', dG) - np.einsum('nrms...->rsmn...', dG)
          + J('rml,lns->rsmn', Gam, Gam) - J('rnl,lms->rsmn', Gam, Gam))
    Ric = np.einsum('msmn...->sn...', Rc)
    Rs = J('sn,sn->', gi, Ric)
    G = Ric - 0.5 * J('mn,->mn', g, Rs)
    return dict(e=e, E=E, g=g, gi=gi, Gam=Gam, om=om, G=G, Rs=Rs, det=jdet(e))


def frame_curv(om_v, dom_v):
    """Werte: R_{mu nu}^{ab} aus omega_{mu ab} und d_r omega_{mu ab}."""
    up = np.einsum('mab,a,b->mab', om_v, et, et); mix = np.einsum('mab,a->mab', om_v, et)
    dup = np.einsum('rmab,a,b->rmab', dom_v, et, et)
    return (dup - np.einsum('rmab->mrab', dup) + np.einsum('mac,ncb->mnab', mix, up)
            - np.einsum('nac,mcb->mnab', mix, up))


def Dpsi(psi, om, A, Jc, q):
    Om = 0.5 * J('mab,abuv->muv', om, SIG)
    return d(psi) + J('muv,v->mu', Om, psi) + 1j * q * Jc * J('m,u->mu', A, psi)


def current(psis, w=None):
    w = np.ones(len(psis)) if w is None else w
    return sum(wk * J('u,auv,v->a', np.conj(p), SBAR, p) for wk, p in zip(w, psis))


def weyl_eom(psis, s, geo, om, A, Jc, q, lam):
    p = psis[s]; Dp = Dpsi(p, om, A, Jc[s], q)
    jl = J('ab,b->a', ETA, current(psis))
    return 1j * J('auv,ma,mv->u', SBAR, geo['E'], Dp) + 2 * lam * J('a,auv,v->u', jl, SBAR, p)


def affine_project(f, x_rand):
    """f affin in x (komplex-linear oder reell): kleinste Korrektur von x_rand auf f = 0."""
    x0 = np.zeros_like(x_rand); b = f(x0)
    M = np.array([f(np.eye(len(x_rand), dtype=x_rand.dtype)[k]) - b for k in range(len(x_rand))]).T
    x = x_rand - np.linalg.pinv(M) @ (M @ x_rand + b)
    return x, np.max(np.abs(f(x))), np.linalg.matrix_rank(M)


def run(seed, sg, kap=1.3, q=0.7, onshell=True, scale=0.25):
    rng = np.random.default_rng(seed)
    Jc = np.array([1., -1., 1.]); out = {}
    # Hintergrund: Vierbein als zufaelliges Polynom vom Grad ORD
    e = np.zeros((4, 4, NJ), complex); e[..., 0] = np.eye(4) + scale * rng.standard_normal((4, 4))
    e[..., 1:] = scale * rng.standard_normal((4, 4, NJ - 1))
    geo = geometry(e); E0, g0, det0 = val(geo['E']).real, val(geo['g']).real, val(geo['det']).real
    om = geo['om']; om_v = val(om); dom_v = val(d(om))
    # Kontrollen der Geometrie
    out['omega_antisym'] = float(np.max(np.abs(om[..., :NJ] + np.einsum('mab...->mba...', om))[..., :1 + 4]))
    tors = (np.einsum('man...->amn...', d(e)) - np.einsum('nam...->amn...', d(e))
            + J('mab,bn->amn', om * et[None, :, None, None], e) - J('nab,bm->amn', om * et[None, :, None, None], e))
    out['torsion_free'] = float(np.max(np.abs(val(tors))))
    Rf = frame_curv(om_v, dom_v)
    out['R_omega_minus_R_Christoffel'] = float(abs(np.einsum('ma,nb,mnab', E0, E0, Rf) - val(geo['Rs'])))
    # Felder: A reell, drei Weyl-Spinoren
    A = np.zeros((4, NJ), complex); A[...] = scale * rng.standard_normal((4, NJ))
    psis = []
    for s in range(3):
        p = np.zeros((2, NJ), complex)
        p[...] = scale * (rng.standard_normal((2, NJ)) + 1j * rng.standard_normal((2, NJ)))
        p[:, 0] = rng.standard_normal(2) + 1j * rng.standard_normal(2)
        psis.append(p)
    psi0 = [p[:, 0] for p in psis]

    # --- H90a(i): Cartan-Gleichung am Punkt ---------------------------------------------
    def Lval(omv, domv, psil):
        Rs = np.einsum('ma,nb,mnab', E0, E0, frame_curv(omv, domv))
        LW = 0.0
        for s, p in enumerate(psil):
            dp = p[:, I1].T                                    # [mu, alpha]
            Dp = dp + 0.5 * np.einsum('mab,abuv,v->mu', omv, Sig, p[:, 0]) + 1j * q * Jc[s] * np.outer(val(A), p[:, 0])
            LW += np.real(np.conj(p[:, 0]) @ (1j * np.einsum('auv,ma,mv->u', sbar, E0, Dp)))
        return det0 * (sg / (2 * kap) * Rs + LW)
    C = J('ac,bd->abcd', geo['E'], geo['E'])                  # C[al,be,c,d] = E^al_c E^be_d
    Pj = (C - np.einsum('nmab...->nmba...', C) - np.einsum('nmab...->mnab...', C) + np.einsum('nmab...->mnba...', C))
    Pj = sg / (2 * kap) * J('nmab,->nmab', Pj, geo['det']) * np.einsum('a,b->ab', et, et)[None, None, :, :, None]
    divP = np.einsum('nnmab->mab', val(d(Pj)))
    pairs = [(a, b) for a in range(4) for b in range(a + 1, 4)]

    def EL(omv, psil):
        r = []
        for m in range(4):
            for (a, b) in pairs:
                dl = np.zeros((4, 4, 4)); dl[m, a, b] = 1; dl[m, b, a] = -1
                r.append((Lval(omv + dl, dom_v, psil) - Lval(omv - dl, dom_v, psil)) / 2 - divP[m, a, b].real)
        return np.array(r)
    zero = [np.zeros_like(p) for p in psis]
    out['cartan_vacuum_residual'] = float(np.max(np.abs(EL(om_v, zero))))
    out['cartan_vacuum_scale'] = float(np.max(np.abs(divP)))

    def Kfull(kv):
        K = np.zeros((4, 4, 4))
        for n, (m, (a, b)) in enumerate([(m, ab) for m in range(4) for ab in pairs]):
            K[m, a, b] = kv[n]; K[m, b, a] = -kv[n]
        return K
    kv, res, rk = affine_project(lambda kv: EL(om_v + Kfull(kv), psis), np.zeros(24))
    K_coord = Kfull(kv); Kf = np.einsum('mc,mab->cab', E0, K_coord)    # K_{cab}, Frame
    jv = val(current(psis)).real; jl = et * jv
    X = kap * np.einsum('cabd,d->cab', eps, jv)
    cK = float(np.sum(Kf * X) / np.sum(X * X))
    out.update(cartan_residual=float(res), cartan_rank=int(rk), K_c=cK,
               K_fit_rel=float(np.linalg.norm(Kf - cK * X) / np.linalg.norm(Kf)),
               K_totally_antisym=float(np.max(np.abs(Kf + np.einsum('cab->acb', Kf)))))
    # --- H90a(iii): K-Term der EC-Weyl-Gleichung = 2 lam j.sigmabar psi -------------------
    v1 = np.concatenate([1j * np.einsum('auv,acd,cdvw,w->u', sbar, Kf, Sig, p) * 0.5 for p in psi0])
    v2 = np.concatenate([np.einsum('a,auv,v->u', jl, sbar, p) for p in psi0])
    lam = np.vdot(v2, v1) / (2 * np.vdot(v2, v2))
    out.update(lam_over_kappa=complex(lam / kap).real, lam_imag=float(abs(lam.imag)),
               lam_fit_rel=float(np.linalg.norm(v1 - 2 * lam * v2) / np.linalg.norm(v1)))
    lam = lam.real

    # --- Felder auf die Feldgleichungen legen -------------------------------------------
    if onshell:
        for s in range(3):
            def f1(x, s=s):
                ps = [p.copy() for p in psis]; ps[s][:, I1] = x.reshape(2, 4)
                return val(weyl_eom(ps, s, geo, om, A, Jc, q, lam))
            x, r1, _ = affine_project(f1, psis[s][:, I1].reshape(-1))
            psis[s][:, I1] = x.reshape(2, 4)
        out['weyl_order0'] = float(r1)
        for s in range(3):
            def f2(x, s=s):
                ps = [p.copy() for p in psis]; ps[s][:, I2] = x.reshape(2, len(I2))
                return weyl_eom(ps, s, geo, om, A, Jc, q, lam)[:, I1].reshape(-1)
            x, r2, _ = affine_project(f2, psis[s][:, I2].reshape(-1))
            psis[s][:, I2] = x.reshape(2, len(I2))
        out['weyl_order1'] = float(r2)

        def fM(x):
            Al = A.copy(); Al[:, I2] = x.reshape(4, len(I2))
            dA = d(Al); F = np.einsum('mn...->mn...', dA) - np.einsum('nm...->mn...', dA)
            Fu = J('ma,nb,ab->mn', geo['gi'], geo['gi'], F)
            div = np.einsum('mmn->n', val(d(J('mn,->mn', Fu, geo['det'])))) / det0
            jJ = E0 @ val(current(psis, Jc))
            return (div - q * jJ)
        x, rM, _ = affine_project(fM, A[:, I2].reshape(-1).real.astype(complex))
        A[:, I2] = x.real.reshape(4, len(I2)); out['maxwell'] = float(rM)
        out['maxwell_imag'] = float(np.max(np.abs(x.imag)))
    psi0 = [p[:, 0] for p in psis]

    # --- Riemann-Form: T_eff als Jet ------------------------------------------------------
    dA = d(A); F = dA - np.einsum('nm...->mn...', dA)
    gi, g = geo['gi'], geo['g']
    sblow = J('ab,bm,auv->muv', ETA, e, SBAR)                  # sigmabar_mu
    TBel = 0; LW = 0
    for s, p in enumerate(psis):
        Dp = Dpsi(p, om, A, Jc[s], q)
        Xm = J('u,muv,nv->mn', np.conj(p), sblow, Dp)
        TBel = TBel - 0.5 * np.imag(Xm + np.einsum('mn...->nm...', Xm))
        LW = LW + np.real(1j * J('u,auv,ma,mv->', np.conj(p), SBAR, geo['E'], Dp))
    jj = current(psis); L4 = lam * J('a,ab,b->', jj, ETA, jj)
    TMax = -J('ml,ns,ls->mn', F, F, gi) + 0.25 * J('mn,ab,cd,ac,bd->mn', g, F, F, gi, gi)
    Teff = TBel - J('mn,->mn', g, LW + L4) + TMax
    Tno4 = TBel - J('mn,->mn', g, LW) + TMax

    # --- H90a(ii): Einstein-Cartan-Gleichung (Variation nach dem Vierbein bei festem omega) ---
    Kj = cK * kap * J('fm,fabd,d->mab', e, EPS, jj)
    omEC = om + Kj; omv, domv = val(omEC).real, val(d(omEC)).real
    RfEC = frame_curv(omv, domv); Fv = val(F).real; giv = val(gi).real
    Dps = []
    for s, p in enumerate(psis):
        Dps.append(p[:, I1].T + 0.5 * np.einsum('mab,abuv,v->mu', omv, Sig, p[:, 0]) + 1j * q * Jc[s] * np.outer(val(A).real, p[:, 0]))

    def Ffun(Ev):
        gu = Ev @ eta @ Ev.T
        R = np.einsum('ma,nb,mnab', Ev, Ev, RfEC)
        LWv = sum(np.real(np.conj(p) @ (1j * np.einsum('auv,ma,mv->u', sbar, Ev, Dp))) for p, Dp in zip(psi0, Dps))
        return sg / (2 * kap) * R + LWv - 0.25 * np.einsum('ab,cd,ac,bd', Fv, Fv, gu, gu)

    def dF(Ev):
        gu = Ev @ eta @ Ev.T
        gr = sg / (2 * kap) * (np.einsum('mnad,nd->ma', RfEC, Ev) + np.einsum('nc,nmca->ma', Ev, RfEC))
        mt = sum(np.real(1j * np.einsum('u,auv,mv->ma', np.conj(p), sbar, Dp)) for p, Dp in zip(psi0, Dps))
        mx = -np.einsum('a,mb,rs,bs,ra->ma', et, Fv, Fv, gu, Ev)
        return gr + mt + mx
    E0r = E0.real; dFv = dF(E0r)
    # Kontrolle der Ableitung per Differenzenquotient
    h = 1e-6; fd = np.zeros((4, 4))
    for m in range(4):
        for a in range(4):
            dE = np.zeros((4, 4)); dE[m, a] = h
            fd[m, a] = (Ffun(E0r + dE) - Ffun(E0r - dE)) / (2 * h)
    out['dF_check'] = float(np.max(np.abs(fd - dFv)) / np.max(np.abs(dFv)))
    Z = E0r * Ffun(E0r) - np.einsum('ma,mb,na->nb', dFv, E0r, E0r)   # (1/det) dL/de^b_nu
    e0r = val(e).real
    Y = np.einsum('nb,bm,nk->mk', Z, e0r, val(g).real)
    Gv, Tv, T4v = val(geo['G']).real, val(Teff).real, val(Tno4).real
    out['Y_antisym_rel'] = float(np.max(np.abs(Y - Y.T)) / np.max(np.abs(Y)))
    def fit(Tm):
        Mx = np.stack([Gv.ravel() / kap, Tm.ravel()], 1)
        co, *_ = np.linalg.lstsq(Mx, Y.ravel(), rcond=None)
        return co, float(np.linalg.norm(Mx @ co - Y.ravel()) / np.linalg.norm(Y))
    co, rr = fit(Tv); co4, rr4 = fit(T4v)
    out.update(fit_alpha=float(co[0]), fit_beta=float(co[1]), fit_rel=rr,
               einstein_s=float(-co[1] / co[0]),             # G = s kappa T_eff
               fit_rel_ohne_4f=rr4)

    # --- H90b: Divergenzen ------------------------------------------------------------------
    def div(T):
        dT = val(d(T)); Gm = val(geo['Gam']); Tv_ = val(T)
        t = (np.einsum('ma,amn->n', val(gi), dT) - np.einsum('ma,lam,ln->n', val(gi), Gm, Tv_)
             - np.einsum('ma,lan,ml->n', val(gi), Gm, Tv_))
        sc = np.max(np.abs(np.einsum('ma,amn->mn', val(gi), dT)))
        return float(np.max(np.abs(t)) / sc)
    out.update(div_Teff_rel=div(Teff), div_T_ohne_4f_rel=div(Tno4), div_G_rel=div(geo['G']),
               T_imag=float(np.max(np.abs(val(Teff).imag))))
    return out


if __name__ == '__main__':
    res = {}
    for sg in (+1, -1):
        for seed in (1, 2, 3):
            res[f'sg{sg:+d}_seed{seed}'] = run(seed, sg)
        res[f'sg{sg:+d}_offshell'] = run(1, sg, onshell=False)
    keys = ['torsion_free', 'R_omega_minus_R_Christoffel', 'cartan_vacuum_residual', 'cartan_residual', 'K_c', 'K_fit_rel',
            'K_totally_antisym', 'lam_over_kappa', 'lam_fit_rel', 'weyl_order1', 'maxwell', 'dF_check', 'Y_antisym_rel',
            'einstein_s', 'fit_rel', 'fit_rel_ohne_4f', 'div_Teff_rel', 'div_T_ohne_4f_rel', 'div_G_rel']
    for k, v in res.items():
        print(k, {kk: (round(v[kk], 12) if isinstance(v.get(kk), float) else v.get(kk)) for kk in keys if kk in v})
    if len(sys.argv) > 1:
        json.dump(res, open(sys.argv[1], 'w'), indent=1, default=str)
