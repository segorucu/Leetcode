class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if n == 1:
            return 0
        directions = [(0,1),(1,0),(0,-1),(-1,0)]

        def valid(r,c):
            return 0 <= r < n and 0 <= c < n

        def bfs(val):
            q = collections.deque()
            if grid[0][0] <= val:
                q.append((0,0))
            visited = set()
            visited.add((0,0))
            while q:
                r,c = q.popleft()
                if (r,c) == (n-1,n-1):
                    return True
                for dr, dc in directions:
                    nr, nc = r+dr, c+dc
                    if valid(nr, nc) and (nr,nc) not in visited and grid[nr][nc] <= val:
                        q.append((nr,nc))
                        visited.add((nr,nc))
            return False


        l = 0
        r = n**2-1
        while l < r:
            mid = (l+r) // 2
            if bfs(mid):
                r = mid
            else:
                l = mid+1

        return l
