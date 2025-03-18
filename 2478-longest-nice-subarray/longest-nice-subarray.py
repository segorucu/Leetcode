class Solution:

    def __init__(self):
        self.counter = collections.defaultdict(list)
        self.currmp = collections.defaultdict(int)

    def check(self, i):
        for digit in self.counter[i]:
            if self.currmp[digit] > 0:
                return True
        return False

    def moveright(self,i):
        for digit in self.counter[i]:
            self.currmp[digit] -= 1

    def addright(self,i):
        for digit in self.counter[i]:
            self.currmp[digit] += 1

    def buildmp(self,nums):
        for i,num  in enumerate(nums):
            for digit in range(30):
                mask = 1 << digit
                if (num & mask):
                    self.counter[i].append(digit)

    def longestNiceSubarray(self, nums: List[int]) -> int:
        
        self.buildmp(nums)
    
        n = len(nums)
        ans = 0
        l = 0
        for r in range(n):
            while self.check(r):
                self.moveright(l)
                l += 1
            self.addright(r)
            ans = max(ans, r-l+1)

        return ans
