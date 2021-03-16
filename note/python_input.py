read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines

read_int = lambda: int(readline())
read_ints = lambda: map(int,readline().split())
read_str = lambda: readline().rstrip()
read_strs = lambda: readline().rstrip().split()
read_ints_list = lambda: list(map(int,readline().split()))
read_ints_grid = lambda h:list(list(map(int,readline().split())) for _ in range(h))
read_strs_list = lambda: list(map(str,list(readline().rstrip())))
read_strs_grid = lambda h:list(list(readline().rstrip()) for _ in range(h))

def read_allints_grid(w):
    grid = map(int,read().split())
    grid = list(map(list,zip(*(grid for _ in range(w)))))
    return grid

def read_allstrs_grid(w):
    grid = map(str,read().split())
    grid = list(map(list,zip(*(grid for _ in range(w)))))
    return grid