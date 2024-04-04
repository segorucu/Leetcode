class Solution:
    def maxDepth(self, s: str) -> int:
        

        tot = ans = 0
        for c in s:
            if tot and c == ")":
                ans = max(ans, tot)
                tot -= 1

            elif c == "(":
                tot += 1

        return ans
