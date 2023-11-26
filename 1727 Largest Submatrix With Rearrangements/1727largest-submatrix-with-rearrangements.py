class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:

        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] != 0 and i > 0:
                    matrix[i][j] = matrix[i-1][j] + 1

        ans = 0
        for i in range(m):
            row = matrix[i]
            row = sorted(row, reverse = True)
            # print(row)
            for j, val in enumerate(row):
                if val != 0:
                    cand = val * (j+1)
                    if cand > ans:
                        ans = cand

        return ans