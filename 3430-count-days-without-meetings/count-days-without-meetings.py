class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        
        meetings.sort(key = lambda x: (x[0],x[1]))
        # print(meetings)

        total = meetings[0][0] - 1
        lastdate = 0
        for i,(beg,end) in enumerate(meetings):
            if i == 0:
                lastdate = max(lastdate, end)
                continue
            if beg > lastdate:
                total += beg - lastdate - 1
            lastdate = max(lastdate, end)
            # print(i, total)
        if days > lastdate:
            total += days - lastdate
        

        return total