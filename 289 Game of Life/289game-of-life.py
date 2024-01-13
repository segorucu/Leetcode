class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        directions = [(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)]
        def valid(i,j):
            return 0 <= i < m and 0 <= j < n

        def countones(i,j):
            ones = 0
            for move in directions:
                ni = i + move[1]
                nj = j + move[0]
                if valid(ni,nj) and board[ni][nj] == 1:
                    ones += 1
            return ones

        def shoulditdie(i,j):
            ones = countones(i,j)
            if ones < 2 or ones > 3:
                return True
            else:
                return False

        def shoulditbeborn(i,j):
            ones = countones(i,j)
            return ones == 3
            

        dying = set()
        born = set()
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] == 1 and shoulditdie(i,j):
                    dying.add((i,j))
                elif board[i][j] == 0 and shoulditbeborn(i,j):
                    born.add((i,j))

        for i,j in dying:
            board[i][j] = 0
        for i,j in born:
            board[i][j] = 1
        return board
        