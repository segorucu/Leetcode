from heapq import heappush, heappop
class SmallestInfiniteSet:

    def __init__(self):
        self.heap = []
        self.minnum = 1
        

    def popSmallest(self) -> int:
        if self.heap:
            return heappop(self.heap)

        self.minnum += 1
        return self.minnum - 1
        

    def addBack(self, num: int) -> None:
        if num < self.minnum and num not in self.heap:
            heappush(self.heap,num)

        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)