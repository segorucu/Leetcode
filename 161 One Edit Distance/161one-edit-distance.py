class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        
        if s == t:
            return False
        m = len(s)
        n = len(t)
        if abs(m-n) >= 2:
            return False

        i = 0
        while i < m and i < n:
            if s[i] != t[i]:
                if s[i+1:] == t[i+1:]:
                    return True
                if s[i:] == t[i+1:]:
                    return True
                if s[i+1:] == t[i:]:
                    return True
                return False
            i += 1
        if m == n:
            return False
        return True
