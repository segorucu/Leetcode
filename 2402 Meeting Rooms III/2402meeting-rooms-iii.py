from heapq import heapify, heappush, heappop
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        
        meetings.sort()
        N = len(meetings)
        heapcurr = []
        available = []
        for i in range(n):
            heappush(available,i)
        rooms = n * [1]
        
        for in_s, end_s in meetings:
            #  = heappop(meetings)
            while heapcurr and in_s >= heapcurr[0][0]:
                currend, room = heappop(heapcurr)
                heappush(available,room)
            if not available:
                currend, room = heappop(heapcurr)
                dum = currend + end_s - in_s
            else:
                room = heappop(available)
                dum = end_s
            heappush(heapcurr,(dum,room))
            rooms[room] += 1

        maxval = max(rooms)
        room = rooms.index(maxval)

        return room