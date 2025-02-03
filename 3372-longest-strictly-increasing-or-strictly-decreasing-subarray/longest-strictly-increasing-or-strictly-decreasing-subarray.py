class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        

        
        increasing = 1
        curr = 1
        n = len(nums)
        for i in range(1,n):
            if nums[i] > nums[i-1]:
                curr += 1
            elif nums[i] <= nums[i-1]:
                curr = 1
            increasing = max(increasing, curr)

        curr = 1
        decreasing = 1
        for i in range(1,n):
            if nums[i] < nums[i-1]:
                curr += 1
            elif nums[i] >= nums[i-1]:
                curr = 1
            decreasing = max(decreasing, curr)
        
        return max(increasing,decreasing)
            

