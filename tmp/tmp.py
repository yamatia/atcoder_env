"""
URL:https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_10_A&lang=ja#
DATE:2021/03/17
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
def f(n):
    if dp[n]>0:
        return dp[n]
    
    if n==0:
        dp[0]=1
        return 1
    elif n==1:
        dp[1]=1
        return 1
    else:
        tmp = f(n-1)+f(n-2)
        dp[n] = tmp
        return tmp
    
def main():
    n = read_int()
    
    global dp
    dp = [-1]*45

    f(n)
    print(dp[n])
    return 0

if __name__=='__main__':
    main()