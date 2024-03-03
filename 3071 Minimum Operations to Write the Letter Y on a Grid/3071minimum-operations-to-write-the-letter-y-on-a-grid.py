class Solution:
    def minimumOperationsToWriteY(self, grid: List[List[int]]) -> int:
        
        n = len(grid)
        yfreq = collections.defaultdict(int)
        outside = collections.defaultdict(int)
        
        center = n // 2
        
        for r in range(n):
            for c in range(n):
                num = grid[r][c]
                if r < center:
                    if r == c or c == n - r -1:
                        yfreq[num] += 1
                    else:
                        outside[num] += 1
                elif r >= center:
                    if c == center:
                        yfreq[num] += 1
                    else:
                        outside[num] += 1
           
        ysize = sum(yfreq.values())
        nysize = n*n - ysize
        # print(ysize,nysize)
        scenarios = [(0,1),(0,2),(1,0),(1,2),(2,0),(2,1)]
        ops = float("inf")
        for y, ny in scenarios:
            cost = ysize - yfreq[y]
            cost += nysize - outside[ny]
            if cost < ops:
                ops = cost
            
        return ops
        