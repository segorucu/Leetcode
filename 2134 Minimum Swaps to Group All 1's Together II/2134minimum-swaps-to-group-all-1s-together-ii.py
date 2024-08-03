class Solution:
    def minSwaps(self, nums: List[int]) -> int:

        tot_ones = nums.count(1)
        N = len(nums)
        if tot_ones == 0:
            return 0

        ones = max_ones = l = 0
        for r in range(2*N):
            if nums[r % N] == 1:
                ones += 1
            while r-l+1 > tot_ones:
                if nums[l % N] == 1:
                    ones -= 1
                l += 1
            max_ones = max(max_ones,ones)

        return tot_ones - max_ones
        