from sortedcontainers import SortedList
class Solution:
    def subarraysWithMoreZerosThanOnes(self, nums: List[int]) -> int:

        MOD =10**9 + 7
        n = len(nums)
        sl = SortedList()
        sl.add(0)
        count = 0
        for i in range(n):
            if i == 0:
                last = 1 if nums[0] > 0 else -1
                sl.add(last)
                if last == 1:
                    count = 1
            else:
                last += (1 if nums[i] > 0 else -1)
                sl.add(last)
                count += bisect_left(sl, last)
                count = count % MOD
            
        return count
        