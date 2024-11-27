class Solution:
    def minScore(self, grid: List[List[int]]) -> List[List[int]]:
        

        m = len(grid)
        n = len(grid[0])

        rows = m * [0]
        cols = n * [0]

        spaces = []
        for r in range(m):
            for c in range(n):
                spaces.append((grid[r][c],r,c))
        spaces.sort()

        for space in spaces:
            val, r, c = space
            val = max(rows[r],cols[c]) + 1
            rows[r] = cols[c] = val
            grid[r][c] = val
        return grid