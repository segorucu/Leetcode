from functools import cache
class Solution:
    def maxSumAfterOperation(self, nums: List[int]) -> int:
    
        prev_used = prev_not_used = -inf
        maxval = -inf
        for num in nums:
            used = max(num ** 2 ,prev_not_used + num ** 2, prev_used + num)
            not_used = max(num, prev_not_used + num)
            maxval = max(maxval, used, not_used)
            prev_used, prev_not_used = used, not_used


        return maxval
