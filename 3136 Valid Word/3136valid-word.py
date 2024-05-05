class Solution:
    def isValid(self, word: str) -> bool:

        incorrect = {'@', '#', '$'}
        vowel = {'a', 'e', 'i', 'o', 'u'}
        consonant = {'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', \
                     'r', 's', 't', 'v', 'w', 'x', 'y', 'z'}

        if len(word) < 3:
            return False

        word = word.lower()
        vflag = cflag = False
        for val in word:
            if val in incorrect:
                return False
            if val in vowel:
                vflag = True
            if val in consonant:
                cflag = True
            



        return vflag and cflag
        