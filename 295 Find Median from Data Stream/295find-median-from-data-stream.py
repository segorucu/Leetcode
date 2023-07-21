from heapq import heappush, heappop
class MedianFinder:

    def __init__(self):
        self.findmax = []
        self.findmin = []
        

    def addNum(self, num: int) -> None:
        if not self.findmax and not self.findmin:
            heappush(self.findmin,num)
        elif not self.findmax:
            if num <= self.findmin[0]:
                heappush(self.findmax,-num)
            else:
                val = heappop(self.findmin)
                heappush(self.findmax,-val)
                heappush(self.findmin,num)
        else:
            if -self.findmax[0] <= num <= self.findmin[0]:
                if len(self.findmax) >= len(self.findmin):
                    heappush(self.findmin,num)
                else:
                    heappush(self.findmax,-num)
            elif -self.findmax[0] > num:
                if len(self.findmax) >= len(self.findmin):
                    val = -heappop(self.findmax)
                    heappush(self.findmin,val)
                    heappush(self.findmax,-num)
                else:
                    heappush(self.findmax,-num)
            elif num > self.findmin[0]:
                if len(self.findmax) >= len(self.findmin):
                    heappush(self.findmin,num)
                else:
                    val = heappop(self.findmin)
                    heappush(self.findmax,-val)
                    heappush(self.findmin,num)
            else:
                print("error")


    def findMedian(self) -> float:
        if (len(self.findmin) + len(self.findmax)) % 2 == 0:
            return (-self.findmax[0]+self.findmin[0]) / 2
        else:
            return self.findmin[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()