class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        
        count = 0
        m = len(pref)
        for word in words:
            n = len(word)
            if n < m:
                continue
            if word[0:m] == pref[:]:
                count += 1
        return count