class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        
        m = len(nums1)
        n = len(nums2)

        dp = [(n+1)*[0] for _ in range(m+1)]

        for i in range(m+1):
            dp[i][0] = -inf

        for j in range(n+1):
            dp[0][j] = -inf

        for i in range(m):
            for j in range(n):
                curr = nums1[i] * nums2[j]
                dp[i+1][j+1] = max(curr,dp[i][j]+curr,dp[i+1][j],dp[i][j+1])
                # print(dp)

        return dp[-1][-1]