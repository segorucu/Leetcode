class Solution:
    def possibleStringCount(self, word: str) -> int:

        ans = 0
        for k,v in groupby(word):
            v = len(list(v))
            ans += v-1

        return ans + 1
        