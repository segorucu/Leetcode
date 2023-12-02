from collections import defaultdict
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:

        tab = defaultdict(int)
        for c in chars:
            tab[c] += 1

        ans = 0
        for word in words:
            dum = tab.copy()
            for c in word:
                if dum[c] == 0:
                    break
                else:
                    dum[c] -= 1
            else:
                ans += len(word)

        return ans