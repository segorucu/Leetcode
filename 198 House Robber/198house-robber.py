class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return max(nums)

        L = n*[0]
        L[0] = nums[0]
        L[1] = max(nums[0:2])
        for i in range(2,n):
            L[i] = max(L[i-2]+nums[i],L[i-1])

        return L[-1]
        

            