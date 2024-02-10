class Solution:
    def countSubstrings(self, s: str) -> int:

        n = len(s)

        ans = 0
        for i in range(n):
            ans += 1
            l = i - 1
            r = i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                ans += 1
                l -= 1
                r += 1

        for l in range(n-1):
            r = l + 1
            while l >= 0 and r < n and s[l] == s[r]:
                ans += 1
                l -= 1
                r += 1
        
        return ans
        