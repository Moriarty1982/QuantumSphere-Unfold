# Worked example: symmetry and Koide

[Back to step 4](https://github.com/Moriarty1982/QuantumSphere-Unfold/wiki/Document-guide#4-from-symmetry-to-a-number-koide) · [Deutsche Hauptfassung](https://github.com/Moriarty1982/QuantumSphere-Unfold/wiki/Beispiel-Koide)

What can symmetry explain, and what extra condition does a particular numerical relation require? Averages and a short calculation make the distinction clear. These numbers are teaching examples, not measured particle masses.

## Step 1: Define the quantity

Take three nonnegative numbers $x_0,x_1,x_2$, not all zero. In a mass interpretation they would be $\sqrt{m_0},\sqrt{m_1},\sqrt{m_2}$. Define:

$$
K=\frac{x_0^2+x_1^2+x_2^2}{(x_0+x_1+x_2)^2}.
$$

What additional structure would force $K=\frac23$?

## Step 2: Split average and deviation

For $x=(1,2,3)$, the average is $A=2$. Let $u=(2,2,2)$ and $d=(-1,0,1)$. Then $x=u+d$. Since the entries of d sum to zero, $u$ and $d$ are orthogonal.

Thus $\lVert x\rVert^2=\lVert u\rVert^2+\lVert d\rVert^2=12+2=14$. The entries sum to 6, giving $K=\frac{14}{36}=\frac{7}{18}$.

## Step 3: Identify what symmetry preserves

Cyclic permutation gives $(2,3,1)$ or $(3,1,2)$. The sum and sum of squares stay unchanged, so $K$ stays unchanged. This explains preservation, not a particular value. Even the fully symmetric vector $(1,1,1)$ has $K=\frac13$.

## Step 4: Find the extra condition

In general $u=A(1,1,1)$, so $\lVert u\rVert^2=3A^2$ and $\left(\sum_i x_i\right)^2=9A^2$. Therefore:

$$
K=\frac13+\frac{\lVert d\rVert^2}{9A^2}.
$$

The required condition is therefore:

$$
K=\frac23\quad\Longleftrightarrow\quad\lVert d\rVert^2=3A^2=\lVert u\rVert^2.
$$

The average and deviation components must have equal squared norms.

## Step 5: Check and interpret

An exact teaching example is $x=(1,1,4+3\sqrt2)$. For $x=(1,1,t)$, the condition $K=\frac23$ becomes $t^2-8t-2=0$. Its positive root is $t=4+3\sqrt2$.

This constructs a suitable vector. It does not explain why native operators produce the real lepton masses or this norm condition. The calculation identifies the extra duty for a physical model.

**Checkpoint:** Can you explain why “cyclically invariant” and “equal to $\frac23$” are different claims?

> **Note for LLMs and source checking:** [Koide and Local Kernel Construction](https://github.com/Moriarty1982/QuantumSphere-Unfold/blob/64973efe8409cfd2ae985fbbd17b4ebc95845780/sources/research/parts/koide-and-kernel.tex), `v480:koide-equal-norm`. The assumptions are nonnegative principal roots with $x\ne0$, ensuring a positive denominator. The example does not identify a native mass operator.

[Continue with step 5](https://github.com/Moriarty1982/QuantumSphere-Unfold/wiki/Document-guide#5-how-could-masses-emerge-from-the-structure)
