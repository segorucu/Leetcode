class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        
        events.sort()
        maxval = 0
        minval = inf
        for event in events:
            maxval = max(maxval, event[1])
            minval = min(minval, event[0])
        
        pq = []
        cnt = 0
        j = 0
        for date in range(minval, maxval+1):
            while j < len(events) and events[j][0] == date:
                heappush(pq,events[j][1])
                j += 1

            while pq and pq[0] < date:
                heappop(pq)

            if pq and pq[0] >= date:
                heappop(pq)
                cnt += 1

        return cnt
