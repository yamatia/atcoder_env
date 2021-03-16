class UnionFind:
    '''
    重みなし経路圧縮UnionFind/O(α(n))
    '''
    def __init__(self, n):
        self.parents = [-1] * n
        self.rank = [0] * n
        self.group_count = n
        self.n = n
    
    def find(self, x):
        if self.parents[x] < 0:
            return x
        
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]
 
    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
 
        if x == y:
            return
 
        if self.rank[x] == self.rank[y]:
            self.parents[x] += self.parents[y]
            self.parents[y] = x
            self.rank[x] += 1
        
        elif self.rank[x] > self.rank[y]:
            self.parents[x] += self.parents[y]
            self.parents[y] = x
        else:
            self.parents[y] += self.parents[x]
            self.parents[x] = y
        
        self.group_count -= 1
    
    def same(self, x, y):
        return self.find(x) == self.find(y)
 
    def get_group_member_list(self, x):
        x = self.find(x)
        return [i for i in range(self.n) if self.find(i) == x]
    
    def get_group_member_count(self, x):
        x = self.find(x)
        return -self.parents[x]
 
    def get_all_groups(self):
        return {idx:-n for idx, n in enumerate(self.parents) if n < 0}

    def get_len_groups(self):
        return self.group_count