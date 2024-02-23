from heapq import heappush, heappop, heapify
class Solution:



    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        prices = n * [float("inf")]
        prices[src] = 0
        prev = prices.copy()
        for _ in range(k+1):
            for s,d,c in flights:
                dum = prev[s] + c
                if dum < prices[d]:
                    prices[d] = dum
            prev = prices.copy()
        
        if prices[dst] == float("inf"):
            return -1
        return prices[dst]

    
        