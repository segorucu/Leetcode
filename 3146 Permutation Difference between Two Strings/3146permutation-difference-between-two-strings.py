class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        
        mp = {}
        ans = 0
        for i,a in enumerate(s):
            mp[a] = i

        for i,a in enumerate(t):
            ans += abs(i-mp[a])

        return ans