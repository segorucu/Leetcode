from heapq import heapify, heappop, heappush
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:

        hp = []
        for gift in gifts:
            heappush(hp,-gift)

        while k:
            val = heappop(hp)
            val *= -1
            remain = math.floor(val ** 0.5)
            heappush(hp,-remain)
            k -= 1

        return -sum(hp)
        
