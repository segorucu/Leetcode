class Vector2D:

    def __init__(self, vec: List[List[int]]):
        self.m = len(vec)
        self.arr = []
        for lst in vec:
            self.arr.append(lst.copy())
        self.r = 0
        self.c = 0
        while self.r < self.m and self.c == len(self.arr[self.r]):
            self.r += 1
            self.c = 0
            
    def next(self) -> int:
        val = self.arr[self.r][self.c]
        self.c += 1
        while self.r < self.m and self.c == len(self.arr[self.r]):
            self.r += 1
            self.c = 0
        return val

        
    def hasNext(self) -> bool:
        if self.r >= self.m:
            return False
        return True

        


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(vec)
# param_1 = obj.next()
# param_2 = obj.hasNext()