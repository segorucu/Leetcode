class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        
        m = len(mat)
        n = len(mat[0])

        answer = [[0 for j in range(n)] for i in range(m)]

        def valid(i,j):
            return 0 <= i < m and 0 <= j < n

        for row in range(m):
            for col in range(n):
                sm = 0
                for nrow in range(max(row-k,0),min(row+k+1,m)):
                    for ncol in range(max(col-k,0),min(col+k+1,n)):
                        sm += mat[nrow][ncol]
                answer[row][col] = sm

        return answer