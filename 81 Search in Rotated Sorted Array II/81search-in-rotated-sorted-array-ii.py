class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left = 0
        right = len(nums) -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target or nums[left] == target or nums[right] == target:
                return True
            elif nums[mid] > nums[0] and nums[mid] < target:
                left = mid + 1
            elif nums[mid] > nums[0] and nums[mid] > target:
                right = mid - 1
            elif nums[mid] < nums[-1] and nums[mid] < target:
                left = mid + 1
            elif nums[mid] < nums[-1] and nums[mid] > target:
                right = mid - 1
            else:
                for num in nums:
                    if target == num:
                        return True
                else:
                    return False
        return False
