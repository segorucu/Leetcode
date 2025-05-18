class Solution:    
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: (x[0],x[1]))
        
        ans = []
        ans.append(intervals[0])

        for b,e in intervals:
            beg = b
            end = e
            while ans and ans[-1][1] >= b:
                be, ee = ans.pop()
                beg = min(be,beg)
                end = max(ee, end)
            ans.append([beg,end])

            
        return ans
        