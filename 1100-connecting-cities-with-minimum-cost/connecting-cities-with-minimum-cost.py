class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.size = [1] * n
        self.count = n

    def find(self, x):
        # This one finds the parent and does path compression as well.
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
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
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:

        connections.sort(key = lambda x: -x[2])
        m = len(connections)
        for i in range(m):
            connections[i][0] -= 1
            connections[i][1] -= 1

        Union = UnionFind(n)
        tot = 0
        while connections:
            n1, n2, cost = connections.pop()
            if Union.find(n1) == Union.find(n2):
                continue
            Union.union(n1, n2)
            tot += cost

        parent = set()
        for i in range(n):
            par = Union.find(i)
            parent.add(par)

        if len(parent) != 1:
            return -1
        return tot
        