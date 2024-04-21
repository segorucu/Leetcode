class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        
        n = len(nums)
        nums.sort()
        maxval = 0
        for one,two in zip(nums[:-1],nums[1:]):
            if two-one > maxval:
                maxval = two-one
        return maxval
