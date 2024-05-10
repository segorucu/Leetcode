from heapq import heappush, heappop, heapify
class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        
        heap = []
        n = len(arr)
        for i in range(n-1):
            heappush(heap,(arr[i]/arr[-1],i,n-1))

        for it in range(k):
            div, i, j = heappop(heap)
            if it == k-1:
                return [arr[i],arr[j]]
            j -= 1
            if j > i:
                heappush(heap,(arr[i]/arr[j],i,j))
            
        