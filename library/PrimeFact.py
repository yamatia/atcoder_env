def singlePrimeFact(n:int)->list:
    '''
    割り続ける素因数分解/O(sqrt(n))
    '''
    ret = []
    tmp = n
    i = 2
    while i*i<=n:
        if tmp%i==0:
            cnt = 0
            while tmp%i==0:
                cnt+=1
                tmp//=i
            ret.append((i,cnt))
        i+=1
    if tmp>1:
        ret.append((tmp,1))
    
    return ret


class spfPrimeFact:
    '''
    SPFを前処理して使う複数の素因数分解
    前処理/O(n loglog n)
    クエリ/O(log n)
    '''
    def __init__(self,n):
        spf = [0]*(n+1)
        for i in range(n):
            spf[i] = i
        i = 2
        while i*i<=n:
            if spf[i]==i:
                j = i*i
                while j<=n:
                    if spf[j]==j:
                        spf[j] = i
                    j+=i
            i+=1
        self._spf = spf
    
    def factorization(self,x):
        if x==1:
            return [1]
        ret = []
        while x!=1:
            ret.append(self._spf[x])
            x//=self._spf[x]
        ret.sort()
        return ret

pr = spfPrimeFact(1000)
print(pr.factorization(13))
print(singlePrimeFact(24))