class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        

        m = len(matrix)
        n = len(matrix[0])

        for r in range(1,m):
            for c in range(n):
                if matrix[r][c] == 1:
                    matrix[r][c] = matrix[r-1][c] + 1

        ans = 0
        for r in range(m):
            for c in range(n):
                minsize = matrix[r][c]
                for i in range(matrix[r][c]):
                    if c-i < 0:
                        break
                    minsize = min(minsize, matrix[r][c-i])
                    if  minsize >= i+1:
                        ans += 1
                    else:
                        break

        return ans


# [0,1,1,1] 0 1 1 1
# [1,1,0,1] 1 1 0 1
# [1,1,1,1] 1 2 1 1
# [1,0,1,0] 1 0 1 0