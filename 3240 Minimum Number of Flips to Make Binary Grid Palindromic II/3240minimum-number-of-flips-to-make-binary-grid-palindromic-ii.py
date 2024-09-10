from functools import cache
class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        
        m = len(grid) 
        n = len(grid[0])
        flips = 0
        for row in range(m // 2):
            for col in range(n // 2):
                ones = 0
                if grid[row][col]:
                    ones += 1
                if grid[m-row-1][col]:
                    ones += 1
                if grid[row][n-col-1]:
                    ones += 1
                if grid[m-row-1][n-col-1]:
                    ones += 1
                flips += min(ones,4-ones)

        
        arr = []
        if m % 2:
            l, r = 0, n-1
            midrow = m // 2
            while l < r:
                arr.append((grid[midrow][l],grid[midrow][r]))
                l += 1
                r -= 1
        if n % 2:
            l, r = 0, m - 1
            midcol = n // 2
            while l < r:
                arr.append((grid[l][midcol],grid[r][midcol]))
                l += 1
                r -= 1

        if n % 2 and m % 2:
            arr.append((grid[midrow][midcol],))

        N = len(arr)
        @cache
        def dp(i,ones):
            ones = ones % 4
            if i == N:
                return ones % 4
            curr = arr[i]
            currlen = len(curr)
            currzeros, currones = 0, 0
            for val in curr:
                if val == 0:
                    currzeros += 1
                else:
                    currones += 1
            allzeroscost = dp(i+1,ones) + currones
            allonescost = dp(i+1,ones+currlen) + currzeros
            return min(allzeroscost,allonescost)

        return flips + dp(0,0)

        