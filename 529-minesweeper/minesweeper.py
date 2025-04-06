class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        
        R = len(board)
        C = len(board[0])

        def valid(r,c):
            return 0 <= r < R and 0 <= c < C

        mineadjacent = defaultdict(int)
        for r in range(R):
            for c in range(C):
                neighs = [(r+1,c),(r+1,c-1),(r+1,c+1),(r-1,c),(r-1,c-1),(r-1,c+1),(r,c-1),(r,c+1)]
                for nr,nc in neighs:
                    if valid(nr,nc) and board[nr][nc] in {"M","X"}:
                        mineadjacent[(r,c)] += 1

        if board[click[0]][click[1]] in {"M"}:
            board[click[0]][click[1]] = "X"
            return board

        def recurse(r,c):
            if mineadjacent[(r,c)] > 0:
                board[r][c] = str(mineadjacent[(r,c)])
                return

            board[r][c] = "B"
            neighs = [(r+1,c),(r+1,c-1),(r+1,c+1),(r-1,c),(r-1,c-1),(r-1,c+1),(r,c-1),(r,c+1)]
            for nr,nc in neighs:
                if valid(nr,nc) and board[nr][nc] == "E":
                    recurse(nr,nc)

        

        recurse(*click)


        return board