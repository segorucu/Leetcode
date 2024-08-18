from functools import cache
class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:

        MOD = 10**9+7
        endPos -= startPos

        @cache
        def dp(currpos, left):
            if left == 0:
                if currpos == 0:
                    return 1
                return 0

            return (dp(currpos-1,left-1) + dp(currpos+1,left-1)) % MOD

        return dp(endPos, k)

        
        

