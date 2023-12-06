from functools import cache
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        @cache
        def dp(row,col):
            if obstacleGrid[row][col] == 1:
                return 0
            if row == col == 0:
                return 1
            
            ans = 0
            if row > 0:
                ans += dp(row-1,col)
            if col > 0:
                ans += dp(row,col-1)

            return ans

        return dp(m-1,n-1)
        