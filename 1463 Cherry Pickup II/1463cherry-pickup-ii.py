from functools import cache
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        
        ROWS = len(grid)
        COLS = len(grid[0])
        @cache
        def dfs(row, col1, col2):
            if row == ROWS-1:
                return grid[row][col1] + grid[row][col2]

            maxval = 0
            for d1 in [-1,0,1]:
                for d2 in [-1,0,1]:
                    ncol1 = col1 + d1
                    ncol2 = col2 + d2
                    if ncol1 >= ncol2 or ncol1 < 0 or ncol2 >= COLS:
                        continue
                    maxval = max(maxval,dfs(row+1, ncol1, ncol2))
            maxval += grid[row][col1] + grid[row][col2]
            return maxval

        path.append([0, 0, COLS-1])
        return dfs(0, 0, COLS-1)