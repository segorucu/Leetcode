class Solution:
    

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        m = len(board)
        n = len(board[0])
        visited = set()
        def isontheedge(i,j):
            return i == 0 or i == (m-1) or j == 0 or j == n-1

        def valid(i,j):
            return 0 <= i < m and 0 <= j < n and board[i][j] == "O" 

        def explore(i, j):
            visited.add((i,j))
            currset.add((i,j))
            res = isontheedge(i,j)
            for move in directions:
                ni = i + move[1]
                nj = j + move[0]
                if valid(ni,nj) and (ni,nj) not in visited:
                    res2 = explore(ni,nj)
                    res = res or res2
            return res

        for  i in (range(m)):
            for j in range(n):
                if board[i][j] == "O" and (i,j) not in visited:
                    currset = set()
                    res = explore(i,j)
                    if not res:
                        for curr in currset:
                            board[curr[0]][curr[1]] = 'X'

        return board


        