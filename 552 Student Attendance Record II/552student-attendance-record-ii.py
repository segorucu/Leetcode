class Solution:
    def checkRecord(self, n: int) -> int:
        
        MOD = 10**9+7
        dp = [[[0] * 3 for _ in range(2)] for _ in range(n)]
        
        dp[0][0][0] = 1  # P
        dp[0][0][1] = 1  # L
        dp[0][1][0] = 1  # A

        for i in range(1,n):

            for k in range(3):
                dp[i][0][0] += dp[i-1][0][k] % MOD
            dp[i][0][1] = dp[i-1][0][0]
            dp[i][0][2] = dp[i-1][0][1]
            for j in range(2):
                for k in range(3):
                    dp[i][1][0] += dp[i-1][j][k] % MOD
            dp[i][1][1] = dp[i-1][1][0] 
            dp[i][1][2] = dp[i-1][1][1] 


        count = 0
        for j in range(2):
            for k in range(3):
                count = (count + dp[-1][j][k]) % MOD


        return count