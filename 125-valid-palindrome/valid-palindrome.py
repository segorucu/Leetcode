class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s = s.lower()
        txt = []
        lower = ord("a")
        upper = ord("z")
        for a in s:
            if lower <= ord(a) <= upper or a in "0123456789":
                txt.append(a)
        
        n = len(txt)
        l = 0
        r = n-1
        while l < r:
            if txt[l] != txt[r]:
                return False
            l += 1
            r -= 1


        return True