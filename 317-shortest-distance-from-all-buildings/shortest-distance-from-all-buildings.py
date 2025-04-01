class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        
        ones = []
        m = len(grid)
        n = len(grid[0])

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    ones.append((r,c))

        def valid(r,c):
            return 0 <= r < m and 0 <= c < n

        
        def dfs(r,c):
            neighs = [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]
            for nr,nc in neighs:
                if valid(nr,nc):
                    if grid[nr][nc] == 1:
                        reachable_ones.add((nr,nc))
                    elif grid[nr][nc] == 0 and (nr,nc) not in zeros:
                        zeros.add((nr,nc))
                        dfs(nr,nc)


        r,c = ones[0]
        reachable_ones = set()
        reachable_ones.add((r,c))

        neighs = [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]

        for nr, nc in neighs:
            if valid(nr,nc) and grid[nr][nc] == 0:
                zeros = set()
                zeros.add((nr,nc))
                dfs(nr,nc)
                if len(reachable_ones) == len(ones):
                    break
        else:
            return -1

        if len(zeros) == 0:
            return -1

        def calcdist(r,c):
            queue = deque()
            queue.append((0,r,c))
            visited = set()
            visited.add((r,c))
            sm = 0
            while queue:
                dist,r,c = queue.popleft()
                if grid[r][c] == 1:
                    sm += dist
                    continue
                neighs = [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]
                for nr, nc in neighs:
                    if valid(nr,nc) and (nr,nc) not in visited and grid[nr][nc] != 2:
                        visited.add((nr,nc))
                        queue.append((dist+1,nr,nc))
            return sm

        medr, medc = 0, 0
        for r,c in ones:
            medr += r
            medc += c
        medr = medr // len(ones)
        medc = medc // len(ones)

        hp = []
        for r,c in zeros:
            dist = abs(r-medr) + abs(c-medc)
            heappush(hp,(dist,r,c))

        mindiff = inf
        for i in range(min(100,len(zeros))):
            _,r,c = heappop(hp)
            dist = calcdist(r,c)
            mindiff = min(mindiff, dist)

        return mindiff

        
        """

[1,1,1,1,1,0]
[0,0,0,0,0,1]
[0,1,1,0,0,1],
[1,0,0,1,0,1],
[1,0,0,0,0,1]


        """