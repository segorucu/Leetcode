from collections import Counter
import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = Counter(s)
        heap = []
        for key, val in counter.items():
            heap.append((-val,key))
        heapq.heapify(heap)
        n = len(s)
        
        if n % 2 == 0:
            mx = n // 2
        else:
            mx = n // 2 + 1
        if -heap[0][0] > mx:
            return ""

        ans = []
        while heap:
            val, key = heapq.heappop(heap)
            if len(ans) == 0 or ans[-1] != key:
                val = -val -1
                ans.append(key)
            if val > 0:
                heap.append((-val,key))

        return ''.join(ans)

        
        