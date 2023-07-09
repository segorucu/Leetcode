from collections import deque, defaultdict
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:

        n = len(board)
        if n == 2:
            return 1

        convert = defaultdict(int)
        direction = 1
        block = 0
        mult = n
        for i in range(n-1,-1,-1):
            mult -= 1
            for j in range(n):
                block += 1
                if direction > 0:
                    convert[block] = (mult,j)
                else:
                    convert[block] = (mult,n-j-1)
            direction *= -1

        queue = deque()
        queue.append((1,0))

        seen = set()
        seen.add(1)

        while queue:
            state, steps = queue.popleft()
            if state == n**2:
                return steps
            for move in range(1,7):
                newstate = state+move
                if convert[newstate] and newstate not in seen:
                    seen.add(newstate)
                    ni, nj = convert[newstate][0], convert[newstate][1]
                    if board[ni][nj] > 0:
                        newstate = board[ni][nj]
                    queue.append((newstate,steps+1))

        return -1
                    
