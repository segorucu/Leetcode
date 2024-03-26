from heapq import heapify, heappop, heappush
class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:

        n = len(nums1)
        sortd = sorted(nums1)
        MOD = 10**9 + 7
        heap = []
        sm = 0
        for i in range(n):
            diff = abs(nums1[i]-nums2[i])
            sm = (sm + diff) % MOD
            heappush(heap,(-diff,i))
        
        reduction = 0
        while heap and reduction < -heap[0][0]:
            diff, i = heappop(heap)
            diff = -diff
            ind = bisect_right(sortd,nums2[i])
            r = min(n-1,ind)
            l = max(0,ind-1)
            newdiff = min(abs(nums2[i] - sortd[r]), abs(nums2[i] - sortd[l]))
            reduction = max(reduction, max(diff - newdiff,0))

        return (sm - reduction) % MOD
