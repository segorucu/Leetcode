class Solution:
    def longestIdealString(self, s: str, k: int) -> int:

        mp = {}
        n = len(s)
        dp = n * [0]

        for i, c in enumerate(s):
            maxval = 0
            curr = ord(c)
            for prev in range(curr-k,curr+k+1):
                if prev in mp:
                    ind = mp[prev]
                    maxval = max(maxval, dp[ind])
            dp[i] = maxval + 1
            mp[ord(c)] = i

        return max(dp)
            
        