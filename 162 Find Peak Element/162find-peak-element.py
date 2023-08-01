class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        n = len(nums)
        right = n - 1

        if len(nums) == 1:
            return 0
        elif len(nums) == 2:
            return 1 if nums[1] > nums[0] else 0

        while left <= right:
            mid = (left + right) // 2
            if mid == 0 and nums[mid] > nums[mid+1]:
                return mid
            elif mid == n-1 and nums[mid] > nums[mid-1]:
                return mid
            else:
                if nums[mid-1] < nums[mid] and nums[mid] > nums[mid+1]:
                    return mid
            if nums[mid] < nums[mid-1]:
                right = mid - 1
            else:
                left = mid + 1
            
        