class Solution:
    def maximumSum(self, arr: List[int]) -> int:

        if max(arr) <= 0:
            return max(arr)

        n = len(arr)
        dp = [[0]*n for _ in range(2)]
        dp[1][0] = -inf
        last = -inf
        ans = -inf
        for i,num in enumerate(arr):
            dp[0][i] = max(num,last+num)
            last = dp[0][i]
            ans = max(ans,last)
            

        for i,num in enumerate(arr[1:],1):
            dp[1][i] = max(dp[1][i-1]+num,dp[0][i-1])
            ans = max(ans,dp[1][i])
        return ans




        