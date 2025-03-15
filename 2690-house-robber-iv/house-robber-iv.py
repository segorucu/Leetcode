class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        

        n = len(nums)
        left = min(nums)
        right = max(nums)

        def good(val):
            dp = n * [0]
            if nums[0] <= val:
                dp[0] = 1
                if n == 1:
                    return dp[0] >= k
                dp[1] = 1
            if nums[1] <= val:
                dp[1] = 1
            for i in range(2,n):
                dp[i] = max(dp[i-2]+int(nums[i] <= val),dp[i-1])
                    
            return dp[-1] >= k


        res = 0
        while left <= right:
            mid = (left+right) // 2
            if good(mid):
                res = mid
                right = mid-1
            else:
                left = mid+1

        return res