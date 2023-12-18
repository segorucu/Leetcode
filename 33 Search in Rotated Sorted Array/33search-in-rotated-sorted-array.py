class Solution:
    def search(self, nums: List[int], target: int) -> int:

        n = len(nums)
        if len(nums) == 2:
            if nums[0] == target:
                return 0
            elif nums[1] == target:
                return 1
            else:
                return -1
        if nums[0] == target:
            return 0
        left, right = 0, n-1
        while left < right:
            mid = (left+right) // 2
            if nums[mid] == target:
                return mid
            elif target < nums[mid] <= nums[0]:
                right = mid
            elif target < nums[0] <= nums[mid]:
                left = mid + 1
            elif nums[0] <= nums[mid] < target:
                left = mid + 1
            elif nums[0] < target < nums[mid]:
                right = mid
            elif nums[mid] < target < nums[0]:
                left = mid + 1
            elif nums[mid] <= nums[0] < target:
                right = mid


        if nums[left] == target:
            return left

        return -1

        
        