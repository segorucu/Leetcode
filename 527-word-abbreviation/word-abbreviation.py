class TrieNode:
    def __init__(self):
        self.child = {}
        self.endword = False
        self.count = {}

class Trie:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        curr = self.root
        for w in word:
            if w not in curr.child:
                curr.child[w] = TrieNode()
                curr.count[w] = 1
            else:
                curr.count[w] += 1
            curr = curr.child[w]
        curr.endword = True
        

    def findsinglecount(self, word: str) -> bool:
        curr = self.root
        for i, w in enumerate(word):
            if curr.count[w] == 1:
                return i
            else:
                curr = curr.child[w]
        return len(word)
       
class Solution:
    def wordsAbbreviation(self, words: List[str]) -> List[str]:
        
        abbreviation = defaultdict(list)
        convert = {}

        n = len(words)
        ans = n * [""]

        for i, word in enumerate(words):
            if len(word) <= 3:
                ans[i] = word
            else:
                width = len(word) - 2
                tmp = word[0] + str(width) + word[-1]
                abbreviation[tmp].append(word)

        for k, v in abbreviation.items():
            if len(v) == 1:
                word = v[0]
                convert[word] = word[0] + str(len(word)-2) + word[-1]
            else:
                trie = Trie()
                for word in v:
                    trie.insert(word)
                for word in v:
                    ind = trie.findsinglecount(word)
                    if ind + 3 < len(word):
                        tmp = word[0:ind+1] + str(len(word)-ind-2) + word[-1]
                    else:
                        tmp = word
                    convert[word] = tmp

        for i, word in enumerate(words):
            if word in convert:
                ans[i] = convert[word]
        return ans
                


        


