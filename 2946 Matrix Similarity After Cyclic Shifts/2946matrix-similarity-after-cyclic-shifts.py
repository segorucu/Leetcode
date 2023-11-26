class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        
        m = len(mat)
        n = len(mat[0])
        
        if n == 1:
            return True
        
        
        mato = mat.copy()
        for it in range(k):
            matn = [n*[0] for _ in range(m)]
            for i in range(m):
                for j in range(n):
                    if m % 2 == 1:
                        matn[i][(j+1)%n] = mato[i][j]
                    else:
                        matn[i][(j-1)%n] = mato[i][j]
            mato = matn.copy()
            
        for i in range(m):
            for j in range(n):
                if matn[i][j] != mat[i][j]:
                    return False
            
        return True
        