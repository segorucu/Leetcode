class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        
        n = len(grid)

        for row in range(n):
            c = 0
            r = row
            currarr = []
            for step in range(n-r):
                currarr.append(grid[r][c])
                r += 1
                c += 1
            currarr.sort(reverse = True)
            c = 0
            r = row
            for step in range(n-r):
                grid[r][c] = currarr[step]
                r += 1
                c += 1


        for col in range(1,n):
            c = col
            r = 0
            currarr = []
            for step in range(n-col):
                currarr.append(grid[r][c])
                r += 1
                c += 1
            currarr.sort()
            c = col
            r = 0
            for step in range(n-col):
                grid[r][c] = currarr[step]
                r += 1
                c += 1


        return grid
