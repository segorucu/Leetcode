class Solution:
    def titleToNumber(self, columnTitle: str) -> int:

        mp = collections.defaultdict(int)
        base = ord('A')
        for i in range(26):
            mp[chr(base+i)] = i + 1

        ans = 0
        for c in columnTitle:
            ans = ans * 26 + mp[c]


        return ans
        