from copy import deepcopy
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        

        m = len(points)
        n = len(points[0])
        prev = points[0].copy()
        left = n * [0]
        right = n * [0]
        nxt = n * [0]
        for r in range(1,m):  
            left[0] = prev[0]
            for c in range(1,n):
                left[c] = max(prev[c],left[c-1]-1)
            right[-1] = prev[n-1]
            for c in range(n-2,-1,-1):
                right[c] = max(prev[c],right[c+1]-1)
            for c in range(n):
                nxt[c] = max(left[c],right[c]) + points[r][c]
            prev = nxt
                

        return max(prev)