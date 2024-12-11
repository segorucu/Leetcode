class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:

        seen = set()
        m = len(board)
        n = len(board[0])
        def valid(r,c):
            return 0 <= r < m and 0 <= c < n

        directions = [(0,1),(1,0),(-1,0),(0,-1)]

        def dfs(r,c):
            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                if valid(nr,nc) and (nr,nc) not in seen and board[nr][nc] == "X":
                    seen.add((nr,nc))
                    dfs(nr,nc)

        ships = 0
        for r in range(m):
            for c in range(n):
                if (r,c) not in seen and board[r][c] == "X":
                    ships += 1
                    seen.add((r,c))
                    dfs(r,c)
        return ships

        