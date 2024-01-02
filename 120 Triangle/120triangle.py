class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        n = len(triangle)
        for i in range(1,n):
            row = triangle[i].copy()
            for j in range(i+1):
                if j == i:
                    add = triangle[i-1][j-1]
                elif j == 0:
                    add = triangle[i-1][j]
                else:
                    add = min(triangle[i-1][j],triangle[i-1][j-1])
                triangle[i][j] = triangle[i][j] + add
                

        return min(triangle[-1])

