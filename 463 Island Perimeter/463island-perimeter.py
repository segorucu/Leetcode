class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        nrows = len(grid)
        ncols = len(grid[0])

        directions = ([0,1],[1,0],[0,-1],[-1,0])

        def valid(row,col):
            return 0 <= row < nrows and 0 <= col < ncols

        ans = 0
        for row in range(nrows):
            for col in range(ncols):
                if grid[row][col] == 1:
                    for move in directions:
                        newy, newx = row + move[0], col + move[1] 
                        if not valid(newy,newx):
                            ans += 1
                        elif grid[newy][newx] == 0:
                            ans += 1
        return ans


                        
