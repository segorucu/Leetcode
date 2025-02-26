# from sortedcontainers import SortedList
class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        
        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1] + num)

        n = len(prefix)
        minval = maxval = 0
        ans = 0
        for i in range(1,n):
            if prefix[i] < minval:
                minval = prefix[i]
            elif prefix[i] > maxval:
                maxval = prefix[i]
            ans = max(ans, maxval - minval)

        return ans


        