from collections import Counter
import math
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        counter = Counter(nums)

        sm = 0
        for key, val in counter.items():
            if val == 1:
                return -1
            count = math.ceil(val / 3)
            sm += count

        return sm