class Solution:
    def numberOfMatches(self, n: int) -> int:
        
        if n == 1:
            return 0
        def recurse(n):
            if n == 2:
                return 1
            if n % 2 == 0:
                return recurse(n//2) + n // 2
            else:
                return recurse((n+1)//2) + (n-1) // 2

        
        return recurse(n)