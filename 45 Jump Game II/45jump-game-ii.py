from collections import defaultdict
class Solution:
    def jump(self, nums: List[int]) -> int:

        minstep = defaultdict(int)
        minstep[0] = 0
        n = len(nums)
        for i in range(n-1):
            num = nums[i]
            for j in range(1,num+1):
                if minstep[i+j] == 0:
                    minstep[i+j] = minstep[i]+1
                else:
                    minstep[i+j] = min(minstep[i+j],minstep[i]+1)

        return minstep[n-1]