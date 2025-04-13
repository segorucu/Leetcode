class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        
        intervals.sort()

        for a,b in pairwise(intervals):
            if b[0] < a[1]:
                return False
        return True