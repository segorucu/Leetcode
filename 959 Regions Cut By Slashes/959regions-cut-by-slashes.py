class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:

        n = len(grid)
        directions = ((0,1),(1,0),(-1,0),(0,-1))
        
        newgrid = [(3*n)*[0] for _ in range(3*n)]
        for r in range(n):
            for c in range(n):
                nr = 3*r
                nc = 3*c
                if grid[r][c] == "/":
                    for i in range(3):
                        newgrid[nr+2-i][nc+i] = 1
                elif grid[r][c] == "\\":
                    for i in range(3):
                        newgrid[nr+i][nc+i] = 1

        n = len(newgrid)
        seen = set()
        def dfs(r,c):
            seen.add((r,c))
            for dr,dc in directions:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < n and 0 <= nc < n and (nr,nc) not in seen \
                   and newgrid[nr][nc] == 0:
                   dfs(nr,nc)

        islands = 0
        for r in range(n):
            for c in range(n):
                if newgrid[r][c] == 0 and (r,c) not in seen:
                    islands += 1
                    dfs(r,c)

        return islands

        