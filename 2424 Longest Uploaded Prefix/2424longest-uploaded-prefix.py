from sortedcontainers import SortedList
class LUPrefix:

    def __init__(self, n: int):
        self.sl = set()
        self.last = 0
        

    def upload(self, video: int) -> None:
        self.sl.add(video)
        if video == self.last + 1:
            attempt = self.last+1
            while attempt in self.sl:
                self.last = attempt
                attempt += 1
        

    def longest(self) -> int:
        return self.last
        


# Your LUPrefix object will be instantiated and called as such:
# obj = LUPrefix(n)
# obj.upload(video)
# param_2 = obj.longest()