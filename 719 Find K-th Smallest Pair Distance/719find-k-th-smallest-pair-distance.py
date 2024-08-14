from sortedcontainers import SortedList
class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:


        nums.sort()
        n = len(nums)

        def count(m):
            l = 0
            r = 1
            add = 0
            while r < n:
                while nums[r] - nums[l] > m:
                    l += 1
                add += r-l
                r += 1
            return add


        l = 0
        r = nums[-1]
        while l < r:
            m = (l+r) // 2
            curr = count(m)
            if curr < k:
                l = m + 1
            else:
                r = m

        return r

        