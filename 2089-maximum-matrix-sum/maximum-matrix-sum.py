class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        
        minval = inf
        n = len(matrix)
        negs = 0
        sm = 0
        for r in range(n):
            for c in range(n):
                if matrix[r][c] <= 0:
                    negs += 1
                    matrix[r][c] *= -1
                sm += matrix[r][c]
                minval = min(minval, matrix[r][c])
        
        if negs % 2 == 1:
            sm -= 2 * minval
        return sm

        





