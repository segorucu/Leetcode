class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        

        n = len(nums)
        left = min(nums)
        right = max(nums)

        def good(val):
            dp = n * [0]
            for i in range(n):
                if i < 2:
                    if nums[i] <= val:
                        dp[i] = 1
                    if i == 1:
                        dp[1] = max(dp[0],dp[1])
                else:
                    add = 0
                    if nums[i] <= val:
                        add += 1
                    dp[i] = max(dp[i-2]+add,dp[i-1])
                    
            return max(dp) >= k


        res = 0
        while left <= right:
            mid = (left+right) // 2
            if good(mid):
                res = mid
                right = mid-1
            else:
                left = mid+1

        return res