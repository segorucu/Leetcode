from itertools import groupby
class Solution:
    def numSub(self, s: str) -> int:
        
        MOD = 10**9+7

        ans = 0
        for k,v in groupby(s):
            v = len(list(v))
            if k == "1":
                tmp = (v * (v+1)) // 2
                ans = ans + tmp
                ans = ans % MOD

        return ans

