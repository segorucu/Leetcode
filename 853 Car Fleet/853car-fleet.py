from heapq import heapify, heappop, heappush
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        n = len(position)
        if n == 1:
            return n
        data = []
        for i in range(n):
            heappush(data,(target - position[i],speed[i]))

        p1, v1 = heappop(data)
        group = 1
        while data: 
            p2, v2 = heappop(data)
            if v1 < v2:
                meeting = (v2*p1-v1*p2) / (v2 - v1)
                if meeting < 0:
                    group += 1
                    v1 = v2
                    p1 = p2
            else:
                group += 1
                p1 = p2
                v1 = v2


        return group

        