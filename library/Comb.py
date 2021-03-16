def nCk_withoutmod(n:int,r:int)->int:
    '''
    二項係数nCrをmodなしで求める
    '''
    import math
    return factorial(n) // factorial(r) // factorial(n-r)

class Comb:
    '''
    二項係数をmodで割ったものを求める(n<=10**7でmodが素数の場合)
    前処理でfact=i%P,fact_inv,i_invを求める
    前処理/O(n),query/O(1)
    '''
    def __init__(self,n:int,r:int=0,mod:int=10**9+7):
        fac = [1, 1]
        finv = [1, 1]
        inv = [0, 1]
        for i in range(2,n+1):
            fac.append(fac[-1]*i%mod)
            inv.append(-inv[mod%i]*(mod//i)%mod)
            finv.append(finv[-1]*inv[-1]%mod)
        
        self.mod = mod
        self.fac = fac
        self.inv = inv
        self.finv = finv

    def nCk(self,n:int,k:int)->int:
        if n<k:return 0
        elif n<0 or k<0:return 0
        else:
            return self.fac[n] * self.finv[k] * self.finv[n-k] % self.mod

comb = Comb(10**5)
print(comb.nCk(15,5))