class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        
        rows = collections.defaultdict(int)
        cols = collections.defaultdict(int)

        m = len(grid)
        n = len(grid[0])

        for r in range(m):
            for c in range(n):
                if grid[r][c]:
                    rows[r] += 1
                    cols[c] += 1

        count = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c]:
                    if rows[r] > 1 or cols[c] > 1:
                        count += 1

        return count