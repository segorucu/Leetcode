from functools import cache
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @cache
        # holding = 0: not holding
        # cooling = 1: 
        # holding = 2
        def df(i,holding):
            if len(prices) == i:
                return 0

            ans = df(i+1,holding)
            if holding == 2:
                ans = max(ans,df(i+1,0)+prices[i])
            elif holding == 1:
                ans = max(ans,df(i+1,2)-prices[i])
            elif holding == 0:
                ans = max(ans,df(i+1,1))

            return ans
        return df(0,1)

            




        return df(0,2)