class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        

        dp = (days[-1]+1) * [0]
        dayset = set(days)
        for i in range(1,days[-1]+1):
            if i not in dayset:
                dp[i] = dp[i-1]
                continue
            daily = dp[i-1] + costs[0]
            if i >= 7:
                weekly = dp[i-7] + costs[1]
            else:
                weekly = costs[1]
            if i >= 30:
                monthly = dp[i-30] + costs[2]
            else:
                monthly = costs[2]
            dp[i] = min(daily, weekly, monthly)


        return dp[-1]