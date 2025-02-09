from functools import cache
class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        
        n = len(costs)
        k = len(costs[0])

        @cache
        def dp(i,mask):
            if i == n:
                return 0

            ans = inf
            for color in range(k):
                if (mask & (1 << color)):
                    continue
                
                newmask = 1 << color
                ans = min(ans, dp(i+1,newmask) + costs[i][color])
            return ans
            
        return dp(0,0)