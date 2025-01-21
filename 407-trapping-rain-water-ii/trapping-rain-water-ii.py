from heapq import heappop, heappush, heapify
class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        
        m = len(heightMap)
        n = len(heightMap[0])

        
        hp = []
        for r in range(m):
            for c in range(n):
                if r == 0 or r == m-1 or c == 0 or c == n-1:
                    heappush(hp, (heightMap[r][c], r, c))
                    heightMap[r][c] = -1

        res = 0
        max_h = -1
        while hp:
            h, r, c = heappop(hp)
            max_h = max(max_h, h)
            res += max_h - h

            neighs = [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]
            for nr,nc in neighs:
                if nr < 0 or nc < 0 or nr == m or nc == n or heightMap[nr][nc] == -1:
                    continue

                heappush(hp, ( heightMap[nr][nc], nr, nc))
                heightMap[nr][nc] = -1

        return res

