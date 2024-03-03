class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        
        m = len(grid)
        n = len(grid[0])
        prefix = n *[0]
        
        cnt = 0
        for r in range(m):
            currsm = 0
            for c in range(n):
                currsm += grid[r][c]
                prefix[c] += currsm
                if prefix[c] <= k:
                    cnt += 1
        return cnt
                    