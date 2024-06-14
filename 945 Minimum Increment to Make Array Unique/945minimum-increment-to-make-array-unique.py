class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:

#   1 1 2 2 3 7
#   1 2 3 4 5 7
        nums.sort()
        n = len(nums)
        ans = 0
        for i in range(1,n):
            if nums[i] <= nums[i-1]:
                ans += (nums[i-1] + 1 - nums[i])
                nums[i] = nums[i-1] + 1

        return ans
        