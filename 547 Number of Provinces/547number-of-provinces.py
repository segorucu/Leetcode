class UnionFind:
    def __init__(self,n):
        self.parent = [i for i in range(n)]
        self.size = [1] * n
        self.count = n
    
    def find(self,x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self,x,y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return 
        if self.size[px] <= self.size[py]:
            self.parent[px] = py
            self.size[py] += self.size[px]
        else:
            self.parent[py] = px
            self.size[px] += self.size[py]
        self.count -= 1


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)

        union = UnionFind(n)

        for i in range(n):
            for j in range(i):
                if isConnected[i][j] == 1:
                    union.union(i,j)
        
        return union.count