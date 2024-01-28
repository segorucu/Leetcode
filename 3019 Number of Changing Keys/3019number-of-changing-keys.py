class Solution:
    def countKeyChanges(self, s: str) -> int:
        
        s = s.lower()
        ans = 0
        for i in range(1,len(s)):
            if s[i] != s[i-1]:
                ans += 1
        
        
        return ans
        