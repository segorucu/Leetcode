from sortedcontainers import SortedList
class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        suffix = n * [0]
        suffix[-1] = -inf

        for i in range(n-2,-1,-1):
            suffix[i] = max(suffix[i+1],nums[i+1])

        sl = SortedList()
        sl.add(nums[0])
        ans = -inf
        for i in range(1,n-1):
            ind = bisect_right(sl,nums[i]-1)
            ind = ind-1
            if   ind >= 0 and sl[ind] < nums[i] < suffix[i]:
                ans = max(ans, sl[ind] - nums[i] + suffix[i])
            # print(i,ind,sl[ind],nums[i])
            sl.add(nums[i])
        return ans