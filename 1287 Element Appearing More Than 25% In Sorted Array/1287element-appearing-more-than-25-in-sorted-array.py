from collections import Counter
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        counter = Counter(arr)
        ans = None
        count = 0
        for key, val in counter.items():
            if val > count:
                count = val
                ans = key
        return ans
        