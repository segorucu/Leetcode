class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        sm = nums.pop(0)
        one = min(nums)
        nums.remove(one)
        two = min(nums)
        return sm + one + two
        
        