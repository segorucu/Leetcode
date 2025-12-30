class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        ans = 0

        for r in range(m):
            for c in range(n):
                if grid[r][c] < 0:
                    ans += n - c
                    break
        return ans
            
