class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        
        def distance(arr,val):
            sm = 0
            for x in arr:
                sm += abs(x-val)
            return sm

        m = len(grid)
        n = len(grid[0])

        xs = []
        ys = []

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    xs.append(j)
                    ys.append(i)


        xs.sort()
        ys.sort()
        ntot = len(xs)
        med = ntot // 2
        return distance(xs,xs[med]) + distance(ys,ys[med])

    

