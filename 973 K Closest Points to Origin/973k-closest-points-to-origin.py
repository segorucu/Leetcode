from heapq import heappush, heappop
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        heap = []
        for i,j in points:
            dist = i*i + j*j
            heappush(heap,(-dist,i,j))
            if len(heap) > k:
                heappop(heap)
                
        return [[val[1],val[2]] for val in heap]
            
            
        