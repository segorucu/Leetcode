import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        stones = [-stone for stone in stones ]
        heapq.heapify(stones)

        while len(stones) > 1:
            y = abs(heapq.heappop(stones))
            x = abs(heapq.heappop(stones))
            if y == x:
                continue
            else:
                heapq.heappush(stones,x-y)

        if len(stones) == 0:
            return 0
        else:
            return -stones[0]

