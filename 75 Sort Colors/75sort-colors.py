class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        zeros = nums.count(0)
        ones = nums.count(1)
        twos = nums.count(2)

        count = 0
        for i in range(zeros):
            nums[count] = 0
            count += 1
        for i in range(ones):
            nums[count] = 1
            count += 1
        for i in range(twos):
            nums[count] = 2
            count += 1

        return 