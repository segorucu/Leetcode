class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        
        original = word
        it = 0
        while True:
            word = word[k:]
            it += 1
            if word == original[0:len(word)]:
                return it