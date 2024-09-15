class Solution:
    def maxScore(self, a: List[int], b: List[int]) -> int:
        n = len(b)
    
        dp = [4*[-inf] for _ in range(n)]

        for i in range(n):
            dp[i][0] = a[0] * b[i]
            if i > 0:
                dp[i][0] = max(dp[i-1][0],dp[i][0])

        for i in range(1, n):
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + a[1] * b[i])

        for i in range(2, n):
            dp[i][2] = max(dp[i - 1][2], dp[i - 1][1] + a[2] * b[i])

        ans = -inf
        for i in range(3, n):
            dp[i][3] = max(dp[i - 1][3], dp[i - 1][2] + a[3] * b[i])
            ans = max(ans, dp[i][3])

        return ans