class Solution:
    def sumRemoteness(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])

        sm = 0
        visited = set()
        for r in range(m):
            for c in range(n):
                if grid[r][c] > 0 :
                    sm += grid[r][c]
                else:
                    visited.add((r,c))

        def valid(r,c):
            return 0 <= r < m and 0 <= c < n

        def dfs(r,c):
            neighs = [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]
            currsm = grid[r][c]
            count = 1
            for nr, nc in neighs:
                if valid(nr,nc) and (nr,nc) not in visited:
                    visited.add((nr,nc))
                    a,b = dfs(nr,nc)
                    currsm += a
                    count += b
            return currsm, count

        ans = 0
        for r in range(m):
            for c in range(n):
                if (r,c) not in visited:
                    visited.add((r,c))
                    currsm, count = dfs(r,c)
                    ans += count * (sm - currsm)

        return ans