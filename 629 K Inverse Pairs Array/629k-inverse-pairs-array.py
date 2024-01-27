from functools import cache
class Solution:
    def kInversePairs(self, n: int, k: int) -> int:

        MOD = 10**9 + 7

        if k > n * (n-1) / 2:
            return 0
        elif k == n * (n-1) / 2:
            return 1
        if k == 0:
            return 1

        @cache
        def backtrack(n,k):
            if k == 0:
                return 1
            if n <= 0 or k < 0:
                return 0
            

            tot = backtrack(n-1,k) + backtrack(n,k-1) - backtrack(n-1,k-n)
            return tot % MOD
            

        return backtrack(n,k)