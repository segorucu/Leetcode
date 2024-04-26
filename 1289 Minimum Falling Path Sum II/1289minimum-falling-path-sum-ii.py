class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:


        n = len(grid)


        for row in range (1,n):
            for col in range(n):
                prerow = grid[row-1]
                minpath = inf
                for pre in range(n):
                    if col == pre:
                        continue
                    if prerow[pre] < minpath:
                        minpath = prerow[pre]
                grid[row][col] += minpath

        # print(grid)


        return min(grid[-1])      