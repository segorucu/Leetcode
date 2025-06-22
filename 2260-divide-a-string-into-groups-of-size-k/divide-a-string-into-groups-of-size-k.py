class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        
        ans = []
        n = len(s)

        i = 0
        while i < n:
            end = min(i+k,n)
            curr = s[i:end]
            ans.append(curr)
            i = end

        if len(ans[-1]) < k:
            ans[-1] = ans[-1] + (k-len(ans[-1])) * fill

        return ans