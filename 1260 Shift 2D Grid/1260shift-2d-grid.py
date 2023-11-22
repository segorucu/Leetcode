class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:

        m = len(grid)
        n = len(grid[0])
        k = k % (m*n)

        new_grid = [n*[0] for i in range(m)]
        for i in range(m):
            for j in range(n):
                dy = (j + k) // n
                dx = (j + k) % n
                new_grid[(i+dy)%m][dx] = grid[i][j]

        return new_grid
        