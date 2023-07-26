class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()
        for i,num in enumerate(nums):
            if num >= 0:
                break
            elif num < 0:
                nums[i] *= -1
                k -= 1
            if k == 0:
                return sum(nums)

        mnval = min(nums)
        i = nums.index(mnval)
        if k % 2 == 1:
            nums[i] *= -1

        return sum(nums)

