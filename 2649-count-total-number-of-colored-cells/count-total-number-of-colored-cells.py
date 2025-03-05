class Solution:
    def coloredCells(self, n: int) -> int:

        return n * (n-1) * 2 + 1

        dp = (n+1) * [0]
        dp[1] = 1
        if n == 1:
            return 1

        dp[2] = 4
        for i in range(3,n+1):
            dp[i] = dp[i-1] + 4

        return sum(dp)
