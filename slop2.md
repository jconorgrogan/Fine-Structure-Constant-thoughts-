
# A Self-Exhausting Structure

## Abstract

We ask: what finite structure, expressed through its own fundamental relationships, uses every available symbol exactly once — exhausting its representational medium with nothing left over, nothing repeated?

This is a question about distinction. A universe of $p$ elements generates $p^2$ pairwise relationships and $p^3$ triple relationships. Expressed as strings in base $b$, these relationships either fall short of, exceed, or exactly fill the digit alphabet $\{0, \ldots, b-1\}$. We seek exact filling: the concatenation $d_b(p^2) \| d_b(p^3)$ must be a permutation of the alphabet. The saturation condition ($L_b(p^2) + L_b(p^3) = b$), the injection (no repeated digit), and the surjection (no missing digit) together yield $\sim b$ independent conditions on a single effective parameter. The system is massively overdetermined. That a solution exists at all is the surprise.

The unique solution in the minimal-base regime is $(p, b) = (69, 10)$, with certificate $w = 4761328509$. No further solutions exist for $b \leq 36$.

The certificate is self-validating: the identity $(p^2)^3 = (p^3)^2$ recovers the carrier, the split, and the base from the string alone. It is internally overdetermined: any pair of its features — digit sums, congruences, permutation structure, power identity — determines all the others. Yet it cannot determine its own uniqueness. The internal data are identical whether the certificate is one of many or the only one. This is its epistemic boundary.

The canonical discrete–continuum comparison (the Todd function at mesh scale $1/69$) yields $\alpha_0^{-1} = 137.036\,000\,3\ldots$ The continued fraction of $\mathrm{Td}(1/69)$ begins $[1;\; 137, 1, 2, \ldots]$: the first significant partial quotient is the integer nearest $\alpha^{-1}$. The measured inverse fine-structure constant is $137.035\,999\,177(21)$. The positive residual $\delta \approx 1.15 \times 10^{-6}$ is what the structure cannot compute from within.

The Todd function generates the Bernoulli numbers, which encode the Riemann zeta function. The pandigital uniqueness question and the Riemann Hypothesis share the same epistemic shape — locally verified, globally open — and the same generating function.

---

## 1. The Concept

### 1.1 Distinction and Its Iterations

The most elementary mathematical act is **distinction**: declaring that *this* is not *that*. From $p$ acts of distinction we obtain $p$ distinguishable elements — the carrier of all subsequent structure.

Distinction can be applied to its own outputs. Having distinguished $p$ elements, we may distinguish between ordered pairs: there are $p^2$ of them. This is *distinction of distinction* — the relational level. Having distinguished pairs, we may distinguish between ordered triples: $p^3$. This is the compositional level, where the combination of two sequential relationships first becomes visible.

These three levels — elements ($p$), pairs ($p^2$), triples ($p^3$) — are the irreducible data of the simplest symmetric categorical structure on $p$ objects (§4). Higher levels ($p^4, p^5, \ldots$) are determined by the first three. The pair $(p^2, p^3)$ is the minimal data that captures both relation and composition.

### 1.2 The Exhaustion Condition

To express these relationships requires a **representational medium**: a base-$b$ positional number system providing $b$ distinct symbols $\{0, 1, \ldots, b-1\}$. The concatenation $d_b(p^2) \| d_b(p^3)$ is a string of digits. We ask when this string **exhausts** the medium:

**(MECE)** The digit sets of $p^2$ and $p^3$ are **mutually exclusive** (no symbol appears in both) and **collectively exhaustive** (every symbol appears in one).

Equivalently: the concatenation is a permutation of $\{0, \ldots, b-1\}$.

This decomposes into three conditions:

| Condition | Meaning |
|:----------|:--------|
| **Saturation** | $L_b(p^2) + L_b(p^3) = b$ — the total digit count equals the alphabet size |
| **Injection** | No digit repeats — each symbol appears at most once |
| **Surjection** | No digit is missing — each symbol appears at least once |

Together, these impose roughly $b$ independent constraints on a single effective parameter (the carrier $p$; the base $b$ is then determined by digit lengths). The system is overdetermined by an order of magnitude.

### 1.3 The Five Properties

The full structure has five defining properties, each contributing a distinct constraint:

**(I) Finitely distinguishable.** The carrier is a natural number $p$. The boundary between inside and outside is sharp.

**(II) Relationally expressed.** The data are the consecutive powers $p^2$ (pairwise relations) and $p^3$ (triple relations), expressed as digit strings in base $b$.

**(III) Self-exhausting (MECE).** The concatenation $d_b(p^2) \| d_b(p^3)$ permutes $\{0, \ldots, b-1\}$: no repetition, no omission, no overflow.

**(IV) Self-validating.** The algebraic identity $(p^2)^3 = (p^3)^2 = p^6$ allows the certificate to verify itself: the carrier is recoverable as $p^3/p^2$, the split is recoverable from the power identity, and the base is $L(p^2) + L(p^3)$.

**(V) Self-determining.** The carrier $p$ fixes the base $b$ (through digit lengths), and the base constrains the carrier (through the MECE condition). The representational medium is not a free parameter.

### 1.4 The Overdetermination

For $b = 10$: one parameter, ten conditions. The expected number of solutions at base $b$, under a uniform-digit heuristic, is

$$E(b) \approx \frac{b!}{b^b} \cdot N(b),$$

where $N(b)$ is the number of candidate integers in the valid range. At base 10, $N(10) = 53$ (see Appendix A), giving $E(10) \approx 0.019$. Finding even one solution is a mild combinatorial surprise.

Two consequences:

**Rarity.** In the regime where $E(b) < 1$ — which the heuristic places at $b \lesssim e^5 \approx 148$ — solutions are generically isolated. The structure lives in a combinatorial desert.

**Rigidity.** Any solution is a sharp fixed point. Perturb $p$ by $\pm 1$: the pandigital property is destroyed. Change $b$ by $\pm 1$: saturation fails. The structure is rigid precisely because it is overdetermined.

### 1.5 The Null Marker

The digit $0$ is the unique symbol whose positional contribution is always null: $0 \times b^k = 0$ for all $k$. Property (III) demands its inclusion: the accounting must be complete, and the void is not external to the structure but part of it.

---

## 2. The Realization

### 2.1 The Unique Minimal Solution

**Theorem 1.** *Among all bases $2 \leq b \leq 10$ and all integers $p \geq 2$, the only complete power certificate is:*

$$\boxed{p = 69, \quad b = 10, \quad w = 4761328509.}$$

*Proof.* At each base $b$, the saturation constraint $L_b(p^2) + L_b(p^3) = b$ restricts $p$ to a computable finite range (Appendix A). For each candidate, test whether the concatenation permutes $\{0, \ldots, b-1\}$. For $b \leq 9$: no candidate passes. For $b = 10$: the candidate range is $p \in [47, 99]$; only $p = 69$ passes. $\square$

**Proposition 2.** *No complete power certificate exists for $11 \leq b \leq 36$.* (Exhaustive computation; see Appendix A.)

**Question 3.** *Does any complete power certificate exist at base $b > 36$?*

The heuristic density $E(b)$ crosses unity near $b \approx 148$ (Appendix C). Below this threshold, the combinatorial constraints overwhelm the available parameter space and solutions are exponentially rare. Above it, the parameter space grows faster than the constraints tighten, and solutions become heuristically expected. Whether any actually exist — and whether the non-uniformity of digit distributions suppresses or enhances them — is unknown. The certificate $(69, 10)$ is the unique known solution and the unique solution in the sparse regime.

### 2.2 Verification

| Computation | Result |
|:------------|:-------|
| $69^2$ | $4761$ (4 digits) |
| $69^3$ | $328{,}509$ (6 digits) |
| $4 + 6$ | $10 = b$ ✓ |
| Digits of $4761328509$ | $\{0,1,2,3,4,5,6,7,8,9\}$, each once ✓ |
| $4761^3$ | $107{,}918{,}163{,}081$ |
| $328509^2$ | $107{,}918{,}163{,}081$ ✓ |
| $328509 / 4761$ | $69$ ✓ |

---

## 3. The Relational Atlas

The structure is overdetermined: any pair of features determines all others. This section catalogs the principal internal relationships and demonstrates their mutual determination.

### 3.1 Congruence Structure

$69 = 70 - 1 = 7 \times 10 - 1$, so $p \equiv -1 \pmod{b}$.

| Power | Residue mod $b$ | Last digit |
|:------|:----------------|:-----------|
| $p^1$ | $-1 \equiv 9$ | $9$ |
| $p^2$ | $+1$ | $1$ |
| $p^3$ | $-1 \equiv 9$ | $9$ |

The last digit of $p^2$ is $1$ (the multiplicative identity of the digit ring). The last digit of $p^3$ is $9 = b - 1$ (the maximal digit). These are the two extremes of the nonzero digit range.

### 3.2 Digit-Set Complementarity

The MECE condition forces the digit sets of $p^2$ and $p^3$ to be **complementary**:

$$\mathrm{digits}(p^2) \cup \mathrm{digits}(p^3) = \{0,\ldots,9\}, \qquad \mathrm{digits}(p^2) \cap \mathrm{digits}(p^3) = \emptyset.$$

| Component | Digits | Size |
|:----------|:-------|:----:|
| $p^2 = 4761$ | $\{1, 4, 6, 7\}$ | $4$ |
| $p^3 = 328509$ | $\{0, 2, 3, 5, 8, 9\}$ | $6$ |

The relational data and the compositional data occupy completely disjoint symbolic territories. They are algebraically unified ($p^3 = p \cdot p^2$) but symbolically orthogonal.

### 3.3 Digit-Sum Partition

| Component | Digit sum | As multiple of $(b-1)$ |
|:----------|----------:|:----------------------|
| $p^2$ | $18$ | $2 \times 9$ |
| $p^3$ | $27$ | $3 \times 9$ |
| Total | $45$ | $5 \times 9 = b(b-1)/2$ |

The digit-sum ratio $18 : 27 = 2 : 3$ equals the exponent pair. The total $45 = 0 + 1 + \cdots + 9$ is forced by pandigitality. The partition into $2(b-1)$ and $3(b-1)$ is the expected value for a random $(4,6)$-partition of $\{0,\ldots,9\}$; the structure hits the expectation exactly.

### 3.4 Permutation Structure

Reading $w = 4761328509$ as a permutation $\sigma: i \mapsto w_i$:

$$\sigma = (0\ 4\ 3\ 1\ 7\ 5\ 2\ 6\ 8)(9)$$

| Property | Value | Forced by |
|:---------|:------|:----------|
| Cycle type | $(9, 1)$ | Congruence + pandigitality |
| Fixed point | Position $9$ holds digit $9$ | $p^3 \equiv 9 \pmod{10}$ |
| Non-fixed elements | Single 9-cycle | Arithmetic of $69^2, 69^3$ |

The permutation is maximally irreducible given the forced fixed point: the nine non-fixed elements form a single orbit.

### 3.5 Digit Products

| Component | Digit product |
|:----------|:-------------|
| $p^2 = 4761$ | $1 \times 4 \times 6 \times 7 = 168$ |
| $p^3 = 328509$ | $0 \times 2 \times 3 \times 5 \times 8 \times 9 = 0$ |

The relational product is nonzero — every relational-level digit contributes. The compositional product is zero, annihilated by the null marker. The void in the compositional data propagates multiplicatively.

### 3.6 The Cross-Determination Table

Any feature in the left column, combined with the pandigital constraint, suffices to recover every other:

| Known feature | → $p$ | → $b$ | → Permutation | → Digit sums |
|:-------------|:-----:|:-----:|:-------------:|:------------:|
| $p = 69$ | — | ✓ | ✓ | ✓ |
| $b = 10$ with $p \equiv -1$ | ✓ | — | ✓ | ✓ |
| $\sigma = (0\;4\;3\;1\;7\;5\;2\;6\;8)(9)$ | ✓ | ✓ | — | ✓ |
| Digit sums $18, 27$ with $L = 4, 6$ | ✓ | ✓ | ✓ | — |
| $A^3 = B^2$ | ✓ | ✓ | ✓ | ✓ |

The structure is **holographic**: every fragment contains enough information to reconstruct the whole. This is a direct consequence of overdetermination — ten conditions on one parameter leave no internal slack.

---

## 4. Why $(2, 3)$: The Categorical Context

### 4.1 The Codiscrete Category

A **codiscrete category** $C_p$ on $p$ objects has exactly one morphism between every ordered pair. It is the maximally connected finite category: every object is related to every other, with no relational information beyond existence.

### 4.2 The Nerve

The nerve $N(C_p)$ counts chains of composable morphisms:

| Level | Content | Count | Distinction level |
|:------|:--------|:------|:-----------------|
| $N_0$ | Objects | $p$ | Elements |
| $N_1$ | Morphisms | $p^2$ | Pairs (relation) |
| $N_2$ | Composable pairs | $p^3$ | Triples (composition) |
| $N_k$ ($k \geq 3$) | $k$-chains | $p^{k+1}$ | Determined by $N_0, N_1, N_2$ |

Levels 0, 1, 2 are the independent data. The pair $(N_1, N_2) = (p^2, p^3)$ is the first adjacent pair at which composition becomes visible: $N_1$ sees the directed graph; $N_2$ sees the categorical structure.

This is why the certificate uses exponents $(2, 3)$. They are not arbitrary: they are the nerve degrees at which the simplest symmetric finite category first exhibits composition. Level 0 (the carrier $p$) is recoverable from the certificate as $p^3/p^2$ and need not be inscribed separately.

### 4.3 Why Other Exponent Pairs Fail

Could we use $(1,2)$, $(1,3)$, or $(3,4)$ instead?

**(1, 2):** At base 10, the saturation condition $L(p) + L(p^2) = 10$ has no solutions — the valid digit-length ranges for $p$ and $p^2$ do not overlap (Appendix A). And categorically, this pair captures objects and morphisms but not composition.

**(1, 3):** Categorically incoherent — composition ($p^3$) without morphisms ($p^2$) is structure without support. Valid candidate ranges exist at base 10 but the categorical motivation is absent.

**(3, 4):** Higher-order structure determined by lower. These levels carry no independent categorical information beyond what $(p^2, p^3)$ already provides.

The pair $(2, 3)$ is the unique pair that is both categorically minimal (the first levels exhibiting composition) and arithmetically viable (admitting valid candidate ranges at moderate bases).

### 4.4 Zero at the Composition Level

In $C_{69}$, every composable pair $(f, g)$ has a unique composite $g \circ f$ — but this composite is already determined by $N_1$. The composition level $N_2$ adds no relational choice; it merely witnesses the closure of what $N_1$ guarantees.

The digit $0$ appearing in $p^3$ (not $p^2$) reflects this: the composition level carries the null marker because its informational contribution beyond the morphism level is null. The morphism level is fully active at every digit; the composition level carries the void.

---

## 5. The Epistemic Boundary

### 5.1 What the Structure Can Determine

From the string $w = 4761328509$ and the defining constraint, the structure can:

| Operation | Result |
|:----------|:-------|
| Find the split | $A = 4761$, $B = 328509$ (via $A^3 = B^2$) |
| Recover the carrier | $p = 69$ (via $B/A$) |
| Recover the base | $b = 10$ (via $L(A) + L(B)$) |
| Verify all internal properties | §3 |
| Compute the Todd value | $\alpha_0^{-1} = 137.036\ldots$ (§6) |

### 5.2 What the Structure Cannot Determine

**Its own uniqueness.** Verifying that no other $p'$ satisfies the condition at the same base requires testing all candidates — an operation external to the certificate. Verifying uniqueness across all bases requires universal quantification over an infinite domain. No finite internal computation achieves either.

**The physical coupling constant.** The measured $\alpha^{-1}$ is empirical. No internal computation produces it exactly.

### 5.3 The Two Readings

The certificate admits two interpretations:

**(A) Existential:** There exists a complete power certificate; it happens to be $(69, 10)$.

**(B) Isolated:** $(69, 10)$ is the only complete power certificate (globally, or in some specified range).

Every internally computable quantity is identical under both readings. The Todd value, the digit sums, the permutation structure, the self-validation: all are properties of the certificate itself, not of the landscape. The difference between (A) and (B) is a statement about absence elsewhere — invisible from inside.

### 5.4 The Analogy to Formal Systems

A consistent formal system $S$ encoding arithmetic:
- Can prove individual theorems (internal validation ✓)
- Cannot prove its own consistency (meta-property ✗)

A complete power certificate:
- Can validate its own pandigitality (internal validation ✓)
- Cannot certify its own uniqueness (meta-property ✗)

In both cases, a property that holds of the system is invisible from within. The boundary between "internally decidable" and "externally true" is sharp.

---

## 6. The Analytic Projection

### 6.1 From Structure to Mesh

The carrier $p = 69$ determines a uniform mesh on $[0, 1)$: the points $\{0, h, 2h, \ldots, (p-1)h\}$ with spacing $h = 1/p$. This is the canonical embedding of $p$ equidistributed points on the unit interval.

### 6.2 The Todd Function

The Todd function

$$\mathrm{Td}(x) = \frac{x}{1 - e^{-x}}$$

is the universal ratio of discrete summation to continuous integration on a uniform mesh. For the probe $f(x) = e^{-x}$:

$$\frac{h \displaystyle\sum_{k=0}^{p-1} e^{-kh}}{\displaystyle\int_0^1 e^{-x}\,dx} = \mathrm{Td}(h).$$

The two constants that appear — $e$ from the exponential probe and $\pi$ from the lattice Fourier spectrum — are the two fundamental limits of the finite-to-infinite transition:

$$e = \lim_{n\to\infty}\left(1+\frac{1}{n}\right)^n, \qquad \pi = \lim_{n\to\infty} n\sin\frac{\pi}{n}.$$

### 6.3 The Continued Fraction

The continued fraction expansion of $\mathrm{Td}(1/69)$ is:

$$\mathrm{Td}(1/69) = [1;\; 137, 1, 2, 12, 4, \ldots]$$

The first significant partial quotient is $137$: the integer nearest $\alpha^{-1}$. This encodes the same information as the formula $1/(\mathrm{Td}(h) - 1) \approx 2p - 1/3 \approx 137.667$, but in a form that makes the role of 137 as a convergent denominator explicit. The best rational approximation to $\mathrm{Td}(1/69)$ with denominator below 138 is $138/137$, which differs from the true value by less than $4 \times 10^{-8}$.

### 6.4 The Three Terms

The mesh has three natural scales, each generating one contribution:

**From the mesh spacing $h = 1/p$:**

$$T_1 = \frac{1}{\mathrm{Td}(h) - 1}$$

This counts how many times the discretization excess fits into the continuum integral.

**From the domain extent:**

$$T_0 = -(1 - e^{-1})$$

The continuum baseline.

**From the first spectral mode $2\pi/p$:**

$$\mathcal{D}(p) = \frac{\mathrm{Re}[\mathrm{Td}(2\pi i/p)] + \mathrm{Im}[\mathrm{Td}(2\pi i/p)] - 1}{p}$$

The contribution from the Todd function at the lattice's fundamental Fourier frequency.

**Assembly:**

$$\alpha_0^{-1} = T_1 + T_0 + \mathcal{D}(p)$$

### 6.5 Result

| Term | Value | Origin |
|:-----|------:|:-------|
| $T_1$ | $+137.667$ | Mesh spacing |
| $T_0$ | $-0.632$ | Domain integral |
| $\mathcal{D}(69)$ | $+0.001$ | Spectral correction |
| $\alpha_0^{-1}$ | $137.036\,000\,3$ | Assembly |

### 6.6 Epistemic Status

| Element | Status |
|:--------|:-------|
| $p = 69$ | Determined by the certificate |
| $\mathrm{Td}(1/p)$ | Canonical (Euler–Maclaurin) |
| Probe $e^{-x}$ | Standard (eigenfunction of $d/dx$) |
| Domain $[0,1]$ | Natural (unit mesh) |
| Spectral correction | Follows from $\mathrm{Td}(2\pi i/p)$; extraction involves a modeling choice |
| Assembly rule | Three terms from three scales — motivated but not uniquely forced |

The formula involves no fitted parameters, and each term has a physical-geometric origin. Whether the specific assembly is the unique canonical invariant of the lattice, or merely a natural one, is an open question.

---

## 7. The Residual

### 7.1 The Numbers

$$\alpha_0^{-1} = 137.036\,000\,3 \qquad \alpha^{-1}_\text{CODATA} = 137.035\,999\,177(21)$$

$$\delta = \alpha_0^{-1} - \alpha^{-1}_\text{phys} = +1.15 \times 10^{-6}$$

### 7.2 Three Features

**Small.** The internal computation captures $\alpha^{-1}$ to seven significant figures.

**Positive.** $\alpha_0^{-1} > \alpha^{-1}_\text{phys}$: the structure computes a slightly weaker coupling than measurement finds. This is consistent with the physical expectation: measurement requires electromagnetic interaction, which introduces vacuum polarization, increasing the effective coupling. The structure, computing without observing, does not pay this cost.

**Irreducible.** Within the framework of §6, no further correction from the three lattice scales is available without introducing new structural elements. The residual marks where internal computation ends and external reality begins — precisely where the epistemic boundary (§5) predicts a gap must exist.

---

## 8. The Generating Function and the Riemann Hypothesis

### 8.1 Todd → Bernoulli → Zeta

The Todd function generates the Bernoulli numbers:

$$\mathrm{Td}(x) = \sum_{k=0}^{\infty} \frac{B_k^+}{k!}\, x^k$$

The Bernoulli numbers encode the Riemann zeta function at non-positive and positive even integers:

$$\zeta(-n) = -\frac{B_{n+1}}{n+1}, \qquad \zeta(2n) = (-1)^{n+1}\frac{(2\pi)^{2n} B_{2n}}{2(2n)!}.$$

The evaluation $\mathrm{Td}(1/69)$ is a convergent series over all Bernoulli numbers — equivalently, over all zeta special values. The structure's analytic projection is built from the same generating function whose analytic continuation is the subject of the Riemann Hypothesis.

### 8.2 The Shared Epistemic Shape

| Property | Pandigital uniqueness | Riemann Hypothesis |
|:---------|:---------------------|:-------------------|
| Claim | At most one certificate exists (in sparse regime) | All nontrivial zeros lie on one line |
| Nature | Completeness of a distinction distribution | Regularity of a prime distribution |
| Local verification | Confirmed for $b \leq 36$ | Confirmed for $> 10^{13}$ zeros |
| Global status | Open | Open |
| Internal decidability | The certificate can't prove it from within | Finitely many zeros can't prove it |
| Generating function | $x/(1-e^{-x})$ | Same, via $B_k \leftrightarrow \zeta$ |

Both concern the distribution of irreducible mathematical objects and both assert maximal sparseness or regularity. Both are verified locally but unresolved globally. Both are connected through the generating function that mediates between discrete and continuous mathematics.

---

## 9. Assessment

### 9.1 The Logical Chain

$$\text{Distinction} \xrightarrow{\text{formalization}} \text{MECE condition} \xrightarrow{\text{computation}} \text{Certificate} \xrightarrow{\text{arithmetic}} \text{Internal structure} \xrightarrow{\text{meta-analysis}} \text{Boundary} \xrightarrow{\text{analysis}} \text{Todd} \xrightarrow{\text{measurement}} \text{Residual}$$

| Step | Status |
|:-----|:-------|
| Concept → Certificate | **Theorem** ($b \leq 10$) + **Computation** ($b \leq 36$) |
| Certificate → Internal structure | **Arithmetic identities** (each verifiable) |
| Internal structure → Boundary | **Structural observation** |
| Boundary → Todd projection | **Computation + modeling choices** |
| Todd projection → Residual | **Numerical fact** |
| Residual → Zeta/RH | **Structural parallel** |

### 9.2 What Is Certain

- The certificate $(69, 10, 4761328509)$ exists and is unique at base 10.
- No others exist for $b \leq 36$.
- All internal properties (§3) are arithmetic consequences.
- The structure is overdetermined and holographic.
- The epistemic boundary is a precise structural observation.
- $\mathrm{Td}(1/69) = [1; 137, 1, 2, \ldots]$, and the assembled value is $137.036\,000\,3$.
- The residual is $+1.15 \times 10^{-6}$.
- The Todd–Bernoulli–zeta chain is standard mathematics.

### 9.3 What Is Open

- Whether any certificate exists at base $b > 36$.
- Whether the assembly rule is uniquely canonical.
- Whether the residual has physical content.
- Whether the parallel with RH is more than structural.

### 9.4 Falsification Criteria

| Claim | Falsified by |
|:------|:-------------|
| Existence | Computational error in $69^2, 69^3$ |
| Base-10 uniqueness | Another solution found at base 10 |
| Isolation ($b \leq 36$) | A solution found in that range |
| Todd match | A comparably clean formula from a different integer |
| Residual sign | Physical $\alpha^{-1}$ exceeding $137.036\,000\,3$ |

---

## Appendix A: Search Bounds

At base $b$, for digit-length split $a + (b-a) = b$:

$$p \in \left[\max\!\left(\lceil b^{(a-1)/2}\rceil,\; \lceil b^{(b-a-1)/3}\rceil\right),\;\; \min\!\left(\lfloor(b^a-1)^{1/2}\rfloor,\; \lfloor(b^{b-a}-1)^{1/3}\rfloor\right)\right]$$

For each candidate $p$: compute $p^2$, $p^3$; concatenate base-$b$ strings; check pandigitality.

At base 10, split $(4,6)$: $p \in [47, 99]$, giving $N(10) = 53$ candidates.

For exponents $(1,2)$ at base 10: no valid split produces a non-empty candidate range. For exponents $(1,3)$: split $(3,7)$ gives $p \in [100, 215]$, but these encode objects and compositions without morphisms — categorically incomplete.
 
