from collections import defaultdict
class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:

        m = len(mat)
        n = len(mat[0])

        rows = defaultdict(int)
        cols = defaultdict(int)
        ones = []
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    rows[i] += 1 
                    cols[j] += 1
                    if rows[i] == 1 and cols[j] == 1:
                        ones.append((i,j))

        ans = 0
        for i, j in ones:
            if rows[i] == 1 and cols[j] == 1:
                ans += 1

        return ans

                

        