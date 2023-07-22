from heapq import heappop, heapify
from itertools import permutations
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:

        m = len(nums1)
        n = len(nums2)
        arr = [[nums1[0]+nums2[0],0,0]]
        ans = []
        visited = set()
        while k > 0 and arr:
            tot, i, j = heappop(arr)
            ans.append([nums1[i],nums2[j]])
            visited.add((i,j))
            if i+1 < m and (i+1,j) not in visited:
                heappush(arr,[nums1[i+1]+nums2[j],i+1,j])
                visited.add((i+1,j))
            if j+1 < n and (i,j+1) not in visited:
                heappush(arr,[nums1[i]+nums2[j+1],i,j+1])
                visited.add((i,j+1))
            k -= 1

        


        return ans