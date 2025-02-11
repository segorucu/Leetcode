from functools import cache

class Solution:
    def minCost(self, n: int, cost: List[List[int]]) -> int:
        
        @cache
        def dp(left,cl,cr):
            if left * 2  == n:
                if cl == cr:
                    return inf
                return 0

            total = inf
            for l in range(3):
                for r in range(3):
                    if l != r and l != cl and r != cr:
                        total = min(total, 
                                dp(left+1,l,r)+cost[left][l]+cost[n-left-1][r])
            return total

        return dp(0,-1,-1)
