from sortedcontainers import SortedList
class MyCalendarTwo:

    def __init__(self):
        self.arr = SortedList()
        self.n = 0
        

    def book(self, start: int, end: int) -> bool:
        ind = self.arr.bisect_left([start, end])
        overlapping = []
        for i in range(ind):
            if self.arr[i][1] > start:
                overlapping.append(self.arr[i][:])
        for i in range(ind,self.n):
            if self.arr[i][0] < end:
                overlapping.append(self.arr[i][:])

        for i in range(1,len(overlapping)):
            s1, e1 = overlapping[i-1]
            s2, e2 = overlapping[i]
            if e1 > s2:
                return False

        self.arr.add([start,end])
        self.n += 1
        
        return True
        


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)