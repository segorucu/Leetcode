class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:

        n = len(arr)
        dp = (n+1) * [0]
        for i,val in enumerate(arr):
            maxval = 0
            for j in range(k):
                if i - j >= 0:
                    maxval = max(maxval, arr[i-j])
                    dp[i+1] = max(dp[i+1], dp[i-j] + (j+1) * maxval )

        return dp[-1]
        