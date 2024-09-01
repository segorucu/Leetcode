class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        
        if m*n != len(original):
            return []

        mat = [n*[0] for _ in range(m)]

        for r in range(m):
            for c in range(n):
                curr = r*n+c
                # print(curr)
                mat[r][c] = original[curr]

        return mat