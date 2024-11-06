from itertools import groupby
class Solution:
    def compressedString(self, word: str) -> str:

        ans = []
        for a,b in groupby(word):
            length = len(list(b))
            while length:
                tmp = min(9,length)
                ans.append(str(tmp)+a)
                length -= tmp

        return "".join(ans)

        