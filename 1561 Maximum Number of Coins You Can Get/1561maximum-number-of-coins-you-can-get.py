class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        n = len(piles) // 3
        piles = sorted(piles)
                    
        sm = 0
        for i in range(n):
            sm += piles[n+2*i]
            
        return sm