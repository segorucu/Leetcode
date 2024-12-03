from functools import cache
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        m = len(matrix)
        n = len(matrix[0])

        directions = [(0,1),(1,0),(0,-1),(-1,0)]

        def valid(r,c):
            return 0 <= r < m and 0 <= c < n

        @cache
        def dfs(r,c):
            maxlen = 0
            for dr,dc in directions:
                nr,nc = r+dr, c+dc
                if valid(nr,nc) and matrix[nr][nc] > matrix[r][c]:
                    maxlen = max(maxlen, dfs(nr,nc))
            return maxlen+1

        ans = 1
        for r in range(m):
            for c in range(n):
                ans = max(ans, dfs(r,c))
        return ans
        