class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        

        m = len(grid)
        n = len(grid[0])

        rend = x + k - 1
        for r in range(x, x + k //2):
            for c in range(y, y + k):
                grid[r][c], grid[rend][c] = grid[rend][c], grid[r][c]
            rend -= 1

        return grid