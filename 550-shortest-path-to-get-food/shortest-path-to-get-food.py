class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        

        m = len(grid)
        n = len(grid[0])
        directions = [(0,1),(1,0),(-1,0),(0,-1)]

        for r in range(m):
            for c in range(n):
                if grid[r][c] == "*":
                    start = (r,c)
                    break

        def valid(r,c):
            return 0 <= r < m and 0 <= c < n and grid[r][c] in {"O", "#"}

        queue = collections.deque()
        queue.append((start[0],start[1],0))
        visited = set()
        visited.add((start[0],start[1]))

        while queue:
            r,c,d = queue.popleft()
            if grid[r][c] == "#":
                return d

            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                if valid(nr,nc) and (nr,nc) not in visited:
                    visited.add((nr,nc))
                    queue.append((nr,nc,d+1))



        return -1