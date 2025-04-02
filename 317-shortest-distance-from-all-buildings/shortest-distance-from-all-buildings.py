class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        
        ones = []
        m = len(grid)
        n = len(grid[0])
        zeros = []
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    ones.append((r,c))
                elif grid[r][c] == 0:
                    zeros.append((r,c))

        def valid(r,c):
            return 0 <= r < m and 0 <= c < n

        if len(zeros) == 0:
            return -1

        EMPTY_SPACE = 0
        distance_graph = defaultdict(int)
        for r,c in ones:
            local_dist = inf
            queue = deque()
            queue.append((r,c,0))
            while queue:
                r, c, dist = queue.popleft()
                neighs= [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]
                for nr, nc in neighs:
                    if valid(nr,nc) and grid[nr][nc] == EMPTY_SPACE:
                        grid[nr][nc] -= 1
                        distance_graph[(nr,nc)] += dist+1
                        queue.append((nr,nc,dist+1))
                        local_dist = min(local_dist, distance_graph[(nr,nc)])
            EMPTY_SPACE -= 1
        
        return local_dist if local_dist != inf else -1


       

        

        return -1 if mindiff == inf else mindiff

    