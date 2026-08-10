class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        

        queue = deque()
        queue.append((0,0,0))
        visited = set()
        visited.add((0, 0))
        while queue:
            steps, c, r = queue.popleft()
            if (c, r) == (x, y):
                return steps
            moves = [(2,1),(1,2),(2,-1),(1,-2),(-1,-2),(-2,-1),(-1,2),(-2,1)]
            for dc, dr in moves:
                nc = c + dc
                nr = r + dr
                if (nc, nr) not in visited:
                    queue.append((steps+1, nc, nr))
                    visited.add((nc, nr))

