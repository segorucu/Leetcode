class TicTacToe:

    def __init__(self, n: int):
        self.diag1 = [0, 0]
        self.diag2 = [0, 0]
        self.n = n
        self.rows = defaultdict(list)
        self.cols = defaultdict(list)
        for i in range(n):
            self.rows[i] = [0, 0]
            self.cols[i] = [0, 0]
            
        
    def move(self, row: int, col: int, player: int) -> int:
        self.rows[row][player-1] += 1
        if self.rows[row][player-1] == self.n:
            return player
        self.cols[col][player-1] += 1
        if self.cols[col][player-1] == self.n:
            return player
        if row + col == self.n-1:
            self.diag2[player-1] += 1
            if self.diag2[player-1] == self.n:
                return player
        if row == col:
            self.diag1[player-1] += 1
            if self.diag1[player-1] == self.n:
                return player
        return 0
    

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)