class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        
        answer = copy.deepcopy(matrix)
        
        m = len(matrix)
        n = len(matrix[0])
        cols = n * [0]
        for r in range(m):
            for c in range(n):
                if matrix[r][c] > cols[c]:
                    cols[c] = matrix[r][c]
        for r in range(m):
            for c in range(n):
                if answer[r][c] == -1:
                    answer[r][c] = cols[c]
        
        return answer
        