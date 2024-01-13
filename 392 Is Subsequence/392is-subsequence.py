class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        if len(s) == 0:
            return True
        elif len(s) > len(t):
            return False

        l = 0
        for p, c in enumerate(t):
            if c == s[l]:
                l += 1
                if l == len(s):
                    return True
        return l == len(s)
        