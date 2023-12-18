class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for i in range(9):
            row = set()
            for j in range(9):
                if board[i][j] == ".":
                    continue
                elif board[i][j] not in row:
                    row.add(board[i][j])
                else:
                    return False

        
        for j in range(9):
            col = set()
            for i in range(9):
                if board[i][j] == ".":
                    continue
                elif board[i][j] not in col:
                    col.add(board[i][j])
                else:
                    return False

        for k in range(9):
            box = set()
            col = 3 * (k % 3)
            row = 3 * (k // 3)
            for i in range(3):
                for j in range(3):
                    ii = row + i
                    jj = col + j
                    if board[ii][jj] == ".":
                        continue
                    elif board[ii][jj] not in box:
                        box.add(board[ii][jj])
                    else:
                        return False

        return True

        