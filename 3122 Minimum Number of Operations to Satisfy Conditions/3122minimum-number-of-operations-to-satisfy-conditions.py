class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        cols = collections.defaultdict(dict)
        for r in range(m):
            for c in range(n):
                val = grid[r][c]
                if val in cols[c]:
                    cols[c][val] += 1
                else:
                    cols[c][val] = 1
        
        dp = [[0 for i in range(10)] for i in range(n)]
        for i in range(10):
            if i in cols[0]:
                dp[0][i] = m - cols[0][i]
            else:
                dp[0][i] = m

        for col in range(1,n):
            for num in range(10):
                minval = inf
                for prev in range(10):
                    if prev != num and dp[col-1][prev] < minval:
                        minval = dp[col-1][prev]
                if num in cols[col]:
                    dp[col][num] = minval + m - cols[col][num]
                else:
                    dp[col][num] = minval + m
        
        ans = inf
        for num in range(10):
            ans = min(ans, dp[-1][num])

        return ans
        