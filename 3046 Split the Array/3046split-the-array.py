class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        
        counter = collections.Counter(nums)
        val = max(counter.values())
        
        if val > 2:
            return False
        else:
            return True
        