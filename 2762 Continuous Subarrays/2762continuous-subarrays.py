from sortedcontainers import SortedList
class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:

        sl =SortedList()
        n = len(nums)
        ans = 0
        start = 0
        for i, num in enumerate(nums):
            while len(sl) > 0 and ( abs(num-sl[0][0]) > 2 or sl[0][1] < start):
                _, ind = sl.pop(0)
                start = max(ind+1,start)
            while len(sl) > 0 and ( abs(num-sl[-1][0]) > 2 or sl[-1][1] < start):
                _, ind = sl.pop(-1)
                start = max(ind+1,start)
            ans += (i-start+1)
            sl.add((num,i))
        return ans

        return ans

        