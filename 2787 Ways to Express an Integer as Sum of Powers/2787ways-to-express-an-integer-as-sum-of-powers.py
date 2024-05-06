class Solution:
    def numberOfWays(self, n: int, x: int) -> int:


        MOD = 10**9 + 7
        i = 1
        unique = []
        while i ** x <= n:
            unique.append(i ** x)
            i += 1

        m = len(unique)
        @cache
        def backtrack(i,curr):
            add = pow(i, x , MOD)
            if curr == n:
                return 1
            elif curr > n:
                return 0
            if add + curr > n:
                return 0

            
            total = backtrack(i+1,curr+add)
            total += backtrack(i+1,curr)
            return total % MOD

            
        return backtrack(1,0)
        