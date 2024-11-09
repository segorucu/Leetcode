class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        
        n = len(nums)
        ans = 0
        for l in range(n):
            biggest = smallest = nums[l]
            for r in range(l+1,n):
                biggest = max(biggest, nums[r])
                smallest = min(smallest, nums[r])
                ans += biggest - smallest
        return ans            