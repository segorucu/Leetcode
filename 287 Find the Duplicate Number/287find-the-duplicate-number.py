class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        nums.sort()
        for i,num in enumerate(nums):
            if num == nums[i-1]:
                return num
        