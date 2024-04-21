class TwoSum:

    def __init__(self):
        self.store = {}
        

    def add(self, number: int) -> None:
        if number in self.store:
            self.store[number] += 1
        else:
            self.store[number] = 1
        

    def find(self, value: int) -> bool:
        for a in self.store.keys():
            # print(a, value-a, self.store)
            if (value - a) in self.store:
                if a != value-a:
                    return True
                elif self.store[a] > 1:
                    return True
        return False
        


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)