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
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:

        islandmap = collections.defaultdict(int)
        moves = [(0,1),(1,0),(0,-1),(-1,0)]
        m = len(grid1)
        n = len(grid1[0])

        
        def explore(grid,row,col):
            for dr,dc in moves:
                nr, nc = row+dr, col+dc
                if 0 <= nr < m and 0 <= nc < n and (nr,nc) not in currset \
                  and grid[nr][nc] == 1:
                  currset.add((nr,nc))
                  explore(grid,nr,nc)



        island = 1 
        visited = set()
        for r in range(m):
            for c in range(n):
                currset = set()
                if grid1[r][c] == 1 and (r,c) not in visited:
                    currset.add((r,c))
                    explore(grid1,r,c)
                    for node in currset:
                        islandmap[node] = island
                    island += 1
                    visited.update(currset)

        ans = 0
        visited = set()      
        for r in range(m):
            for c in range(n):
                currset = set()
                if grid2[r][c] == 1 and (r,c) not in visited:
                    currset.add((r,c))
                    explore(grid2,r,c)
                    match = set()
                    for node in currset:
                        if node in islandmap:
                            match.add(islandmap[node])
                        else:
                            match.add(-1)
                            match.add(-2)
                    if len(match) == 1:
                        ans += 1
                    visited.update(currset)
        

        return ans
        