from sortedcontainers import SortedList
from collections import defaultdict
class MyCalendar:

    def __init__(self):
        self.sl = SortedList()
        self.mp = defaultdict(int)
        

    def book(self, start: int, end: int) -> bool:

        if self.sl:
            ind = bisect_right(self.sl,start)
            n = len(self.sl)
            r = min(ind,n-1)
            l = max(0,ind-1)
            # print(self.sl,self.mp,l,r,self.sl[r],end)
            if self.sl[l] == start or self.sl[r] == start:
                # print("a")
                return False
            if self.sl[l] < start:
                if self.mp[self.sl[l]] > start:
                    # print("b")
                    return False
            if self.sl[r] > start:
                if self.sl[r] < end:
                    # print("c")
                    return False
            # print("s")
            self.sl.add(start)
            self.mp[start] = end
            return True
        else:
            self.sl.add(start)
            self.mp[start] = end
            return True
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)