from heapq import heapify, heappop, heappush
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:

        n = len(heights)
        prev = heights[0]
        stack = []
        usedladder = 0
        for i,num in enumerate(heights):
            diff = num - prev
            if diff > 0:
                if usedladder < ladders:
                    heappush(stack,diff)
                    usedladder += 1
                else:
                    if ladders > 0 and diff > stack[0]:    
                        heappush(stack,diff)
                        diff = heappop(stack)
                    if bricks >= diff:
                        bricks -= diff
                    else:
                        return i-1
            prev = num

        return n-1

        