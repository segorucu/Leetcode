from itertools import groupby
class Solution:
    def makeFancyString(self, s: str) -> str:
        ans = ""
        for a,b in groupby(s):    
            size = min(len(list(b)),2)
            ans += size * a

        return ans 