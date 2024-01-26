class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:

        ans = 1
        n = len(points)
        if n == 1:
            return 1

        for i in range(n):
            anglemp = collections.defaultdict(int)
            for j in range(n):
                if i != j:
                    angle = math.atan2(points[j][1]-points[i][1],points[j][0]-points[i][0])
                    anglemp[angle] += 1
                
            ans = max(ans, max(anglemp.values())+1)
        return ans

        