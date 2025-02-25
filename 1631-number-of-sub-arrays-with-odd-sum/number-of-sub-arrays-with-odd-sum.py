class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        
        n = len(arr)
        dp = [2*[0] for i in range(n)]

        MOD = 10**9 + 7

        if arr[0] % 2 == 0:
            dp[0][0] = 1
        else:
            dp[0][1] = 1

        tot = dp[0][1]
        for i in range(1,n):
            if arr[i] % 2 == 1:
                dp[i][0] = dp[i-1][1] % MOD
                dp[i][1] = dp[i-1][0] + 1
            else:
                dp[i][0] = dp[i-1][0] + 1
                dp[i][1] = dp[i-1][1] % MOD
            tot += dp[i][1] % MOD

        # print(dp)
        return tot % MOD

