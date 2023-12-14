class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        onesRow = m * [0]
        onesCol = n * [0]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    onesRow[i] += 1
                    onesCol[j] += 1

        diff =[n*[0] for _ in range(m)]
        tot = m + n
        for i in range(m):
            for j in range(n):
                diff[i][j] = 2*(onesRow[i] + onesCol[j]) - tot

        return diff
        