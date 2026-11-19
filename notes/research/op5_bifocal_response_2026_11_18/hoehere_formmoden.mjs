function z(l, a) {
  return l > Math.abs(a) ? Math.sqrt((l*l-a*a)/(4*l*l-1)) : 0;
}

function legendre(l, a, maxDegree) {
  const levels = [new Map([[l, 1]])];
  if (Math.abs(a) > l) return Array.from({length: maxDegree+1}, () => new Map());
  for (let degree = 0; degree < maxDegree; degree++) {
    const next = new Map();
    function add(L, value) {
      if (value !== 0) next.set(L, (next.get(L) || 0) + value);
    }
    for (const [L, value] of levels[degree]) {
      const weight = (2*degree+1)*value/(degree+1);
      add(L+1, z(L+1,a)*weight);
      add(L-1, z(L,a)*weight);
    }
    if (degree > 0) {
      for (const [L, value] of levels[degree-1]) add(L,-degree*value/(degree+1));
    }
    levels.push(next);
  }
  return levels;
}

function spin(l,m,sign) {
  if (l<0 || Math.abs(m)>l+sign/2) return null;
  const a = Math.sqrt((l+.5+m)/(2*l+1));
  const b = Math.sqrt((l+.5-m)/(2*l+1));
  return sign === 1 ? [a,b] : [-b,a];
}

function run(maxL=64,maxDegree=12) {
  const grid = Array.from({length:maxDegree+1}, () => [0]);
  let maxNormError=0, maxQuadrupoleError=0;
  for (let k=1;k<=maxL;k++) {
    const l=k-1;
    const increments=Array.from({length:maxDegree+1},(_,ell)=>2*k*k/(2*ell+1));
    const norms=Array(maxDegree+1).fill(0);
    for(let m=-k+.5;m<k;m++) {
      const p=spin(l,m,1), upper=legendre(l,m-.5,maxDegree), lower=legendre(l,m+.5,maxDegree);
      for(let ell=1;ell<=maxDegree;ell++) {
        for(const L of new Set([...upper[ell].keys(),...lower[ell].keys()])) {
          for(const sign of [1,-1]) {
            const q=spin(L,m,sign);
            if (!q) continue;
            const nu=sign===1?L+1:-L;
            const amplitude=p[0]*q[0]*(upper[ell].get(L)||0)+p[1]*q[1]*(lower[ell].get(L)||0);
            const weight=amplitude**2;
            norms[ell]+=weight;
            const kernel=nu===k?k/2:k*(k+nu)/(2*(k-nu));
            increments[ell]+=kernel*weight;
          }
        }
      }
    }
    for(let ell=1;ell<=maxDegree;ell++) {
      grid[ell].push(grid[ell][k-1]+increments[ell]);
      maxNormError=Math.max(maxNormError,Math.abs(norms[ell]-2*k/(2*ell+1)));
    }
    const exact=3*k*k*(4*k**4-3*k*k+1)/(5*(4*k*k-1)**2);
    maxQuadrupoleError=Math.max(maxQuadrupoleError,Math.abs(increments[2]-exact));
  }
  const rows=grid.slice(2).map((row,i)=>({degree:i+2,min:Math.min(...row.slice(1)),largestShell:row[maxL],nonpositive:row.slice(1).filter(x=>x<=0).length}));
  return {grid,rows,maxNormError,maxQuadrupoleError,maxTranslation:Math.max(...grid[1].map(Math.abs))};
}

if (process.argv.includes("--induction")) {
  const result = run(96,24);
  const tolerance = 1e-8;
  const rows = result.grid.slice(2).map((row,index) => {
    const increments = row.slice(1).map((value,k) => value-row[k]);
    return {
      degree: index+2,
      minimum: Math.min(...increments),
      negative: increments.filter(value => value < -tolerance).length,
      unresolved: increments.filter(value => Math.abs(value) <= tolerance).length,
    };
  });
  console.table(rows);
  console.log({maxNormError: result.maxNormError});
} else {
  const result = run();
  console.table(result.rows);
  console.log({
    maxNormError: result.maxNormError,
    maxQuadrupoleError: result.maxQuadrupoleError,
    maxTranslation: result.maxTranslation,
  });
}
