class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]

    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self,x,y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return

        if self.par[px] < self.par[py]:
            self.par[py] = self.par[px]
        else:
            self.par[px] = self.par[py]

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        
        Alice = defaultdict(list)
        Bob = defaultdict(list)
        Both = defaultdict(list)

        for typ,u,v in edges:
            u -= 1
            v -=1
            if typ == 1:
                Alice[u].append(v)
            elif typ == 2:
                Bob[u].append(v)
            else:
                Both[u].append(v)

        removed = 0
        BothUnion = UnionFind(n)
        AliceUnion = UnionFind(n)
        BobUnion = UnionFind(n)
        for u,lst in Both.items():
            for v in lst:
                if BothUnion.find(u) != BothUnion.find(v):
                    BothUnion.union(u,v)
                    AliceUnion.union(u,v)
                    BobUnion.union(u,v)
                else:
                    removed += 1

        for u,lst in Alice.items():
            for v in lst:
                if AliceUnion.find(u) != AliceUnion.find(v):
                    AliceUnion.union(u,v)
                else:
                    removed += 1

        for u,lst in Bob.items():
            for v in lst:
                if BobUnion.find(u) != BobUnion.find(v):
                    BobUnion.union(u,v)
                else:
                    removed += 1

        for i in range(n):
            BobUnion.find(i)
            AliceUnion.find(i)
            BothUnion.find(i)

        visited = set()
        for i in range(n):
            if AliceUnion.par[i] == BobUnion.par[i]:
                BothUnion.par[i] = AliceUnion.par[i]
            visited.add(BothUnion.par[i])

        if len(visited) > 1:
            return -1


        return removed

