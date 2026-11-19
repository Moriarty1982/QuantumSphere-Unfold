from fractions import Fraction
from functools import lru_cache
from sympy import Rational
from sympy.physics.wigner import wigner_3j

@lru_cache(None)
def probability(k, ell, n):
    j = Rational(2*k-1,2)
    jj = Rational(2*n-1,2)
    return Fraction(2*n*wigner_3j(j,ell,jj,-Rational(1,2),0,Rational(1,2))**2)

def row(k,ell):
    return [
        (n if (ell+n-k)%2 == 0 else -n, probability(k,ell,n))
        for n in range(max(1,k-ell,ell+1-k),k+ell+1)
    ]

def increment(k,ell):
    weights=row(k,ell)
    assert sum(p for _,p in weights)==1
    value=Fraction(1,2*k)
    for nu,p in weights:
        value+=p/Fraction(k if nu==k else k-nu)
    return 2*k**3*value/Fraction(2*ell+1)

def plateau_candidate(ell):
    ratio = Fraction(1)
    for p in range(2, ell, 2):
        ratio *= Fraction(p, p + 1)
    return Fraction((ell-1)*ell*(ell+1)*(ell+2), 64*(2*ell+1)) * ratio**2


if __name__ == "__main__":
    for ell in range(3, 44, 2):
        d = (ell-1)//2
        steps = [increment(k, ell) for k in range(1, d+1)]
        assert all(value > 0 for value in steps)
        plateau = sum(steps)
        assert plateau == plateau_candidate(ell)
        if ell <= 25:
            assert all(increment(k, ell) == 0 for k in (d+1, d+2, ell, ell+1, 2*ell+1))
        print(ell, plateau, flush=True)
