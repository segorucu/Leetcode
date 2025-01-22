class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        
        m = len(isWater)
        n = len(isWater[0])

        visited = set()
        q = collections.deque()
        for r in range(m):
            for c in range(n):
                if isWater[r][c]:
                    q.append((0, r, c))
                    visited.add((r,c))

        def valid(r,c):
            return 0 <= r < m and 0 <= c < n

        
        while q:
            h, r, c = q.popleft()
            isWater[r][c] = h

            neighs = [(r+1,c), (r-1,c), (r,c+1), (r,c-1)]
            for nr,nc in neighs:
                if valid(nr,nc) and (nr,nc) not in visited:
                    q.append((h+1,nr,nc))
                    visited.add((nr,nc))


        return isWater