class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:

        def valid(r,c):
            rsum = 3*[0]
            csum = 3*[0]
            first = second = 0
            seen = set()
            for i in range(3):
                for j in range(3):
                    if grid[r+i][c+j] in seen:
                        return 0
                    if grid[r+i][c+j] > 9 or grid[r+i][c+j] < 1:
                        return 0
                    seen.add(grid[r+i][c+j])
                    rsum[i] += grid[r+i][c+j]
                    csum[j] += grid[r+i][c+j]
                    if i == j:
                        first += grid[r+i][c+j]
                    if i + j == 2:
                        second += grid[r+i][c+j]
            curr = rsum[0]
            for i in range(3):
                if rsum[i] != curr:
                    return 0
                if csum[i] != curr:
                    return 0
                if curr != first or curr != second:
                    return 0
            return 1

        Nrows = len(grid)
        Ncols = len(grid[0])
        ans = 0
        for r in range(Nrows-2):
            for c in range(Ncols-2):
                ans += valid(r,c)
                
        return ans
                    
        