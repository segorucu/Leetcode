from functools import cache
class Solution:
    def numWays(self, n: int, k: int) -> int:
        
        if n > 2 and k == 1:
            return 0

        stack = []
        @cache
        def backtrack(n):
            if n <= 2:
                return k**n

            return (k-1) * (backtrack(n-1) + backtrack(n-2))

        return backtrack(n)