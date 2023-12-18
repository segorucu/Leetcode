class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()
        val = nums[-1] * nums[-2] - nums[0] * nums[1]
        return val