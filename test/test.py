"""
URL:https://atcoder.jp/contests/arc114/tasks/arc114_a
DATE:2021/03/15
"""
import sys
# sys.setrecursionlimit(10**9)
# from copy import deepcopy
# from decimal import Decimal
# from math import ceil,floor
# from collections import deque,Counter
# from heapq import heapify,heappop,heappush
# from itertools import accumulate,product,permutations,combinations,combinations_with_replacement
# from bisect import bisect_left,bisect_right
# from functools import lru_cache#@lru_cache(maxsize=None)

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines

read_int = lambda: int(readline())
read_ints = lambda: map(int,readline().split())
read_str = lambda: readline().rstrip()
read_strs = lambda: readline().rstrip().split()
read_ints_list = lambda: list(map(int,readline().split()))
read_ints_array = lambda h:list(list(map(int,readline().split())) for _ in range(h))
read_strs_list = lambda: list(map(str,list(readline().rstrip())))
read_strs_array = lambda h:list(list(readline().rstrip()) for _ in range(h))

# solve
def singlePrimeFact(n:int)->list:
    '''
    割り続ける素因数分解/O(sqrt(n))
    '''
    ret = set()
    tmp = n
    i = 2
    while i*i<=n:
        if tmp%i==0:
            cnt = 0
            while tmp%i==0:
                cnt+=1
                tmp//=i
            ret.add(i)
            if cnt>1:ret.add(cnt)
        i+=1
    if tmp>1:
        ret.add(tmp)
    
    return ret

def GCD(a:int,b:int)->int:
    '''
    ユークリッドの互除法による最大公約数/O(log min(a,b))
    '''
    if b==0:
        return a
    else:
        return GCD(b,a%b)
    
def main():
    n = read_int()
    X = read_ints_list()
    
    prime_li = set()
    for i in range(2,51):
        prime_li|=singlePrimeFact(i)
    
    ans = 10**20
    prime_li = list(prime_li)
    len_prime = len(prime_li)
    
    for i in range(2**len_prime):
        tmp = 1
        for j in range(len_prime):
            if (i>>j &1):
                tmp*=prime_li[j]
                
        for k in range(n):
            if GCD(X[k],tmp)==1:
                break
        else:
            ans = min(ans,tmp)
    
    return print(ans,1)

if __name__=='__main__':
    main()