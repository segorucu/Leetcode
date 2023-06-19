from collections import defaultdict
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:

        counts = defaultdict(int)
        for i in nums:
            counts[i] += 1

        ans = 0
        for num, freq in counts.items():
            if freq > 1:
                ans += freq * (freq - 1) // 2

        return ans