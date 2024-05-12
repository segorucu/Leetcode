class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:

        n = len(grid)
        maxLocal = [(n-2)*[0] for _ in range(n-2)]


        for i in range(n-2):
            for j in range(n-2):
                maxval = 0
                for r in range(3):
                    for c in range(3):
                        maxval = max(maxval, grid[i+r][j+c])
                maxLocal[i][j] = maxval

        return maxLocal
                
        