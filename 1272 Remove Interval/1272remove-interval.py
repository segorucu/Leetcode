class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:

        ans = []
        for beg, end in intervals:
            if end <= toBeRemoved[0] or beg >= toBeRemoved[1]:
                ans.append([beg,end])
            elif beg < toBeRemoved[0] < end:
                ans.append([beg,toBeRemoved[0]])
            if beg < toBeRemoved[1] < end:
                ans.append([toBeRemoved[1],end])
        return ans
        