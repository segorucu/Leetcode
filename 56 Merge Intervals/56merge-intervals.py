class Solution:    
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        
        i = 0
        ip = i + 1
        while i < len(intervals)-1:
            if intervals[i][1] >= intervals[ip][0]:
                intervals[i][1] = max(intervals[i][1],intervals[ip][1])
                intervals.pop(ip)
            else:
                i += 1
                ip = i + 1
            
            
        return intervals
        