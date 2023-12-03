class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        hold = [[0] * (k + 1) for __ in range(n)]
        nohold = [[0] * (k + 1) for __ in range(n)]

        for i in range(k+1):
            hold[0][i] = -prices[0]

        for i in range(1,n):
            for rem in range(1,k+1):
                hold[i][rem] = max(hold[i-1][rem],nohold[i-1][rem-1]-prices[i])
                nohold[i][rem] = max(nohold[i-1][rem],hold[i-1][rem]+prices[i])
        
        return max(nohold[-1])