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
            return
        if self.rank[px] < self.rank[py]:
            self.parent[px] = py
            self.rank[py] += self.rank[px] 
        else:
            self.parent[py] = px
            self.rank[px] += self.rank[py] 
        self.count -= 1


class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:

        k = len(positions)  
        union = UnionFind(k)
        directions = [(0,1),(1,0),(0,-1),(-1,0)]

        def valid(r,c):
            return 0 <= r < m and 0 <= c < n

        mp = {}
        ans = []
        for i, position in enumerate(positions):
            row, col = position[0], position[1]
            if (row,col) in mp:
                x = mp[(row,col)]
                union.union(x,i)
            mp[(row,col)] = i
            for move in directions:
                nrow = row + move[1]
                ncol = col + move[0]
                if valid(nrow,ncol):
                    if (nrow,ncol) in mp:
                        x = mp[(nrow,ncol)]
                        union.union(x,i)
            ans.append(union.count-k+i+1)

        return ans


        
        