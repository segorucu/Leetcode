from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1

        n = len(grid)
        def valid(i,j):
            return 0 <= i < n and 0 <= j < n and grid[i][j] == 0 and (i,j) not in seen
   

        seen = set()
        ans = 0
        directions = [(0, 1), (1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1), (0, -1), (-1, 0)]
        queue = deque()
        queue.append((0,0,1))
        while queue:
            (i,j, val) = queue.popleft()
            seen.add((i,j))
            if [i,j] == [n-1,n-1]:
                return val
            for dx,dy in directions:
                ni, nj = i+dy, j+dx
                if valid(ni,nj):
                    seen.add((ni,nj))
                    queue.append((ni,nj,val+1))

        return -1


