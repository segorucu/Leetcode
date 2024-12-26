from functools import cache
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        @cache
        def backtrack(i,sm):
            if i == len(nums):
                if sm == target:
                    return 1
                return 0

            return backtrack(i+1,sm+nums[i]) + backtrack(i+1,sm-nums[i])


        return backtrack(0,0)