class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.size = [1] * n
        self.count = n
        self.cost = [(1<<32)-1 for i in range(n)]

    def find(self, x):
        # This one finds the parent and does path compression as well.
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x, y, w):
        px, py = self.find(x), self.find(y)
        cost = self.cost[px] & self.cost[py] & w
        self.cost[px] = self.cost[py] = cost

        if px == py:
            return
        if self.size[px] < self.size[py]:
            self.par[px] = py
            self.size[py] += self.size[px]
        else:
            self.par[py] = px
            self.size[px] += self.size[py]
        self.count -= 1
        
class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        
        union = UnionFind(n)
        
        for a,b,w in edges:
            union.union(a,b,w)

        # for i in range(n):
        #     p = union.find(i)
        #     union.cost[p] = union.cost[p] & union.cost[i]
            

        ans = []
        for a,b in query:
            if a == b:
                ans.append(0)
            elif union.find(a) == union.find(b):
                par = union.find(a)
                ans.append(union.cost[par])
            else:
                ans.append(-1)
            
        
        
        return ans
        