class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        n = len(nums)
        for _ in range(k):
            dum = nums[-1]
            for i in range(n):
                dum0 = dum
                dum = nums[i]
                nums[i] = dum0

