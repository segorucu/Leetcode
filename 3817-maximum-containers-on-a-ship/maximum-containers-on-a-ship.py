class Solution:
    def maxContainers(self, n: int, w: int, maxWeight: int) -> int:
        
        if n**2 * w <= maxWeight:
            return n**2


        return maxWeight // w
        