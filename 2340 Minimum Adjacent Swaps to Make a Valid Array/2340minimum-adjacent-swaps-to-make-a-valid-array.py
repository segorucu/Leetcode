class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        
        n = len(nums)
        if n == 1:
            return 0

        minval = min(nums)
        maxval = max(nums)
        if minval == maxval:
            return 0
        minind = nums.index(minval)
        for i in range(n):
            if nums[i] == maxval:
                maxind = i

        cost = minind + (n-1-maxind)
        if minind > maxind:
            cost -= 1
        return cost