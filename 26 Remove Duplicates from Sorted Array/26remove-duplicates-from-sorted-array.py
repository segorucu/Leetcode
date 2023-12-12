class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 0
        n = len(nums)
        seen = set()
        for i in range(n):
            if nums[i] not in seen:
                seen.add(nums[i])
                nums[j] = nums[i]
                j += 1
        return j
            
        