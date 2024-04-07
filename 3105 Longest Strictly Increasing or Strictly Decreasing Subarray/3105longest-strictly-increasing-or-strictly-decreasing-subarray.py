class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        
        ans = 1
        
        l = 0
        r = 1
        n = len(nums)
        while r < n:
            if nums[r] > nums[r-1]:
                r += 1
            else:
                l = r
                r += 1
            ans = max(ans,r-l)
            
        # print(ans)
        
        l = 0
        r = 1
        while r < n:
            if nums[r] < nums[r-1]:
                r += 1
            else:
                l = r
                r += 1
            ans = max(ans,r-l)
        # print(ans)
        
        
        return ans
        