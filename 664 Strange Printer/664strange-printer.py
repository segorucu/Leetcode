from itertools import groupby
from functools import cache
class Solution:
    def strangePrinter(self, s: str) -> int:

        s = "".join(k for k,v in groupby(s))
        n = len(s)

        @cache
        def dp(start, end):
            if start > end:
                return 0

            min_turns = 1 + dp(start+1, end)

            for k in range(start+1,end+1):
                if s[k] == s[start]:
                    min_turns = min(min_turns, \
                      dp(start,k-1) + dp(k+1,end))

            return min_turns

        return dp(0, n-1)

        