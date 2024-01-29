class Solution:
    def minCost(self, costs: List[List[int]]) -> int:

        HOUSES = len(costs)
        dp = [3*[0] for _ in range(HOUSES)]
        for i in range(3):
            dp[0][i] = costs[0][i]

        for h in range(1,HOUSES):
            dp[h][0] = costs[h][0] + min(dp[h-1][1],dp[h-1][2])
            dp[h][1] = costs[h][1] + min(dp[h-1][0],dp[h-1][2])
            dp[h][2] = costs[h][2] + min(dp[h-1][0],dp[h-1][1])

        return min(dp[-1])
        