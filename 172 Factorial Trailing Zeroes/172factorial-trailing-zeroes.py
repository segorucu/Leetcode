class Solution:
    def trailingZeroes(self, n: int) -> int:
        
        start = 5
        sm = 0
        while start <= n:
            sm += (n // start)
            start *= 5

        return sm