class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:

        m = len(grid)
        n = len(grid[0])

        one = 0
        for row in range(m):
            l = 0
            r = n-1
            while l < r:
                if grid[row][l] != grid[row][r]:
                    one += 1
                l += 1
                r -=1

        two = 0
        for col in range(n):
            l = 0
            r = m-1
            while l < r:
                if grid[l][col] != grid[r][col]:
                    two += 1
                l += 1
                r -= 1
        return min(one, two)

        return ans
        