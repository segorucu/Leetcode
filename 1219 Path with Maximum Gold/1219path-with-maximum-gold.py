class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        moves = [(0,1),(1,0),(-1,0),(0,-1)]

        def valid(i,j):
            return 0 <= i < m and 0 <= j < n and (i,j) not in visited and grid[i][j] > 0


        def dfs(i,j):
            dummy = 0
            for dx,dy in moves:
                ni = i + dy
                nj = j + dx
                if valid(ni,nj):
                    visited.add((i,j))
                    dummy = max(dummy,dfs(ni,nj))
                    visited.remove((i,j))
            return dummy + grid[i][j]


        ans = 0
        for r in range(m):
            for c in range(n):
                visited = set()
                if grid[r][c] > 0:
                    visited.add((r,c))
                    ans = max(ans,dfs(r,c))

        return ans