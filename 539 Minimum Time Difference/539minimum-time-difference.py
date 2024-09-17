class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        
        arr = []
        for time in timePoints:
            hour = int(time[0:2])
            minutes = int(time[3:])
            tmp = 60 * hour + minutes
            arr.append(tmp)
        day = 24*60
        arr.sort()
        arr.append(arr[0]+day)
        diff = inf
        n = len(arr)
        for i in range(1,n):
            diff = min(diff, abs(arr[i]-arr[i-1]))

        return diff
