from functools import cache
class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        dp = [n*[0] for _ in range(m)]
        dp[0][0] = inf
        for c in range(1,n):
            dp[0][c] = min(dp[0][c-1],grid[0][c-1])

        for r in range(1,m):
            dp[r][0] = min(dp[r-1][0],grid[r-1][0])

        for r in range(1,m):
            for c in range(1,n):
                dp[r][c] = min(dp[r-1][c],dp[r][c-1],grid[r-1][c],grid[r][c-1])
        
        ans = -inf
        for r in range(m):
            for c in range(n):
                ans = max(ans,grid[r][c]-dp[r][c])
        return ans
