from collections import defaultdict
class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:

        locs = defaultdict(int)
        for i, key in enumerate(keyboard):
            locs[key] = i

        sm = 0
        prev = keyboard[0]
        for a in word:
            sm += abs(locs[prev]-locs[a])
            prev = a
        return sm

        