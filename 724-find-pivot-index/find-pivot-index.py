class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        sm = sum(nums)
        left = 0
        for i,num in enumerate(nums):
            if (sm - num) % 2 == 0:
                if left == (sm - num) // 2:
                    return i
            left += num

        return -1