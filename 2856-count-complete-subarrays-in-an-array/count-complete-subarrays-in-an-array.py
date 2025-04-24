from functools import cache
from collections import defaultdict
class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:

        k = len(set(nums))
        n = len(nums)

        tot = 0
        for left in range(n-k+1):
            curr = set()
            for right in range(left,n):
                curr.add(nums[right])
                if len(curr) == k:
                    tot += n-right
                    break

        return tot
        