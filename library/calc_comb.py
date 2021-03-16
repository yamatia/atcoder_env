def cmb(n, r, mod=10**9+7):
    r = min(r, n-r)
    res = 1
    for i in range(r):
        res = res * (n - i) * pow(i+1, mod-2, mod) % mod
    return res

def cmb(n, r, mod=10**9+7):
    c = 1
    m = 1
    r = min(n - r, r)
    for i in range(r):
        c = c * (n - i) % mod
        m = m * (i + 1) % mod
    return c * pow(m, mod - 2, mod) % mod

MAX = 2000
MOD = 10 ** 9 + 7
 
fac = [1, 1]
finv = [1, 1]
inv = [0, 1]
for i in range(2, MAX + 1):
    fac.append(fac[-1] * i % MOD)
    inv.append(-inv[MOD % i] * (MOD // i) % MOD)
    finv.append(finv[-1] * inv[-1] % MOD)
    
def cmb(n, k, mod=10**9+7):
    if n < k: return 0
    elif n < 0 or k < 0: return 0
    else:
        return fac[n] * finv[k] * finv[n-k] % mod