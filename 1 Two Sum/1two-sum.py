from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tab = defaultdict(int)
        for i, val in enumerate(nums):
            tab[val] = i
        
        for i, val in enumerate(nums):
            if target-val in tab and tab[target-val] != i:
                return i, tab[target-val]
        