class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        
        m = len(matrix)
        n = len(matrix[0])

        for i in range(n):
            c = i
            r = 0
            visited = set()
            while r < m and c < n:
                visited.add(matrix[r][c])
                r += 1
                c += 1
            if len(visited) > 1:
                return False

        for i in range(1,m):
            r = i
            c = 0
            visited = set()
            while r < m and c < n:
                visited.add(matrix[r][c])
                r += 1
                c += 1
            if len(visited) > 1:
                return False


        return True