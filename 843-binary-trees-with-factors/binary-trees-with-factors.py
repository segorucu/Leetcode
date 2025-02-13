class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:

        n = len(arr)
        dp = collections.defaultdict(int)
        arr.sort()
        MOD = 10**9+7

        # print(arr)
        for a in arr:
            dp[a] = 0

        tot = 0
        for i in range(n):
            dp[arr[i]] += 1
            for j in range(i):
                curr = arr[i] * arr[j]
                if curr in dp:
                    dp[curr] += (2 * dp[arr[i]] * dp[arr[j]]) % MOD
                    dp[curr] = dp[curr] % MOD
                    # print(i,j,dp)
            if arr[i] ** 2 in dp:
                dp[arr[i]**2] = (dp[arr[i]] ** 2) % MOD
                dp[arr[i]**2] = dp[arr[i]**2] % MOD

            tot += dp[arr[i]]
            tot = tot % MOD

        # print(dp)
        return tot

        
