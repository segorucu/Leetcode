class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        
        minval = inf
        ans = -1
        for num in nums:
            if num > minval:
                ans = max(ans, num - minval)
            minval = min(minval, num)

        return ans
