class Solution:
    def satisfiesConditions(self, grid: List[List[int]]) -> bool:

        m = len(grid)
        n = len(grid[0])

        for r in range(m):
            for c in range(n):
                if c < n-1:
                    if grid[r][c] == grid[r][c+1]:
                        return False
                if r > 0:
                    if grid[r][c] != grid[r-1][c]:
                        return False

        return True
        