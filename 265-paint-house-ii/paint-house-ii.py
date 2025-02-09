from functools import cache
class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        
        n = len(costs)
        k = len(costs[0])

        @cache
        def dp(i,lastk):
            if i == n:
                return 0

            ans = inf
            for color in range(k):
                if color == lastk:
                    continue
                
                ans = min(ans, dp(i+1,color) + costs[i][color])
            return ans
            
        return dp(0,-1)