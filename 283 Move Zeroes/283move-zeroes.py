class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n = len(nums)
        if n == 1:
            return nums

        for i, num in enumerate(nums):
            if num == 0:
                j = i +1
                while j < n and nums[j] == 0:
                    j += 1
                    if j == n:
                        break
                if j == n:
                    break
                nums[i], nums[j] = nums[j], nums[i]

        
        return nums
            

