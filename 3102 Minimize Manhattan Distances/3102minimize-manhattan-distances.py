class Solution:
    def minimumDistance(self, points: List[List[int]]) -> int:
        

        def findmaxmanhattandistance(remove=-1):

            maxsum, minsum, maxdiff, mindiff = -inf, inf, -inf, inf
            for i, point in enumerate(points):
                if i == remove:
                    continue

                sm = point[0] + point[1]
                diff = point[0] - point[1]

                if sm > maxsum:
                    maxsum = sm
                    maxsumid = i
                
                if sm < minsum:
                    minsum = sm
                    minsumid = i

                if diff > maxdiff:
                    maxdiff = diff
                    maxdiffid = i

                if diff < mindiff:
                    mindiff = diff
                    mindiffid = i

            if maxsum - minsum > maxdiff - mindiff:
                return maxsumid, minsumid
            else:
                return maxdiffid, mindiffid

        m1, m2 = findmaxmanhattandistance(-1)
        p1, p2 = findmaxmanhattandistance(m1)
        ans = abs(points[p1][0]-points[p2][0]) + abs(points[p1][1]-points[p2][1])
        p1, p2 = findmaxmanhattandistance(m2)
        ans = min(ans,abs(points[p1][0]-points[p2][0]) + abs(points[p1][1]-points[p2][1]))
        
        
        return ans