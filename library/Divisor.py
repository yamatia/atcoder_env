def Divisor(n:int)->list:
    '''
    約数全列挙/O(sqrt(N))
    '''
    ret_left = []
    ret_right = []
    i = 1
    while i*i<=n:
        if n%i==0:
            ret_left.append(i)
            if i*i!=n:
                ret_right.append(n//i)
        i+=1
    return ret_left+ret_right[::-1]
