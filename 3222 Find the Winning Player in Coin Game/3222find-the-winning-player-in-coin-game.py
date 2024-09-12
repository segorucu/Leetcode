class Solution:
    def losingPlayer(self, x: int, y: int) -> str:
        
        y = y // 4
        round = min(x,y)
        if round % 2 == 0:
            return "Bob"
        return "Alice"