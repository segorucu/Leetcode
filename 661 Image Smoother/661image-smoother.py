class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        directions = [(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)]


        m= len(img)
        n = len(img[0])
        ans = [n*[0] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                sm = img[i][j]
                tot = 1
                for x,y in directions:
                    row = i + y
                    col = j + x
                    if 0 <= row < m and 0 <= col < n:
                        sm += img[row][col]
                        tot += 1
                ans[i][j] = sm // tot
        return ans
                    