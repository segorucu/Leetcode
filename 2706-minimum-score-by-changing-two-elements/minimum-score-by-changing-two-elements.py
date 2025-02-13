class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        

        n = len(nums)
        if n == 3:
            return 0

        nums.sort()
        #option 1
        opt1 = nums[-1] - nums[2]
        #option 2 
        opt2 = nums[-3] - nums[0]
        #
        opt3 = nums[-2] - nums[1]

        return min(opt1, opt2, opt3)