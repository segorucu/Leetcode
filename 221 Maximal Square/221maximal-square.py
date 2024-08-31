class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        

        m = len(matrix)
        n = len(matrix[0])

        for r in range(m):
            for c in range(n):
                matrix[r][c] = int(matrix[r][c])

        for r in range(1,m):
            for c in range(n):
                if matrix[r][c] != 0:
                    matrix[r][c] = matrix[r-1][c] + 1

        ans = 0
        for r in range(m):
            for c in range(n):
                mincol = matrix[r][c]
                for c2 in range(c,n):
                    mincol = min(mincol,matrix[r][c2])
                    if mincol == 0 or mincol < c2-c+1:
                        break
                    ans = max(ans, (c2-c+1) * mincol)


        return ans

