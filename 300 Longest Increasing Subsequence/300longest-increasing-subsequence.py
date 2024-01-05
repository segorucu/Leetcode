class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        n = len(nums)
        L = (n) *[1]
        for i in range(1,n):
            num = nums[i]
            for j in range(0,i):
                if num > nums[j]:
                    L[i] = max(L[i],L[j]+1)
        
        return max(L)
