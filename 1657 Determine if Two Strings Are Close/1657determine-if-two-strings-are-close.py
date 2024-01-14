from collections import Counter
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:

        counter1 = Counter(word1)
        counter2 = Counter(word2)


        return Counter(counter1.values())==Counter(counter2.values()) and set(word1) == set(word2)