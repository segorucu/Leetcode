from heapq import heappush, heappop
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        arr = []
        for num in nums:
            heappush(arr,num)
            if len(arr) > k:
                heappop(arr)
                
        return arr[0]
        
        
        