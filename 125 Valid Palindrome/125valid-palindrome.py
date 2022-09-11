class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s = s.lower()
        s = s.replace(" ","")
        s = list(filter(lambda ch: ch.isalnum(), s))
                
        N = len(s)
        hi = N-1
        lo = 0
        while(lo<=hi):
            if s[lo] != s[hi]:
                return False
            lo += 1
            hi -= 1
        return True
        
        
        