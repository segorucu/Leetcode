class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        
        events.sort(key = lambda x: (x[1], x[0]))
        maxval = 0
        minval = inf
        for event in events:
            maxval = max(maxval, event[1])
            minval = min(minval, event[0])
        available = SortedList()
        for date in range(minval, maxval+1):
            available.add(date)

        cnt = 0
        for event in events:
            start, end = event
            if not available:
                break
            ind = available.bisect_left(start)
            # print(start, end, ind, available)
            if ind == 0 and start <= available[0] <= end:
                available.pop(0)
                cnt += 1
            elif ind < len(available) and available[ind] <= end:
                available.remove(available[ind])
                cnt += 1
            
        return cnt