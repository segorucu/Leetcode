from functools import cache
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        n = len(s1)
        m = len(s2)
        if n + m != len(s3):
            return False
        dp = [(n+1)*[False] for _ in range(m+1)]
        dp[0][0] = True
        for j in range(n):
            if s1[j] == s3[j]:
                dp[0][j+1] = True
            else:
                break

        for i in range(m):
            if s2[i] == s3[i]:
                dp[i+1][0] = True
            else:
                break

        for i in range(m):
            for j in range(n):
                # print(i,j,s1[j],s2[i],s3[i+j])
                if dp[i][j+1] and s2[i] == s3[i+j+1]:
                    dp[i+1][j+1] = True
                elif dp[i+1][j] and s1[j] == s3[i+j+1]:
                    dp[i+1][j+1] = True
                else:
                    dp[i+1][j+1] = False

        print(dp)
        return dp[-1][-1]