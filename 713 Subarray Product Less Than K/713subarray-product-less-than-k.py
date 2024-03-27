class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        
        l = r = 0
        n = len(nums)
        curr = 1
        ans = 0
        while r < n:
            if nums[r] >= k:
                curr = 1
                r += 1
                l = r
                continue
            curr *= nums[r]
            while l <= r and curr >= k:
                curr = curr // nums[l]
                l += 1
            ans += r - l + 1
            r += 1

        return ans

