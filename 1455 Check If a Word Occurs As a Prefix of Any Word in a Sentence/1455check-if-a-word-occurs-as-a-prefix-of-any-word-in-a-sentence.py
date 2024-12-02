class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        
        sentence = sentence.split()
        m = len(searchWord)
        for i, word in enumerate(sentence):
            if len(word) >= m and word[0:m] == searchWord[:]:
                return i+1
        return -1