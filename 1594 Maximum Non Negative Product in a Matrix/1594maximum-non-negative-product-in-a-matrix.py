from functools import cache
class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        
        MOD = 10**9 + 7
        m = len(grid)
        n = len(grid[0])
        ans = [-1]

        @cache
        def backtrack(i,j,curr):
            if i == m-1 and j == n-1:
                ans[0] = max(ans[0], curr)

            if i < m-1:
                backtrack(i+1, j, curr*grid[i+1][j])
            if j < n-1:
                backtrack(i, j+1, curr*grid[i][j+1])


        backtrack(0,0,grid[0][0])
        if ans[0] < 0:
            return -1

        return ans[0] % MOD