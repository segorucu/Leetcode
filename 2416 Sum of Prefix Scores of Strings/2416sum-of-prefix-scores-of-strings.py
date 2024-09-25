class TrieNode:
    def __init__(self,count=0):
        self.child = {}
        # self.endword = False
        self.count = count

class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        curr = self.root
        for w in word:
            if w not in curr.child:
                curr.child[w] = TrieNode(count=1)
            else:
                curr.child[w].count += 1
            curr = curr.child[w]
            
        
    def search(self, word: str) -> bool:
        curr = self.root
        ans = curr.count
        for w in word:
            curr = curr.child[w]
            ans += curr.count
        return ans
        
class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie = Trie()
        for word in words:
            trie.insert(word)

        n = len(words)
        ans = n * [0]
        for i, word in enumerate(words):
            count = trie.search(word)
            ans[i] = count

        return ans
        