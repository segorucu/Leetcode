class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        

        sentence = sentence.split()
        n = len(sentence)
        for i in range(n):
            prev = sentence[i-1]
            curr = sentence[i]
            if prev[-1] != curr[0]:
                return False


        return True