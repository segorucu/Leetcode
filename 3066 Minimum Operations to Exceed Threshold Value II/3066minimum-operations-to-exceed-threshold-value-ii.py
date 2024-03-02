from heapq import heapify, heappop, heappush
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        
        heapify(nums)
        
        ops = 0
        while nums[0] < k:
            first = heappop(nums)
            second = heappop(nums)
            dum = 2*first + second
            heappush(nums,dum)
            ops += 1
        return ops
        
        