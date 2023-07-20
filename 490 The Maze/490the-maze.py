from collections import deque
class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:

        directions = [(0,1),(1,0),(0,-1),(-1,0)]

        m = len(maze)
        n = len(maze[0])

        def search(i,j,move):
            dx, dy = move
            while True:
                testi = i + dy
                testj = j + dx
                if 0 <= testi < m and 0 <= testj < n:
                    if maze[testi][testj] == 0:
                        i, j = testi, testj
                        continue
                break

            return (i,j)


        visited = set()
        queue = deque()
        queue.append((start[0],start[1]))
        while queue:
            row, col = queue.popleft()
            if [row,col] == destination:
                return True
            visited.add((row,col))
            for move in directions:
                (ni,nj) = search(row,col,move)
                if (ni,nj) != (row,col) and (ni,nj) not in visited:
                    queue.append((ni,nj))
                    visited.add((ni,nj))

        
        return False
