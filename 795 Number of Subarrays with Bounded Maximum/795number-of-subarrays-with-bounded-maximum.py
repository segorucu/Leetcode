class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        
        n = len(nums)
        first = last = 0
        r = 0
        ans = 0
        maxval = 0
        while r < n:
            maxval = max(maxval,nums[r]) 
            if left <= nums[r] <= right:
                last = r
            if maxval < left or maxval > right:
                r += 1
                last = r
                if maxval > right:
                    first = r
                maxval = 0
            else:
                ans += (last-first+1)
                r += 1


            
        

        return ans    