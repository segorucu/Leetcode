from heapq import heapify, heappush, heappop
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:

        hp = []
        k = len(nums)
        mmax = -inf
        for i in range(k):
            heappush(hp,(nums[i][0], i, 0))
            mmax = max(mmax, nums[i][0])

        diff = mmax - hp[0][0]
        selectedrange = [hp[0][0], mmax]
        while True:
            _, i0, i1 = heappop(hp)

            i1 += 1
            if i1 == len(nums[i0]):
                return selectedrange

            add = nums[i0][i1]
            heappush(hp, (add, i0, i1))
            mmax = max(mmax, add)
            if mmax - hp[0][0] < diff:
                diff = mmax - hp[0][0]
                selectedrange = [hp[0][0], mmax]

                

        return selectedrange
        