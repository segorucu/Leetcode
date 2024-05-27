class Solution:
    def specialArray(self, nums: List[int]) -> int:
        
        n = len(nums)

        nums.sort()
        minval = min(nums)
        maxval = max(nums)
        for val in range(1,maxval+1):
            ind = bisect_left(nums,val)
            if val == n - ind:
                return val

        return -1
