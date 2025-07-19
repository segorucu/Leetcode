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
            if curr.endword:
                return True
        return curr.endword
       
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        trie = Trie()
        ans = []
        for txt0 in folder:
            txt = txt0.split("/")
            curr = []
            for a in txt:
                if len(a):
                    curr.append(a)
            res = trie.search(curr)
            if not res:
                trie.insert(curr)
                ans.append(txt0)

        return ans