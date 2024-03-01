class UnionFind:
    def __init__(self,n):
        self.count = n
        self.parent = [i for i in range(n)]
        self.rank = [1] * n

    def find(self,x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self,x,y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False

        if self.rank[px] < self.rank[py]:
            self.rank[py] += self.rank[px]
            self.parent[px] = py
        else:
            self.rank[px] += self.rank[py]
            self.parent[py] = px
        self.count -= 1
        return True



class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        
        n = len(edges)
        union = UnionFind(n)
        stack = []
        indegree = collections.defaultdict(int)
        for u,v in edges:
            indegree[v] += 1
        for u,v in edges:
            stack.append([u,v,indegree[v]])  

        stack.sort(key = lambda x:x[2])

        for u,v, degree in stack:
            if not union.union(u-1,v-1):
                return [u,v]