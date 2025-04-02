class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:

        ordermp = {}
        for i, char in enumerate(order):
            ordermp[char] = i
        

        for word1, word2 in pairwise(words):
            m = len(word1)
            n = len(word2)
            for i in range(min(m,n)):
                if word1[i] == word2[i]:
                    continue
                elif ordermp[word1[i]] > ordermp[word2[i]]:
                    return False
                elif ordermp[word1[i]] < ordermp[word2[i]]:
                    break
            else:
                if m > n:
                    return False
        return True