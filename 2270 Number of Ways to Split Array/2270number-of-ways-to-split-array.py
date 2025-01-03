class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        
        sm = sum(nums)
        left = 0
        right = sm
        n = len(nums)
        count = 0
        for i in range(n-1):
            left += nums[i]
            right -= nums[i]
            if left >= right:
                count += 1

        return count