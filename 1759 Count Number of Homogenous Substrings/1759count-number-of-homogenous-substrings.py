from itertools import groupby
class Solution:
    def countHomogenous(self, s: str) -> int:

        MOD = 10**9 + 7
        sm = 0
        for k,v in groupby(s):
            count = len(list(v))
            sm += (count*(count+1) // 2) % MOD


        return sm
        