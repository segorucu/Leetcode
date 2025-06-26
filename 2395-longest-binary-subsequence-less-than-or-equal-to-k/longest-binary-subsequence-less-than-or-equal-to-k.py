class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        
        l = r = 0
        n = len(s)
        zeros = 0
        ans = 0
        curr = 0
        for r in range(n):
            curr = 2 * curr + int(s[r])
            while curr > k:
                if s[l] == "0":
                    zeros += 1
                else:
                    curr -= pow(2, r-l)
                l += 1
            ans = max(ans, r-l+1 + zeros)

        return ans

