class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        
        startTime = [0] + startTime + [eventTime]
        endTime = [0] + endTime + [eventTime]

        l = 0
        n = len(startTime)
        meeting_time = 0
        ans = 0
        for r in range(1,n-1):
            meeting_time += endTime[r] - startTime[r]
            if r < n -1:
                startr = startTime[r+1]
            else:
                startr = eventTime
            if r - l >= k:
                meeting_time = meeting_time - (endTime[l] - startTime[l])
                l += 1
            endl = endTime[l-1]
            freetime = startr - endl - meeting_time
            ans = max(ans, freetime)

        return ans

        # [0,1,3,5]
        # [0,2,5,5]
            