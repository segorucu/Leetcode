from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        tab = defaultdict(int)
        for w in s:
            tab[w] += 1

        for w in t:
            if tab[w] == 0:
                return False
            tab[w] -= 1
            if tab[w] == 0:
                del tab[w]

        if tab:
            return False
        return True