class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        
        for a,b in zip(nums[0:-1],nums[1:]):
            if a % 2 == b % 2:
                return False

        return True