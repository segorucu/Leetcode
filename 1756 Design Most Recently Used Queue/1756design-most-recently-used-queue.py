from sortedcontainers import SortedList
class MRUQueue:

    def __init__(self, n: int):
        # self.sl = SortedList()
        self.mp = collections.defaultdict(int)
        self.n = n
        for i in range(1,n+1):
            # self.sl.add((i,i))
            self.mp[i] = i
        

    def fetch(self, k: int) -> int:
        val = self.mp[k]
        for i in range(k+1,self.n+1):
            self.mp[i-1] = self.mp[i]
        self.mp[self.n] = val

        return val
        


# Your MRUQueue object will be instantiated and called as such:
# obj = MRUQueue(n)
# param_1 = obj.fetch(k)