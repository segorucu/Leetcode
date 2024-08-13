class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        n = len(grid)
        first = set()
        def dfs(r,c):
            first.add((r,c))

            for dr,dc in directions:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < n and 0 <= nc < n and (nr,nc) not in first \
                    and grid[nr][nc] == 1:
                    dfs(nr,nc)

        first = set()
        completed = False
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    dfs(r,c)
                    completed = True
                    break
            if completed:
                break


        queue = collections.deque()
        for r,c in first:
            queue.append((r,c,0))

        visited = set()
        visited.update(first)
        while queue:
            r,c,dist = queue.popleft()
            if grid[r][c] == 1 and (r,c) not in first:
                return dist-1

            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                if 0 <= nr < n and 0 <= nc < n\
                  and (nr,nc) not in visited:
                  queue.append((nr,nc,dist+1))
                  visited.add((nr,nc))






        