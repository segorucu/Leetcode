class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        
        if nums == sorted(nums):
            return True

        if nums == sorted(nums,reverse=True):
            return True

        return False