class Solution:
    def highestRankedKItems(self, grid: List[List[int]], pricing: List[int], start: List[int], k: int) -> List[List[int]]:
        
        m = len(grid)
        n = len(grid[0])
        moves = [(0,1),(1,0),(-1,0),(0,-1)]
        distmap = collections.defaultdict(int)

        def valid(r, c):
            return 0 <= r < m and 0 <= c < n and grid[r][c] > 0 and (r,c) not in seen

        seen = set()
        seen.add((start[0], start[1]))

        queue = collections.deque()
        queue.append((start[0], start[1], 0))
        arr = []
        while queue:
            r, c, dist = queue.popleft()
            distmap[(r,c)] = dist
            if pricing[0] <= grid[r][c] <= pricing[1]:
                arr.append((dist, grid[r][c], r, c))

            for move in moves:
                nr, nc = r+move[0], c+move[1]
                if valid(nr,nc):
                    queue.append((nr, nc, dist+1))
                    seen.add((nr,nc))
        # print(distmap)
        arr.sort()
        ans = []
        for a in arr:
            ans.append([a[2],a[3]])
            # print(len(ans))
            if len(ans) == k:
                break
        

        return ans