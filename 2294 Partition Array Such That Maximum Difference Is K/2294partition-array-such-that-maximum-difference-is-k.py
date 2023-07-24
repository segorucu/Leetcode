class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:

        nums.sort()
        group = 1
        left = nums[0]
        for num in nums:
            if num - left > k:
                group += 1
                left = num
        return group