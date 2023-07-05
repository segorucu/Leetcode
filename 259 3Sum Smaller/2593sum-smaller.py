class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        if len(nums) <3:
            return 0

        nums = list(sorted(nums))
        self.n = len(nums)
        self.ans = 0
        for i in range(self.n):
            self.twoSumSmaller(i, nums, target)

        return self.ans



    def twoSumSmaller(self, i, nums, target):
        left = i+1
        right = len(nums)-1
        loop = False
        while left < right:
            sm = nums[i] + nums[left] + nums[right]
            if sm < target:
                self.ans += right - left
                left += 1
            else:
                right -= 1


