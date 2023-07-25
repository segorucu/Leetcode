class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:

        heapq.heapify(weight)
        n = len(weight)
        
        tot = 0
        i = 0
        while weight:
            w = heapq.heappop(weight)
            tot += w
            if tot > 5000:
                return i
            i += 1

        return n