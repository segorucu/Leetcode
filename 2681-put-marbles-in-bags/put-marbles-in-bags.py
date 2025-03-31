from functools import cache
class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        
        n = len(weights)
        larger = []
        smaller = []
        for x,y in pairwise(weights):
            larger.append(x+y)
            smaller.append(x+y)

        larger.sort(reverse=True)
        smaller.sort()
        return sum(larger[0:k-1]) - sum(smaller[0:k-1])

