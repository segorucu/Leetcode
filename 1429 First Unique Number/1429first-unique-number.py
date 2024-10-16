from sortedcontainers import SortedList
class FirstUnique:

    def __init__(self, nums: List[int]):
        counter = collections.Counter(nums)
        self.uniquedeque = collections.deque()
        self.uniqueset = set()
        self.banned = set()
        for key, val in counter.items():
            if val == 1:
                self.uniquedeque.append(key)
                self.uniqueset.add(key)
            else:
                self.banned.add(key)
        

    def showFirstUnique(self) -> int:
        while self.uniquedeque and self.uniquedeque[0] in self.banned:
            self.uniquedeque.popleft()

        if self.uniquedeque:
            return self.uniquedeque[0]
        return -1
        

    def add(self, value: int) -> None:
        if value not in self.banned:
            if value not in self.uniqueset:
                self.uniquedeque.append(value)
                self.uniqueset.add(value)
            else:
                self.uniqueset.remove(value)
                self.banned.add(value)
        


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)