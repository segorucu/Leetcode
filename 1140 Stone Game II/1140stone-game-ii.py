from functools import cache
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:

        n = len(piles)
        @cache
        def dp(alice,M,i):
            if i == len(piles):
                return 0
       
            if alice:
                ans = 0
                sm = 0
                for j in range(i, min(i+2*M, n)):
                    sm += piles[j]
                    X = j-i+1
                    val = dp(not alice, max(M,X), j+1) + sm
                    ans = max(ans, val)
            else:
                ans = inf
                for j in range(i, min(i+2*M, n)):
                    X = j-i+1
                    val = dp(not alice, max(M,X), j+1)
                    ans = min(ans, val)
                
            return ans


        return dp(True,1,0)