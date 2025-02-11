class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        
        m = len(part)
        while part in s:
            start = s.index(part)
            s = s[0:start] + s[start+m:]

        return s