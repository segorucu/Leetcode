from heapq import heapify, heappop, heappush
class Solution:

    def minCost(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])

        def valid(r,c):
            return 0 <= r < m and 0 <= c < n and (r,c) not in visited

        directions = {(0,1):1, (0,-1):2, (1,0):3, (-1,0):4}
        visited = set()
        
        hp = [(0,0,0)]
        while hp:
            cost, r, c = heappop(hp)
            if (r,c) in visited:
                continue
            visited.add((r,c))
            if (r,c) == (m-1,n-1):
                return cost

            for (dr,dc), val in directions.items():
                nr, nc = r+dr, c+dc
                if not valid(nr,nc):
                    continue

                if grid[r][c] == val:
                    dist = 0
                else:
                    dist = 1

                heappush(hp,(cost+dist, nr, nc))
                 

            
        