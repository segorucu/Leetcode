class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:

        try:
            end = word.index(ch)
        except:
            return word

        new = word[0:end+1][::-1] + word[end+1:]
        return new
        