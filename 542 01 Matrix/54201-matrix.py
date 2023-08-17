from collections import deque, defaultdict
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:

        directions = [(0,1),(1,0),(-1,0),(0,-1)]

        def valid(ni,nj):
            return 0 <= ni < m and 0 <= nj < n and (ni,nj) not in visited



        m = len(mat)
        n = len(mat[0])

        queue = deque()
        visited = set()
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    queue.append((i,j))
                    visited.add((i,j))

        while queue:
            i, j  = queue.popleft()
            for dx, dy in directions:
                ni, nj = i + dy, j + dx
                if valid(ni,nj):
                    mat[ni][nj] = mat[i][j] + 1
                    queue.append((ni,nj))
                    visited.add((ni,nj))
 
        return mat

