def GCD(a:int,b:int)->int:
    '''
    ユークリッドの互除法による最大公約数/O(log min(a,b))
    '''
    if b==0:
        return a
    else:
        return GCD(b,a%b)

def GCD_multi(vec:list)->int:
    '''
    数列の要素の最大公約数を求める/O(N log(a'))
    '''
    l = vec[0]
    for i in range(len(vec)-1):
        l = GCD(l,vec[i+1])
    return l
