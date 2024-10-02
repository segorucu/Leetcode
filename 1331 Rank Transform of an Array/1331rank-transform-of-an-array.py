class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        
        dum = set(arr)
        dum = list(dum)
        dum.sort()
        mp = {}
        for i, val in enumerate(dum):
            mp[val] = i+1
        n = len(arr)
        ans = n * [0]
        for i, val in enumerate(arr):
            ans[i] = mp[val]
        return ans