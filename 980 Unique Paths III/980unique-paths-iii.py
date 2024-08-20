class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        m = len(grid)
        n = len(grid[0])

        visited = set()
        currpath = []
        ans = [0]
        zeros = 0

        for r in range(m):
            for c in range(n):
                if grid[r][c] in {1,-1}:
                    visited.add((r,c))
                elif grid[r][c] == 0:
                    zeros += 1
                if grid[r][c] == 1:
                    begin =(r,c)
        def dfs(r,c):
            if grid[r][c] == 2:
                if len(currpath) == zeros+1:
                    ans[0] += 1
                return 

            for dr,dc in directions:
                nr, nc = r+dr, c+dc
                if 0 <= nr < m and 0 <= nc < n and (nr,nc) not in visited:
                    print(nr,nc)
                    visited.add((nr,nc))
                    currpath.append((nr,nc))
                    dfs(nr,nc)
                    visited.remove((nr,nc))
                    currpath.pop()
      
        dfs(*begin)

        return ans[0]

            
                