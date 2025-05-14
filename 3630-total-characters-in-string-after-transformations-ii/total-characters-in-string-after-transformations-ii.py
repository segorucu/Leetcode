class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
    
        MOD = 10**9 + 7
        def matmul(matrix1,matrix2):
            R1 = len(matrix1)
            C1 = len(matrix1[0])
            C2 = len(matrix2[0])
            product = [C2*[0] for _ in range(R1)]

            for r in range(R1):
                for c in range(C2):
                    sm = 0
                    for i in range(C1):
                        sm += (matrix1[r][i] * matrix2[i][c] % MOD)
                    product[r][c] = sm % MOD
            return product
                    
        @cache
        def exponentiate(t):
            if t == 1:
                return matrix
            elif t == 2:
                return matmul(matrix, matrix)
            else:
                if t % 2:
                    return matmul(exponentiate(t//2+1), exponentiate(t//2))
                else:
                    return matmul(exponentiate(t//2), exponentiate(t//2))

        matrix = [26*[0] for _ in range(26)]
        for r in range(26):
            for c in range(r+1,r+1+nums[r]):
                matrix[r][c%26] = 1

        mat = exponentiate(t)
        counter = Counter(s)
        vector = [26*[0]]
        for k,v in counter.items():
            vector[0][ord(k)-ord("a")] = v


        res = matmul(vector, mat)

        return sum(res[0]) % MOD
