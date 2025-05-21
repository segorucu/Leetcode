class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s = s.lower()
        s = s.replace(" ", "")
        txt = []
        for a in s:
            if a.isalnum():
                txt.append(a)
                

        return txt[:] == txt[:][::-1]