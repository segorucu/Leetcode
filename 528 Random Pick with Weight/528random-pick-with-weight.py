from random import randint
from bisect import bisect
class Solution:

    def __init__(self, w: List[int]):
        self.prefixsm = []
        prev = 0
        for val in w:
            self.prefixsm.append(prev+val)
            prev = self.prefixsm[-1]
        self.maxval = self.prefixsm[-1]
        # print(self.maxval)
        
    def pickIndex(self) -> int:
        prob = randint(0,self.maxval-1)
        # print(prob)
        ind = bisect(self.prefixsm,prob)
        # print(ind)
        if self.prefixsm[ind] == prob:
            return ind+1
        else:
            return ind


        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()