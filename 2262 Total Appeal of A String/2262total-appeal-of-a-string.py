class Solution:
    def appealSum(self, s: str) -> int:


        letters = set(s)
        lastseen = collections.defaultdict(int)
        for letter in letters:
            lastseen[letter] = -1

        ans = 0
        for i, val in enumerate(s):
            lastseen[val] = i
            for letter in letters:
                ans += lastseen[letter] + 1
        return ans

