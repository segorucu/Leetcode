from collections import defaultdict
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        heapq.heapify(intervals)
        rooms = 1
        ending = [0]
        while intervals:
            beg, end = heapq.heappop(intervals)
            for i in range(rooms):
                if beg >= ending[i]:
                    ending[i] = end
                    break
            else:
                rooms += 1
                ending.append(end)

        return rooms
        