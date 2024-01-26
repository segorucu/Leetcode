from functools import cache
class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        if maxMove == 0:
            return 0

        # @cache
        # def valid(row,col):
        #     return 0 <= row < m and 0 <= col < n

        MOD = 10**9 + 7

        @cache
        def dfs(row,col,step):
            # print(row, col, step)
            if step > maxMove:
                return 0

            if not (0 <= row < m and 0 <= col < n):
                return 1

            tot = 0
            tot += dfs(row+1, col, step + 1)
            tot += dfs(row, col+1, step + 1)
            tot += dfs(row-1, col, step + 1)
            tot += dfs(row, col-1, step + 1)

            return tot % MOD

        return dfs(startRow, startColumn, 0)

