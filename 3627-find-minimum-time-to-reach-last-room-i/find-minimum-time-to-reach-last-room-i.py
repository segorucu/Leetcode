class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        
        m = len(moveTime)
        n = len(moveTime[0])

        def valid(r,c):
            return 0 <= r < m and 0 <= c < n and (r,c) not in visited

        hp = []
        heappush(hp,(0,0,0))
        visited = set()
        distmap = defaultdict(lambda: float("inf"))

        while hp:
            curr, r, c = heappop(hp)
            if (r,c) == (m-1,n-1):
                return curr
            if (r,c) in visited:
                continue
            visited.add((r,c))
            neigh = [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]
            for nr,nc in neigh:
                if valid(nr,nc):
                    dist = max(moveTime[nr][nc]+1, curr + 1)
                    if dist < distmap[(nr,nc)]:
                        heappush(hp,(dist, nr, nc))

        # return distmap[(m-1,n-1)]
