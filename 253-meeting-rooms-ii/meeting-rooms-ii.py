from collections import defaultdict
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        intervals.sort()
        rooms = 0
        occupied = SortedList()
        for s,e in intervals:
            occupied.add(e)
            while occupied[0] <= s:
                occupied.pop(0)
            rooms = max(rooms, len(occupied))
            

        return rooms
        