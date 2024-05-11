from heapq import heapify, heappop, heappush
class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        
        
        n = len(quality)

        data = []
        for i in range(n):
            data.append((wage[i]/quality[i],quality[i]))
        data.sort(key = lambda x: x[0])

        mincost = inf
        heap = []
        qsum = 0
        for wqrat, q in data:
            heappush(heap,-q)
            qsum += q

            if len(heap) > k:
                qsum += heappop(heap)

            if len(heap) == k:
                mincost = min(mincost,qsum * wqrat)
            

        return mincost
