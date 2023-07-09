from collections import deque
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:

        m = len(maze)
        n = len(maze[0])

        def valid(i,j):
            return 0 <= i < m and 0 <= j < n and (i,j) not in seen and maze[i][j] == "."

        def exit(i,j):
            return (i == 0 or j == 0 or i == m-1 or j == n-1) and [i,j] != entrance

        directions = [(0,1),(1,0),(0,-1),(-1,0)]

        seen = set()
        seen.add((entrance[0],entrance[1]))
        queue = deque()
        queue.append((entrance[0],entrance[1],0))
        while queue:
            i,j,steps = queue.popleft()
            if exit(i,j):
                return steps
            for dx,dy in directions:
                row, col = i+dy, j+dx
                if valid(row,col):
                    seen.add((row,col))
                    queue.append((row,col,steps+1))
            

        return -1