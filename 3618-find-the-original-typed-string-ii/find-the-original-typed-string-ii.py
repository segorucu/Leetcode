class Solution:
    def possibleStringCount(self, word: str, k: int) -> int:

        MOD = 10**9 + 7
        total = 1
        stack = []
        for _,v in groupby(word):
            v = len(list(v))
            stack.append(v)
            total *= v
            total = total % MOD

        ngroups = len(stack)

        if k <= ngroups:
            return total

        dp = [k * [0] for _ in range(ngroups+1)]
        dp[0][0] = 1

        for group in range(1,ngroups+1):
            curr = stack[group-1]
            sm = 0
            for i in range(1,k):
                dp[group][i] = dp[group][i-1] + dp[group-1][i-1]
                if i - curr - 1 >= 0:
                    dp[group][i] -= dp[group-1][i-curr-1]
                dp[group][i] = dp[group][i] % MOD
                    
        sm = 0
        for i in range(k):
            sm += dp[ngroups][i]
            sm = sm % MOD

        return (total - sm) % MOD

        """

          0 1 2 3 4
        0 
        1
        2
        


        """

        
