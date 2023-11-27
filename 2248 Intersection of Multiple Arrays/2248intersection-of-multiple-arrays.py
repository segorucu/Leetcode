from collections import defaultdict
class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        mp = defaultdict(int)
        for num in nums:
            for val in num:
                mp[val] += 1

        k = len(nums)
        lst = []
        for val in mp:
            if mp[val] == k:
                lst.append(val)

        lst = sorted(lst)
        return lst

        