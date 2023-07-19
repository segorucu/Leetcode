from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        def valid(i,j):
            return 0 <= i < m and 0 <= j < n and (i,j) not in visited

        def isolated(i,j):
            for dx,dy in directions:
                ni,nj =  i+dy, j+dx
                if 0 <= ni < m and 0 <= nj < n:
                    if grid[ni][nj] >= 1:
                        return False
            return True

        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        m = len(grid)
        n = len(grid[0])

        ones = 0
        twos = 0
        queue = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i,j,0))
                    twos += 1
                elif grid[i][j] == 1:
                    ones += 1
                    if isolated(i,j):
                        return -1
        
        if twos == 0:
            if ones > 0:
                return -1
            return 0
        visited = set()
        time = 0
        maxtime = 0
        while queue:
            i,j,time = queue.popleft()
            maxtime = max(maxtime,time)
            visited.add((i,j))
            for dx,dy in directions:
                ni,nj = i+dy, j+dx
                if valid(ni,nj) and grid[ni][nj] == 1:
                    queue.append((ni,nj,time+1))
                    grid[ni][nj] = 2

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1

        return maxtime


