from functools import cache
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
#   state = 0 => bought
#   state = 1 => skip
#   state = 2 => sold
        @cache
        def dp(days,state,k):
            if k == 2:
                return 0
            if days == len(prices):
                return 0

            if state == 0:
                one = dp(days+1,0,k)  # skip
                two = dp(days+1,2,k+1)+prices[days]      # sell

            elif state == 1:
                one = dp(days+1,0,k)-prices[days]  #buy
                two = dp(days+1,1,k)               #skip

            elif state == 2:
                one = dp(days+1,2,k)                #skip
                two = dp(days+1,0,k)-prices[days]  #buy
            return max(one,two)



        return dp(0,1,0)
        