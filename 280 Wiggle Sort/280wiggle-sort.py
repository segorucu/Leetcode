class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        for i in range(1,n):
            if i % 2 == 1 and nums[i-1] > nums[i]:
                nums[i-1], nums[i] = nums[i], nums[i-1]
            elif i % 2 == 0 and nums[i-1] < nums[i]:
                nums[i-1], nums[i] = nums[i], nums[i-1]
        return nums


        