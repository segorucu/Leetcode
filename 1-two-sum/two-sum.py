from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = set()
        for i,num in enumerate(nums):
            if target - num in seen:
                return i, nums.index(target-num)
            seen.add(num)
        