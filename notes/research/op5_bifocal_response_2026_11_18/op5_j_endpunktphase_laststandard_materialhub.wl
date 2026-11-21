Print["Kernel: ", $Version];
den=(la-I da)(lj-I dj)+g^2;
Print["complex transmission denominator residual = ",
 Expand[den-(la lj+g^2-da dj-I(la dj+lj da))]];
zz=kj+aj; crit=aa+g^2/zz;
Print["J reflection and transmission power on A-critical resonance residuals = ",
 Together[{1-2 kj(crit+aa)/((crit+aa)zz+g^2)-(1-kj/zz (1+aa/crit)),
 4 crit kj g^2/(((crit+aa)zz+g^2)^2)-(kj/zz) g^2/(g^2+aa zz)}]];
probe[x_] := rA+pt x/(1-r x);
Print["centered nonzero load difference residual = ",Together[
 (probe[z0+x]-probe[z0-x])/(2x)-pt/((1-r z0)^2-(r x)^2)]];
p=9/10^6; gf=87131520945535/10^7;
cf=(4 p^2/(1-p^2))^(1/4);
alpha=50000/20001; eta=99/100; kJ0=(1/eta-1)/alpha;
kA0=alpha+1/kJ0;
freq=(640127090337223/10^15)/gf;
phase[x_,l1_,l2_] := ArcTan[l1 l2+1-x^2,(l1+l2)x];
Print["edge transmission phases at earlier limits {ideal, lossy} = ",
 N[{phase[cf,1,1],phase[freq,kA0+alpha,kJ0]},15]];
rho=2 (1/10)(1/100)+((1/10)(1/100))^2+((1/10)(99/200))^2;
slopeBound=(3/1000)^2 rho/(1-rho)+(5/10^8)/(99/200);
Print["nonzero-converter baseline example {bias and readout, allowance} = ",
 N[{slopeBound,(3/1000)^2 (1-(99/100)^2)},15]];

za=(ka+aa)-I da; zj=(kj+aj)-I dj;
dd=za zj+g^2;
Print["independent dissipation balance numerator residual = ",
 Expand[ComplexExpand[Abs[dd]^2-Abs[dd-2 ka zj]^2]-
 4 ka kj g^2-4 ka (aa ((kj+aj)^2+dj^2)+aj g^2)]];

wave[x_] := {1,x}/(1-rs x);
Print["three-load feedback identity residual = ",
 Together[wave[ga]+wave[-ga]-2 wave[0]-rs ga (wave[ga]-wave[-ga])]];
Print["uncompensated nominal load amplitude bias = ", N[(104/10^6)/2/(1-(104/10^6)/2),14]];

tvMin=9591531/100;
Print["necessary normalized hub and hoop strain factors at certified TV floor = ",
 N[{tvMin/(Sqrt[3/4]-Sqrt[1/4]),2 tvMin/(3/4-1/4)},15]];
Print["gradient relation residual = ",
 Expand[-D[-4 Pi grav rho phi[r],r]-4 Pi grav rho D[phi[r],r]]];

gref=1/2; rrmax=104/10^6; raw=1/10^11; ep=9/10^11;
dlower=2 gref^2 (99/100)/(1+(rrmax gref)^2)-2 gref raw;
er=raw (4+2 rrmax gref)/dlower;
amp=1/(1-rrmax gref);
df=(ep+(gref er+rrmax ep+er ep) amp)/(1-(rrmax+er)(gref+ep));
db=(gref+ep) df+ep amp;
Print["three-load conditional norm check {denominator lower, source reflection error, matrix error} = ",
 N[{dlower,er,Sqrt[2] Sqrt[df^2+db^2]},15]];
av=1/4; bv=3/4; mid=(av+bv)/2;
iw=-av Log[mid/av]+bv Log[bv/mid]; run=Sqrt[bv]-Sqrt[av];
Print["physical-unit requirement coefficients {hub, hoop, density, force} = ",
 N[{tvMin/(4 Pi run),tvMin/(2 Pi(bv-av)),tvMin/(Pi iw),2 tvMin/(Pi iw run)},15]];
