"""
URL:https://atcoder.jp/contests/joi2012yo/tasks/joi2012yo_e
DATE:2021/03/16
"""
import sys
# sys.setrecursionlimit(10**9)
# from copy import deepcopy
# from decimal import Decimal
# from math import ceil,floor
from collections import deque,Counter
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

def BFS(que):
    edge = 0
    
    while que:
        x,y = que.popleft()
        
        dxdy = even_dxdy if y%2==0 else odd_dxdy

        for dx,dy in dxdy:
            nx = x + dx
            ny = y + dy
            if nx<0 or nx>=(w+2) or ny<0 or ny>=(h+2):
                continue
            if array[ny][nx]==1:
                edge+=1
                continue
            if visited[ny][nx]:
                continue
            visited[ny][nx]=True
            que.append((nx,ny))
            
        # print(x,y,edge)
            
    return edge
            
def main():
    global visited,array
    global odd_dxdy,even_dxdy
    global w,h
    
    w,h = read_ints()
    
    array = []
    array.append([0]*(w+2))
    for i in range(h):
        array.append([0] + list(map(int,input().split())) + [0])
        
    array.append([0]*(w+2))
    
    even_dxdy = [(-1,-1),(0,-1),(1,0),(0,1),(-1,1),(-1,0)]
    odd_dxdy = [(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,0)]
    
    visited = [[False]*(w+2) for i in range(h+2)]
    visited[0][0] = True

    ans = BFS(deque([(0,0)]))
                
    return print(ans)

if __name__=='__main__':
    main()