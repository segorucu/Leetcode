class TrieNode:
    def __init__(self):
        self.child = {}
        self.endword = False
class Trie:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        curr = self.root
        for w in word:
            if w not in curr.child:
                curr.child[w] = TrieNode()
            curr = curr.child[w]
        curr.endword = True
            
        
    def search(self, word: str) -> bool:
        curr = self.root
        for w in word:
            if w not in curr.child:
                return False
            curr = curr.child[w]
        return curr.endword
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for w in prefix:
            if w not in curr.child:
                return False
            curr = curr.child[w]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)