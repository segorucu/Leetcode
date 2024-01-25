class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)

        L = [(m+1) * [0] for _ in range(n+1)]
        for i in range(1,n+1):
            c1 = text2[i-1]
            for j in range(1,m+1):
                c2 = text1[j-1]
                if c1 == c2:
                    L[i][j] = L[i-1][j-1] + 1
                else:
                    L[i][j] = max(L[i-1][j],L[i][j-1])

        return L[-1][-1]

        