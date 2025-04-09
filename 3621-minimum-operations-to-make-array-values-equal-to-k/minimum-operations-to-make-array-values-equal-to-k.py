class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        
        nums = list(set(nums))
        nums.sort()
        if k > nums[0]:
            return -1

        if k == nums[0]:
            return len(nums)-1

        return len(nums)