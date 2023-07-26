from collections import defaultdict
class Solution:
    def partitionString(self, s: str) -> int:

        visited = set()
        ans = 1
        for c in s:
            if c in visited:
                ans += 1
                visited = set()
            visited.add(c)

        return ans
