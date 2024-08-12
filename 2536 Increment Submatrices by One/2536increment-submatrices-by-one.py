class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:

        mat = [n*[0] for i in range(n)]
        for ri, ci, rj, cj in queries:  
            mat[ri][ci] += 1
            if cj+1 < n:
                mat[ri][cj+1] -= 1
            if rj+1 < n:
                mat[rj+1][ci] -= 1
            if rj+1 < n and cj+1 < n:
                mat[rj+1][cj+1] += 1
            # print(mat)

        for r in range(n):
            for c in range(1,n):
                mat[r][c] += mat[r][c-1]
        for c in range(n):
            for r in range(1,n):
                mat[r][c] += mat[r-1][c]

        return mat  
               