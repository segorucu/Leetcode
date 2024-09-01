from itertools import islice
class Solution:
    def stringHash(self, s: str, k: int) -> str:

        n = len(s)
        m = n // k
        base = ord("a")
        ans = []
        for i in range(m):
            beg = i*k
            end = beg + k
            curr = s[beg:end]
            tmp = 0
            for a in curr:
                tmp += ord(a) - base
            tmp = tmp % 26
            tmp += base 
            tmp = chr(tmp)
            ans.append(tmp)

        return "".join(ans)
        