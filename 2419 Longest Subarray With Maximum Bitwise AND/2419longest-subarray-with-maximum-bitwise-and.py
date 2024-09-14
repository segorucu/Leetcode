class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        
        n = len(nums)
        l = 0
        r = 0
        ans = 1
        maxval = max(nums)
        while r < n:
            if nums[r] != maxval:
                l = r+1

            ans = max(ans,r-l+1)
            r += 1
            
            

        return ans
