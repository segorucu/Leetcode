class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        
        queue = deque()
        for p in piles:
            queue.append(p)

        i = 0
        Alice = Bob = 0
        while queue:
            if queue[0] > queue[-1]:
                win = queue.popleft()
            else:
                win = queue.pop()
            if i % 2 == 0:
                Alice += win
            else:
                Bob += win
        return Alice > Bob