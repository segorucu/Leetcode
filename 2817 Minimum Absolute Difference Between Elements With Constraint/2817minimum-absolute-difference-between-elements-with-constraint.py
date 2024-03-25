from sortedcontainers import SortedList
class Solution:
    def minAbsoluteDifference(self, nums: List[int], x: int) -> int:
        
        sl = SortedList()
        ans = inf
        n = len(nums)
        for i in range(x,n):
            sl.add(nums[i-x])
            ind = bisect_left(sl,nums[i])
            l = max(0,ind-1)
            r = min(ind,len(sl)-1)
            ans = min(ans,abs(sl[r]-nums[i]),abs(sl[l]-nums[i]))
            if ans == 0:
                return 0

        return ans
