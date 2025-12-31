class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
    
        grid = [col * [0] for i in range(row)]
        for t in range(len(cells)):
            r = cells[t][0] - 1
            c = cells[t][1] - 1
            grid[r][c] = t + 1

        l = 1
        r = row * col

        def valid(r,c):
            return 0 <= r < row and 0 <= c < col

        def go(mid):

            queue = deque()
            visited = set()
            for r in range(row):
                for c in range(col):
                    if grid[r][c] <= mid:
                        visited.add((r,c))

            for c in range(col):
                if (0,c) not in visited:
                    queue.append((0,c))

            while queue:
                r,c = queue.popleft()
                neighs = [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]
                for nr, nc in neighs:
                    if valid(nr,nc) and (nr,nc) not in visited:
                        if nr == row-1:
                            return True
                        queue.append((nr,nc))
                        visited.add((nr,nc))         
            return False

        ans = 1
        while l <= r:
            mid = (l+r) // 2
            if go(mid):
                l = mid + 1
                ans = mid
            else:
                r = mid - 1

        return ans
            

        

        