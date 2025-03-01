class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        for i in range(n-1):
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0

        zeros = 0
        for num in nums:
            if num == 0:
                zeros += 1

        r = 0
        while 0 in nums:
            nums.remove(0)

        for i in range(zeros):
            nums.append(0)

        return nums