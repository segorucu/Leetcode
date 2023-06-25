class StockSpanner:

    def __init__(self):   
        self.stack = []
        self.index = []
        

    def next(self, price: int) -> int:
        days = 1
        while self.stack and self.stack[-1] <= price:
            val = self.stack.pop()
            days += self.index.pop()
        self.stack.append(price)
        self.index.append(days)
        return days
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)