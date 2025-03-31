from functools import cache
class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        
        n = len(weights)
        larger = []
        smaller = []
        for x,y in pairwise(weights):
            heappush(larger,-x-y)
            heappush(smaller,x+y)
            while len(larger) > k -1:
                heappop(larger)
                heappop(smaller)

        return sum(larger) + sum(smaller)

