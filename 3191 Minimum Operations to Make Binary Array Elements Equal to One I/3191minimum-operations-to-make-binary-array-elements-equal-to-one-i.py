from itertools import groupby
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        ops = 0
        for i, num in enumerate(nums):
            if nums[i] == 0:
                if i <= len(nums)-3:
                    for j in range(3):
                        nums[i+j] = nums[i+j] ^ 1
                ops += 1

        if len(nums) == sum(nums):
            return ops
                
        return -1