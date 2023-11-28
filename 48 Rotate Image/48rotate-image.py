class Solution:
    def _init_(self,n):
        self.n = n

    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        self.n = len(matrix)
        self.transpose(matrix)
        self.flip(matrix)
        # for i in range(self.n):
        #     print(matrix[i])
        
    def transpose(self,matrix):
        for i in range(self.n):
            for j in range(i+1,self.n):
                dum  = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = dum

    def flip(self,matrix):
        for j in range(self.n // 2):
            for i in range(self.n):
                dum = matrix[i][j]
                matrix[i][j] = matrix[i][self.n-1-j]
                matrix[i][self.n-1-j] = dum

