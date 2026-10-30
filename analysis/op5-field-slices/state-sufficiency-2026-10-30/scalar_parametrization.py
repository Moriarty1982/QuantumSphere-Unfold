"""Local all-order scalar chart; finite high-precision demonstration, no full PDE solve.

python scalar_parametrization.py --input fifth-window-result.json --order 7 --digits 70
Saved coefficients are multiindex-factorial normalized, real12 then imaginary12.
Nonpivot coefficients above the supplied order are zero for this demonstration.
"""
from pathlib import Path
import argparse,itertools,math,json,hashlib,time,platform
from datetime import datetime,timezone
import mpmath as mp

ROOT=Path(__file__).resolve().parent
SIGNS=(1,1,-1,-1,-1,-1,1,1,0,0,0,0)*2

def indices(order):
    result=[]
    for d in range(order+1):
        for axes in itertools.combinations_with_replacement(range(4),d):
            result.append(tuple(axes.count(mu) for mu in range(4)))
    return result

class ScalarTaylor:
    """Normalized formal series on a fixed finite total-degree truncation."""
    def __init__(self,order):
        self.order=order;self.idx=indices(order);self.lookup={a:n for n,a in enumerate(self.idx)}
        self.parts=[]
        for alpha in self.idx:
            row=[]
            for beta in itertools.product(*[range(a+1) for a in alpha]):
                gamma=tuple(a-b for a,b in zip(alpha,beta))
                row.append((self.lookup[beta],self.lookup[gamma]))
            self.parts.append(row)
    def zero(self):return [mp.mpf('0') for _ in self.idx]
    def constant(self,value):
        a=self.zero();a[0]=mp.mpf(value);return a
    def add(self,a,b):return [x+y for x,y in zip(a,b)]
    def sub(self,a,b):return [x-y for x,y in zip(a,b)]
    def scale(self,a,c):return [c*x for x in a]
    def mul(self,a,b):return [mp.fsum(a[i]*b[j] for i,j in row) for row in self.parts]
    def reciprocal(self,a):
        if a[0]==0:raise ValueError('reciprocal requires nonzero central coefficient')
        b=self.zero();b[0]=1/a[0]
        for n in range(1,len(self.idx)):
            b[n]=-mp.fsum(a[i]*b[j] for i,j in self.parts[n] if i!=0)/a[0]
        return b
    def sqrt_positive(self,a):
        if a[0]<=0:raise ValueError('positive real square-root chart requires positive central radicand')
        b=self.zero();b[0]=mp.sqrt(a[0])
        for n in range(1,len(self.idx)):
            b[n]=(a[n]-mp.fsum(b[i]*b[j] for i,j in self.parts[n] if i!=0 and j!=0))/(2*b[0])
        return b
    def coordinate(self,pos,mu):
        a=self.constant(pos[mu])
        if self.order:
            unit=tuple(int(k==mu) for k in range(4));a[self.lookup[unit]]=1
        return a
    def norms(self,a):
        result={}
        for d in range(self.order+1):
            ids=[n for n,alpha in enumerate(self.idx) if sum(alpha)==d]
            raw=[a[n]*math.prod(math.factorial(v) for v in self.idx[n]) for n in ids]
            result[str(d)]={'coefficient_norm':str(mp.sqrt(mp.fsum(a[n]**2 for n in ids))),'actual_derivative_norm':str(mp.sqrt(mp.fsum(x*x for x in raw)))}
        return result

def background_inverse_h(algebra,pos):
    """Exact original local branch h^-1=sqrt(1-r²/t²)*sqrt(1-t²/4)."""
    c=[algebra.coordinate(pos,mu) for mu in range(4)];one=algebra.constant(1)
    ti=algebra.reciprocal(c[0]);ti2=algebra.mul(ti,ti)
    r2=algebra.zero()
    for a in c[1:]:r2=algebra.add(r2,algebra.mul(a,a))
    first=algebra.sub(one,algebra.mul(r2,ti2))
    second=algebra.sub(one,algebra.scale(algebra.mul(c[0],c[0]),mp.mpf(1)/4))
    return algebra.mul(algebra.sqrt_positive(first),algebra.sqrt_positive(second)),first[0],second[0]

def normalize_pivot(algebra,components,target,pivot=0,branch=1):
    """Solve sum D_i u_i²=target exactly in formal truncation on a positive-sign pivot."""
    if SIGNS[pivot]!=1:raise ValueError('this chart implementation requires a positive-sign pivot')
    nonpivot=algebra.zero()
    for i,a in enumerate(components):
        if i!=pivot and SIGNS[i]:nonpivot=algebra.add(nonpivot,algebra.scale(algebra.mul(a,a),SIGNS[i]))
    radicand=algebra.sub(target,nonpivot)
    normalized=[a.copy() for a in components]
    normalized[pivot]=algebra.scale(algebra.sqrt_positive(radicand),branch)
    return normalized,radicand

def scalar_q(algebra,components):
    q=algebra.zero()
    for sign,a in zip(SIGNS,components):
        if sign:q=algebra.add(q,algebra.scale(algebra.mul(a,a),sign))
    return q

def run(path,order=7,digits=70):
    mp.mp.dps=digits;alg=ScalarTaylor(order);started=datetime.now(timezone.utc).isoformat();tic=time.time()
    sources=[Path(__file__).resolve(),path.resolve()];hashes={str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in sources}
    data=json.loads(path.read_text());rows=[]
    for row in data['results']:
        pos=[mp.mpf(str(v)) for v in row['point']];original=[alg.zero() for _ in SIGNS]
        for alpha,packed in zip(row['multiindices'],row['coefficients_real_imag']):
            alpha=tuple(alpha)
            if sum(alpha)>order:continue
            n=alg.lookup[alpha]
            for i,v in enumerate(packed):original[i][n]=mp.mpf(str(v))
        if original[0][0]<=0:raise ValueError('saved germ outside positive Re A0 chart')
        hi,guard1,guard2=background_inverse_h(alg,pos);target=alg.scale(hi,8);h=alg.reciprocal(hi)
        normalized,radicand=normalize_pivot(alg,original,target,pivot=0,branch=1)
        qbefore=scalar_q(alg,original);qafter=scalar_q(alg,normalized)
        gbefore=alg.sub(alg.constant(4),alg.scale(alg.mul(h,qbefore),mp.mpf(1)/2))
        gafter=alg.sub(alg.constant(4),alg.scale(alg.mul(h,qafter),mp.mpf(1)/2))
        change=alg.sub(normalized[0],original[0]);qerror=alg.sub(qafter,target)
        squareerror=alg.sub(alg.mul(normalized[0],normalized[0]),radicand)
        tolerance=mp.power(10,-digits+15)
        assert max(abs(v) for v in qerror)<tolerance
        assert max(abs(v) for v in gafter)<tolerance
        assert max(abs(v) for v in squareerror)<tolerance
        result={'point_index':row['point_index'],'point':row['point'],'pivot':'Re A0','branch':'+',
          'chart_guards':{'1-r2/t2':str(guard1),'1-t2/4':str(guard2),'radicand_central':str(radicand[0]),'old_pivot_central':str(original[0][0]),'new_pivot_central':str(normalized[0][0]),'implicit_derivative_2pivot':str(2*normalized[0][0])},
          'before_g_norms':alg.norms(gbefore),'after_g_norms':alg.norms(gafter),'pivot_change_norms':alg.norms(change),
          'q_minus_target_max_coefficient':str(max(abs(v) for v in qerror)),
          'sqrt_square_error_max_coefficient':str(max(abs(v) for v in squareerror)),
          'multiindices':alg.idx,'normalized_coefficients_real_imag':[[str(normalized[i][n]) for i in range(24)] for n in range(len(alg.idx))]}
        rows.append(result);print('POINT',row['point_index'],'pivot',result['chart_guards'],'maxg',max(abs(v) for v in gafter),'change_degree5',result['pivot_change_norms'].get('5'),flush=True)
    output={'contract':'Local scalar chart only: g=4-h psi†Zbeta psi/2=0. Positive real A0 pivot and original h branch. Formal normalized series, nonpivot absent higher coefficients set zero. No full spinor equation, geometry, native action, convergence or OP5 closure tested.',
      'order':order,'digits':digits,'started_at':started,'seconds':time.time()-tic,'software':{'python':platform.python_version(),'mpmath':mp.__version__},
      'inputs_sha256':hashes,'inputs_unchanged':all(hashlib.sha256(p.read_bytes()).hexdigest()==hashes[str(p)] for p in sources),'results':rows}
    dest=ROOT/f'scalar_parametrization_order{order}_result.json';dest.write_text(json.dumps(output,indent=2))
    return output

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--input',type=Path,default=ROOT/'fifth-window-result.json');parser.add_argument('--order',type=int,default=7);parser.add_argument('--digits',type=int,default=70);args=parser.parse_args();run(args.input,args.order,args.digits)
