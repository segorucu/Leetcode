from functools import cache
class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        
        def reverserow(r):
            for c in range(n):
                grid[r][c] ^= 1
        
        def reversecol(c):
            for r in range(m):
                grid[r][c] ^= 1
        
        for row in range(m):
            if grid[row][0] == 0:
                reverserow(row)

        for col in range(1,n):
            ones = 0
            for row in range(m):
                if grid[row][col] == 1:
                    ones += 1
            zeros = m - ones
            if zeros > ones:
                reversecol(col)


        sm = 0
        for r in range(m):
            num = 0
            i = 0
            for c in range(n-1,-1,-1):
                num |= (grid[r][c] << i)
                i += 1
            sm += num

    
        return sm