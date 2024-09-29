from sortedcontainers import SortedSet
class AllOne:
    def __init__(self):
        self.sortedset = SortedSet()
        self.counter = {}
        
    def inc(self, key: str) -> None:
        if key in self.counter:
            self.sortedset.remove((self.counter[key],key))
            self.counter[key] += 1
        else:
            self.counter[key] = 1
        self.sortedset.add((self.counter[key],key))
            
    
    def dec(self, key: str) -> None:
        self.sortedset.remove((self.counter[key],key))
        if self.counter[key] == 1:
            del self.counter[key]
        else:
            self.counter[key] -= 1
            self.sortedset.add((self.counter[key],key))
        

    def getMaxKey(self) -> str:
        if not self.sortedset:
            return ""
        return self.sortedset[-1][1]
        

    def getMinKey(self) -> str:
        if not self.sortedset:
            return ""
        return self.sortedset[0][1]
        


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()