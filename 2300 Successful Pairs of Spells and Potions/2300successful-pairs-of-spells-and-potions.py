from collections import defaultdict
from heapq import heapify, heappop
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:

        potions.sort()
        m = len(potions)
        n = len(spells)

        def binarysearch(potions,target):
            left = 0
            right = m -1
            while left <= right:
                mid = (left + right) // 2
                if target > potions[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
            return left

        ans = []
        for i in range(n):
            spell = spells[i]
            target = success / spell
            val = binarysearch(potions,target)
            ans.append(m-val)

        return ans




        



