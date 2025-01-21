class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        

        n = len(grid[0])
        if n == 1:
            return 0 

        toprow = sum(grid[0])
        bottom = 0
        ans = inf
        for c in range(n):
            toprow -= grid[0][c]
            if c > 0:
                bottom += grid[1][c-1]
            cand = max(toprow, bottom) 
            # print(cand)
            ans = min(ans, cand)
                 
        return ans