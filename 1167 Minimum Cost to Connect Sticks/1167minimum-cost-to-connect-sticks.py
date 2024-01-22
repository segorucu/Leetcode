from heapq import heappush, heappop, heapify
class Solution:
    def connectSticks(self, sticks: List[int]) -> int:

        if len(sticks) == 1:
            return 0

        heapify(sticks)
        sm = 0
        while sticks:
            stick1 = heappop(sticks)
            stick2 = heappop(sticks)
            new = stick1 + stick2
            sm += new
            if not sticks:
                return sm
            heappush(sticks,new)

