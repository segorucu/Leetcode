class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        

        maxval = 0
        m = len(grid)
        n = len(grid[0])

        def valid(r,c):
            return 0 <= r < m and 0 <= c < n

        def dfs(r,c):
            neighs = [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]
            tot = grid[r][c]
            for nr,nc in neighs:
                if (nr,nc) not in visited and valid(nr,nc) and grid[nr][nc] > 0:
                    visited.add((nr,nc))
                    tot += dfs(nr,nc)
            return tot


        
        visited = set()
        for r in range(m):
            for c in range(n):
                if (r,c) not in visited and grid[r][c] > 0:
                    visited.add((r,c))
                    maxval = max(maxval,dfs(r,c))


        return maxval