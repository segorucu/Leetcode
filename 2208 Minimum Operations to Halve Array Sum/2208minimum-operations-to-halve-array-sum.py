import heapq
class Solution:
    def halveArray(self, nums: List[int]) -> int:

        ops = 0
        nums = [-num for num in nums]
        sm = - sum(nums)
        half = sm / 2.
        heapq.heapify(nums)

        while (sm > half):
            ops += 1
            mx = -heapq.heappop(nums)
            val = mx / 2.
            heapq.heappush(nums,-val)
            sm -= val

        return ops




        return 0