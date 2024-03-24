from heapq import heapify, heappop, heappush
class Solution:
    def mostFrequentIDs(self, nums: List[int], freq: List[int]) -> List[int]:
        
        counter = collections.defaultdict(int)
        heap = []
        ans = []
        for num,fr in zip(nums,freq):
            counter[num] += fr
            if counter[num] > 0:
                heappush(heap, (-counter[num],num))
            while heap and -heap[0][0] != counter[heap[0][1]]:
                heappop(heap)
            ans.append(-heap[0][0] if heap else 0)
        return ans 
            
            
            
            
            
        return ans