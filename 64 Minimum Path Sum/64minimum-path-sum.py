from functools import cache
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        @cache
        def dp(row,col):
            if row == col == 0:
                return grid[row][col]

            ans = float("inf")
            if row > 0:
                ans = min(ans,dp(row-1,col)+grid[row][col])
            if col > 0:
                ans = min(ans,dp(row,col-1)+grid[row][col])

            return ans

        return dp(m-1,n-1)      