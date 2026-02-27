from mpmath import mp

mp.dps = 100

def Td(x):
    # Todd function: x/(1 - exp(-x))
    return x / (1 - mp.e**(-x))

def F(p):
    return 1 / (Td(1/p) - 1)

def fmt50(x):
    # fixed-point, 50 digits after decimal
    return mp.nstr(x, 52, min_fixed=0, max_fixed=0)  # 1 digit before + 50 after typically

def continued_fraction(x, n_terms=30):
    # Regular continued fraction partial quotients for x
    a = []
    y = mp.mpf(x)
    for _ in range(n_terms):
        ai = mp.floor(y)
        a.append(int(ai))
        frac = y - ai
        if frac == 0:
            break
        y = 1 / frac
    return a

# 1) p0
p0 = mp.mpf(69)

# 2) delta = 3/4 + 3/(2*p0) - 3*pi^4/(10*p0^3)
delta = mp.mpf(3)/4 + mp.mpf(3)/(2*p0) - mp.mpf(3)*mp.pi**4/(10*p0**3)

# 3) q = 1/(p0 - delta)
q = 1 / (p0 - delta)

# 4) Td(q)
Td_q = Td(q)

# 5) r = 2*(Td(q) - 1)/q
r = 2 * (Td_q - 1) / q

# 6) S = (1 - exp(-r))/r
S = (1 - mp.e**(-r)) / r

# 7) p_eff = p0 - S/2
p_eff = p0 - S/2

# 8) alpha_inv = 1/(Td(1/p_eff) - 1)
alpha_inv = 1 / (Td(1/p_eff) - 1)

# Also compute bare exchange rate F(69)
F_bare = F(p0)

# CODATA value: 137.035999177(21) => sigma = 0.000000021
codata = mp.mpf("137.035999177")
sigma = mp.mpf("0.000000021")
diff = alpha_inv - codata
z = diff / sigma

# Print results
print("mp.dps =", mp.dps)
print()

print("p0 =", int(p0))
print("delta =", fmt50(delta))
print("q =", fmt50(q))
print("Td(q) =", fmt50(Td_q))
print("r =", fmt50(r))
print("S =", fmt50(S))
print("p_eff =", fmt50(p_eff))
print()

print("F(69) (bare) =", fmt50(F_bare))
print()

print("alpha_inv =", fmt50(alpha_inv))
print("CODATA alpha_inv = 137.035999177(21)")
print("difference (alpha_inv - CODATA) =", mp.nstr(diff, 55))
print("discrepancy (sigmas) =", mp.nstr(z, 20))
print()

cf30 = continued_fraction(F_bare, 30)
print("Continued fraction partial quotients of F(69), first", len(cf30), "terms:")
print(cf30)
