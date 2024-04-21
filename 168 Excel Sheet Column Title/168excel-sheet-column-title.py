class Solution:
    def convertToTitle(self, columnNumber: int) -> str:

        mp = collections.defaultdict(str)
        base = ord('A')-1

        for i in range(26):
            mp[i] = chr(base+i+1)

        ans = ""
        while columnNumber > 0:
            mod = (columnNumber-1) % 26
            ans += mp[mod]
            columnNumber = (columnNumber-1) // 26

        return ans[::-1]
        