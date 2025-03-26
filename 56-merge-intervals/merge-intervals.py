class Solution:    
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: (x[0],x[1]))
        # print(intervals)
        
        ans = []
        ans.append(intervals[0])

        n = len(intervals)
        maxe = intervals[0][-1]
        for i in range(1,n):
            if intervals[i][1] <= maxe:
                continue
            if intervals[i][0] <= ans[-1][1]:
                ans[-1][1] = intervals[i][1]
            else:
                ans.append(intervals[i])
            # print(i , ans)
            maxe = max(maxe, intervals[i][1])

            
            
        return ans
        