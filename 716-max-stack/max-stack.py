class MaxStack:

    def __init__(self):
        self.hp = []
        self.stack = SortedList()
        self.mp = defaultdict(list)
        self.time = 0
        self.removed = set()
        

    def push(self, x: int) -> None:
        heappush(self.hp,(-x,-self.time))
        self.stack.add((self.time,x))
        self.mp[x].append(self.time)
        self.time += 1
        # print(self.hp)
        return
        

    def pop(self) -> int:
        time, x = self.stack.pop()
        self.mp[x].pop()
        self.removed.add(time)
        return x
        

    def top(self) -> int:
        # print(self.stack[-1][1])
        return self.stack[-1][1]
        

    def peekMax(self) -> int:
        # print(self.hp)
        while self.hp and -self.hp[0][1] in self.removed:
            heappop(self.hp)
        return -self.hp[0][0]
        

    def popMax(self) -> int:
        while self.hp and -self.hp[0][1] in self.removed:
            heappop(self.hp)
        x, time = heappop(self.hp)
        x = -x
        time = -time
        # print(x)
        self.mp[x].pop()
        self.stack.remove((time,x))
        return x
        


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()