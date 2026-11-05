"""k191b: Lauf 2 fuer H76a (mehr Stichproben bei grossem L, je ein Prozess pro L und Saat)."""
import json, sys
L, seed, N = float(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
src = open('k191_vakuumzerfall.py').read().split('out = {}')[0]
g = {}; sys.argv = ['x', str(seed)]; exec(src, g)
m, e = g['integrate'](L, s_cut=1.0, N=N, chunk=500_000)
json.dump({'L': L, 'seed': seed, 'N': N, 'mean': m, 'err': e}, open(f'k191b_L{int(L)}_s{seed}.json', 'w'))
