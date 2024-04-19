class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def valid(ni, nj):
            if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == "1" and (ni,nj) not in visited:
                return True
            else:
                return False

        def dfs(i,j):
            for move in directions:
                ni, nj = i+move[1], j+move[0]
                if valid(ni, nj):
                    visited.add((ni,nj))
                    dfs(ni,nj)

        island = 0
        visited = set()
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and (i,j) not in visited:
                    island += 1
                    visited.add((i,j))
                    dfs(i,j)

        return island
