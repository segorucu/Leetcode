class ProductOfNumbers:

    def __init__(self):
        self.queue = collections.deque()
        
    def add(self, num: int) -> None:
        if num == 0:
            self.queue = collections.deque()
        else:
            if len(self.queue) == 0:
                self.queue.append(1)
                self.queue.append(num)
            else:
                self.queue.append(self.queue[-1]*num)

        
    def getProduct(self, k: int) -> int:
        if len(self.queue) <= k:
            return 0
        
        end = self.queue[-1]
        beg = self.queue[-1-k]
        return end // beg
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)