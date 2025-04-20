class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        alphabet = set(s)
        n = len(s)
        ans = 0
        for truth in alphabet:
            r = 0    
            l = 0
            changed = 0
            while r < n:
                if s[r] != truth:
                    changed += 1
                while changed > k:
                    if s[l] != truth:
                        changed -= 1
                    l += 1
                r += 1
                ans = max(ans, r-l)
        return ans