"""Torch scalar chart inside the original full Taylor residual, not postprocessing."""
from pathlib import Path
import importlib.util,math,numpy as np,torch as T,mpmath as mp
ROOT=Path(__file__).resolve().parent
def load(name,path):
    spec=importlib.util.spec_from_file_location(name,path);module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module);return module
base=load('scalar_chart_base',ROOT/'recursive_calibrator.py')
scalar=load('scalar_chart_exact',ROOT/'scalar_parametrization.py')

class ChartModel:
    def __init__(self,order,pos):
        self.order=order;self.pos=np.array(pos,float);self.base=base.TaylorModel(order)
        self.idx=self.base.fullidx;self.parts=scalar.ScalarTaylor(order).parts
        with mp.workdps(70):
            alg=scalar.ScalarTaylor(order);hi,a,b=scalar.background_inverse_h(alg,[mp.mpf(str(v)) for v in pos]);target=alg.scale(hi,8);h=alg.reciprocal(hi)
            self.target=T.tensor(list(map(float,target)));self.h=T.tensor(list(map(float,h)))
        self.bg=self.base.background(pos);self.sign=T.tensor(scalar.SIGNS[1:],dtype=T.float64)
        pairs=[(i,j,n) for n,row in enumerate(self.parts) for i,j in row]
        self.left=T.tensor([v[0] for v in pairs]);self.right=T.tensor([v[1] for v in pairs]);self.dest=T.tensor([v[2] for v in pairs])
        self.interior=[[(i,j) for i,j in row if i and j] for row in self.parts]
    def conv_scalar(self,a,b):
        return T.zeros(len(self.idx),dtype=T.float64).index_add(0,self.dest,a[self.left]*b[self.right])
    def from_nonpivot(self,u,real=False):
        """u is N x23 real, all normalized Taylor coefficients. Gradients flow through every pivot coefficient."""
        terms=(u[self.left]*u[self.right]*self.sign).sum(dim=1)
        nonpivot_q=T.zeros(len(self.idx),dtype=T.float64).index_add(0,self.dest,terms)
        R=self.target-nonpivot_q
        root=[T.sqrt(R[0])]
        for n in range(1,len(self.idx)):
            correction=sum((root[i]*root[j] for i,j in self.interior[n]),T.zeros((),dtype=T.float64))
            root.append((R[n]-correction)/(2*root[0]))
        full=T.cat((T.stack(root)[:,None],u),dim=1)
        return full if real else T.complex(full[:,:12],full[:,12:])
    def evaluate(self,u):return self.base.evaluate(self.from_nonpivot(u),self.bg)
    def g_coefficients(self,u):
        full=self.from_nonpivot(u,real=True);d=T.tensor(scalar.SIGNS,dtype=T.float64)
        q=T.zeros(len(self.idx),dtype=T.float64).index_add(0,self.dest,(full[self.left]*full[self.right]*d).sum(dim=1))
        g=-self.conv_scalar(self.h,q)/2
        return g+T.cat((T.tensor([4.]),T.zeros(len(self.idx)-1)))
    def central_tangent(self,u):
        full=self.from_nonpivot(u,real=True)[0].detach().numpy();M=np.zeros((24,23));M[1:]=np.eye(23);M[0]=-np.array(scalar.SIGNS[1:])*full[1:]/full[0]
        return M
    def top_operator(self,u):
        full=self.from_nonpivot(u).detach().numpy();A,topstart,rowstart=self.base.top_operator(full,self.bg);M=self.central_tangent(u)
        reduced=np.einsum('rni,ij->rnj',A.reshape(A.shape[0],-1,24),M).reshape(A.shape[0],-1)
        return reduced,topstart,rowstart
    def coefficients_from_row(self,row):
        lookup={tuple(a):n for n,a in enumerate(row['multiindices'])};old=np.array(row['coefficients_real_imag']);packed=np.zeros((len(self.idx),24))
        for n,a in enumerate(self.idx):
            if a in lookup:packed[n]=old[lookup[a]]
        return packed[:,1:]
    def residual_norms(self,u):
        f=self.evaluate(u).detach().numpy();g=self.g_coefficients(u).detach().numpy();result={}
        for d in range(self.order):
            ids=[n for n,a in enumerate(self.base.idx) if sum(a)==d];fac=np.array([base.factorial(self.base.idx[n]) for n in ids]);result[str(d)]={'coefficient_norm':float(np.linalg.norm(f[ids])),'actual_derivative_norm':float(np.linalg.norm(f[ids]*fac[:,None]))}
        gs={}
        for d in range(self.order+1):
            ids=[n for n,a in enumerate(self.idx) if sum(a)==d];fac=np.array([base.factorial(self.idx[n]) for n in ids]);gs[str(d)]={'coefficient_norm':float(np.linalg.norm(g[ids])),'actual_derivative_norm':float(np.linalg.norm(g[ids]*fac))}
        return result,gs
