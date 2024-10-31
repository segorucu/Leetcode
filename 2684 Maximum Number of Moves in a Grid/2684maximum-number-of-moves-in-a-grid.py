class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])

        dp = [n*[0] for _ in range(m)]
        maxval = 0
        for col in range(1,n):
            for row in range(m):
                for direc in [-1,0,1]:
                    if (0 <= row+direc < m) and grid[row+direc][col-1] < grid[row][col]:
                        if col > 1 and dp[row+direc][col-1] == 0:
                            continue
                        dp[row][col] = max(dp[row][col],dp[row+direc][col-1]+1)
                        maxval = max(maxval, dp[row][col])
                            

        return maxval
