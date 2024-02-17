from sortedcontainers import SortedList
class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        
        points = sorted(points, key = lambda x: (x[0], -x[1]))
        
        n = len(points)
        c = 0
        for i in range(n):
            ax, ay = points[i]
            sl = SortedList()
            for j in range(i+1,n):
                bx, by = points[j]
                if ay < by:
                    continue
                index = sl.bisect_left(by)
                if not (0 <= index < len(sl)):
                    c += 1
                sl.add(points[j][1])
        
        return c
                
        