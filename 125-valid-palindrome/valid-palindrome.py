class Solution:
    def isPalindrome(self, s: str) -> bool:

        digits = {"0","1","2","3","4","5","6","7","8","9"}
        
        s = s.lower()
        txt = []
        lower = ord("a")
        upper = ord("z")
        for a in s:
            if lower <= ord(a) <= upper or a in digits:
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