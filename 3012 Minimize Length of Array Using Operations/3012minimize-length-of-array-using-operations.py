from heapq import heapify, heappop, heappush
class Solution:
    def minimumArrayLength(self, nums: List[int]) -> int:
        
        counter = collections.Counter(nums)
        minval = min(counter.keys())
        
        for num in nums:
            if 0 < num % minval < minval:
                return 1

        zeros = counter[minval] // 2
        n = counter[minval] % 2
            
            
        return zeros + n
            
            
        
        