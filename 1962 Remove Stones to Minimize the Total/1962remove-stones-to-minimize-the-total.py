import heapq
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles = [-pile for pile in piles]
        heapq.heapify(piles)

        for _ in range(k):
            val = -heapq.heappop(piles)
            val -= val // 2
            heapq.heappush(piles,-val)

        return -sum(piles)