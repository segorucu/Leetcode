from heapq import heapify, heappop, heappush
class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        
        if grid[0][0] == 1:
            grid[0][0] = 0
            health -= 1

        if grid[-1][-1] == 1:
            grid[-1][-1] = 0
            health -= 1

        if health < 1:
            return False

        m = len(grid)
        n = len(grid[0])

        def valid(r,c):
            return 0 <= r < m and 0 <= c < n

        hp = [(0,0,0)]
        visited = set()
        while hp:
            cost, r, c = heappop(hp)
            if (r,c) in visited:
                continue
            if (r,c) == (m-1,n-1):
                return health > cost
            visited.add((r,c))
            neighs = [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]

            for nr,nc in neighs:
                if valid(nr,nc) and (nr,nc) not in visited:
                    new_cost = cost
                    if grid[nr][nc] == 1:
                        new_cost = cost + 1
                    heappush(hp,(new_cost,nr,nc))