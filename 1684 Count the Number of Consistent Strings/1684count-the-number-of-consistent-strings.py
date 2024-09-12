class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        
        allowed = set(allowed)
        ans = 0
        for word in words:
            word = set(word)
            for a in word:
                if a not in allowed:
                    break
            else:
                ans += 1

        return ans
