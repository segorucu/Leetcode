from collections import defaultdict
from heapq import heappush
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        if w < min(capital):
            return w

        hsh = defaultdict(list)
        for c,p in zip(capital,profits):
            hsh[c].append(p)

        sorted_keys = sorted(hsh.keys())
        maxheap = []

        visited = set()
        def add2heap(start,w,maxheap):
            key = None
            for i in range(start,len(sorted_keys)):
                key = sorted_keys[i]
                if key <= w and key not in visited:
                    visited.add(key)
                    for val in hsh[key]:
                        heappush(maxheap,-val)
                if key > w:
                    break
            if not key:
                return -1
            return i

        start = add2heap(0,w,maxheap)
        while k > 0 and maxheap:
            p = -heappop(maxheap)
            w += p
            if start >= 0:
                start = add2heap(start,w,maxheap)
            k -= 1

        return w



        