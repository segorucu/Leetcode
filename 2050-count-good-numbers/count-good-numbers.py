class Solution:
    def countGoodNumbers(self, n: int) -> int:
        
        prod = 1
        MOD = 10**9+7

        fives = (n+1) // 2
        fours = n // 2

        prod = pow(5, fives, MOD)
        prod = (prod * pow(4, fours, MOD)) % MOD

        return prod