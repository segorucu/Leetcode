from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        freq = defaultdict(int)
        freq[0] = 1
        prefix = 0
        n = len(nums)
        ans = 0
        for i in range(n):
            prefix += nums[i]
            if prefix - k in freq:
                ans += freq[prefix-k]
            freq[prefix] += 1
            

        return ans