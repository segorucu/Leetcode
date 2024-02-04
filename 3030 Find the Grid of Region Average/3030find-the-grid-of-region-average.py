class Solution:
    def resultGrid(self, image: List[List[int]], threshold: int) -> List[List[int]]:
        
        m = len(image)
        n = len(image[0])
        def checkregion(i,j):
            if abs(image[i-1][j-1] -image[i-1][j]) > threshold:
                return False
            if abs(image[i-1][j-1] -image[i][j-1]) > threshold:
                return False
            if abs(image[i-1][j] -image[i-1][j+1]) > threshold:
                return False
            if abs(image[i-1][j] -image[i][j]) > threshold:
                return False
            if abs(image[i-1][j+1] -image[i][j+1]) > threshold:
                return False
            if abs(image[i][j-1] -image[i][j]) > threshold:
                return False
            if abs(image[i][j-1] -image[i+1][j-1]) > threshold:
                return False
            if abs(image[i][j] -image[i][j+1]) > threshold:
                return False
            if abs(image[i][j] -image[i+1][j]) > threshold:
                return False
            if abs(image[i][j+1] -image[i+1][j+1]) > threshold:
                return False
            if abs(image[i+1][j-1] -image[i+1][j]) > threshold:
                return False
            if abs(image[i+1][j] -image[i+1][j+1]) > threshold:
                return False
            return True


        s = [(n) * [0] for _ in range(m)]
        c = [(n) * [0] for _ in range(m)]
        for row in range(1,m-1):
            for col in range(1,n-1):
                if checkregion(row,col):
                    sm = 0
                    for i in [-1,0,1]:
                        for j in [-1,0,1]:
                            sm += image[row+j][col+i]
                    mn = sm // 9
                    s[row-1][col-1] += mn
                    s[row-1][col] += mn
                    s[row-1][col+1] += mn
                    s[row][col-1] += mn
                    s[row][col] += mn
                    s[row][col+1] += mn
                    s[row+1][col-1] += mn
                    s[row+1][col] += mn
                    s[row+1][col+1] += mn
                    c[row-1][col-1] += 1
                    c[row-1][col] += 1
                    c[row-1][col+1] += 1
                    c[row][col-1] += 1
                    c[row][col] += 1
                    c[row][col+1] += 1
                    c[row+1][col-1] += 1
                    c[row+1][col] += 1
                    c[row+1][col+1] += 1

        
        for row in range(m):
            for col in range(n):
                if c[row][col] > 0:
                    image[row][col] = s[row][col] // c[row][col]
                
        return image
                
        