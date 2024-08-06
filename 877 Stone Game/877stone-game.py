class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        
        queue = collections.deque()
        queue.extend(piles)
        Alice = Bob = 0
        i = 0
        while queue:
            if queue[0] > queue[-1]:
                curr = queue.popleft()
            else:
                curr = queue.pop()
            if i % 2 == 0:
                Alice += curr
            else:
                Bob += curr

        return Alice > Bob