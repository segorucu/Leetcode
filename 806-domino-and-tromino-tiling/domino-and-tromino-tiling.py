class Solution:
    def numTilings(self, n: int) -> int:

        MOD = 10**9+7
        f = (n+1) * [0]
        p = (n+1) * [0]
        f[1] = 1
        p[1] = 0
        if n > 1:
            f[2] = 2
            p[2] = 1
        for i in range(3,n+1):
            f[i] = f[i-1] + f[i-2] + 2 * p[i-1]
            p[i] = f[i-2] + p[i-1]
        

        return f[-1] % MOD