class Solution:
    def candy(self, ratings: List[int]) -> int:
        

        n = len(ratings)
        dp = (n) * [1]
        change = True
        while change:
            change = False
            for i,val in enumerate(ratings):
                if i > 0 and val > ratings[i-1] and dp[i-1]+1 > dp[i]:
                    dp[i] = dp[i-1]+1
                    change = True
                # if i < n - 1 and val > ratings[i+1] and dp[i+1]+1 > dp[i]:
                #     dp[i] = dp[i+1]+1
                #     change = True

            for i in range(n-1,-1,-1):
                val = ratings[i]
                # if i > 0 and val > ratings[i-1] and dp[i-1]+1 > dp[i]:
                #     dp[i] = dp[i-1]+1
                #     change = True
                if i < n - 1 and val > ratings[i+1] and dp[i+1]+1 > dp[i]:
                    dp[i] = dp[i+1]+1
                    change = True

        return sum(dp)

