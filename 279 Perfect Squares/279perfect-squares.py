class Solution:
    def numSquares(self, n: int) -> int:

        squares = [1]
        i = 2
        while i ** 2 <= n:
            squares.append(i**2)
            i += 1

        dp = (n+1) * [0]
        for i in range(1,n+1):
            dum = float("inf")
            for sq in squares:
                if sq > i:
                    break
                dum = min(dum,dp[i-sq]+1)
            dp[i] = dum

        return dp[-1]


