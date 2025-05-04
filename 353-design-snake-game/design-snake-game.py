class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.queue = deque()
        self.queue.append((0,0))
        self.cols = width
        self.rows = height
        self.food = deque()
        for curr in food:
            self.food.append(tuple(curr))
        self.direction = {"R": [0,1], "L": [0,-1], "U": [-1,0], "D": [1,0]}
        
    def valid(self, r, c):
        return 0 <= r < self.rows and 0 <= c < self.cols

    def move(self, direction: str) -> int:
        dr, dc = self.direction[direction]
        curr = self.queue[-1]
        nxt = (curr[0] + dr, curr[1] + dc)
        if nxt in self.queue:
            if nxt != self.queue[0]:   
                return -1
        if not self.valid(*nxt):
            return -1

        self.queue.append(nxt)
        if self.food and nxt == self.food[0]:
            self.food.popleft()
        else:
            prev = self.queue.popleft()

        return len(self.queue)-1
        


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)