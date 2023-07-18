from collections import defaultdict
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = defaultdict(int)
        self.keyorder = []
        

    def get(self, key: int) -> int:
        if key in self.map:
            self.keyorder.remove(key)
            self.keyorder.append(key)
            return self.map[key]
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self.map[key] = value
            self.keyorder.remove(key)
            self.keyorder.append(key)
        else:
            if len(self.keyorder) == self.capacity:
                old = self.keyorder.pop(0)
                del self.map[old]
            self.keyorder.append(key)
            self.map[key] = value
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)