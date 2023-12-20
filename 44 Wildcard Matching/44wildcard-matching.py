class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        n = len(s)
        m = len(p)
        dp = [(n+1)*[False] for _ in range(m+1)]
        dp[0][0] = True
        left = 1
        while left <= m and p[left-1] == "*":
            dp[left][0] = True
            left += 1
            # print(left)

        for i in range(1,m+1):
            for j in range(1,n+1):
                if dp[i-1][j-1] == True:
                    if s[j-1] == p[i-1]:
                        dp[i][j] = True
                    elif p[i-1] == "?" or p[i-1] == "*":
                        dp[i][j] = True
                elif dp[i-1][j] == True:
                    if p[i-1] == "*":
                        dp[i][j] = True
                elif dp[i][j-1] == True:
                    if p[i-1] == "*":
                        dp[i][j] = True

        # print(dp)
        return dp[-1][-1]
        