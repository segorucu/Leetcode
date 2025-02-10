class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        
        l = r = 0

        for i,h in enumerate(hours):
            if h > 8:
                hours[i] = 1
            else:
                hours[i] = -1

        ans = 0
        curr = 0
        lastseen = {}
        for i,h in enumerate(hours):

            curr += h
            if curr > 0:
                ans = max(ans,i+1)
            elif curr-1 in lastseen:
                ans = max(ans,i-lastseen[curr-1])

            if curr not in lastseen:
                lastseen[curr] = i

        return ans


  