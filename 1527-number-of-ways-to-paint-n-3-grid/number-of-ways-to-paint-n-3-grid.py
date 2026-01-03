class Solution:
    def numOfWays(self, n: int) -> int:

        ai = bi = 6
        MOD = 10 ** 9 + 7

        for i in range(n-1):
            ai, bi = ((3 * ai) % MOD + (2 * bi) % MOD) % MOD, ((2 * ai) % MOD + (2 * bi) % MOD) % MOD
            ai = ai % MOD
            bi = bi % MOD

        return (ai + bi) % MOD