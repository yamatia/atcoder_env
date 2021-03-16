def Pow(x:int,n:int)->int:
    '''
    再帰的にX**nを求める/O(log n)
    '''
    if n==0:return 1
    k = 1
    
    while n>1:
        if n%2!=0:
            k*=x
        x*=x
        n//=2

    return k*x

# print(Pow(2,10))