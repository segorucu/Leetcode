class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        j = 0
        for i,num in enumerate(nums):
            if num != val:
                nums[j] =num
                j += 1
        return j
        