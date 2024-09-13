from functools import cache
class Solution:
    def getSmallestString(self, s: str) -> str:
        
        @cache
        def recurse(s,i,swapped):
            if i == len(s):
                return s

            first = None
            if not swapped and int(s[i]) % 2 == int(s[i-1]) % 2:
                first = recurse(s[0:i-1]+s[i]+s[i-1]+s[i+1:], i+1, True)
            second = recurse(s,i+1,swapped)
            if first:
                return min(first, second)
            return second
            

        return recurse(s,1,False)
        