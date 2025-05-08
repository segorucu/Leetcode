class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        

        m = len(moveTime)
        n = len(moveTime[0])

        def valid(r,c):
            return 0 <= r < m and 0 <= c < n and (r,c) not in visited
            
        hp = [(0,0,0,0)]
        visited = set()
        costmp = defaultdict(lambda: float("inf"))

        while hp:
            cost, r, c, step = heappop(hp)
            if (r,c) in visited:
                continue
            if (r,c) == (m-1,n-1):
                return cost
            visited.add((r,c)) 
            neighs = [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]
            for nr,nc in neighs:
                if valid(nr,nc):
                    dist = max(moveTime[nr][nc],cost) + step + 1
                    if dist < costmp[(nr,nc)]:
                        heappush(hp,(dist,nr,nc,1-step))
                        costmp[(nr,nc)] = dist

        return costmp[(m-1,n-1)]