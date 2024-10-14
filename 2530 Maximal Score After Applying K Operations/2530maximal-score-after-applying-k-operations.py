from heapq import heapify, heappop, heappush
import math
class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        
        hp = []
        for num in nums:
            heappush(hp, -num)

        sm = 0
        while k:
            curr = heappop(hp)
            curr = -curr
            sm += curr
            curr = - math.ceil(curr / 3)
            heappush(hp, curr)
            k -= 1

        return sm