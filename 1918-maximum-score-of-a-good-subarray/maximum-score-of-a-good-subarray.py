class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        

        minval = nums[k]
        if minval == 0:
            return 0

        l = k-1
        n = len(nums)
        r = k+1
        ans = minval 
        while l >= 0 or r < n:
            if l >= 0 and nums[l] >= minval:
                l -= 1
                ans = max(ans, minval * (r-l-1))
            elif r < n and nums[r] >= minval:
                r += 1 
                ans = max(ans, minval * (r-l-1))
            elif r == n:
                minval = min(minval, nums[l])
                l -= 1
                ans = max(ans, minval * (r-l-1))
            elif l == -1:
                minval = min(minval, nums[r])
                r += 1
                ans = max(ans, minval * (r-l-1))
            elif nums[r] <= nums[l]:
                minval = min(minval, nums[l])
                l -= 1
                ans = max(ans, minval * (r-l-1))
            else:
                minval = min(minval, nums[r])
                r += 1
                ans = max(ans, minval * (r-l-1))
        
        return ans
                
            



