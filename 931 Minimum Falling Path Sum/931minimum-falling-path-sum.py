class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)

        for i in range(1,n):
            for j in range(n):
                val = matrix[i-1][j]
                if 0 < j:
                    val = min(val,matrix[i-1][j-1])
                if j < n-1:
                    val = min(val,matrix[i-1][j+1])
                matrix[i][j] += val
        
        return min(matrix[-1])
        