class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        
        m = len(mat1)
        k = len(mat1[0])
        n = len(mat2[0])

        ans = [n * [0] for _ in range(m)]

        for r in range(m):
            for c in range(n):
                curr = 0
                for j in range(k):
                    curr += mat1[r][j] * mat2[j][c]
                ans[r][c] = curr

        return ans