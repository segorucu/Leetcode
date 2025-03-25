class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        

        xdim = []
        ydim = []
        for xs, ys, xe, ye in rectangles:
            xdim.append((xs,xe))
            ydim.append((ys,ye))

        xdim.sort()
        ydim.sort()
        count = 0
        m = len(xdim)
        end = xdim[0][1]
        for i in range(1,m):
            if xdim[i][0] >= end:
                count += 1
            end = max(end, xdim[i][1])
        if count >= 2:
            return True

        end = ydim[0][1]
        count = 0
        for i in range(1,m):
            if ydim[i][0] >= end:
                count += 1
            end = max(end, ydim[i][1])
        if count >= 2:
            return True

        return False

        
