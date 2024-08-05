class Solution:
    def longestRepeatingSubstring(self, s: str) -> int:

        seen = set()
        n = len(s)
        ans = 0
        for i in range(n):
            for j in range(i+1):
                if s[j:i+1] in seen:
                    ans = max(ans,i+1-j)
                seen.add(s[j:i+1])

        return ans
        