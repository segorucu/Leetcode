class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        
        if not nums:
            return [[lower,upper]]
 
        ans = []
        if nums[0] > lower:
            ans.append([lower,nums[0]-1])
        lastcovered = nums[0]
        n = len(nums)
        for i in range(1,n):
            if nums[i] == lastcovered + 1:
                lastcovered = nums[i]
            else:
                ans.append([lastcovered+1,nums[i]-1])
                lastcovered = nums[i]

        if lastcovered < upper:
            ans.append([lastcovered+1,upper])

        return ans