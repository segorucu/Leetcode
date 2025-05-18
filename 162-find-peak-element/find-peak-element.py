class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 1
        n = len(nums)
        right = n - 2
        if n == 1:
            return 0

        if nums[0] > nums[1]:
            return 0

        if nums[-1] > nums[-2]:
            return n-1


        while left <= right:
            mid = (left+right) // 2
            if nums[mid] > max(nums[mid-1],nums[mid+1]):
                return mid
            if nums[mid+1] > nums[mid]:
                left = mid + 1
            else:
                right = mid

        return left

        