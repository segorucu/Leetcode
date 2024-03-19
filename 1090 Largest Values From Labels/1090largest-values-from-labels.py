from heapq import heapify, heappop, heappush
class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int:
        
        queue = []
        for v,l in zip(values,labels):
            heappush(queue,(-v,l))

        sm = 0
        counter = collections.defaultdict(int)
        while queue and numWanted:
            v,l = heappop(queue)
            v = -v
            if counter[l] < useLimit:
                sm += v
                numWanted -= 1
                counter[l] += 1

        return sm