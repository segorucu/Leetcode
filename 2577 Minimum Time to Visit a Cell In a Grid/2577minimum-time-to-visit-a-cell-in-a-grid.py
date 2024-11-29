class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        

        if min(grid[0][1],grid[1][0]) > 1:
            return -1

        m = len(grid)
        n = len(grid[0])

        hp = [(0,0,0)]
        visited = set()
        while hp:
            time, r, c = heappop(hp)
            if r == m-1 and c == n-1:
                return time

            neighs = [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]
            for nr,nc in neighs:
                if 0 <= nr < m and 0 <= nc < n and (nr,nc) not in visited:
                    add = 0
                    if grid[nr][nc] > time+1 and (grid[nr][nc] - time) % 2 == 0:
                        add = 1
                    nextime = max(grid[nr][nc]+add,time+1)
                    heappush(hp,(nextime,nr,nc))
                    visited.add((nr,nc))

        
