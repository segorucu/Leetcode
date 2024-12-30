class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        
        dp = (high+1) * [0]
        dp[zero] += 1
        dp[one] += 1
        count = 0
        mod = 10**9+7
        for i in range(1,high+1):
            if i-zero > 0:
                dp[i] += dp[i-zero]
            if i-one > 0:
                dp[i] += dp[i-one]
            if i >= low:
                count += dp[i]
                count %= mod
        return count