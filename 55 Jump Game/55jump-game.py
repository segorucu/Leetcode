class Solution:
    def canJump(self, nums: List[int]) -> bool:


        maxind = 0
        for i in range(len(nums)-1):
            maxind = max(maxind,i+nums[i])
            if maxind == i:
                return False
        return True