from collections import deque
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:

        def valid(i,j):
            return 0 <= i < m and 0 <= j < n
             
        m = len(grid)
        n = len(grid[0]) 
        if m == 1 and n == 1:
            return 0
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        queue = deque()
        queue.append((0,0,k,0))
        seen = set()
        seen.add((0,0,k))
        while queue:
            i, j, remain, steps = queue.popleft()
            if i == m-1 and j == n-1:
                    return steps
            for dx, dy in directions:
                row, col = i + dy, j + dx
                if valid(row,col):
                    if grid[row][col] == 0:
                        if (row,col,remain) not in seen:
                            queue.append((row,col,remain,steps+1))
                            seen.add((row,col,remain))
                    elif grid[row][col] == 1 and remain > 0:
                        if (row,col,remain-1) not in seen:
                            queue.append((row,col,remain-1,steps+1))
                            seen.add((row,col,remain-1))
                    
        return -1

