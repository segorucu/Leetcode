from heapq import heappush, heappop
from collections import Counter, deque
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:

        counts = Counter(words)

        heap = []
        for word, freq in counts.items():
            heappush(heap,(-freq,word))

        ans = []
        for _ in range(k):
            ans.append(heappop(heap))

        ans = sorted(ans, key=lambda x: (x[0], x[1]))
        
        return [val[1] for val in ans]