from functools import cache
class Solution:
    def __init__(self):
        self.ans = float("inf")
    def lastStoneWeightII(self, stones: List[int]) -> int:

        totalweight = sum(stones)
        n = len(stones)
        target = ceil(totalweight / 2)

        @cache
        def dfs(i,total):
            if i == n or total >= target:
                return abs(2*total-totalweight)

            return min(dfs(i+1,total),dfs(i+1,total+stones[i]))

        return dfs(0,0)
        
