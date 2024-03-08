class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        counter = collections.Counter(nums)
        maxval = max(counter.values())
        
        count = 0
        for key,val in counter.items():
            if val == maxval:
                count += 1
        
        
        return maxval * count
        