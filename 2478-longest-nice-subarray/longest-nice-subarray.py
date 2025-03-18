class Solution:

    def longestNiceSubarray(self, nums: List[int]) -> int:
        
        mask = l = 0
        ans = 0
        for r, num in enumerate(nums):
            while mask & num:
                mask ^= nums[l]
                l += 1
            mask |= num
            ans = max(ans, r-l+1)
            

        return ans
