class Leaderboard:

    def __init__(self):
        self.board = SortedList()
        self.id_score = defaultdict(int)
        

    def addScore(self, playerId: int, score: int) -> None:
        prev_score = 0
        if playerId in self.id_score:
            prev_score = self.id_score[playerId]
            self.board.remove((prev_score, playerId))
        self.board.add((prev_score + score, playerId))
        self.id_score[playerId] = prev_score + score
        

    def top(self, K: int) -> int:
        sm = 0
        n = len(self.board)
        for i in range(n-K,n):
            sm += self.board[i][0]
        return sm
        

    def reset(self, playerId: int) -> None:
        prev_score = self.id_score[playerId]
        self.board.remove((prev_score, playerId))
        del self.id_score[playerId]

        


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)