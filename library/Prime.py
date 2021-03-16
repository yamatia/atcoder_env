def Is_prime(n:int)->bool:
    '''
    nが素数かどうか判定/O(sqrt(n))
    '''
    i = 2
    while i*i<=n:
        if n%i==0:
            return False
        i+=1
    return True

def Prime_list(n:int)->list:
    '''
    エラトステネスの篩でNまでの素数判定をリストで作成/O(nloglogn)
    '''
    vec = [True]*(n+1)
    if n>=0:vec[0] = False
    if n>=1:vec[1] = False
    
    i = 2
    while i*i<=n:
        j = i*i
        if not vec[i]:
            i+=1
            continue
        while  j<=n:
            vec[j] = False
            j+=i
        i+=1
    return vec

# print(Is_prime(911))
# print(Prime_list(911))
    