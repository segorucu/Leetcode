class Solution:
    def longestValidParentheses(self, s: str) -> int:
        
        
        n = len(s)
        if n <= 1:
            return 0
        dp = n * [0]
        if s[0:2] == "()":
            dp[1] = 2
        for i in range(2,n):
            if s[i] == ")":
                if s[i-1] == "(":
                    dp[i] = dp[i-2] + 2
                elif i-dp[i-1]-1 >= 0 and s[i-dp[i-1]-1] == "(":
                    dp[i] = dp[i-1] + dp[i-dp[i-1]-2] + 2
        return max(dp)

