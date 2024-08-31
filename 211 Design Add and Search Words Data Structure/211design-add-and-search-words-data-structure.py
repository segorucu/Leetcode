import string
class WordDictionary:

    def __init__(self):
        self.seen = set()
        

    def addWord(self, word: str) -> None:
        self.seen.add(word)
        

    def search(self, word: str) -> bool:
        dots = word.count(".")
        alp = "abcdefghijklmnopqrstuvwxyz"
        n = len(alp)
        if dots == 0:
            return word in self.seen
        elif dots == 1:
            ind = word.index(".")
            word = list(word)
            for i in range(n):
                word[ind] = alp[i]
                tmp = "".join(word)
                if tmp in self.seen:
                    return True
            return False
        elif dots == 2:
            l = word.index(".")
            r = l + 1 + word[l+1:].index(".")
            word = list(word)
            for i in range(n):
                word[l] = alp[i]
                for j in range(n):
                    word[r] = alp[j]
                    tmp = "".join(word)
                    if tmp in self.seen:
                        return True
            return False
                    
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)