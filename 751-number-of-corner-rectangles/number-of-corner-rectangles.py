class Solution:
    def countCornerRectangles(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        columnpairs = defaultdict(int)
        tot = 0
        for r in range(m):
            for c in range(n):
                for cprev in range(c):
                    if grid[r][c] == grid[r][cprev] == 1:
                        tot += columnpairs[(cprev,c)]
                        columnpairs[(cprev,c)] += 1

        return tot
