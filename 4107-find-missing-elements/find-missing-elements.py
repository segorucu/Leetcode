class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        
        minval = min(nums)
        maxval = max(nums)
        nums = set(nums)
        values = []
        for i in range(minval, maxval+1):
            if i not in nums:
                values.append(i)

        return values

        