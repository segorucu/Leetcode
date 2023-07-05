class Solution:
    def longestSubarray(self, nums: List[int]) -> int:

        if len(nums)==1:
            return 0

        left = 0
        right = 0
        tot = 0 
        ans = 0
        while right < len(nums):
            if nums[right] == 0:
                tot += 1
            while tot > 1 and left < right:
                if nums[left] == 0:
                    tot -= 1
                left += 1
            ans = max(ans,right-left)
            right += 1
        return ans

