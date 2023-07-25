from collections import defaultdict
class Solution:
    def minSetSize(self, arr: List[int]) -> int:

        counter = collections.Counter(arr)
        freqs = [-value for value in counter.values()]
        heapq.heapify(freqs)
        
        n = len(arr)
        visited = 0
        goal = math.ceil(n /2)
        while freqs:
            freq = -heappop(freqs)
            goal -= freq 
            visited += 1
            if goal <= 0:
                return visited

        return visited