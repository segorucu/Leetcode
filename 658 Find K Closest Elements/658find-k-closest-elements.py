from heapq import heappush, heappop, heapify
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        pairs = []
        for i, num in enumerate(arr):
            heappush(pairs,(-abs(num-x),-num))
            if len(pairs) > k:
                heappop(pairs)

        return sorted([-val[1] for val in pairs])