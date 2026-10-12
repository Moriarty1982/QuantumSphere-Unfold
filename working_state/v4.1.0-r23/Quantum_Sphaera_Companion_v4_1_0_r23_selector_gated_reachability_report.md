# v4.1.0-r23 Selector-Gated Reachability Diagnostic

## Main move

Reachability is now checked only inside the graph that already passed the first
selector gate:

```tex
G_{chi,adm}^{(1)} = (V,E_{chi,adm}^{(1)})
```

## New obstruction

```tex
D_reach^{chi,(1)}
```

records targets unreachable from `q_clk` after selector filtering and ordinary
admissibility filtering.

## OP 1/4

If:

```tex
D_chi^(1) = empty
D_reach,1/4^{chi,(1)} = empty
```

then every relevant anchor component has a first-layer readout-compatible
clock-to-anchor route certificate.

## OP 5(B)

If:

```tex
D_chi^(1) = empty
D_reach,5B^{chi,(1)} = empty
```

then the promoted boundary target has a first-layer readout-compatible route
certificate.

## Status

Still pre-TE, pre-residual, and pre-OP-4-stability.
