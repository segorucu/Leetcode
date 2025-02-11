class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        

        prev = (None,-1)
        ans = inf
        for i, word in enumerate(wordsDict):
            if word in {word1,word2}:
                if prev[0] is None or prev[0] == word:
                    prev = (word, i)
                else:
                    ans = min(ans, i - prev[1])
                    prev = (word, i)

        return ans