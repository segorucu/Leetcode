class Solution:
    def numberOfRightTriangles(self, grid: List[List[int]]) -> int:

        m = len(grid)
        n = len(grid[0])

        rows = m * [0]
        cols = n * [0]

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    rows[r] += 1
                    cols[c] += 1

        ans = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    ans += (rows[r] - 1) * (cols[c] - 1)


        return ans   