class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points,key = lambda x: x[1])
        
        currright = points[0][1]
        burst = 1
        for i, point in enumerate(points):
            if points[i][0] <= currright:
                continue
            else:
                burst += 1
                currright = points[i][1]

        return burst
        