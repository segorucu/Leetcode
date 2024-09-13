class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        

        prefix = [0]
        for a in arr:
            prefix.append(prefix[-1] ^ a)
        
        ans = []
        for l,r in queries:
            val = prefix[r+1] ^ prefix[l]
            ans.append(val)

        return ans