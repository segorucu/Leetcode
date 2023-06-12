class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        
        prefix = [nums[0]]
        n = len(nums)
        
        for i in range(1,n):
            prefix.append(prefix[i-1]+nums[i])
            
        x = -min(prefix)+1
        x = max(x,1)
        return x
        