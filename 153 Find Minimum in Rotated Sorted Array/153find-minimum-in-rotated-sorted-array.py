class Solution:
    def findMin(self, nums: List[int]) -> int:

        if nums[0] < nums[-1]:
            return nums[0]
        if len(nums) == 1:
            return nums[0]


        n = len(nums)
        left = 0
        right = n - 1
        while left <= right:
            mid = (left + right) // 2
            pre = (mid - 1) % n
            post = (mid + 1) % n
            if nums[pre] > nums[mid]:
                return nums[mid]
            if nums[post] < nums[mid]:
                return nums[post]
            elif nums[mid] > nums[0]: 
                left = mid + 1
            else:
                right = mid - 1