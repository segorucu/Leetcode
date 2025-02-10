class Solution:
    def clearDigits(self, s: str) -> str:
        
        s = list(s)
        r = 0
        while r < len(s):
            if s[r].isdigit():
                s.pop(r)
                s.pop(r-1)
                r -= 1
            else:
                r += 1 


        return "".join(s)