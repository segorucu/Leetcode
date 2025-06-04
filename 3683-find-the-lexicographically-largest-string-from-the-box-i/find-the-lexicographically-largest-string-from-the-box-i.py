class Solution:
    def answerString(self, word: str, numFriends: int) -> str:

        if numFriends <= 1:
            return word
        
        
        n = len(word)
        maxsize = n - numFriends + 1
        numFriends -= 1
        maxk = max(word)
        start = word.index(maxk)
        word = word[start:]
        substract = n - len(word)
        numFriends -= substract
        options = []
        for i,w in enumerate(word):
            if w == maxk:
                options.append(word[i:min(len(word),i+maxsize)])

        options.sort()
        return options[-1]
        