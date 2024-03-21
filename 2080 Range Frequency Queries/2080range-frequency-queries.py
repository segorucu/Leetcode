from bisect import bisect_left
class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        self.c = collections.defaultdict(list)
        for i,a in enumerate(arr):
            self.c[a].append(i)
        

    def query(self, left: int, right: int, value: int) -> int:
        beg = bisect_left(self.c[value],left)
        end = bisect_right(self.c[value],right)
        # print(self.c[value],left,right,beg,end)
        return end - beg
        
        


# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)