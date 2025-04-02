class Solution:

    def __init__(self, nums: List[int]):
        self.indexmp = defaultdict(list)
        for i,num in enumerate(nums):
            self.indexmp[num].append(i)
        

    def pick(self, target: int) -> int:
        i = random.randint(0,len(self.indexmp[target])-1)
        return self.indexmp[target][i]
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)