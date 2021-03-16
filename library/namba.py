import numpy as np
 
def solve(stdin):
    n = stdin[0]
    dp = np.zeros(n+1,dtype=np.int64)
    for i in range(1,n+1):
        for j in range(i,n+1,i):
            dp[j]+=1
    dp*=np.arange(n+1)
    return dp.sum()
 
def main():
    stdin = np.fromstring(open(0).read(), dtype=np.int64, sep=' ')
    print(solve(stdin))
 
def cc_export():
    from numba.pycc import CC
    cc = CC('my_module')
    cc.export('solve', '(i8[:],)')(solve)
    cc.compile()
 
if __name__ == '__main__':
    import sys
    if sys.argv[-1] == 'ONLINE_JUDGE':
        cc_export()
        exit(0)
    from my_module import solve
    main()