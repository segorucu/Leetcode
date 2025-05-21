class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])

        lst = []
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    lst.append((i,j))

            
        for ior,jor in lst:
            for i in range(m):
                if matrix[i][jor] != 0:
                    matrix[i][jor] = 0
            for j in range(n):
                if matrix[ior][j] != 0:
                    matrix[ior][j] = 0

        return matrix
            
