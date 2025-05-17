class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        horizontal = [n*[0] for _ in range(m)]
        vertical = [n*[0] for _ in range(m)]

        def search_hor(r,c):
            count = 0
            while c < n and grid[r][c] != "W":
                if grid[r][c] == "E":
                    count += 1
                elif grid[r][c] == "0":
                    curr.append((r,c))
                c += 1
            return count

        def search_ver(r,c):
            count = 0
            while r < m and grid[r][c] != "W":
                if grid[r][c] == "E":
                    count += 1
                elif grid[r][c] == "0":
                    curr.append((r,c))
                r += 1
            return count

        for r in range(m):
            c = 0
            while c < n:
                if grid[r][c] != "W":
                    curr = []
                    count = search_hor(r,c)
                    for r,c in curr:
                        horizontal[r][c] = count
                c += 1

        for c in range(n):
            r = 0
            while r < m:
                if grid[r][c] != "W":
                    curr = []
                    count = search_ver(r,c)
                    for r,c in curr:
                        vertical[r][c] = count
                r += 1

        ans = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == "0":
                    ans = max(ans, horizontal[r][c] + vertical[r][c])

        return ans

        # ["W","W","W","W","E"],
        # ["W","E","E","E","E"],
        # ["W","E","0","E","0"],
        # ["W","E","E","E","E"],
        # ["W","W","W","W","W"]

