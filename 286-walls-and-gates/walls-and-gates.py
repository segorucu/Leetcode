class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        R = len(rooms)
        C = len(rooms[0])

        def valid(r,c):
            return 0 <= r < R and 0 <= c < C and (r,c) not in walls and (r,c) not in gates

        gates = set()
        walls = set()
        for r in range(R):
            for c in range(C):
                if rooms[r][c] == 0:
                    gates.add((r,c))
                elif rooms[r][c] == -1:
                    walls.add((r,c))

        queue = deque()
        for r,c in gates:
            queue.append((0,r,c))

        visited = set()
        while queue:
            dist, r, c = queue.popleft()
            rooms[r][c] = dist

            neighs = [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]
            for nr, nc in neighs:
                if valid(nr,nc) and (nr,nc) not in visited:
                    visited.add((nr,nc))
                    queue.append((dist+1,nr,nc))

        return rooms



