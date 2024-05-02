class Solution:
    def findMaxK(self, nums: List[int]) -> int:

        st = set(nums)
        maxval = -1
        for num in nums:
            if num > 0 and -num in st and num > maxval:
                maxval = num
        return maxval
        