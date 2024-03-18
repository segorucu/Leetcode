class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        
        if len(s) == 0:
            return ""

        c = collections.Counter(s)
        pos = 0
        for i,a in enumerate(s):
            if a < s[pos]: pos = i
            c[a] -= 1
            if c[a] == 0:
                break

        return s[pos] + self.removeDuplicateLetters(s[pos:].replace(s[pos],""))