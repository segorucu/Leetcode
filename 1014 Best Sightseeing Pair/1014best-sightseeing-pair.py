class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        
        n = len(values)
        maxprev = values[0]-1
        ans = 0
        for i in range(1,n):
            curr = values[i]
            ans = max(ans,curr+maxprev)
            maxprev = max(maxprev,curr)-1
        return ans
