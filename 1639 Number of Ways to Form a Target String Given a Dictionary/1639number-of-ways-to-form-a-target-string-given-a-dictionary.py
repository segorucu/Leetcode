from functools import cache
class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        
        freq = collections.defaultdict(lambda: collections.defaultdict(int))
        MOD = 10**9 + 7
        n = len(words[0])
        m = len(target)
        for word in words:
            for i,a in enumerate(word):
                freq[i][a] += 1
        @cache
        def dp(i,j):
            if j == m:
                return 1
            if i == n:
                return 0

            count = 0
            for k in range(i,n):
                if n-k < m-j:
                    break
                if freq[k][target[j]] > 0:
                    count += dp(k+1,j+1) * freq[k][target[j]]
            return count % MOD

        return dp(0,0)
