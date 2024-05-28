class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        
        n = len(s)
        l = r = 0
        sm = 0
        ans = 0
        for r in range(n):
            val = abs(ord(s[r])-ord(t[r]))
            sm += val
            while sm > maxCost:
                sm -= abs(ord(s[l])-ord(t[l]))
                l += 1
            ans = max(ans,r-l+1)
        return ans