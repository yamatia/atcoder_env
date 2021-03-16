def GCD(a:int,b:int)->int:
    '''
    ユークリッドの互除法による最大公約数/O(log min(a,b))
    '''
    if b==0:
        return a
    else:
        return GCD(b,a%b)

def LCM(a:int,b:int)->int:
    '''
    最大公約数を利用した最小公倍数/O(log min(a,b))
    '''
    d = GCD(a,b)
    return a*b//d

def LCM_multi(vec:list)->int:
    '''
    数列の要素の最小公倍数を求める/O(N log(a'))
    '''
    l = vec[0]
    for i in range(len(vec)-1):
        l = LCM(l,vec[i+1])
    return l