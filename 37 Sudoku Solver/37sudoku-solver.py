from collections import defaultdict
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    rows[i].add(board[i][j])
                    cols[j].add(board[i][j]) 
                    boxes[(i//3,j//3)].add(board[i][j])

        integers = ["1","2","3","4","5","6","7","8","9"]

        def nextloc(i,j):
            if j == 8:
                return i+1,0
            else:
                return i,j+1

        def backtrack(board,i,j):
            if i == 9 and j == 0:
                return True

            if board[i][j] != ".":
                ii, jj = nextloc(i,j)
                res = backtrack(board,ii,jj)
                if res:
                    return True
                else:
                    return False

            box = (i//3,j//3)
            for val in integers:
                if val not in rows[i] and val not in cols[j] and val not in boxes[box]:
                    rows[i].add(val)
                    cols[j].add(val)
                    boxes[box].add(val)
                    board[i][j] = val
                    ii,jj = nextloc(i,j)
                    res = backtrack(board,ii,jj)
                    if res:
                        return True
                    rows[i].remove(val)
                    cols[j].remove(val)
                    boxes[box].remove(val)
                    board[i][j] = "."
            return False


        backtrack(board,0,0)


        return board
        