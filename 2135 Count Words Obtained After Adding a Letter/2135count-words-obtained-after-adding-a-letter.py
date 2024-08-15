class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:

        base = set()
        for word in startWords:
            base.add(frozenset(word))

        ans = 0
        for word in targetWords:
            for i in range(len(word)):
                curr = word[0:i] + word[i+1:]
                curr = frozenset(curr)
                if curr in base:
                    ans += 1
                    break

        return ans
        