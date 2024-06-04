from collections import defaultdict
class Solution:
    def longestPalindrome(self, s: str) -> int:

        freqtab = defaultdict(int)
        for c in s:
            freqtab[c] += 1

        ans = 0
        lodd = False
        for key,val in freqtab.items():
            if not lodd:
                if val % 2 == 1:
                    lodd = True
            ans += (val // 2) * 2
        if lodd:
            ans += 1

        return ans
