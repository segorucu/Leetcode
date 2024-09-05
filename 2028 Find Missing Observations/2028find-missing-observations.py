class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        
        m = len(rolls)
        sm = (m+n) * mean
        nsum = sm - sum(rolls)
        if nsum < n:
            return []
        if nsum > n*6:
            return []
        
        ans = []
        while n > 0:
            curr = nsum // n
            nsum -= curr
            ans.append(curr)
            n -= 1

        return ans