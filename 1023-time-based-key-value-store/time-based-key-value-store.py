from bisect import bisect_left
class TimeMap:

    def __init__(self):
        self.mp = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.mp[key].append((timestamp,value))
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.mp or self.mp[key][0][0] > timestamp:
            return ""

        ind = bisect_left(self.mp[key], (timestamp,))
        if len(self.mp[key]) == ind:
            return self.mp[key][ind-1][1]
        if self.mp[key][ind][0] == timestamp:
            return self.mp[key][ind][1]
        return self.mp[key][ind-1][1]
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)