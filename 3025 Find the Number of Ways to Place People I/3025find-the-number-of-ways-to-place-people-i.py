class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        
        points = sorted(points, key = lambda x: (x[0], -x[1]))
        
        n = len(points)
        c = 0
        for i in range(n):
            for j in range(i+1,n):
                if points[i][0] > points[j][0]:
                    continue
                if points[i][1] < points[j][1]:
                    continue
                maxy = max(points[i][1],points[j][1])
                miny = min(points[i][1],points[j][1])
                for k in range(i+1,j):
                    if miny <= points[k][1] <= maxy:
                        break
                else:
                    c += 1
        
        return c
                
        