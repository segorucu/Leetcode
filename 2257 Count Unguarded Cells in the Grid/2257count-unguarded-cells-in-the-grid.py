class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        

        unguarded = set()
        guardset = set()
        wallset = set()
        for a,b in guards:
            guardset.add((a,b))
        for a,b in walls:
            wallset.add((a,b))
        for r in range(m):
            for c in range(n):
                if (r,c) not in guardset and (r,c) not in wallset:
                    unguarded.add((r,c))
        

        direction = [(0,1),(1,0),(-1,0),(0,-1)]
        def valid(r,c):
            return 0 <= r < m and 0 <= c < n

        for r,c in guards:
            for dr,dc in direction:
                nr, nc = r+dr, c+dc
                while valid(nr,nc) and (nr,nc) not in guardset and (nr,nc) not in wallset:
                    if (nr,nc) in unguarded:
                        unguarded.remove((nr,nc))
                    nr, nc = nr+dr, nc+dc

        return len(unguarded)