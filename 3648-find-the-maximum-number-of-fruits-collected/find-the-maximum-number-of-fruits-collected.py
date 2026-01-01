class Solution:
    def maxCollectedFruits(self, fruits: List[List[int]]) -> int:
        
        
        one = 0
        n = len(fruits)

        def valid(r,c):
            return 0 <= r < n and 0 <= c < n

        for i in range(n):
            one += fruits[i][i]

        dp = [n * [-100000] for _ in range(n-1)]
        dp[0][n-1] = fruits[0][n-1]

        for r in range(1,n-1):
            for c in range(r,n):
                maxval = dp[r-1][c]
                if valid(r-1,c-1):
                    maxval = max(maxval, dp[r-1][c-1])
                if valid(r-1,c+1):
                    maxval = max(maxval, dp[r-1][c+1])
                if r != c:
                    dp[r][c] = maxval + fruits[r][c]
                else:
                    dp[r][c] = maxval

        two = dp[n-2][n-1]

        dp = [n * [-100000] for _ in range(n)]
        dp[n-1][0] = fruits[n-1][0]

        for c in range(1,n-1):
            for r in range(c,n):
                maxval = dp[r][c-1]
                if valid(r-1,c-1):
                    maxval = max(maxval, dp[r-1][c-1])
                if valid(r+1,c-1):
                    maxval = max(maxval, dp[r+1][c-1])
                if r != c:
                    dp[r][c] = maxval + fruits[r][c]
                else:
                    dp[r][c] = maxval

        three = dp[n-1][n-2]

        return one + two + three