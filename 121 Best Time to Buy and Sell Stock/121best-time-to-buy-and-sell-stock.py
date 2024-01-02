class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        minval = float('inf')
        ans = 0
        for price in prices:
            ans = max(ans,price-minval)
            if price < minval:
                minval = price

        return ans
