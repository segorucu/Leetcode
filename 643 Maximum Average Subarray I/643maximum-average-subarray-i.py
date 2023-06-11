class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        
        ans = 0.
        for i in range(k):
            ans += nums[i]
        ans /= k

        
        dum = ans
        for i in range(k,n):
            dum += (nums[i] - nums[i-k])/k
            ans = max(ans,dum)
        

        
        return ans
            
            
        