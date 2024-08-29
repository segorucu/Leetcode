from heapq import heapify, heappop, heappush
class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        
        # maxval = max(nums)
        # while min()
# ###
#         [2,1,3,5,6] 1
#         [2,2,3,5,6] 0
#         [4,2,3,5,6] 1
#         [4,4,3,5,6] 2
#         [4,4,6,5,6] 1
#         [4,4,6,5,6] 0
#         [8,4,6,5,6] 1
#         [8,8,6,5,6] 3
#         [8,8,6,10,6] 2
#         [8,8,12,10,6] 4
#         [8,8,12,10,12] 01324
#         ###

        if multiplier == 1:
            return nums

        m = max(nums)
        n= len(nums)
        hq = [[nums[i],i] for i in range(n)]
        heapify(hq)

        while k > 0 and hq[0][0] <= m:
            num,i = heappop(hq)
            num *= multiplier
            heappush(hq,[num,i])
            k -= 1

        mult = k // len(nums)
        pi = pow(multiplier,mult,10**9+7)
        k = k % len(nums)

        for i in range(n):
            hq[i][0] *= pi

        while k > 0:
            num,i = heappop(hq)
            num *= multiplier
            heappush(hq,[num,i])
            k -= 1

        MOD = 10**9+7
        for i in range(len(nums)):
            hq[i][0] = hq[i][0] % MOD
        hq.sort(key = lambda x: x[1])

        nums = [hq[i][0] for i in range(n)]

        return nums

        
