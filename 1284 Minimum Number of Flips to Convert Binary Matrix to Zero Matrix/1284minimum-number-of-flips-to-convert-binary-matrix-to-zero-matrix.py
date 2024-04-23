class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        

        m = len(mat)
        n = len(mat[0])
        self.ans = inf

        def flip(row,col):
            mat[row][col] = 1 - mat[row][col] 
            if row-1 >= 0:
                mat[row-1][col] = 1 - mat[row-1][col] 
            if row+1 < m:
                mat[row+1][col] = 1 - mat[row+1][col] 
            if col-1 >= 0:
                mat[row][col-1] = 1 - mat[row][col-1] 
            if col+1 < n:
                mat[row][col+1] = 1 - mat[row][col+1] 

        def backtrack(x,flips):
            if x == m*n:
                zeros = True
                for r in range(m):
                    for c in range(n):
                        if mat[r][c] == 1:
                            zeros = False
                            break
                    if False:
                        break
                if zeros:
                    self.ans = min(self.ans,flips)
                return

            row, col = divmod(x,n)
            
            flip(row,col)
            backtrack(x+1,flips+1)
            flip(row,col)
            backtrack(x+1,flips)

        backtrack(0,0)
        if self.ans == inf:
            return -1
        return self.ans