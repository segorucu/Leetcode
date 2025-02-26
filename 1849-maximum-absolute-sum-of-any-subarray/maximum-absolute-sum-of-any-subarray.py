class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        

        n = len(prefix)
        minval = maxval = 0
        ans = 0
        curr = 0
        for num in nums:
            curr += num
            if curr < minval:
                minval = curr
            elif curr > maxval:
                maxval = curr
            ans = max(ans, maxval - minval)

        return ans


        