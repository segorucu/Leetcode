class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        

        n = len(intervals)
        if n == 0:
            return [newInterval]
        if newInterval[0] <= intervals[0][0]:
            intervals = [newInterval] + intervals
        elif newInterval[0] >= intervals[-1][0]:
            intervals = intervals + [newInterval] 
        else:
            for i in range(n-1):
                if intervals[i][0] <= newInterval[0] < intervals[i+1][0]:
                    intervals = intervals[:i+1] + [newInterval] + intervals[i+1:]
        i = 0
        while i < len(intervals) - 1:
            if intervals[i][1] >= intervals[i+1][0]:
                intervals[i][1] = max(intervals[i][1],intervals[i+1][1])
                intervals.pop(i+1)
            else:
                i += 1 
        
        return intervals