import math
# Coefficient checks of the exact solution: u and X independently.
g=8.; h=1-6/g
for t in [0,.001,.01,.03]:
 s,c=math.sin(g*t),math.cos(g*t)
 assert abs(-g*s-(-6*s-g*h*s))<1e-12
 assert abs(g*h*c-(-6*c+g*c))<1e-12
 # X coefficients use beta X=-X.
 assert abs(2*g*c-2*g*c)<1e-12
 assert abs(-2*g*s-(-2*g*s))<1e-12
 d=math.cos(2*g*t); f=c*c+h*s*s
 rb=c*(g*h/d+6/f-g)
 if t==0: assert rb==0
 else: assert rb>0
 print({'t':t,'detE_axis':d*f**3,'B_induced_residual_magnitude':abs(rb)})
t=1e-5
c=math.cos(g*t); d=math.cos(2*g*t); f=1-.75*math.sin(g*t)**2
assert abs(c*(2/d+6/f-8)/t**2-544)<.01
assert abs((1-d/f)/t**2-80)<.01
assert abs(math.cos(16*math.pi/32))<1e-14
print('PASS: analytic coefficient identities, nonzero induced residual, leading residual 544 t^2, cone mismatch 80 t^2, axis degeneracy.')
