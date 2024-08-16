class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:

        n = len(arrays)
        minval = min(arrays[0])
        maxval = max(arrays[0])
        ans = 0
        for i in range(1,n):
            # print(minval,maxval)
            currmin = min(arrays[i])
            currmax = max(arrays[i])
            ans = max(ans,abs(currmin-maxval),abs(currmax-minval))
            minval = min(minval,currmin)
            maxval = max(maxval,currmax)

        return ans

