class Solution:
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        
        
        n = len(nums)
        l = r = 0
        alternating = True
        ans = 0
        while r < n:
            if r > 0 and nums[r] == nums[r-1]:
                l = r
            ans = ans + (r - l + 1)
            r += 1
            
            
        return ans