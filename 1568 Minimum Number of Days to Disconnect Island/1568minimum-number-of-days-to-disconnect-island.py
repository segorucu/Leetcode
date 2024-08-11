class Solution:
    def minDays(self, grid: List[List[int]]) -> int:

        m = len(grid)
        n = len(grid[0])

        directions = [(0,1),(1,0),(-1,0),(0,-1)]

        def valid(r,c):
            return 0 <= r < m and 0 <= c < n and (r,c) not in seen

        def dfs(r,c):
            seen.add((r,c))
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                if valid(nr,nc) and grid[r][c] == 1:
                    dfs(nr,nc)


        def countislands(grid):
            islands = 0
            for r in range(m):
                for c in range(n):
                    if grid[r][c] == 1 and (r,c) not in seen:
                        islands += 1
                        dfs(r,c)
            return islands

        seen = set()
        islands = countislands(grid)

        if islands != 1:
            return 0

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    grid[r][c] = 0
                    seen = set()
                    islands = countislands(grid)
                    if islands != 1:
                        return 1
                    grid[r][c] = 1


        return 2

