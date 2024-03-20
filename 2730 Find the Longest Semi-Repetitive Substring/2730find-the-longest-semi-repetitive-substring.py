class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        
        n = len(s)
        arr = n * [False]
        for i in range(n-1):
            if s[i] == s[i+1]:
                arr[i] = True

        tot = 0
        l = r = 0
        ans = 1
        while r < n:
            if r > 0 and arr[r-1]:
                tot += 1
            while tot > 1:
                if arr[l]:
                    tot -= 1
                l += 1
            r += 1
            ans = max(ans,r-l)
        return ans