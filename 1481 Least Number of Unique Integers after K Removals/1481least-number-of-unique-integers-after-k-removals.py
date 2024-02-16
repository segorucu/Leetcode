from collections import Counter
from heapq import heapify, heappop
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:

        counter = Counter(arr)
        unique = len(counter.keys())
        freqs = list(counter.values())
        del counter
        heapify(freqs)
        while freqs:
            key = heappop(freqs)
            k -= key
            if k < 0:
                return unique
            elif k == 0:
                return unique-1
            unique -= 1

        return unique
