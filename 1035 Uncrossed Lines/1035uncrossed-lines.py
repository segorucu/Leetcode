class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        
        """
       [] 2 5 1 2 5
    []  0 0 0 0 0 0
    10  0 0 0 0 0 0
    5   0 0 1 1 1 1
    2   0 1 1 1 2 2
    1   0 1 1 2 2 2
    5   0 1 2 2 2 3
    2   0 1 2 2 3 3

        """


        m = len(nums1)
        n = len(nums2)

        dp = [(m+1)*[0] for row in range(n+1)]

        for row in range(n):
            for col in range(m):
                if nums1[col] == nums2[row]:
                    dp[row+1][col+1] = max(dp[row][col]+1, dp[row+1][col], dp[row][col+1])
                else:
                    dp[row+1][col+1] = max(dp[row+1][col], dp[row][col+1])

        return dp[-1][-1]