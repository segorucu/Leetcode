from collections import defaultdict
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        events = []
        for s,e in intervals:
            events.append((s,"s"))
            events.append((e,"e"))
        events.sort()

        stack = 0
        ans = 0
        for i in range(len(events)):
            time, state = events[i]
            if state == "s":
                stack += 1
            else:
                stack -= 1
            ans = max(ans, stack)

        return ans
        