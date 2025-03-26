class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        
        arr = []
        m = len(grid)
        n = len(grid[0])

        for r in range(m):
            for c in range(n):
                arr.append(grid[r][c])

        arr.sort()
        remainder = None
        for a in arr:
            if not remainder:
                remainder = a % x
            else:
                if (a % x) != remainder:
                    return -1

        median = arr[m*n//2]
        count = 0
        for a in arr:
            count += abs(a-median) // x

        return count